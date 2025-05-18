from pathlib import Path
from pxr import Usd, UsdGeom, Sdf

example_relative_path = Path("openusd_learning_path\practical_examples\\00_instancing\\01_instanceable_external_arcs")

# barrel.usda
barrel_stage = Usd.Stage.CreateNew((example_relative_path  / "barrel.usda").as_posix())
barrel_prim = UsdGeom.Xform.Define(barrel_stage, "/Barrel")
barrel_stage.SetDefaultPrim(barrel_prim.GetPrim())
barrel_prim.GetPrim().SetKind("component")
geometry_prim = UsdGeom.Xform.Define(barrel_stage, barrel_prim.GetPath().AppendPath("Geometry"))
UsdGeom.Cylinder.Define(barrel_stage, geometry_prim.GetPath().AppendPath("Cylinder"))
barrel_stage.Save()

# factory.usda
factory_stage = Usd.Stage.CreateNew((example_relative_path  / "factory.usda").as_posix())
factory_prim_ref = UsdGeom.Scope.Define(factory_stage, "/Factory")
factory_prim_ref.GetPrim().SetKind("assembly")
factory_stage.SetDefaultPrim(factory_prim_ref.GetPrim())
assemled_barrels_prim = UsdGeom.Scope.Define(factory_stage, factory_prim_ref.GetPath().AppendPath("AssembledBarrels"))
assemled_barrels_prim.GetPrim().SetKind("group")
barrel_0_prim = factory_stage.DefinePrim(assemled_barrels_prim.GetPath().AppendPath("Barrel_0"))
barrel_0_prim.GetPrim().GetReferences().AddReference((example_relative_path  / "barrel.usda").as_posix())
barrel_0_prim.GetPrim().SetInstanceable(True)
xform_barrel_0_prim = UsdGeom.XformCommonAPI(barrel_0_prim)
xform_barrel_0_prim.SetTranslate((100, 0, 0))
barrel_1_prim = factory_stage.DefinePrim(assemled_barrels_prim.GetPath().AppendPath("Barrel_1"))
barrel_1_prim.GetPrim().GetReferences().AddReference((example_relative_path  / "barrel.usda").as_posix())
barrel_1_prim.GetPrim().SetInstanceable(True)
xform_barrel_1_prim = UsdGeom.XformCommonAPI(barrel_1_prim)
xform_barrel_1_prim.SetTranslate((110, 0, 0))
factory_stage.Save()

# factory2.usda
factory_stage = Usd.Stage.CreateNew((example_relative_path  / "factory2.usda").as_posix())
factory_prim_ref = UsdGeom.Scope.Define(factory_stage, "/Factory")
factory_prim_ref.GetPrim().SetKind("assembly")
factory_stage.SetDefaultPrim(factory_prim_ref.GetPrim())
assemled_barrels_prim = UsdGeom.Scope.Define(factory_stage, factory_prim_ref.GetPath().AppendPath("AssembledBarrels"))
assemled_barrels_prim.GetPrim().SetKind("group")
barrel_0_prim = factory_stage.DefinePrim(assemled_barrels_prim.GetPath().AppendPath("Barrel_0"))
barrel_0_prim.GetPrim().GetReferences().AddReference((example_relative_path  / "barrel.usda").as_posix())
barrel_0_prim.GetPrim().SetInstanceable(True)
xform_barrel_0_prim = UsdGeom.XformCommonAPI(barrel_0_prim)
xform_barrel_0_prim.SetTranslate((100, 0, 0))
barrel_1_prim = factory_stage.DefinePrim(assemled_barrels_prim.GetPath().AppendPath("Barrel_1"))
barrel_1_prim.GetPrim().GetReferences().AddReference((example_relative_path  / "barrel.usda").as_posix())
barrel_1_prim.GetPrim().SetInstanceable(True)
xform_barrel_1_prim = UsdGeom.XformCommonAPI(barrel_1_prim)
xform_barrel_1_prim.SetTranslate((110, 0, 0))
factory_stage.Save()

# scenario0.usda
scenario_stage = Usd.Stage.CreateNew((example_relative_path  / "scenario.usda").as_posix())
factory_prim = UsdGeom.Scope.Define(scenario_stage, "/Factory_0")
factory_prim.GetPrim().GetReferences().AddReference((example_relative_path  / "factory.usda").as_posix())
factory_prim = UsdGeom.Scope.Define(scenario_stage, "/Factory_1")
factory_prim.GetPrim().GetReferences().AddReference((example_relative_path  / "factory2.usda").as_posix())
scenario_stage.Save()