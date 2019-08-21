# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..mesh import MeshWarpMaths


def test_MeshWarpMaths_inputs():
    input_map = dict(
        float_trait=dict(),
        in_surf=dict(
            extensions=None,
            mandatory=True,
        ),
        operation=dict(usedefault=True, ),
        operator=dict(
            mandatory=True,
            usedefault=True,
        ),
        out_file=dict(
            extensions=None,
            usedefault=True,
        ),
        out_warp=dict(
            extensions=None,
            usedefault=True,
        ),
    )
    inputs = MeshWarpMaths.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MeshWarpMaths_outputs():
    output_map = dict(
        out_file=dict(extensions=None, ),
        out_warp=dict(extensions=None, ),
    )
    outputs = MeshWarpMaths.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
