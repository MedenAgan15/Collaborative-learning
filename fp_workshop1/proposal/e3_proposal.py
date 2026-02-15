from refs import Item

# ----------------------------------------------------------------------------------------------------
#region ETAPE 3 - TRI
# ----------------------------------------------------------------------------------------------------
'''
Proposition d'implémentation.

'''
# ----------------------------------------------------------------------------------------------------
def get_category_order (item:Item) -> int:
    return int(item.category)

#region Tri avc list.sort
def sort_by_category_with_list(items:list[Item])-> list[Item]:

    result:list[Item] = list(items) # Nous créons ici un clone de l'objet liste passé en paramètre car list.sort utilisé ci-dessous modifie la liste cible
    list.sort(result, key = get_category_order) # La liste "result" est 
    return result
#endregion

#region Tri avec la fonction native sorted
def sort_by_category_with_sorted(items:list[Item])-> list[Item]:
    return sorted(items, key = get_category_order) # The list "items" remains unchanged and a new ordered list is returned
#endregion

#endregion
