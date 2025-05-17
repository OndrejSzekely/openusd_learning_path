from pathlib import Path

from pxr import Usd, Sdf, UsdGeom


working_dir = Path(__file__).parent

stage = Usd.Stage.CreateNew(str(working_dir / "my_skyscraper.usda"))
UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.centimeters)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

root_layer: Sdf.Layer = stage.GetRootLayer()
root_layer.subLayerPaths.append("./contents/shading.usd")
root_layer.subLayerPaths.append("./contents/geometry.usd")

stage.Save()