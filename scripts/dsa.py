TYPE = "type"
DEF = "def"
ARGS = "agrs"
RETURN = "return"
IMPORT = "import"
PROPERTIES = "properties"
NAME = "name"
VALUE = "value"
METHODS = "methods"
FUNCTION = "function"

LENGTH_PROPERTY = {
    NAME: "length",
    VALUE: '0',
}

LIST_INTERFACE = [{ 
    DEF: "prepend",
    ARGS: "item",
    RETURN: "None",
}, {
    DEF: "insertAt",
    ARGS: "item, idx",
    RETURN: "None",
}, {
    DEF: "append",
    ARGS: "item",
    RETURN: "None",
}, {
    DEF: "remove",
    ARGS: "item",
    RETURN: "None",
}, {
    DEF: "get",
    ARGS: "idx",
    RETURN: "None",
}, {
    DEF: "removeAt",
    ARGS: "idx",
    RETURN: "None",
}]

modules = {
    "linear_search_list": {
        TYPE: "function",
        DEF: "linear_search",
        ARGS: "haystack, needle",
        RETURN: "bool",
    },

    "binary_search_list": {
        TYPE: "function",
        DEF: "binary_search",
        ARGS: "haystack, needle",
        RETURN: "bool",
    },

    "two_crystal_balls": {
        TYPE: "function",
        DEF: "two_crystal_balls",
        ARGS: "breaks",
        RETURN: "int",
    },

    "bubble_sort": {
        TYPE: "function",
        DEF: "bubble_sort",
        ARGS: "arr",
        RETURN: "None",
    },

    "array_dutch_flag_partition": {
        TYPE: "function",
        DEF: "dutch_flag_partition",
        ARGS: "pivot_idx, A",
        RETURN: "None",
    },

    "array_plus_one": {
        TYPE: "function",
        DEF: "plus_one",
        ARGS: "A",
        RETURN: "list",
    },

    "array_multiply": {
        TYPE: "function",
        DEF: "multiply",
        ARGS: "num1, num2",
        RETURN: "list",
    },

    "array_can_reach_end": {
        TYPE: "function",
        DEF: "can_reach_end",
        ARGS: "A",
        RETURN: "bool",
    },

    "array_delete_duplicates": {
        TYPE: "function",
        DEF: "delete_duplicates",
        ARGS: "A",
        RETURN: "int",
    },

    "array_buy_and_sell_stock_once": {
        TYPE: "function",
        DEF: "buy_and_sell_stock_once",
        ARGS: "prices",
        RETURN: "int",
    },

    "array_buy_and_sell_stock_twice": {
        TYPE: "function",
        DEF: "buy_and_sell_stock_twice",
        ARGS: "prices",
        RETURN: "int",
    },

    "array_generate_primes": {
        TYPE: "function",
        DEF: "generate_primes",
        ARGS: "n",
        RETURN: "list",
    },

    "array_apply_permutation": {
        TYPE: "function",
        DEF: "apply_permutation",
        ARGS: "perm, A",
        RETURN: "None",
    },

    "array_next_permutation": {
        TYPE: "function",
        DEF: "next_permutation",
        ARGS: "perm",
        RETURN: "list",
    },

    "queue": {
        TYPE: "class",
        DEF: "Queue",
        PROPERTIES: [
            LENGTH_PROPERTY,
        ],
        METHODS: [{ 
            DEF: "enqueue",
            ARGS: "item",
            RETURN: "None",
        }, {
            DEF: "deque",
            ARGS: "",
            RETURN: "None",
            }, {
            DEF: "peek",
            RETURN: "None",
            ARGS: "",
        }]
    },

    "stack": {
        TYPE: "class",
        DEF: "Stack",
        PROPERTIES: [
            LENGTH_PROPERTY,
        ],
        METHODS: [{ 
            DEF: "push",
            ARGS: "item",
            RETURN: "None",
        }, {
            DEF: "pop",
            ARGS: "",
            RETURN: "None",
            }, {
            DEF: "peek",
            RETURN: "None",
            ARGS: "",
        }]
    },

    "maze_solver": {
        TYPE: "function",
        DEF: "solve",
        ARGS: "maze, wall, start, end",
        RETURN: "None",

    },

    "quick_sort": {
        TYPE: "function",
        DEF: "quick_sort",
        ARGS: "arr",
        RETURN: "None",
    },

    "doubly_linked_list": {
        TYPE: "class",
        DEF: "DoublyLinkedList",
        PROPERTIES: [
            LENGTH_PROPERTY,
        ],
        METHODS: LIST_INTERFACE,
    }
}

