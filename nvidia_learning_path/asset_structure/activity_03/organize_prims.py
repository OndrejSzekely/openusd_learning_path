from pathlib import Path

from pxr import Usd, UsdGeom, UsdShade


working_dir = Path(__file__).parent

stage: Usd.Stage = Usd.Stage.Open(str(working_dir / "lrg_bldgF.usd"))
# Get all existing root prims
default_prim = stage.GetDefaultPrim()
default_prim_children = default_prim.GetChildren()
geom_scope = UsdGeom.Scope.Define(stage, default_prim.GetPath().AppendChild("Geometry")).GetPrim()
looks_scope = UsdGeom.Scope.Define(stage, default_prim.GetPath().AppendChild("Looks")).GetPrim()

editor = Usd.NamespaceEditor(stage)
for prim in default_prim_children:
    if prim.IsA(UsdGeom.Mesh):
        editor.ReparentPrim(prim, geom_scope)
        editor.ApplyEdits()
    elif prim.IsA(UsdShade.Material):
        editor.ReparentPrim(prim, looks_scope)
        editor.ApplyEdits()

stage.GetRootLayer().Export(str(working_dir / "lrg_bldgF.usd"), args={"format":"usda"})