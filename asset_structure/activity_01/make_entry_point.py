from pathlib import Path

from pxr import Usd, UsdGeom


working_dir = Path(__file__).parent

stage = Usd.Stage.Open(str(working_dir / "export.usd"))
# Get all existing root prims
root_prims = stage.GetPseudoRoot().GetChildren()
# Create the entry point print. 
# We use the namespace `/World` by convention.
world_prim = UsdGeom.Xform.Define(stage, "/World").GetPrim()
# Set the default prim for referencing and payloading.
stage.SetDefaultPrim(world_prim)

# ADD CODE BELOW HERE
# vvvvvvvvvvvvvvvvvvv

# Move all root prims under new entry point prim.
editor = Usd.NamespaceEditor(stage)
for prim in root_prims:
    editor.ReparentPrim(prim, world_prim)
    # NamespaceEditor takes care of updating all relationship targets (e.g. material bindings)
    editor.ApplyEdits()

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE

stage.GetRootLayer().Export(str(working_dir / "lrg_bldgF.usd"), args={"format":"usda"})