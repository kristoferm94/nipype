# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dti import DTIRecon


def test_DTIRecon_inputs():
    input_map = dict(
        DWI=dict(
            argstr='%s',
            extensions=None,
            mandatory=True,
            position=1,
        ),
        args=dict(argstr='%s', ),
        b0_threshold=dict(argstr='-b0_th', ),
        bvals=dict(
            extensions=None,
            mandatory=True,
        ),
        bvecs=dict(
            argstr='-gm %s',
            extensions=None,
            mandatory=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        image_orientation_vectors=dict(argstr='-iop %f', ),
        n_averages=dict(argstr='-nex %s', ),
        oblique_correction=dict(argstr='-oc', ),
        out_prefix=dict(
            argstr='%s',
            position=2,
            usedefault=True,
        ),
        output_type=dict(
            argstr='-ot %s',
            usedefault=True,
        ),
    )
    inputs = DTIRecon.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DTIRecon_outputs():
    output_map = dict(
        ADC=dict(extensions=None, ),
        B0=dict(extensions=None, ),
        FA=dict(extensions=None, ),
        FA_color=dict(extensions=None, ),
        L1=dict(extensions=None, ),
        L2=dict(extensions=None, ),
        L3=dict(extensions=None, ),
        V1=dict(extensions=None, ),
        V2=dict(extensions=None, ),
        V3=dict(extensions=None, ),
        exp=dict(extensions=None, ),
        tensor=dict(extensions=None, ),
    )
    outputs = DTIRecon.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
