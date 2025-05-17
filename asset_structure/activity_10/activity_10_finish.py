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

Usd.ModelAPI(world_prim).SetKind(Kind.Tokens.assembly)

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE
# END PART 1

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.centimeters)

# PART 2
# ADD CODE BELOW HERE
# vvvvvvvvvvvvvvvvvvv

for x in range(1,7):
    ref_path: Sdf.Path = world_prim.GetPath().AppendChild(f"lrg_bldgF_{x:02}")
    ref_target_prim = UsdGeom.Xform.Define(stage, ref_path).GetPrim()
    ref_target_prim.GetReferences().AddReference("./lrg_bldgF/lrg_bldgF.usd")
    position_bldg(ref_target_prim, x)

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE
# END PART 2

stage.Save()