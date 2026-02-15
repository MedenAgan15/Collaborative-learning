import refs
from refs import Item

# ----------------------------------------------------------------------------------------------------
#region FILTRER
# ----------------------------------------------------------------------------------------------------
'''
Proposition d'implémentation pour la première étape
'''
# ----------------------------------------------------------------------------------------------------

def accept_item (item:Item) -> bool:
    return item.price >= refs.MIN_PRICE

#region Filtre avec implémentation impérative
def filter_items_classic (items:list[Item]) -> list[Item]:
       
    filtered_items:list[Item] = []
    
    for item in items:
        if accept_item(item):
            filtered_items.append(item)

    return filtered_items
#endregion

#region Filtre avec la fonction native filter
def filter_items_with_filter (items:list[Item]) -> list[Item]:    
    return list(filter(accept_item, items))
#endregion

#endregion

