TYPE = "type"
DEF = "def"
ARGS = "agrs"
RETURN = "return"
IMPORT = "import"

modules = {
    "linear_search_list": {
        TYPE: "function",
        DEF: "linear_search",
        ARGS: "haystack: List[int], needle: int",
        RETURN: "bool",
        IMPORT: ["from typing import List"]
    },

   "binary_search_list": {
        TYPE: "function",
        DEF: "binary_search",
        ARGS: "haystack: List[int], needle: int",
        RETURN: "bool",
        IMPORT: ["from typing import List"]
   },

   "two_crystal_balls": {
        TYPE: "function",
        DEF: "two_crystal_balls",
        ARGS: "breaks: List[bool]",
        RETURN: "int",
        IMPORT: ["from typing import List"]
   },
}
    
