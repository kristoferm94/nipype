# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..epi import EddyCorrect


def test_EddyCorrect_inputs():
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
            position=0,
        ),
        out_file=dict(
            argstr='%s',
            extensions=None,
            name_source=['in_file'],
            name_template='%s_edc',
            output_name='eddy_corrected',
            position=1,
        ),
        output_type=dict(),
        ref_num=dict(
            argstr='%d',
            mandatory=True,
            position=2,
            usedefault=True,
        ),
    )
    inputs = EddyCorrect.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_EddyCorrect_outputs():
    output_map = dict(eddy_corrected=dict(extensions=None, ), )
    outputs = EddyCorrect.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
