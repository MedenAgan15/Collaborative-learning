
import refs
from refs import Item
import tests as ut

# ----------------------------------------------------------------------------------------------------
#region ETAPE 2 - TRANSFORMATION UNITAIRE
# ----------------------------------------------------------------------------------------------------
'''
Contexte : 
Les organisateurs du vide grenier pourront bénéficier de la salle de fêtes de leur commune pour y installer
leurs stands le jour venu. Un élément imprévu survient toutefois : en effet, si la 
municipalité leur laisse les lieux à titre gracieux, elle demande une participation financière pour le nettoyage
qui sera réalisé par un prestataire externe après l'événement. Pour absorber une partie de cette charge, les trois
amis estiment qu'une augmentation forfaitaire de 10% sur tous les vêtements proposés devrait suffire.

Objectif :
A partir de la liste initiale des objets proposés à la vente, modifier le prix des objets appartenenant à la catégorie
refs.ItemCategory.VETEMENTS. Le taux à appliquer, exprimé en pourcentage, est disponible dans refs.TAX_RATE.  
'''
# ----------------------------------------------------------------------------------------------------

#region Via approche impérative
def apply_taxes_classic (items:list[Item])-> list[Item]:
    '''
    Cette fonction a pour mission de parcourir tous les objets de la liste qui lui est fournie en argument,
    d'augmenter de refs.TAX_RATE% le prix des objets appartenant à la catégorie refs.ItemCategory.VETEMENTS,
    puis de retourner une liste d'objets avec les prix actualisés. Notons que la liste initiale ne devra pas être
    impactée : la fonciton renvoie une liste nouvelle composée d'objets distincts des objets initiaux.

    L'implémentation devra ici faire appel aux concepts de boucle et de condition. Ces derniers étant ceux qui viennent
    naturellement à l'esprit du public pour lequel l'ateliera été conçu, à savoir des développeurs habitués au paradigme impératif, la fonction a été qualifiée de "classique".
    D'où son suffixe.
    '''
    raise NotImplementedError(f"{apply_taxes_classic.__name__} n'est pas encore implémentée")
#endregion

#region Via la fonction native map
def apply_taxes_with_map (items:list[Item])-> list[Item]:
    '''
    Cette fonction a le même objectif que la fonction 'apply_taxes_classic' implélentée ci-dessus.
    Toutefois, l'implémentation NE DOIT pas ici faire appel aux concepts de boucle et de condition. En lieu et place,
    on utilisera la fonction native 'map'.

    Sur le principe, cette dernière permet d’appliquer une fonction à chaque élément d’un itérable (par exemple, une liste)
    et de retourner un nouvel itérable contenant les résultats.

    Elle s'utilise comme suit :
    resultat = map(fonction, iterable)

    Elle retourne un objet de type map, qui est un itérable. Attention, cet objet n'est pas une liste (list).

    Exemple :

    def carre(x):
    return x**2

    nombres = [1, 2, 3, 4, 5]
    resultat = map(carre, nombres)

    print(list(resultat))
    [1, 4, 9, 16, 25]
    '''
    raise NotImplementedError(f"{apply_taxes_with_map.__name__} n'est pas encore implémentée")
#endregion

#region Exécution (ne pas toucher)
if __name__ == "__main__":
    print("TEST - ETAPE 2 - Début...")
    ut.TestMap().run(apply_taxes_classic, apply_taxes_with_map)
    print("TEST - ETAPE 2 - Fin")
#endregion
#endregion
