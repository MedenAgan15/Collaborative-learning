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

    '''
    Adds to the result array the revenue of the specified item.
    The amount is added to the element of the array matching the seller of the item.
    '''
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

    '''
    La fonction itertools.reduce est ici mise à profit pour obtenir le résultat souhaité par application
    successive de la fonction _add_item à chacun des items à traiter.
    Sur le principe, un tableau initial est fourni à la fonction, dont tous les éléments sont initialisés à 0.
    La fonction fait ensuite successivement appel à _add_item, en lui fournissant :
    - En premier argument, le résultat de l'exécution précédente de _add_item (ou la valeur d'initialisation la première fois),
    - L'élément suivant à traiter.
    Cet appel fournit un tableau résultat, qui servira à alimenter le prochain appel.
    '''
    return reduce (_add_item, items, array('i', [0,0,0]))
#endregion   

#region avec approche récursive
def compute_revenue_recursive (items:list[Item]) -> array:

    if len(items) > 1 : 
        # The process goes on with the rest of the list, excluding the first element 
        # since it has been taken into account
        return _add_item(compute_revenue_recursive(items[1:]), items[0])
    else:
        return _add_item([0, 0, 0], items[0])

def compute_revenue_recursive2 (items:list[Item], result: array=[0,0,0]) -> array:

    if (items is None or len(items) == 0) :
        return [0, 0, 0]
    
    _add_item(result, items[0])

    if len(items) > 1 : 
        # The process goes on with the rest of the list, excluding the first element 
        # since it has been taken into account
        return compute_revenue_recursive(items[1:])
    
    return result
        
#endregion
     
#endregion