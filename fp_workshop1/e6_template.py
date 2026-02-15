from array import array
from functools import reduce

import refs
from refs import Item as Item
import tests as ut

# ----------------------------------------------------------------------------------------------------
#region REDUCTION
# ----------------------------------------------------------------------------------------------------
'''
Contexte :
"La vente a eu lieu et les affaires ont été profitables aux trois amis. Le prix auquel chaque objets a été vendu
est connu et a été consigné de sorte que, désormais, il devrait être possible de déterminer la recette de chacun
des vendeurs."

Objectif :
Implémenter la fonction qui, à partir de la liste des items, calcule la recette de chaque vendeur. Pour cela, on s'appuiera sur 
refs.get_revenue(item), qui indique le prix auquel l'objet a été vendu, et item.seller, qui indique quel est le vendeur de l'objet.
Le résultat devra être présenté sous la forme d'un tableau de trois éléments, chacun d'eux contenant la recette d'un des vendeurs.
L'indice de l'élément propre à un vendeur donné est accessible simplement par la fonction :
refs.Seller.get_index(item.seller).

On trouvera dans la page ci-après plus d'information sur les tableaux Python :
https://docs.python.org/3/library/array.html
'''
# ----------------------------------------------------------------------------------------------------

#region Réduction via implémentation impérative  

def compute_revenue_classic (items:list[Item]) -> array:
    '''
    Il s'agit ici de faire appel à la notion de boucle pour produire le résultat attendu.
    '''
    raise NotImplementedError(f"{compute_revenue_classic.__name__} n'est pas encore implémentée")
#endregion

#region avec la fonction native 'reduce"

def compute_revenue_studied (items:list[Item]) -> array:
    '''
    Il convient ici de se passer complètement de la notion de boucle, et de faire appel à la fonction native 'reduce' pôr obtenir le même résultat que
    précédement.
    On pouyrra trouver dans la page ci-après plus d'indications sur cette fonction :
    https://www.datacamp.com/fr/tutorial/python-reduce-complete-guide
    '''
    raise NotImplementedError(f"{compute_revenue_studied.__name__} n'est pas encore implémentée")
 #endregion   

#region Exécution (ne pas toucher)
if __name__ == "__main__":
    ut.TestReduce().run(compute_revenue_classic, compute_revenue_studied)
#endregion
#endregion