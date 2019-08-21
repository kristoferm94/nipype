# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..misc import AddCSVRow


def test_AddCSVRow_inputs():
    input_map = dict(
        _outputs=dict(usedefault=True, ),
        in_file=dict(
            extensions=None,
            mandatory=True,
        ),
    )
    inputs = AddCSVRow.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_AddCSVRow_outputs():
    output_map = dict(csv_file=dict(extensions=None, ), )
    outputs = AddCSVRow.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
