# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..simpleregiongrowingsegmentation import SimpleRegionGrowingSegmentation


def test_SimpleRegionGrowingSegmentation_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputVolume=dict(
            argstr='%s',
            extensions=None,
            position=-2,
        ),
        iterations=dict(argstr='--iterations %d', ),
        labelvalue=dict(argstr='--labelvalue %d', ),
        multiplier=dict(argstr='--multiplier %f', ),
        neighborhood=dict(argstr='--neighborhood %d', ),
        outputVolume=dict(
            argstr='%s',
            hash_files=False,
            position=-1,
        ),
        seed=dict(argstr='--seed %s...', ),
        smoothingIterations=dict(argstr='--smoothingIterations %d', ),
        timestep=dict(argstr='--timestep %f', ),
    )
    inputs = SimpleRegionGrowingSegmentation.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SimpleRegionGrowingSegmentation_outputs():
    output_map = dict(
        outputVolume=dict(
            extensions=None,
            position=-1,
        ), )
    outputs = SimpleRegionGrowingSegmentation.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
