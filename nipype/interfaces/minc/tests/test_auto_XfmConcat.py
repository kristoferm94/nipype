# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import XfmConcat


def test_XfmConcat_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        clobber=dict(
            argstr='-clobber',
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        input_files=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
            sep=' ',
        ),
        input_grid_files=dict(),
        output_file=dict(
            argstr='%s',
            extensions=None,
            genfile=True,
            hash_files=False,
            name_source=['input_files'],
            name_template='%s_xfmconcat.xfm',
            position=-1,
        ),
        verbose=dict(argstr='-verbose', ),
    )
    inputs = XfmConcat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_XfmConcat_outputs():
    output_map = dict(
        output_file=dict(extensions=None, ),
        output_grids=dict(),
    )
    outputs = XfmConcat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
