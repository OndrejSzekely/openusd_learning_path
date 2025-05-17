from pathlib import Path

from pxr import Sdf, Usd, UsdGeom, UsdShade

working_dir = Path(__file__).parent

stage: Usd.Stage = Usd.Stage.Open(str(working_dir / "lrg_bldgF.usd"))
default_prim: Usd.Prim = stage.GetDefaultPrim()
primvars_api = UsdGeom.PrimvarsAPI(default_prim)
accent_color = primvars_api.CreatePrimvar("accentColor", Sdf.ValueTypeNames.Float3, UsdGeom.Tokens.constant)
accent_color.Set((1.0, 0.0, 0.0))

stage.Save()