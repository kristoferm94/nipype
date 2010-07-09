# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""The freesurfer module provides basic functions for interfacing with
freesurfer tools.

Currently these tools are supported:

     * Dicom2Nifti: using mri_convert
     * Resample: using mri_convert
     
Examples
--------
See the docstrings for the individual classes for 'working' examples.

"""
__docformat__ = 'restructuredtext'

import os
from glob import glob

import numpy as np

from nipype.utils.filemanip import FileNotFoundError, fname_presuffix
from nipype.interfaces.base import CommandLine, traits, TraitedSpec,\
    Directory, CommandLineInputSpec
from nipype.utils.misc import isdefined

class Info(object):
    """ Freesurfer subject directory and version information.

    Examples
    --------

    >>> from nipype.interfaces.freesurfer import Info
    >>> Info.version()  # doctest: +SKIP
    >>> Info.subjectsdir()  # doctest: +SKIP
    
    """
    
    @staticmethod
    def version():
        """Check for freesurfer version on system
    
        Find which freesurfer is being used....and get version from
        /path/to/freesurfer/build-stamp.txt
    
        Returns
        -------
        
        version : string
           version number as string 
           or None if freesurfer version not found
    
        """
        fs_home = os.getenv('FREESURFER_HOME')
        if fs_home is None:
            Exception('FREESURFER_HOME is not defined')
        versionfile = os.path.join(fs_home,'build-stamp.txt')
        if not os.path.exists(versionfile):
            return None
        fid = open(versionfile,'rt')
        version = fid.readline()
        fid.close()
        return version
    
    @classmethod
    def subjectsdir(cls):
        """Check the global SUBJECTS_DIR
        
        Parameters
        ----------
        
        subjects_dir :  string
            The system defined subjects directory
    
        Returns
        -------
        
        subject_dir : string
            Represents the current environment setting of SUBJECTS_DIR
    
        """
        if cls.version():
            return os.environ['SUBJECTS_DIR']
        return None


class FSTraitedSpec(CommandLineInputSpec):
    subjects_dir =  Directory(exists=True, desc='subjects directory')
    
class FSCommand(CommandLine):
    """General support for FreeSurfer commands.

       Every FS command accepts 'subjects_dir' input.
    """
    
    input_spec = FSTraitedSpec
    
    _subjects_dir = None

    def __init__(self, **inputs):
        super(FSCommand, self).__init__(**inputs)
        self.inputs.on_trait_change(self._subjects_dir_update, 'subjects_dir')
        if not self._subjects_dir:
            self._subjects_dir = Info.subjectsdir()
        if not isdefined(self.inputs.subjects_dir) and self._subjects_dir:
            self.inputs.subjects_dir = self._subjects_dir
        self._subjects_dir_update()

    def _subjects_dir_update(self):
        if self.inputs.subjects_dir:
            self.inputs.environ.update({'SUBJECTS_DIR':
                                            self.inputs.subjects_dir})
    
    @classmethod
    def set_default_subjects_dir(cls, subjects_dir):
        cls._subjects_dir = subjects_dir

    def _gen_fname(self, basename, fname=None, cwd=None, suffix='_fs', use_ext=True):
        '''Define a generic mapping for a single outfile

        The filename is potentially autogenerated by suffixing inputs.infile

        Parameters
        ----------
        basename : string (required)
            filename to base the new filename on
        fname : string
            if not None, just use this fname
        cwd : string
            prefix paths with cwd, otherwise os.getcwd()
        suffix : string
            default suffix
        '''
        if basename == '':
            msg = 'Unable to generate filename for command %s. ' % self.cmd
            msg += 'basename is not set!'
            raise ValueError(msg)
        if cwd is None:
            cwd = os.getcwd()
        fname = fname_presuffix(basename, suffix=suffix,
                                use_ext=use_ext, newpath=cwd)
        return fname

