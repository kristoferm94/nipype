# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import MRITessellate


def test_MRITessellate_inputs():
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
            position=-3,
        ),
        label_value=dict(
            argstr='%d',
            mandatory=True,
            position=-2,
        ),
        out_file=dict(
            argstr='%s',
            extensions=None,
            genfile=True,
            position=-1,
        ),
        subjects_dir=dict(),
        tesselate_all_voxels=dict(argstr='-a', ),
        use_real_RAS_coordinates=dict(argstr='-n', ),
    )
    inputs = MRITessellate.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MRITessellate_outputs():
    output_map = dict(surface=dict(extensions=None, ), )
    outputs = MRITessellate.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
