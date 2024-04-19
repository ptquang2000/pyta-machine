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
    # The Last Algorithm Course You'll Need

    "core_linear_search_list": {
        TYPE: "function",
        DEF: "linear_search",
        ARGS: "haystack, needle",
        RETURN: "bool",
    },

    "core_binary_search_list": {
        TYPE: "function",
        DEF: "binary_search",
        ARGS: "haystack, needle",
        RETURN: "bool",
    },

    "core_two_crystal_balls": {
        TYPE: "function",
        DEF: "two_crystal_balls",
        ARGS: "breaks",
        RETURN: "int",
    },

    "core_bubble_sort": {
        TYPE: "function",
        DEF: "bubble_sort",
        ARGS: "arr",
        RETURN: "None",
    },

    "core_queue": {
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

    "core_stack": {
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

    "core_maze_solver": {
        TYPE: "function",
        DEF: "solve",
        ARGS: "maze, wall, start, end",
        RETURN: "None",

    },

    "core_quick_sort": {
        TYPE: "function",
        DEF: "quick_sort",
        ARGS: "arr",
        RETURN: "None",
    },

    "core_doubly_linked_list": {
        TYPE: "class",
        DEF: "DoublyLinkedList",
        PROPERTIES: [
            LENGTH_PROPERTY,
        ],
        METHODS: LIST_INTERFACE,
    },

    # Element of Programming Interviews

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

    "multi_dim_array_is_valid_sudoku": {
        TYPE: "function",
        DEF: "is_valid_sudoku",
        ARGS: "partial_assignment",
        RETURN: "bool",
    },

    "multi_dim_array_matrix_in_spiral_order": {
        TYPE: "function",
        DEF: "matrix_in_spiral_order",
        ARGS: "square_matrix",
        RETURN: "list",
    },

    "multi_dim_array_rotate_matrix": {
        TYPE: "function",
        DEF: "rotate_matrix",
        ARGS: "square_matrix",
        RETURN: "None",
    },

    "multi_dim_array_generate_pascal_triangle": {
        TYPE: "function",
        DEF: "generate_pascal_triangle",
        ARGS: "n",
        RETURN: "list",
    },

    "string_int_to_string": {
        TYPE: "function",
        DEF: "int_to_string",
        ARGS: "x",
        RETURN: "str",
    },

    "string_string_to_int": {
        TYPE: "function",
        DEF: "string_to_int",
        ARGS: "s",
        RETURN: "int",
    },

    "string_convert_base": {
        TYPE: "function",
        DEF: "convert_base",
        ARGS: "num_as_string, b1, b2",
        RETURN: "str",
    },

    "string_ss_decode_col_id": {
        TYPE: "function",
        DEF: "ss_decode_col_id",
        ARGS: "col",
        RETURN: "int",
    },

    "string_replace_and_remove": {
        TYPE: "function",
        DEF: "replace_and_remove",
        ARGS: "size, s",
        RETURN: "int",
    },

    "string_is_palindrome": {
        TYPE: "function",
        DEF: "is_palindrome",
        ARGS: "s",
        RETURN: "bool",
    },

    "string_reverse_words": {
        TYPE: "function",
        DEF: "reverse_words",
        ARGS: "s",
        RETURN: "None",
    },

    "string_look_and_say": {
        TYPE: "function",
        DEF: "look_and_say",
        ARGS: "n",
        RETURN: "str",
    },

    "string_roman_to_integer": {
        TYPE: "function",
        DEF: "roman_to_integer",
        ARGS: "s",
        RETURN: "int",
    },

    "string_snake_string": {
        TYPE: "function",
        DEF: "snake_string",
        ARGS: "s",
        RETURN: "str",
    },

    "string_string_decoding": {
        TYPE: "function",
        DEF: "string_decoding",
        ARGS: "s",
        RETURN: "str",
    },

    "string_string_encoding": {
        TYPE: "function",
        DEF: "string_encoding",
        ARGS: "s",
        RETURN: "str",
    },

    "string_rabin_karp": {
        TYPE: "function",
        DEF: "rabin_karp",
        ARGS: "t, s",
        RETURN: "int",
    },

    "linked_lists_merge_two_sorted_lists": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "merge_two_sorted_lists",
        ARGS: "L1, L2",
        RETURN: "ListNode",
    },

    "linked_lists_reverse_sublist": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "reverse_sublist",
        ARGS: "L, start, finish",
        RETURN: "ListNode",
    },

    "linked_lists_has_cycle": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "has_cycle",
        ARGS: "head",
        RETURN: "ListNode",
    },

    "linked_lists_overlapping_no_cycle_lists": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "overlapping_no_cycle_lists",
        ARGS: "L1, L2",
        RETURN: "ListNode",
    },

    "linked_lists_overlapping_lists": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "overlapping_lists",
        ARGS: "L1, L2",
        RETURN: "ListNode",
    },

    "linked_lists_deletion_from_list": {
        TYPE: "function",
        DEF: "deletion_from_list",
        ARGS: "node_to_delete",
        RETURN: "None",
    },

    "linked_lists_remove_kth_last": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "remove_kth_last",
        ARGS: "L, k",
        RETURN: "ListNode",
    },

    "linked_lists_remove_duplicates": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "remove_duplicates",
        ARGS: "L",
        RETURN: "ListNode",
    },

    "linked_lists_cyclically_right_shift_list": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "cyclically_right_shift_list",
        ARGS: "L, k",
        RETURN: "ListNode",
    },

    "linked_lists_even_odd_merge": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "even_odd_merge",
        ARGS: "L",
        RETURN: "ListNode",
    },

    "linked_lists_is_linked_list_a_palindrome": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "is_linked_list_a_palindrome",
        ARGS: "L",
        RETURN: "bool",
    },

    "linked_lists_list_pivoting": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "list_pivoting",
        ARGS: "L, x",
        RETURN: "ListNode",
    },

    "linked_lists_add_two_numbers": {
        TYPE: "function",
        IMPORT: ["from common import ListNode"],
        DEF: "add_two_numbers",
        ARGS: "L1, L2",
        RETURN: "ListNode",
    },

    "stack_evaluate_rpn_expression": {
        TYPE: "function",
        DEF: "evaluate",
        ARGS: "RPN_expression",
        RETURN: "int",
    },

    "stack_is_well_formed": {
        TYPE: "function",
        DEF: "is_well_formed",
        ARGS: "s",
        RETURN: "bool",
    },

    "stack_shortest_equivalent_path": {
        TYPE: "function",
        DEF: "shortest_equivalent_path",
        ARGS: "path",
        RETURN: "str",
    },

    "stack_examine_buildings_with_sunset": {
        TYPE: "function",
        DEF: "examine_building_with_sunset",
        ARGS: "sequence",
        RETURN: "list",
    },
}

