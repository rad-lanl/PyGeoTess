from geotess.model import Layer, Attribute, GeoTessModel
from geotess.position import GeoTessPosition

def ak135_interp(layer):
    # do some stuff
    radii = attrib_values = None
    return radii, attrib_values)

dscr = """
Simple example of populating a 3D GeoTess model
comprised of 3 multi-level tessellations
author: Sandy Ballard
contact: sballar@sandia.gov"""

layers = [Layer(name='INNER_CORE', tess_id=0),
          Layer('OUTER_CORE', 0),
          Layer('LOWER_MANTLE', 1),
          Layer('LOWER_MANTLE', 1),
          Layer('TRANSITION_ZONE', 1),
          Layer('UPPER_MANTLE', 1),
          Layer('LOWER_CRUST', 2),
          Layer('UPPER_CRUST', 2)]

attributes = [Attribute(name='Vp', unit='km/sec'),
              Attribute('Vs', 'km/sec'),
              Attribute('rho', 'g/cc')]

# Initialize the model.  It is full of null data.
model = GeoTessModel(gridfile='path/to/gridfile.ascii', description=dscr, 
                     layers=layers, attributes=attributes, dtype=float)

# populate the model from ak135
for layer in model.layers:
    for vertex in model.grid.vertices:
        radii, attrib_values = ak135_interp(layer)
        model.set_profile(vertex, layer, radii, attrib_values)


# a helpful human-readable form of model info
print(model)

# write to file
model.write('path/to/output/small_model.ascii')


