"""
Earley’s dynamic lexer
======================

This example demonstrates Earley’s dynamic lexer for parsing a toy configuration language, resolving ambiguities without needing delimiters. For a faster but less powerful alternative, see the LALR contextual lexer example in examples/conf_lalr.py.







"""
from lark import Lark

parser = Lark(r"""
        start: _NL? section+
        section: "[" NAME "]" _NL item+
        item: NAME "=" VALUE? _NL

        NAME: /\w/+
        VALUE: /./+

        %import common.NEWLINE -> _NL
        %import common.WS_INLINE
        %ignore WS_INLINE
    """, parser="earley")

def test():
    sample_conf = """
[bla]

a=Hello
this="that",4
empty=
"""

    r = parser.parse(sample_conf)
    print (r.pretty())

if __name__ == '__main__':
    test()
