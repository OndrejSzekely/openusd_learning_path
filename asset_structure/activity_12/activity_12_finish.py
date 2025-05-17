from pathlib import Path
import random

from pxr import Sdf, Usd, UsdGeom

accent_choices = [(0.3372549, 0.7372549, 0.6), (0.14835148, 0.44579056, 0.74917495), 
                  (0.8151815, 0.76243955, 0.46005294), (0.81166536, 0.46005294, 0.8151815)]

working_dir = Path(__file__).parent

stage: Usd.Stage = Usd.Stage.Open(str(working_dir / "city_blockA.usd"))
shading_layer_path = "./contents/shading.usd"
shading_layer = Sdf.Layer.FindOrOpen(str(working_dir /shading_layer_path))
with Usd.EditContext(stage, shading_layer):
    # ADD CODE BELOW HERE
    # vvvvvvvvvvvvvvvvvvv

    for prim in stage.Traverse():
        if prim.IsComponent() and prim.GetVariantSets().HasVariantSet("exteriorType"):
            accent_primvar = UsdGeom.PrimvarsAPI(prim).GetPrimvar("accentColor")
            accent_primvar.Set(random.choice(accent_choices))
            vset = prim.GetVariantSet("exteriorType")
            vset.SetVariantSelection(random.choice(vset.GetVariantNames()))
    
    # ^^^^^^^^^^^^^^^^^^^^
    # ADD CODE ABOVE HERE

stage.Save()