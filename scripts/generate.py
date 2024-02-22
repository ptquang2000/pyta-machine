import os
import dsa

script_path = os.path.dirname(__file__)
work_path = os.path.join(script_path, '..')
tests_path = os.path.join(work_path, 'tests')

day_dirs = [dir_name for dir_name in os.listdir(work_path) if 'day' == dir_name[0:3]]
today_dir = "day" + str(len(day_dirs) + 1)
try:
    today_path = os.path.join(work_path, today_dir)
    os.mkdir(today_path)
except FileExistsError:
    print(f"Directory '{today_path}' has already existed")
    exit(1)

def generate_method(props):
    body = "pass"
    if props[dsa.RETURN] == "bool":
        body = "return False" 
    elif props[dsa.RETURN] == "int":
        body = "return 0" 

    request_pkgs = ''
    if dsa.IMPORT in props:
        for pkg in props[dsa.IMPORT]:
            request_pkgs += f"{pkg}\n"

    return f'''{request_pkgs}
def {props[dsa.DEF]}({props[dsa.ARGS]}) -> {props[dsa.RETURN]}:

    {body}
'''

def add_import_pkg(pkg, att):
    return f'''
from {today_dir}.{pkg} import {att}
'''

os.chdir(today_path)
for module, props in dsa.modules.items():
    module_path = os.path.join(today_path, f"{module}.py")
    with open(module_path, 'w') as f:
        if props[dsa.TYPE] == "function":
            f.write(generate_method(props))
    
os.chdir(tests_path)
tests_init_file = os.path.join(tests_path, "__init__.py")
with open(tests_init_file, 'w') as f:
    for module, props in dsa.modules.items():
        f.write(add_import_pkg(f"{module}", props[dsa.DEF]))