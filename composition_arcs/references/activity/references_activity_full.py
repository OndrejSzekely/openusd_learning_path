import os
from pathlib import Path

from pxr import Usd, UsdGeom, Gf


asset_library = Path(__file__).parent.parent.parent / "lib" / "assets"
working_dir = Path(__file__).parent
skyscraperA_file = asset_library / "envir" / "city" / "skyscraperA" / "skyscraperA.usd"
skyscraperA_relpath = os.path.relpath(skyscraperA_file, working_dir)
# Use forward slashes for file URIs for better cross-platform portability.
skyscraperA_relpath = Path(skyscraperA_relpath).as_posix()
skyscraperE_file = asset_library / "envir" / "city" / "skyscraperE" / "skyscraperE.usd"
skyscraperE_relpath = os.path.relpath(skyscraperE_file, working_dir)
skyscraperE_relpath = Path(skyscraperE_relpath).as_posix()
stage = Usd.Stage.CreateNew(str(working_dir / "city.usda"))
UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.centimeters)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

UsdGeom.Xform.Define(stage, "/World")
skyscraper_01 = UsdGeom.Xform.Define(stage, "/World/skyscraperA_01")
skyscraper_01.GetPrim().GetReferences().AddReference(skyscraperA_relpath)
skyscraper_02 = UsdGeom.Xform.Define(stage, "/World/skyscraperA_02")
skyscraper_02.GetPrim().GetReferences().AddReference(skyscraperA_relpath)
skyscraper_02_xformapi = UsdGeom.XformCommonAPI(skyscraper_02)
skyscraper_02_xformapi.SetTranslate(Gf.Vec3d(180, 0, 0))
skyscraper_03 = UsdGeom.Xform.Define(stage, "/World/skyscraperE_01")
skyscraper_03.GetPrim().GetReferences().AddReference(skyscraperE_relpath)
skyscraper_03_xformapi = UsdGeom.XformCommonAPI(skyscraper_03)
skyscraper_03_xformapi.SetTranslate(Gf.Vec3d(340, 0, 0))

stage.Save()

