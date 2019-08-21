# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brains import BRAINSEyeDetector


def test_BRAINSEyeDetector_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        debugDir=dict(argstr='--debugDir %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputVolume=dict(
            argstr='--inputVolume %s',
            extensions=None,
        ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
    )
    inputs = BRAINSEyeDetector.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BRAINSEyeDetector_outputs():
    output_map = dict(outputVolume=dict(extensions=None, ), )
    outputs = BRAINSEyeDetector.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
