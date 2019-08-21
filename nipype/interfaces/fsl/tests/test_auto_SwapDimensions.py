# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import SwapDimensions


def test_SwapDimensions_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            extensions=None,
            mandatory=True,
            position='1',
        ),
        new_dims=dict(
            argstr='%s %s %s',
            mandatory=True,
        ),
        out_file=dict(
            argstr='%s',
            extensions=None,
            genfile=True,
            hash_files=False,
        ),
        output_type=dict(),
    )
    inputs = SwapDimensions.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SwapDimensions_outputs():
    output_map = dict(out_file=dict(extensions=None, ), )
    outputs = SwapDimensions.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
