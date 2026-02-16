import refs
from refs import Item as Item
from proposal import e1_proposal as e1
from proposal import e2_proposal as e2
from proposal import e4_proposal as e4

def combine ():

    items:list[Item]= refs.get_all_items()
    result = e4.groupby_category_with_itertools(e2.apply_taxes_with_map(e1.filter_items_with_filter(items)))
    
    for categorie in result:
        print(f"{categorie}")
        print(refs.convert_items_to_string(result[categorie]))