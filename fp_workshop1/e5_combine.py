import refs
from refs import Item as Item

import e1_filter as e1
import e2_map as e2
import e4_groupby as e4

# ----------------------------------------------------------------------------------------------------
#region ETAPE 5 - COMPOSITION DE METHODE
# ----------------------------------------------------------------------------------------------------
'''
Au fil des étapes précédentes, nous avons commencé par créer une fonction capable de filtrer, parmi une liste d’objets fournie en argument, ceux dont le prix satisfait au critère d’une valeur minimale. Puis, nous avons codé une fonction permettant d'appliquer une modification du prix de vente des objets relevant de la catégorie vêtements parmi une liste d’objets fournie en entrée. Enfin, nous avons implémenté une fonction permettant de répartir les objets d'une liste dans autant de listes que de catégories présentes.

En elles-mêmes, ces fonctions sont indépendants les unes des autres, mais en les combinant, nous pouvons appliquer successivement à une liste initiale une série d’actions qui produira un résultat complet :

La liste d’objets initiale est fournie à la fonction filtre. Cette dernière produit à titre de résultat une nouvelle liste ne contenant que les objets retenus pour la vente. Celle-ci est à son tour injectée dans la fonction de recalcul des prix, qui produit en retour une liste modifiée. Cette dernière est enfin utilisée à titre d’argument d’entrée de la dernière fonction, assurant une répartoition par liste des objets.

Liste initiale --> Filtre --> Liste filtrée --> Réévaluation des prix --> Liste filtrée avec prix modifiés --> Répartion par catégorie --> Listes filtrées, réévaluées par catégorie
'''
# ----------------------------------------------------------------------------------------------------

def combine ():
    raise NotImplementedError(f"{combine.__name__} n'est pas encore implémentée")