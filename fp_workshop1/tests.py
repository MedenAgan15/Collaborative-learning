import unittest

from proposal import e1_proposal as s1
from proposal import e2_proposal as s2
from proposal import e3_proposal as s3
from proposal import e4_proposal as s4
from proposal import e5_proposal as s5
from proposal import e6_proposal as s6

from typing import Iterable
from array import array

import refs
from refs import Item as Item

def print_items(items:list[Item]) -> None:
    print (refs.convert_items_to_string(items))

def print_banner (title:str) -> None:
        print("------")    
        print(title.upper())    
        print("------")    
        print("") 

class FunctionContext ():

    def __init__ (self, 
                  tested_function:callable,
                  solution_function:callable, 
                  banner:str):
        self.function = tested_function
        self.solution_function = solution_function
        self.banner=banner

class TestBase(unittest.TestCase):

    def list_comparator (self, expected:list[Item], actual:list[Item]) -> None:
        self.assertEqual(expected, actual, "La liste ne correspond pas au résultat attendu")

    def test_func(self, function_ctx:FunctionContext, comparator:callable=list_comparator) -> list[Item]:

        print_banner(function_ctx.banner)

        if function_ctx.function is not None:
            try:
                all_items:list[Item] = refs.get_all_items()

                actual:list[Item] = function_ctx.function(all_items)
                expected:list[Item] = function_ctx.solution_function(all_items)

                comparator(expected, actual)

                print("> Exécution réussie : le résultat est conforme à l'attendu")  

                return actual  
            except NotImplementedError as e:
                print(f"> Exécution non réalisée : {e}")       
                return None   

class TestFilter(TestBase):
    
    def run(self, filtering_classic_func:callable, filtering_studied_func:callable, filtering_studied_lambda_func:callable):
        self.test_func(FunctionContext(filtering_classic_func, s1.filter_items_classic,'Filtrage "classique" des objets'), self.list_comparator)
        self.test_func(FunctionContext(filtering_studied_func, s1.filter_items_with_filter,'Filtrage des objets avec la fonction native "filter"'), self.list_comparator)
        self.test_func(FunctionContext(filtering_studied_lambda_func, s1.filter_items_with_filter_and_lambda,'Filtrage des objets avec la fonction native "filter" et lambda'), self.list_comparator)

class TestMap(TestBase):

    def run(self, mapping_classic_ctx:callable, mapping_studied_ctx:callable):
        self.test_func(FunctionContext(mapping_classic_ctx, s2.apply_taxes_classic,'Application de la taxe par voie "classique"'), self.list_comparator)
        self.test_func(FunctionContext(mapping_studied_ctx, s2.apply_taxes_with_map,'Application de la taxe avec la fonction native "map"'), self.list_comparator)

class TestSorting(TestBase):

    def run(self, sorting_classic_func:callable, sorting_studied_func:callable):
        self.test_func(FunctionContext(sorting_classic_func, s3.sort_by_category_with_list,'Tri "classique"'), self.list_comparator)
        self.test_func(FunctionContext(sorting_studied_func, s3.sort_by_category_with_sorted,'Tri avec la fonction native "sorted"'), self.list_comparator)

class TestGroupBy(TestBase):

    def dict_comparator (self, expected:dict[str, Iterable[Item]], actual:dict[str, Iterable[Item]]) -> None:
            
            self.assertEqual(set(expected.keys()) , set(actual.keys()), "Les catégories attendues ne correspondent pas aux catégories produites par la méthode testée")

            for category_name in expected.keys():
                expected_list:list[Item] = list.sort(expected[category_name], key = lambda i : i.label)
                actual_list:list[Item] = list.sort(actual[category_name], key = lambda i : i.label)
                self.assertEqual(expected_list, actual_list,f"Les items de la catégorie {category_name} ne correspondent pas à ceux attendus")

    def print_category_items (self, category_key:str, group:list[Item]):
        print (f"CATEGORIE : {category_key}")
        print_items(group)

    def run (self, group_by_classic_func:callable, group_by_studied_with_itertools_func:callable) -> None:
        self.test_func(FunctionContext(group_by_classic_func, s4.groupby_category_classic,'Groupement "classique"'), self.dict_comparator)
        self.test_func(FunctionContext(group_by_studied_with_itertools_func, s4.groupby_category_with_itertools,'Groupement avec la fonction "itertools.groupby"'), self.dict_comparator)
        
class TestReduce(TestBase):

   def array_comparator (self, expected:array, actual: array) -> None:
       return expected == actual
   
   def print_revenues (self, result:array) -> None :
    
        if result is None : return

        for seller_enum_name, seller_enum_member in refs.Seller.__members__.items() :
            if seller_enum_member != refs.Seller.NOONE:
                print (f"Recette de {seller_enum_name} : {result[refs.Seller.get_index(seller_enum_member)]} €")

   def run (self, reduce_classic:callable, reduce_studied: callable) -> None:
        
        result:list[Item] = self.test_func(FunctionContext(reduce_classic, s6.compute_revenue_classic,'Réduction "classique"'), self.array_comparator)
        self.print_revenues(result)
        print ("")

        result:list[Item] = self.test_func(FunctionContext(reduce_studied, s6.compute_revenue_studied,'Réduction avec la fonction "itertools.reduce"'), self.array_comparator)
        self.print_revenues(result)
       
       
            


