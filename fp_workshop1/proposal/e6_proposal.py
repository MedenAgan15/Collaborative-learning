from array import array
from functools import reduce

import refs
from refs import Item as Item

# ----------------------------------------------------------------------------------------------------
#region REDUCTION
# ----------------------------------------------------------------------------------------------------
'''
Proposition d'implémentation
'''
# ----------------------------------------------------------------------------------------------------

def _get_index_from_item (item:Item) -> int:
    return refs.Seller.get_index(item.seller)
        
      
def _add_item (result:array, item:Item) -> array:

    if item is None:
        return result

    index:int = _get_index_from_item(item)
    if refs.Seller.is_Noone(index):
        return result
    
    revenue:float = refs.get_revenue(item)
    result[index]+=revenue

    return result

#region Réduction via implémentation impérative  
def compute_revenue_classic (items:list[Item]) -> array:

    result:array = array('i', [0,0,0])
    for item in items:
        _add_item(result, item)
    
    return result
#endregion

#region avec la fonction native 'reduce"
def compute_revenue_studied (items:list[Item]) -> array:

    return reduce (_add_item, [array('i', [0,0,0])] + items)
#endregion   
#endregion