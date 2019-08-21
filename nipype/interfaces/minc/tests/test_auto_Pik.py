# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import Pik


def test_Pik_inputs():
    input_map = dict(
        annotated_bar=dict(argstr='--anot_bar', ),
        args=dict(argstr='%s', ),
        auto_range=dict(
            argstr='--auto_range',
            xor=('image_range', 'auto_range'),
        ),
        clobber=dict(
            argstr='-clobber',
            usedefault=True,
        ),
        depth=dict(argstr='--depth %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        horizontal_triplanar_view=dict(
            argstr='--horizontal',
            xor=('vertical_triplanar_view', 'horizontal_triplanar_view'),
        ),
        image_range=dict(
            argstr='--image_range %s %s',
            xor=('image_range', 'auto_range'),
        ),
        input_file=dict(
            argstr='%s',
            extensions=None,
            mandatory=True,
            position=-2,
        ),
        jpg=dict(xor=('jpg', 'png'), ),
        lookup=dict(argstr='--lookup %s', ),
        minc_range=dict(argstr='--range %s %s', ),
        output_file=dict(
            argstr='%s',
            extensions=None,
            genfile=True,
            hash_files=False,
            keep_extension=False,
            name_source=['input_file'],
            name_template='%s.png',
            position=-1,
        ),
        png=dict(xor=('jpg', 'png'), ),
        sagittal_offset=dict(argstr='--sagittal_offset %s', ),
        sagittal_offset_perc=dict(argstr='--sagittal_offset_perc %d', ),
        scale=dict(
            argstr='--scale %s',
            usedefault=True,
        ),
        slice_x=dict(
            argstr='-x',
            xor=('slice_z', 'slice_y', 'slice_x'),
        ),
        slice_y=dict(
            argstr='-y',
            xor=('slice_z', 'slice_y', 'slice_x'),
        ),
        slice_z=dict(
            argstr='-z',
            xor=('slice_z', 'slice_y', 'slice_x'),
        ),
        start=dict(argstr='--slice %s', ),
        tile_size=dict(argstr='--tilesize %s', ),
        title=dict(argstr='%s', ),
        title_size=dict(
            argstr='--title_size %s',
            requires=['title'],
        ),
        triplanar=dict(argstr='--triplanar', ),
        vertical_triplanar_view=dict(
            argstr='--vertical',
            xor=('vertical_triplanar_view', 'horizontal_triplanar_view'),
        ),
        width=dict(argstr='--width %s', ),
    )
    inputs = Pik.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Pik_outputs():
    output_map = dict(output_file=dict(extensions=None, ), )
    outputs = Pik.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
