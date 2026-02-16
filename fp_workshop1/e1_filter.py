import refs
from refs import Item
import tests as ut

# ----------------------------------------------------------------------------------------------------
#region FILTRER
# ----------------------------------------------------------------------------------------------------
'''
Contexte :
"Nos trois amis considèrent que la valeur de certains objets est si faible qu'il ne vaut pas la peine de passer
du temps à essayer de les vendre. Ils souhaitent donc éliminer de leurs étalages tous les objets dont le prix de vente estimé est 
inférieur strictement à 10 euros".

Objectif de l'étape :
L'objectif est ici de ne conserver à la vente que les objets dont le prix estimé est supérieur ou égal à un seuil donné.
Ce seuil est paramétré dans refs.MIN_PRICE
'''
# ----------------------------------------------------------------------------------------------------

#region Filtre avec implémentation impérative
def filter_items_classic (items:list[Item]) -> list[Item]:
     '''
    Dans cette fonction, il s'agit d'implémenter la mise en oeuvre du filtre en utilisant les concepts de boucle
    et de condition. Ces derniers étant ceux qui viennent naturellement à l'esprit du public pour lequel l'atelier
    a été conçu, à savoir des développeurs habitués au paradigme impératif, la fonction a été qualifiée de "classique".
    D'où le suffixe de son nom.

    Elle admet en entrée la liste des objets à filtrer, et produit en sortie une nouvelle liste composée uniquement
    des objets remplissant la condition souhaitée. 
    Attention : 
    - la liste fournie en argument ne doit donc pas être impactée, 
    - la liste résultat ne doit pas altérer l'ordre des objets tel que trouvé dans la liste initiale.
    '''
     raise NotImplementedError(f"{filter_items_classic.__name__} n'est pas encore implémentée")
#endregion

#region Filtre avec la fonction native filter
def filter_items_with_filter (items:list[Item]) -> list[Item]:
    '''
    Cette fonction a également pour mission d'implémenter la mise en oeuvre du filtre mais cette fois SANS utiliser les concepts de boucle
    et de condition. En lieu et place, nous souhaitons faire appel à la fonction native 'filter'.

    Cette fonction admet deux arguments :
    1. *function* : le premier est une fonction qui sera appliquée à chaque élément à traiter. Cette fonction doit renvoyer un booléen qui vaudra
    True si l'élément souscrit aux conditions du filtre, et False sinon.
    2. *iterable*: le second est une itérable qui indique tous les éléments à traiter.

    Elle s'invoque comme suit : filter(function, iterable)
    Elle renvoie un objet 'filtre' qui contient tous les éléments qui satisfont à la condition de filtrage vérifiée par la fonction.
    Cet objet est lui-même un itérable, et pourra donc être parcouru. Attention toutefois, il n'est pas une liste (list) et devra donc être converti.

    Exemple :

    >>> def is_even(number):
    ...     return number % 2 == 0
    ...

    >>> list(filter(is_even, [1, 3, 10, 45, 6, 50]))
    [10, 6, 50]

    La fonction 'filter_items_with_filter' à implémenter présente le même principe d'usage que son homologue "classique" développée précédemment :
    elle admet en entrée une liste d'objets à filtrer, et produit en sortie une nouvelle liste composée uniquement
    des objets remplissant la condition souhaitée. La liste fournie en argument ne doit donc pas être impactée, et la liste
    résultat ne doit pas altérer l'ordre des objets tel que trouvé dans la liste initiale.

    Le résultat doit être identique à celui produit par filter_items_classic
    '''
    raise NotImplementedError(f"{filter_items_with_filter.__name__} n'est pas encore implémentée")
#endregion

#region Exécution (ne pas toucher)
if __name__ == "__main__":
    print("TEST - ETAPE 1 - Début...")
    ut.TestFilter().run(filter_items_classic, filter_items_with_filter)
    print("TEST - ETAPE 1 - Fin")
#endregion

#endregion

