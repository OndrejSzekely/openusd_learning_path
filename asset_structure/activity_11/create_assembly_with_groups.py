from enum import Enum
from pathlib import Path

from pxr import Kind, Sdf, Usd, UsdGeom

class Side(Enum):
    North = 1
    South = 2

### UPDATED - Added side parameter
def position_bldg(prim: Usd.Prim, index: int, side: Side):
    xform_api = UsdGeom.XformCommonAPI(prim)
    z_offset = 0.0
    rotY = 0.0
    ### UPDATED - Replaced index with side
    if side == Side.South:
        z_offset = 200.0
        rotY = 180.0
    ### UPDATED - Removed modulus
    xform_api.SetTranslate((300.0*(index-1), 0.0, z_offset))
    xform_api.SetRotate((0.0, rotY, 0.0))


working_dir = Path(__file__).parent

asset_layer = Sdf.Layer.CreateNew(str(working_dir / "city_blockA.usd"), args={"format": "usda"})
stage = Usd.Stage.Open(asset_layer)
world_prim = UsdGeom.Xform.Define(stage, "/World").GetPrim()
stage.SetDefaultPrim(world_prim)
Usd.ModelAPI(world_prim).SetKind(Kind.Tokens.assembly)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.centimeters)

# ADD CODE BELOW HERE
# vvvvvvvvvvvvvvvvvvv

# [...]

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE

stage.Save()