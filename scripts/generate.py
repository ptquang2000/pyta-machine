import os
import dsa

script_path = os.path.dirname(__file__)
work_path = os.path.join(script_path, '..')
test_path = os.path.join(work_path, 'test')

day_dirs = [dir_name for dir_name in os.listdir(work_path) if 'day' == dir_name[0:3]]
today_dir = "day" + str(len(day_dirs) + 1)
try:
    today_path = os.path.join(work_path, today_dir)
    os.mkdir(today_path)
except FileExistsError:
    print(f"Directory '{today_path}' has already existed")
    exit(1)

def generate_method(props):
    content = "return"
    if dsa.RETURN in props:
        if props[dsa.RETURN] == "bool":
            content = "return bool()" 
        elif props[dsa.RETURN] == "int":
            content = "return int()"
        elif props[dsa.RETURN] == "str":
            content = "return str()"
        elif props[dsa.RETURN] == "list":
            content = "return list()"

    request_pkgs = ''
    if dsa.IMPORT in props:
        for pkg in props[dsa.IMPORT]:
            request_pkgs += f"{pkg}\n"

    return f'''{request_pkgs}
def {props[dsa.DEF]}({props[dsa.ARGS]}):
    {content}
    '''

def generate_class(props):
    content = f'''
class {props[dsa.DEF]}():
    def __init__(self) -> None:
    '''

    for member in props[dsa.PROPERTIES]:
        content += f'''
        self.{member[dsa.NAME]} = {member[dsa.VALUE]}
        '''

    content += f'''
        return
    '''

    if dsa.METHODS in props:
        for method in props[dsa.METHODS]:
            args = f", {method[dsa.ARGS]}" if len(method[dsa.ARGS]) else ''
            content += f'''
    def {method[dsa.DEF]}(self{args}):
        return
            '''
    return content


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
        elif props[dsa.TYPE] == "class":
            f.write(generate_class(props))
    
os.chdir(test_path)
test_init_file = os.path.join(test_path, "__init__.py")
with open(test_init_file, 'w') as f:
    for module, props in dsa.modules.items():
        f.write(add_import_pkg(f"{module}", props[dsa.DEF]))
