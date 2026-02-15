import refs
from refs import Item

# ----------------------------------------------------------------------------------------------------
#region ETAPE 2 - TRANSFORMATION UNITAIRE
# ----------------------------------------------------------------------------------------------------
'''
Proposition d'implémentation  
'''
# ----------------------------------------------------------------------------------------------------

def apply_tax (item: refs.Item) -> refs.Item:

    if item.category == refs.ItemCategory.VETEMENTS:
        tax:float = item.price * (refs.TAX_RATE / 100)
        return Item(item.seller, item.category, item.label, item.price + tax)
    
    return item
    
def apply_taxes_classic (items:list[Item])-> list[Item]:

    items_with_tax:list[Item] = []

    for item in items:
        items_with_tax.append(apply_tax(item))
    
    return items_with_tax

def apply_taxes_with_map (items:list[Item])-> list[Item]:
    return list(map(apply_tax, items))


#endregion
