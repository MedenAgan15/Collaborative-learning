from enum import IntEnum
from collections import namedtuple

"""
References all basic components for the workshop
"""
# -----
MIN_PRICE = 15
TAX_RATE = 10

# -----
class Seller(IntEnum):
    """
    All possible sellers
    """
    NOONE=-1
    A = 0,
    B = 1,
    C = 2

    def get_index (self) -> int:
        if self is None: return Seller.NOONE
        return self.value
    
    def is_Noone (index:int) -> bool:
        return Seller.NOONE == index
    
# -----
class ItemCategory(IntEnum):
    """
    All available items'categories
    """
    JARDINAGE = 1,
    AMEUBLEMENT = 2,
    VETEMENTS = 3,
    BRICOLAGE = 4

# -----
Item = namedtuple("Item", ["seller","category","label","price"])

# -----
def convert_item_to_string (item:Item) -> str:
    """
    Converts an Item named tuple into a string that describes it
    
    :param item: item to be converted
    :type item: Item
    :return: the string description of th given item
    :rtype: str
    """

    if (item is None):
        return ""
    
    if not isinstance(item, Item) :
        return f"Unexpected type {type(item)}"
    
    return f"Seller: {item.seller.name}, Category:{item.category.name}, Label:{item.label}, Price:{item.price} €"

# -----
def clone_item (item:Item) -> Item:
    return Item(item.seller, item.category, item.label, item.price)

# -----
def convert_items_to_string (items:list[Item]) -> str:
    for item in items:
        print (convert_item_to_string(item))

# -----

def get_all_items():
    return [
        Item(Seller.C, ItemCategory.VETEMENTS, "Jean taille L", 15),
        Item(Seller.A, ItemCategory.AMEUBLEMENT, "Tapis en laine", 25),
        Item(Seller.C, ItemCategory.JARDINAGE, "Paire de gants de jardinage renforcés", 16),
        Item(Seller.B, ItemCategory.BRICOLAGE, "Chevilles placo x 100", 10),
        Item(Seller.C, ItemCategory.BRICOLAGE, "Protections auditives", 20),
        Item(Seller.A, ItemCategory.VETEMENTS, "Bottes de cuir", 25),
        Item(Seller.B, ItemCategory.AMEUBLEMENT, "Coussins brodés (x2)", 15),
        Item(Seller.C, ItemCategory.AMEUBLEMENT, "Chaises en paille (x4)", 60),
        Item(Seller.A, ItemCategory.BRICOLAGE, "Disqueuse D125", 35),
        Item(Seller.B, ItemCategory.JARDINAGE, "Taille-haies", 70),
        Item(Seller.C, ItemCategory.VETEMENTS, "Chapeau de paille", 13),
        Item(Seller.A, ItemCategory.JARDINAGE, "Pulvérisateur", 20),
        Item(Seller.B, ItemCategory.VETEMENTS, "Casquette MAGA", 5),
        Item(Seller.C, ItemCategory.JARDINAGE, "Sécateur", 15),
        Item(Seller.A, ItemCategory.AMEUBLEMENT, "Rideaux", 10),
        Item(Seller.B, ItemCategory.BRICOLAGE, "Marteau perforateur", 50),
        Item(Seller.A, ItemCategory.VETEMENTS, "Chapeau melon", 50),
        Item(Seller.C, ItemCategory.BRICOLAGE, "Lunettes de protection", 12),
        Item(Seller.B, ItemCategory.AMEUBLEMENT, "Table basse verre", 25),
        Item(Seller.A, ItemCategory.BRICOLAGE, "Perseuse sans fil 12V", 15),
        Item(Seller.C, ItemCategory.AMEUBLEMENT, "Commode en pin", 80),
        Item(Seller.B, ItemCategory.VETEMENTS, "Veste polaire bleue", 15),
        Item(Seller.A, ItemCategory.JARDINAGE, "Arrosoir 20L", 8),
        Item(Seller.B, ItemCategory.BRICOLAGE, "Echaffaudage", 100),
        Item(Seller.C, ItemCategory.JARDINAGE, "Paire de gants de jardinage", 10),
        Item(Seller.A, ItemCategory.VETEMENTS, "Lot de 3 T-shirts taille S", 25),
        Item(Seller.A, ItemCategory.AMEUBLEMENT, "Chaise à bascule", 55),
        Item(Seller.B, ItemCategory.JARDINAGE, "Ramasse-feuilles", 30)
       ]


def get_revenue (item:Item) -> float:
    '''
    Returns the sale price of the item
    '''
    if item is None: return 0
    return ITEM_TO_REVENUE.get(item.label, 0)

ITEM_TO_REVENUE:dict[str, float] = {
    "Jean taille L":12,
    "Tapis en laine":20,
    "Paire de gants de jardinage renforcés":10,
    "Chevilles placo x 100":10,
    "Protections auditives":20,
    "Bottes de cuir":22,
    "Coussins brodés (x2)":10,
    "Chaises en paille (x4)":50,
    "Disqueuse D125":0,
    "Taille-haies":50,
    "Chapeau de paille":0,
    "Pulvérisateur":5,
    "Casquette MAGA":0,
    "Sécateur":15,
    "Rideaux":5,
    "Marteau perforateur":50,
    "Chapeau melon":60,
    "Lunettes de protection":10,
    "Table basse verre":25,
    "Perseuse sans fil 12V":15,
    "Commode en pin":80,
    "Veste polaire bleue":5,
    "Arrosoir 20L":0,
    "Echaffaudage":90,
    "Paire de gants de jardinage":5,
    "Chaise à bascule":60,
    "Ramasse-feuilles":30,
}


