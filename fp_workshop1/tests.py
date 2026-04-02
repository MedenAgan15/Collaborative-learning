import unittest
import datetime

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
import files

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
                  banner:str,
                  title:str=""):
        self.function = tested_function
        self.solution_function = solution_function
        self.banner=banner
        self.title=title

class TestBase(unittest.TestCase):

    def __init__ (self, name:str) -> None:
        super().__init__ ()
        self.name= name

    def list_comparator (self, expected:list[Item], actual:list[Item]) -> None:
        self.assertEqual(expected, actual, "La liste produite ne correspond pas au résultat attendu")

    def test_func(self, function_ctx:FunctionContext, comparator:callable=list_comparator) -> list[Item]:

        print_banner(function_ctx.banner)

        if function_ctx.function is not None:

            with files.open_result_file(self.name, function_ctx.title) as file:
                try:
                    file.write (f"TEST du {str(datetime.datetime.now())}")
                    file.write(f"\n{function_ctx.banner}")
                    file.flush()
                
                    all_items:list[Item] = refs.get_all_items()
                    cloned_list:list[Item] = list(all_items)

                    actual:list[Item] = function_ctx.function(all_items)                    
                    file.write (f"\nRESULTAT PRODUIT")
                    files.write(actual, file)
                    file.flush()

                    expected:list[Item] = function_ctx.solution_function(cloned_list)
                    file.write ("\nRESULTAT ATTENDU")
                    files.write(expected,file)
                    file.flush()

                    comparator(expected, actual)
                    print("> Le résultat produit est conforme à l'attendu")  

                    self.assertEqual(cloned_list, all_items, "Attention, la liste initiale a été modifiée !")
                    print("> Test achevé avec succès")  

                    return actual  
                except NotImplementedError as e:
                    print(f"> Test non réalisé : {e}")       
                    file.write (f"> Test non réalisé : {e}")  
                    return None   

class TestFilter(TestBase):
    
    def __init__ (self) -> None:
        super().__init__("test_filters")

    def run(self, filtering_classic_func:callable, filtering_studied_func:callable, filtering_studied_lambda_func:callable):
        self.test_func(FunctionContext(filtering_classic_func, s1.filter_items_classic,'Filtrage "classique" des objets', 'classic'), self.list_comparator)
        self.test_func(FunctionContext(filtering_studied_func, s1.filter_items_with_filter,'Filtrage des objets avec la fonction native "filter"', 'with_filter'), self.list_comparator)
        self.test_func(FunctionContext(filtering_studied_lambda_func, s1.filter_items_with_filter_and_lambda,'Filtrage des objets avec la fonction native "filter" et lambda','lambda'), self.list_comparator)

class TestMap(TestBase):

    def __init__ (self) -> None:
        super().__init__("test_maps")

    def run(self, mapping_classic_ctx:callable, mapping_studied_ctx:callable):
        self.test_func(FunctionContext(mapping_classic_ctx, s2.apply_taxes_classic,'Application de la taxe par voie "classique"','classic'), self.list_comparator)
        self.test_func(FunctionContext(mapping_studied_ctx, s2.apply_taxes_with_map,'Application de la taxe avec la fonction native "map"','with_map'), self.list_comparator)

class TestSorting(TestBase):

    def __init__ (self) -> None:
        super().__init__("test_sorting")

    def run(self, sorting_classic_func:callable, sorting_studied_func:callable):
        self.test_func(FunctionContext(sorting_classic_func, s3.sort_by_category_with_list,'Tri "classique"', 'with_sort'), self.list_comparator)
        self.test_func(FunctionContext(sorting_studied_func, s3.sort_by_category_with_sorted,'Tri avec la fonction native "sorted"','with_sorted'), self.list_comparator)

class _dict_comparator (TestBase) :
    def compare (self, expected:dict[str, Iterable[Item]], actual:dict[str, Iterable[Item]]) -> None:
        
        self.assertEqual(set(expected.keys()) , set(actual.keys()), "Le résultat attendu n'est pas celui espéré.")

        for category_name in expected.keys():
            expected_list:list[Item] = list.sort(expected[category_name], key = lambda i : i.label)
            actual_list:list[Item] = list.sort(actual[category_name], key = lambda i : i.label)
            self.assertEqual(expected_list, actual_list,f"Les items de la catégorie {category_name} ne correspondent pas à ceux attendus")

    def print_category_items (self, category_key:str, group:list[Item]):
        print (f"CATEGORIE : {category_key}")
        print_items(group)

class TestGroupBy(_dict_comparator):

    def __init__ (self) -> None:
        super().__init__("test_groupby")        

    def run (self, group_by_classic_func:callable, group_by_studied_with_itertools_func:callable) -> None:
        self.test_func(FunctionContext(group_by_classic_func, s4.groupby_category_classic,'Groupement "classique"', 'classic'), self.compare)
        self.test_func(FunctionContext(group_by_studied_with_itertools_func, s4.groupby_category_with_itertools,'Groupement avec la fonction "itertools.groupby"', 'groupby'), self.compare)

class TestCombine(_dict_comparator):

    def __init__ (self) -> None:
        super().__init__("test_combine")

    def run (self, combine:callable) -> None:
        self.test_func(FunctionContext(combine, s5.combine,'Combinaison','combine'), self.compare)        

class TestReduce(TestBase):

   def __init__ (self) -> None:
        super().__init__("test_reduce")

   def array_comparator (self, expected:array, actual: array) -> None:
       return expected == actual
   
   def print_revenues (self, result:array) -> None :
    
        if result is None : return

        for seller_enum_name, seller_enum_member in refs.Seller.__members__.items() :
            if seller_enum_member != refs.Seller.NOONE:
                print (f"Recette de {seller_enum_name} : {result[refs.Seller.get_index(seller_enum_member)]} €")

   def run (self, compute_revenue_classic:callable, compute_revenue_studied: callable, compute_revenue_recursive : callable) -> None:
        
        result:list[Item] = self.test_func(FunctionContext(compute_revenue_classic, s6.compute_revenue_classic,'Réduction "classique"', 'classic'), self.array_comparator)
        self.print_revenues(result)

        result:list[Item] = self.test_func(FunctionContext(compute_revenue_studied, s6.compute_revenue_studied,'Réduction avec la fonction "itertools.reduce"', 'with_itertools'), self.array_comparator)
        self.print_revenues(result)

        result:list[Item] = self.test_func(FunctionContext(compute_revenue_recursive, s6.compute_revenue_studied,'Réduction avec approche récursive', 'recursive'), self.array_comparator)
        self.print_revenues(result)
       
       
            


