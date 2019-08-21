# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..specialized import BRAINSConstellationDetector


def test_BRAINSConstellationDetector_inputs():
    input_map = dict(
        BackgroundFillValue=dict(argstr='--BackgroundFillValue %s', ),
        LLSModel=dict(
            argstr='--LLSModel %s',
            extensions=None,
        ),
        acLowerBound=dict(argstr='--acLowerBound %f', ),
        args=dict(argstr='%s', ),
        atlasLandmarkWeights=dict(
            argstr='--atlasLandmarkWeights %s',
            extensions=None,
        ),
        atlasLandmarks=dict(
            argstr='--atlasLandmarks %s',
            extensions=None,
        ),
        atlasVolume=dict(
            argstr='--atlasVolume %s',
            extensions=None,
        ),
        cutOutHeadInOutputVolume=dict(argstr='--cutOutHeadInOutputVolume ', ),
        debug=dict(argstr='--debug ', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        forceACPoint=dict(
            argstr='--forceACPoint %s',
            sep=',',
        ),
        forceHoughEyeDetectorReportFailure=dict(
            argstr='--forceHoughEyeDetectorReportFailure ', ),
        forcePCPoint=dict(
            argstr='--forcePCPoint %s',
            sep=',',
        ),
        forceRPPoint=dict(
            argstr='--forceRPPoint %s',
            sep=',',
        ),
        forceVN4Point=dict(
            argstr='--forceVN4Point %s',
            sep=',',
        ),
        houghEyeDetectorMode=dict(argstr='--houghEyeDetectorMode %d', ),
        inputLandmarksEMSP=dict(
            argstr='--inputLandmarksEMSP %s',
            extensions=None,
        ),
        inputTemplateModel=dict(
            argstr='--inputTemplateModel %s',
            extensions=None,
        ),
        inputVolume=dict(
            argstr='--inputVolume %s',
            extensions=None,
        ),
        interpolationMode=dict(argstr='--interpolationMode %s', ),
        mspQualityLevel=dict(argstr='--mspQualityLevel %d', ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        otsuPercentileThreshold=dict(argstr='--otsuPercentileThreshold %f', ),
        outputLandmarksInACPCAlignedSpace=dict(
            argstr='--outputLandmarksInACPCAlignedSpace %s',
            hash_files=False,
        ),
        outputLandmarksInInputSpace=dict(
            argstr='--outputLandmarksInInputSpace %s',
            hash_files=False,
        ),
        outputMRML=dict(
            argstr='--outputMRML %s',
            hash_files=False,
        ),
        outputResampledVolume=dict(
            argstr='--outputResampledVolume %s',
            hash_files=False,
        ),
        outputTransform=dict(
            argstr='--outputTransform %s',
            hash_files=False,
        ),
        outputUntransformedClippedVolume=dict(
            argstr='--outputUntransformedClippedVolume %s',
            hash_files=False,
        ),
        outputVerificationScript=dict(
            argstr='--outputVerificationScript %s',
            hash_files=False,
        ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
        rVN4=dict(argstr='--rVN4 %f', ),
        rac=dict(argstr='--rac %f', ),
        rescaleIntensities=dict(argstr='--rescaleIntensities ', ),
        rescaleIntensitiesOutputRange=dict(
            argstr='--rescaleIntensitiesOutputRange %s',
            sep=',',
        ),
        resultsDir=dict(
            argstr='--resultsDir %s',
            hash_files=False,
        ),
        rmpj=dict(argstr='--rmpj %f', ),
        rpc=dict(argstr='--rpc %f', ),
        trimRescaledIntensities=dict(argstr='--trimRescaledIntensities %f', ),
        verbose=dict(argstr='--verbose ', ),
        writeBranded2DImage=dict(
            argstr='--writeBranded2DImage %s',
            hash_files=False,
        ),
        writedebuggingImagesLevel=dict(
            argstr='--writedebuggingImagesLevel %d', ),
    )
    inputs = BRAINSConstellationDetector.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BRAINSConstellationDetector_outputs():
    output_map = dict(
        outputLandmarksInACPCAlignedSpace=dict(extensions=None, ),
        outputLandmarksInInputSpace=dict(extensions=None, ),
        outputMRML=dict(extensions=None, ),
        outputResampledVolume=dict(extensions=None, ),
        outputTransform=dict(extensions=None, ),
        outputUntransformedClippedVolume=dict(extensions=None, ),
        outputVerificationScript=dict(extensions=None, ),
        outputVolume=dict(extensions=None, ),
        resultsDir=dict(),
        writeBranded2DImage=dict(extensions=None, ),
    )
    outputs = BRAINSConstellationDetector.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
