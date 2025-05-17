from pathlib import Path

from pxr import Sdf, Usd, UsdGeom


working_dir = Path(__file__).parent

stage = Usd.Stage.CreateNew(str(working_dir / "scene.usda"))
world_prim = UsdGeom.Xform.Define(stage, "/World").GetPrim()
stage.SetDefaultPrim(world_prim)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.centimeters)

for x in range(1,4):
    ref_path: Sdf.Path = world_prim.GetPath().AppendChild(f"lrg_bldgF_{x:02}")
    ref_target_prim = UsdGeom.Xform.Define(stage, ref_path).GetPrim()
    ref_target_prim.GetReferences().AddReference("./lrg_bldgF.usd")
    xform_api = UsdGeom.XformCommonAPI(ref_target_prim)
    xform_api.SetTranslate((300.0*(x-1), 0.0, 0.0))

stage.Save()