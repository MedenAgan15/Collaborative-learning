import itertools
from typing import Iterable

from refs import Item
import tests as ut
import proposal.e3_proposal as e3

# ----------------------------------------------------------------------------------------------------
#region ETAPE 4 - GROUPEMENT PAR CATEGORIE
# ----------------------------------------------------------------------------------------------------
'''
Contexte : les organisateurs ont prévu de créer un étal par catégorie d'objets. Un espace dédié sera donc 
proposé pour les vêtements, un autre pour le jardinage, etc... Pour faciliter la mise en place de cette structuration, 
il apparaît plus pratique de disposer de la liste des objets pour chaque catégorie.

Objectif :
A partir d'une liste d'items, déterminer les catégories qui entrent en jeu. Pour chacune d'entre elles, créer
une liste spécique contenant tous les items qui relève de cette catégorie. Le résultat sera un dictionnaire,
dont la clé est le NOM de la cétgorie, et la valeur est la liste associée : dict[str, Iterable[Item]].

Exemple :
Soit la liste initiale [ (JARDINAGE, "bêche"), (VETEMENTS, "bonnet"), (JARDINAGE, "râteau")].
Le résultat attendu est :
{
    JARDINAGE: [(JARDINAGE, "bêche"), (JARDINAGE, "râteau")],
    VETEMENTS: [(VETEMENTS, "bonnet")]
}
'''
# ----------------------------------------------------------------------------------------------------

def groupby_category_classic (items:list[Item]) -> dict[str, Iterable[Item]]:
    '''
    L'idée est ici de s'appuyer sur la notion de boucles et de conditions afin de proposer une implémentation de la solution
    sur la base d'une approche itérative.
    Astuce :
    On pourra, si on le juge opportun, s'appuyer sur e3.sort_by_category_with_list(items) afin de disposer des items déjà triés par catégorie
    '''
    raise NotImplementedError(f"{groupby_category_classic.__name__} n'est pas encore implémentée")
            

def groupby_category_with_itertools (items:list[Item]) -> dict[str, Iterable[Item]]:
    '''
    Il s'agit ici de produire le même résultat que précédement, mais en faisant cette fois appel à la fonction '*itertools.groupby*'.
    Sur le principe, cette fonction admet deux arguments :
    - L'itérable dont les éléments doivent être groupés,
    - Une fonction qui renvoie la clé d'appartenance d'un élément qui lui est fourni en argument.
    Généralement, il est préférable que l'itérable soit déjà trié selon la même clé que celle utilisée par la fonction passée en second argument/

    L'appel est donc formulé sur le schéma suivant :
    itertools.groupby(iterable, key=None)

    Le second argument illustre l'idée de fonction supérieure : une fonction qui admet parmi ses arguments une fonction.

    On trouvera dans le lien suivant une explication plus détaillée sur cette fonction :
    https://docs.python.org/3/library/itertools.html#itertools.groupby

    La fonction 'itertools.groupby' renvoie une liste tuples : (clé, liste correspondant à la clé).

    Ce n'est pas exactement ce que nous souhaitons et il est donc nécessaire d'opérer une transformation de ce premier résultat.
    On pourra s'inspirer de la page ci-dessous pour imaginer une solutoin simple :
    @see https://dnmtechs.com/converting-groupby-results-to-dictionary-of-lists-in-python-3/
    '''
    raise NotImplementedError(f"{groupby_category_with_itertools.__name__} n'est pas encore implémentée")

#region Exécution (ne pas toucher)
if __name__ == "__main__":
    print("TEST - ETAPE 4 - Début...")
    ut.TestGroupBy().run(groupby_category_classic, groupby_category_with_itertools)
    print("TEST - ETAPE 4 - Fin")
#endregion
#endregion

