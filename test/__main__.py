import sys
import unittest
import os

def main():
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    from scripts.dsa import modules

    modules = {module.lower().replace('_', ''): module for module in modules.keys()}
    args = [argv.lower().replace('_', '') for argv in sys.argv[1:]]

    request_modules = set()
    for module_key in modules.keys():
        for arg in args:
            if arg not in module_key: continue
            request_modules.add(modules[module_key])

    sys.argv = [sys.argv[0]]
    suite = unittest.TestSuite()
    for request_module in request_modules:
        pkg_name = f"test_{request_module}"
        module = __import__(pkg_name, {}, {}, ['1'])
        suite.addTest(unittest.TestLoader().loadTestsFromModule(module))

    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    main()
