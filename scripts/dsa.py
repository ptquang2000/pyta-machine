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

    "list_node": {
        TYPE: "class",
        DEF: "ListNode",
        PROPERTIES: [
            {NAME: "value", VALUE: "None"},
            {NAME: "next", VALUE: "None"},
            {NAME: "prev", VALUE: "None"},
        ]
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

    "array_list": {
        TYPE: "class",
        DEF: "Stack",
        PROPERTIES: [
            LENGTH_PROPERTY,
        ],
        METHODS: LIST_INTERFACE,
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
    }
}

