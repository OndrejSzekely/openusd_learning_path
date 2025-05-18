from pathlib import Path
from pxr import Usd, UsdGeom, Sdf

example_relative_path = Path("openusd_learning_path\practical_examples\\00_instancing\\00_instanceable_internal_arcs")

# factory.usda
factory_stage = Usd.Stage.CreateNew((example_relative_path  / "factory.usda").as_posix())
factory_prim_ref = UsdGeom.Scope.Define(factory_stage, "/Factory")
factory_prim_ref.GetPrim().SetKind("assembly")
factory_stage.SetDefaultPrim(factory_prim_ref.GetPrim())
barrel_bundle_prim = UsdGeom.Scope.Define(factory_stage, factory_prim_ref.GetPath().AppendPath("BarrelBundle"))
barrel_bundle_prim.GetPrim().SetKind("group")
barrel_0_prim = UsdGeom.Xform.Define(factory_stage, barrel_bundle_prim.GetPath().AppendPath("Barrel_0"))
barrel_0_prim.GetPrim().SetKind("component")
xform_barrel_0_prim = UsdGeom.XformCommonAPI(barrel_0_prim)
xform_barrel_0_prim.SetTranslate((100, 0, 0))
barrel_geom_prim = UsdGeom.Xform.Define(factory_stage, barrel_0_prim.GetPath().AppendPath("Geometry"))
UsdGeom.Cylinder.Define(factory_stage, barrel_geom_prim.GetPath().AppendPath("Cylinder"))
barrel_1_prim = UsdGeom.Xform.Define(factory_stage, barrel_bundle_prim.GetPath().AppendPath("Barrel_1"))
barrel_1_prim.GetPrim().GetReferences().AddInternalReference(barrel_0_prim.GetPath())
barrel_1_prim.GetPrim().SetInstanceable(True)
UsdGeom.XformCommonAPI(barrel_1_prim).SetTranslate((110, 0, 0))
factory_stage.Save()

# scenario.usda
scenario_stage = Usd.Stage.CreateNew((example_relative_path  / "scenario.usda").as_posix())
factory_prim = UsdGeom.Scope.Define(scenario_stage, "/Factory")
factory_prim.GetPrim().GetReferences().AddReference((example_relative_path  / "factory.usda").as_posix())
scenario_stage.Save()

# loading_dock.usda
factory_stage = Usd.Stage.CreateNew((example_relative_path  / "loading_dock.usda").as_posix())
factory_prim_ref = UsdGeom.Scope.Define(factory_stage, "/Factory")
factory_stage.SetDefaultPrim(factory_prim_ref.GetPrim())
barrel_bundle_prim = UsdGeom.Scope.Define(factory_stage, factory_prim_ref.GetPath().AppendPath("BarrelBundle"))
barrel_0_prim = UsdGeom.Xform.Define(factory_stage, barrel_bundle_prim.GetPath().AppendPath("Barrel_0"))
barrel_0_prim.GetPrim().SetKind("component")
xform_barrel_0_prim = UsdGeom.XformCommonAPI(barrel_0_prim)
xform_barrel_0_prim.SetTranslate((100, 0, 0))
barrel_geom_prim = UsdGeom.Xform.Define(factory_stage, barrel_0_prim.GetPath().AppendPath("Geometry"))
UsdGeom.Cylinder.Define(factory_stage, barrel_geom_prim.GetPath().AppendPath("Cylinder"))
barrel_1_prim = UsdGeom.Xform.Define(factory_stage, barrel_bundle_prim.GetPath().AppendPath("Barrel_1"))
barrel_1_prim.GetPrim().GetReferences().AddInternalReference(barrel_0_prim.GetPath())
barrel_1_prim.GetPrim().SetInstanceable(True)
UsdGeom.XformCommonAPI(barrel_1_prim).SetTranslate((110, 0, 0))
factory_stage.Save()

# scenarios.usda
scenario_stage = Usd.Stage.CreateNew((example_relative_path  / "scenarios.usda").as_posix())
factory_prim = UsdGeom.Scope.Define(scenario_stage, "/Factory_1")
factory_prim.GetPrim().GetReferences().AddReference((example_relative_path  / "factory.usda").as_posix())
loading_dock = UsdGeom.Scope.Define(scenario_stage, "/Loading_Dock")
loading_dock.GetPrim().GetReferences().AddReference((example_relative_path  / "loading_dock.usda").as_posix())
scenario_stage.Save()