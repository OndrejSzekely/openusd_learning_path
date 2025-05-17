from pathlib import Path

from pxr import Usd, UsdGeom


working_dir = Path(__file__).parent

stage = Usd.Stage.Open(str(working_dir / "lrg_bldgF.usd"))
default_prim = stage.GetDefaultPrim()
unencapsulated_prims = []
for prim in stage.GetPseudoRoot().GetChildren():
    if prim != default_prim:
        unencapsulated_prims.append(prim)

editor = Usd.NamespaceEditor(stage)
for prim in unencapsulated_prims:
    editor.ReparentPrim(prim, default_prim)
    # NamespaceEditor takes care of updating all relationship targets (e.g. material bindings)
    editor.ApplyEdits()

stage.Save()