"""
LALR’s contextual lexer
=======================

This example showcases LALR's contextual lexer by parsing a toy configuration language where the NAME and VALUE terminals overlap. Unlike a basic lexer, which might cause parse errors by arbitrarily choosing tokens, Lark's LALR(1) algorithm correctly predicts which token to expect, ensuring a correct parse. Alternatively, the Earley algorithm can handle more cases but with a performance trade-off. See examples/conf_earley.py for details.







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
    """, parser="lalr")


sample_conf = """
[bla]
a=Hello
this="that",4
empty=
"""

print(parser.parse(sample_conf).pretty())
