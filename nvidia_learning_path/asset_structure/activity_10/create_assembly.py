from pathlib import Path

from pxr import Kind, Sdf, Usd, UsdGeom


def position_bldg(prim: Usd.Prim, index: int):
    xform_api = UsdGeom.XformCommonAPI(prim)
    z_offset = 0.0
    rotY = 0.0
    if index > 3:
        z_offset = 200.0
        rotY = 180.0
    xform_api.SetTranslate((300.0*((index-1) % 3), 0.0, z_offset))
    xform_api.SetRotate((0.0, rotY, 0.0))


working_dir = Path(__file__).parent

asset_layer = Sdf.Layer.CreateNew(str(working_dir / "city_blockA.usd"), args={"format": "usda"})
stage = Usd.Stage.Open(asset_layer)
world_prim = UsdGeom.Xform.Define(stage, "/World").GetPrim()
stage.SetDefaultPrim(world_prim)
# PART 1
# ADD CODE BELOW HERE
# vvvvvvvvvvvvvvvvvvv

# [...]

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE
# END PART 1

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.centimeters)

# PART 2
# ADD CODE BELOW HERE
# vvvvvvvvvvvvvvvvvvv

# [...]

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE
# END PART 2

stage.Save()