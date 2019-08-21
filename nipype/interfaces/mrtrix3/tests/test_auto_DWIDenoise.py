# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import DWIDenoise


def test_DWIDenoise_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        bval_scale=dict(argstr='-bvalue_scaling %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        extent=dict(argstr='-extent %d,%d,%d', ),
        grad_file=dict(
            argstr='-grad %s',
            extensions=None,
            xor=['grad_fsl'],
        ),
        grad_fsl=dict(
            argstr='-fslgrad %s %s',
            xor=['grad_file'],
        ),
        in_bval=dict(extensions=None, ),
        in_bvec=dict(
            argstr='-fslgrad %s %s',
            extensions=None,
        ),
        in_file=dict(
            argstr='%s',
            extensions=None,
            mandatory=True,
            position=-2,
        ),
        mask=dict(
            argstr='-mask %s',
            extensions=None,
            position=1,
        ),
        noise=dict(
            argstr='-noise %s',
            extensions=None,
            keep_extension=True,
            name_source='in_file',
            name_template='%s_noise',
        ),
        nthreads=dict(
            argstr='-nthreads %d',
            nohash=True,
        ),
        out_file=dict(
            argstr='%s',
            extensions=None,
            keep_extension=True,
            name_source='in_file',
            name_template='%s_denoised',
            position=-1,
        ),
    )
    inputs = DWIDenoise.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DWIDenoise_outputs():
    output_map = dict(
        noise=dict(extensions=None, ),
        out_file=dict(extensions=None, ),
    )
    outputs = DWIDenoise.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
