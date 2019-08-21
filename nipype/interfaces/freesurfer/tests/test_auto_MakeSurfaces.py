# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import MakeSurfaces


def test_MakeSurfaces_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        copy_inputs=dict(),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fix_mtl=dict(argstr='-fix_mtl', ),
        hemisphere=dict(
            argstr='%s',
            mandatory=True,
            position=-1,
        ),
        in_T1=dict(
            argstr='-T1 %s',
            extensions=None,
        ),
        in_aseg=dict(
            argstr='-aseg %s',
            extensions=None,
        ),
        in_filled=dict(
            extensions=None,
            mandatory=True,
        ),
        in_label=dict(
            extensions=None,
            xor=['noaparc'],
        ),
        in_orig=dict(
            argstr='-orig %s',
            extensions=None,
            mandatory=True,
        ),
        in_white=dict(extensions=None, ),
        in_wm=dict(
            extensions=None,
            mandatory=True,
        ),
        longitudinal=dict(argstr='-long', ),
        maximum=dict(argstr='-max %.1f', ),
        mgz=dict(argstr='-mgz', ),
        no_white=dict(argstr='-nowhite', ),
        noaparc=dict(
            argstr='-noaparc',
            xor=['in_label'],
        ),
        orig_pial=dict(
            argstr='-orig_pial %s',
            extensions=None,
            requires=['in_label'],
        ),
        orig_white=dict(
            argstr='-orig_white %s',
            extensions=None,
        ),
        subject_id=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
            usedefault=True,
        ),
        subjects_dir=dict(),
        white=dict(argstr='-white %s', ),
        white_only=dict(argstr='-whiteonly', ),
    )
    inputs = MakeSurfaces.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MakeSurfaces_outputs():
    output_map = dict(
        out_area=dict(extensions=None, ),
        out_cortex=dict(extensions=None, ),
        out_curv=dict(extensions=None, ),
        out_pial=dict(extensions=None, ),
        out_thickness=dict(extensions=None, ),
        out_white=dict(extensions=None, ),
    )
    outputs = MakeSurfaces.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
