import sys
import unittest

def main():
    from scripts.dsa import modules

    modules = {module.lower().replace('_', ''): module for module in modules.keys()}
    args = [argv.lower().replace('_', '') for argv in sys.argv[1:]]

    request_modules = set()
    for module_key in modules.keys():
        for arg in args:
            if arg not in module_key: continue
            request_modules.add(modules[module_key])

    sys.argv = [sys.argv[0]]
    for request_module in request_modules:
        pkg_name = f"tests.test_{request_module}"
        unittest.main(pkg_name)

if __name__ == "__main__":
    main()
