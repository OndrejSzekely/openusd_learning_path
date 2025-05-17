from pathlib import Path

from pxr import Usd, Kind

working_dir = Path(__file__).parent

stage: Usd.Stage = Usd.Stage.Open(str(working_dir / "lrg_bldgF.usd"))
default_prim: Usd.Prim = stage.GetDefaultPrim()
# ADD CODE BELOW HERE
# vvvvvvvvvvvvvvvvvvv

Usd.ModelAPI(default_prim).SetKind(Kind.Tokens.component)

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE

stage.Save()