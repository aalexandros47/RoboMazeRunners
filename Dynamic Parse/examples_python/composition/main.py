"""
Grammar Composition
===================

We define storage.lark, which imports csv.lark and json.lark, allowing them to be used sequentially.

In the resulting parse tree, each imported rule and terminal is automatically prefixed (with json__ or csv__), creating an implicit namespace that prevents collisions and allows both formats to coexist.

We merge the transformers from each format into a new base transformer.

The combined transformer can evaluate both JSON and CSV in the parse tree. The methods from each transformer are renamed according to their respective namespaces using the given prefixes. This approach ensures full reusability: the transformers remain unaware of whether their grammar is used directly, imported, or who is importing it.

"""
from pathlib import Path
from lark import Lark
from json import dumps
from lark.visitors import Transformer, merge_transformers

from eval_csv import CsvTreeToPandasDict
from eval_json import JsonTreeToJson

__dir__ = Path(__file__).parent

class Storage(Transformer):
    def start(self, children):
        return children

storage_transformer = merge_transformers(Storage(), csv=CsvTreeToPandasDict(), json=JsonTreeToJson())

parser = Lark.open("storage.lark", rel_to=__file__)

def main():
    json_tree = parser.parse(dumps({"test": "a", "dict": { "list": [1, 1.2] }}))
    res = storage_transformer.transform(json_tree)
    print("Just JSON: ", res)

    csv_json_tree = parser.parse(open(__dir__ / 'combined_csv_and_json.txt').read())
    res = storage_transformer.transform(csv_json_tree)
    print("JSON + CSV: ", dumps(res, indent=2))


if __name__ == "__main__":
    main()
