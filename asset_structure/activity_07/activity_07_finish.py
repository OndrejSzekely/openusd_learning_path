from pathlib import Path

from pxr import Sdf

working_dir = Path(__file__).parent

asset_layer = Sdf.Layer.FindOrOpen(str(working_dir / "lrg_bldgF.usd"))
contents_layer = Sdf.Layer.FindOrOpen(str(working_dir / "contents.usd"))

# ADD CODE BELOW HERE
# vvvvvvvvvvvvvvvvvvv

prim_spec = contents_layer.GetPrimAtPath("/World")
prop_spec: Sdf.PropertySpec
for prop_spec in prim_spec.properties:
    Sdf.CopySpec(contents_layer, prop_spec.path, asset_layer, prop_spec.path)
    prim_spec.RemoveProperty(prop_spec)

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE

asset_layer.Save()
contents_layer.Save()
