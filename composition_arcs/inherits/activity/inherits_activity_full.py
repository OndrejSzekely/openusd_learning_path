import os
from pathlib import Path

from pxr import Usd, UsdLux, UsdShade, Sdf

working_dir = Path(__file__).parent
asset_stage = Usd.Stage.Open(str(working_dir / "street_lamp_dbl.usd"))
class_prim = asset_stage.CreateClassPrim("/_street_lamp_dbl")
root = asset_stage.GetDefaultPrim()
root.GetInherits().AddInherit(class_prim.GetPath())
asset_stage.Save()

scenario2 = Usd.Stage.Open(str(working_dir / "scenario_02.usd"))
class_prim = scenario2.OverridePrim("/_street_lamp_dbl")
light_prim = scenario2.OverridePrim(class_prim.GetPath().AppendPath("Lights/sphere_light_01"))
light = UsdLux.LightAPI(light_prim)
light.CreateColorAttr((0.5, 0.4, 0.1))
light_prim = scenario2.OverridePrim(class_prim.GetPath().AppendPath("Lights/sphere_light_02"))
light = UsdLux.LightAPI(light_prim)
light.CreateColorAttr((0.5, 0.4, 0.1))
shader_prim = scenario2.OverridePrim(class_prim.GetPath().AppendPath("Looks/light/light"))
shader = UsdShade.Shader(shader_prim)
shader.CreateInput("emissiveColor", Sdf.ValueTypeNames.Color3f).Set((0.5, 0.4, 0.1))

scenario2.Save()
