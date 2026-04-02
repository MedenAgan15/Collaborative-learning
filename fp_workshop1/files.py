from io import TextIOWrapper
import os
import refs
from array import array

def create_result_files_home () -> str:
    '''
    Creates the directory storing all result files
    '''
    current_dir:str = os.getcwd()
    result_dir:str = f"{current_dir}/tmp"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    return result_dir

def open_result_file (step:str, title:str) :

    suffix = ""
    if title != "":
        suffix= f'_{title}'

    result_file_path = os.path.join(create_result_files_home(), f'{step}{suffix}.txt')
    print (f"> Fichier résultat : {result_file_path}")
    return open (result_file_path, "w")

def write(items, file) -> None :
    
    if items is None or file is None: 
        return
    
    file.write("\n")
    if isinstance(items, list) :        
        file.write('\n'.join(list (map (lambda i : refs.convert_item_to_string(i), items))))
    elif isinstance(items, dict):
        for k,v in items.items() :
            file.write(f"{k}\n")
            for item in v :
                file.write(f"   {refs.convert_item_to_string(item)}\n")
    elif isinstance(items, array) :
        file.write('\n'.join(list (map (lambda i : str(i), items))))
    else :
        file.write(f"Désolé, ce type de données n'est pas pris en charge : {type(items)}")
        file.flush()
