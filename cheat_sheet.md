# Cheat-Sheet

## LIVRP

### Local
* **Having two sublayers defining the same Prim**. If the stronger def doesn't specify all properties, the composed prim can inherit values from the weaker layer, but only non-conflicting ones (e.g., if LayerB doesn't specify rotation but LayerA does).
* If there is no `def` of the prim, only `over` in whole composition, then the prim is *undefined*.
* `over` does not *redefine* Prim, but only modify/add new property opinion.
* Prim *over* could be on weaker layer, but in case of conflict, stronger layer opinion wins.
* There must some `def` of a prim. It does not need to be in the strongest layer (could be preceeded and followed by layers with `over`).

### Inherits
* Used to broadcast edit operation to a prim collection.
* Can not inherit from descendant nor ancestor.
* Prim can inherit from `Class` or any prim. 
* The key difference between references and inherits is that references fully encapsulate their targets, and therefore “disappear” when composed through another layer of referencing, whereas the relationship between inheritors and their inherits target remains “live” through arbitrary levels of referencing. In other words, when a prim inherits from another prim, it subscribes itself and all referencing contexts to changes made to the inherited prim. You can see this difference with the following example that uses the previous example as Trees.usd

### Variant Sets
* No variant could be selected.
* Each variant can in fact create an entire subtree of prims (that will be combined on top of any referenced scene description), as well as apply overrides.
* Inlined into layer.
* Prim can have unlimited number of variant sets. Their relative strenght follows list editing order.
* Variant sets could be nested inside other variant sets.
* VariantSets allow optimal scattering of instancing variation.
* 