import re
from typing import Optional


class BinaryNode:
   def __init__(self, value:int=0, left:Optional['BinaryNode']=None, right:Optional['BinaryNode']=None):
      self.value = value
      self.left = left
      self.right = right

   @classmethod
   def create(cls, value: Optional[int]):
      if value is None:
         return None
      else:
         return cls(value)

   @classmethod
   def cast(cls, value: Optional['BinaryNode']) -> 'BinaryNode':
      assert value is not None, "Fail to cast to BinaryNode"
      return value


def form_binary_tree(values: list[Optional[int]]) -> Optional[BinaryNode]:
   if not values:
      return None

   head = BinaryNode.create(values.pop(0))
   next_node: list[Optional[BinaryNode]] = [head]
   node_index = 0

   while values:
      node = next_node.pop(0)
      assert node is not None, f"Node at index {node_index} should not be None"

      assert len(values) > 1, "Missing child nodes"
      node.left = BinaryNode.create(values.pop(0))
      node.right = BinaryNode.create(values.pop(0))
      node_index += 2

      if node.left:
         next_node.append(node.left)
      if node.right:
         next_node.append(node.right)

   return head

def to_bfs(tree: Optional[BinaryNode]) -> list[Optional[int]]:
   if tree is None:
      return []
   nodes: list[Optional[BinaryNode]] = [tree]
   result = []
   while nodes:
      node = nodes.pop()
      result.append(node.value if node is not None else None)
      if node:
         nodes.append(node.left)
         nodes.append(node.right)
   return result


def find_node_by_index(tree: Optional[BinaryNode], node_index: int) -> BinaryNode:
   nodes: list = [tree]
   index = 0
   while index < node_index:
      nodes.append(nodes[index].left)
      nodes.append(nodes[index].right)
      index += 1
   return nodes[node_index]
