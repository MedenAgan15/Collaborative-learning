import refs
from refs import Item
import tests as ut

# ----------------------------------------------------------------------------------------------------
#region ETAPE 3 - TRI
# ----------------------------------------------------------------------------------------------------
'''
Contexte :
"Les organisateurs envisagent de mettre en place un stand par catégorie d'objets à vendre. Il y aura donc un
stand dédié au bricolage, un autre aux vêtements... Pour se faciliter la tâche, ils aimeraient donc bien
disposer d'une version de la liste des objets à vendre dans laquelle ces derniers apparaissent triés par catégorie."

Objectif :
Ecrire une fonction qui admet en entrée une liste non ordonnée d'objets et fournit en sortie une nouvelle liste dans laquelle
les objets sont ordonnés selon la valeur de l'attribut 'category'.

'''
# ----------------------------------------------------------------------------------------------------

#region Tri avc list.sort

def sort_by_category_with_list(items:list[Item])-> list[Item]:
    '''
    Cette fonction a pour mission de trier par catégorie les objets de la liste fournie en argument. Notons que la liste initiale ne devra pas être
    impactée : la fonciton renvoie une liste nouvelle composée d'objets distincts des objets initiaux.

    L'implémentation devra ici faire appel à la fonction 'list.sort'. 
    Attention, cette dernière altère la liste qui lui est fournie en argument !
    '''
    raise NotImplementedError(f"{sort_by_category_with_list.__name__} n'est pas encore implémentée")
#endregion

#region Tri avec la fonction native sorted

def sort_by_category_with_sorted(items:list[Item])-> list[Item]:
    '''
    Même attendu pour cette fonction que celui exposé pour la fonction 'sort_by_category_with_list' telle qu'implémentée précédemment.
    La différence est que l'on impose ici l'usage de la fonction native 'sorted'.
    '''
    raise NotImplementedError(f"{sort_by_category_with_sorted.__name__} n'est pas encore implémentée")
#endregion

#region Exécution (ne pas toucher)
if __name__ == "__main__":
    print("TEST - ETAPE 3 - Début...")
    ut.TestSorting().run(sort_by_category_with_list, sort_by_category_with_sorted)
    print("TEST - ETAPE 3 - Fin")
#endregion
#endregion
