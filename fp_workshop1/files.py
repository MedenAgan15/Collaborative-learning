import os
import refs

def create_result_files_home () -> str:
    '''
    Creates the directory storing all result files
    '''
    current_dir:str = os.getcwd()
    result_dir:str = f"{current_dir}/tmp"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    return result_dir

def open_result_file (step:str) :
    result_file_path = os.path.join(create_result_files_home(), f'{step}.txt')
    print (f"> Fichier résultat : {result_file_path}")
    return open (result_file_path, "w")

def write(items:list[refs.Item], file) -> None :
    if items is None or file is None: return
    file.write("\n")
    file.write('\n'.join(list (map (lambda i : refs.convert_item_to_string(i), items))))
