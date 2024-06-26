"""
Custom SPPF Prioritizer
=======================

This example demonstrates how to subclass ForestVisitor to create a custom SPPF node prioritizer for use with TreeForestTransformer.

Our prioritizer counts the number of token descendants of a node. By negating this count, the prioritizer prefers nodes with fewer token descendants, thereby selecting the more specific parse.


"""

from lark import Lark
from lark.parsers.earley_forest import ForestVisitor, TreeForestTransformer

class TokenPrioritizer(ForestVisitor):

    def visit_symbol_node_in(self, node):
        # visit the entire forest by returning node.children
        return node.children

    def visit_packed_node_in(self, node):
        return node.children

    def visit_symbol_node_out(self, node):
        priority = 0
        for child in node.children:
            # Tokens do not have a priority attribute
            # count them as -1
            priority += getattr(child, 'priority', -1)
        node.priority = priority

    def visit_packed_node_out(self, node):
        priority = 0
        for child in node.children:
            priority += getattr(child, 'priority', -1)
        node.priority = priority

    def on_cycle(self, node, path):
        raise Exception("Oops, we encountered a cycle.")

grammar = """
start: hello " " world | hello_world
hello: "Hello"
world: "World"
hello_world: "Hello World"
"""

parser = Lark(grammar, parser='earley', ambiguity='forest')
forest = parser.parse("Hello World")

print("Default prioritizer:")
tree = TreeForestTransformer(resolve_ambiguity=True).transform(forest)
print(tree.pretty())

forest = parser.parse("Hello World")

print("Custom prioritizer:")
tree = TreeForestTransformer(resolve_ambiguity=True, prioritizer=TokenPrioritizer()).transform(forest)
print(tree.pretty())

# Output:
#
# Default prioritizer:
# start
#   hello Hello
#
#   world World
#
# Custom prioritizer:
# start
#   hello_world   Hello World
