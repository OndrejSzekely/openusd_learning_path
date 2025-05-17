from pathlib import Path

from pxr import Usd

working_dir = Path(__file__).parent

stage: Usd.Stage = Usd.Stage.Open(str(working_dir / "lrg_bldgF.usd"))
default_prim: Usd.Prim = stage.GetDefaultPrim()
# Hard-coded, but by convention of our asset structure we can trust that the default
# prim has a Looks scope. 
looks_prim: Usd.Prim = stage.GetPrimAtPath(default_prim.GetPath().AppendChild("Looks"))
vsets: Usd.VariantSets = looks_prim.GetVariantSets()
# Loop through all of the variant sets defined on the Looks prim.
# Again relying on a convention of our custom asset structure that
# artists are define shading variant sets on the Looks prim.
for vset_name in vsets.GetNames():
    vset: Usd.VariantSet = vsets.GetVariantSet(vset_name)
    variants = vset.GetVariantNames()
    default = vset.GetVariantSelection()
    # ADD CODE BELOW HERE
    # vvvvvvvvvvvvvvvvvvv
    
    # Create the same variant set on the default_prim.
    lofted_vset: Usd.VariantSet = default_prim.GetVariantSets().AddVariantSet(vset_name)
    for variant in variants:
        lofted_vset.AddVariant(variant)
        lofted_vset.SetVariantSelection(variant)
        # The lofted variant set just selects the 
        # same variant from the nested variant set.
        with lofted_vset.GetVariantEditContext():
            vset.SetVariantSelection(variant)
    lofted_vset.SetVariantSelection(default)

    # ^^^^^^^^^^^^^^^^^^^^
    # ADD CODE ABOVE HERE

stage.Save()