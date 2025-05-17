from pathlib import Path

from pxr import Sdf

working_dir = Path(__file__).parent

asset_layer = Sdf.Layer.FindOrOpen(str(working_dir / "lrg_bldgF.usd"))
contents_layer = Sdf.Layer.FindOrOpen(str(working_dir / "contents.usd"))

# ADD CODE BELOW HERE
# vvvvvvvvvvvvvvvvvvv

# [...]

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE

asset_layer.Save()
contents_layer.Save()
