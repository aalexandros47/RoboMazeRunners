'''
Imports necessary modules: This includes custom modules for reading files, parsing sentences, handling logic (such as different types of logical sentences), and reasoning methods (truth tables, forward chaining, and backward chaining).
main function:
File Reading: It reads a file specified by the user to retrieve logical statements (tell) and a query (query).
Symbol and Sentence Extraction: Extracts symbols and sentences from the tell part of the file.
Symbol Dictionary Creation: Creates a dictionary where each unique symbol from the extracted data is stored as a Symbol object.
Knowledge Base Creation: Transforms the extracted sentences into a structured knowledge base of logical sentences.
Query Parsing: Converts the query into a structured logical format suitable for evaluation.
Model Check: Checks if the knowledge base entails the query using the specified reasoning method.
Reasoning Method Execution:
Depending on the method specified (TT for truth table, FC for forward chaining, BC for backward chaining), the script performs the relevant logical reasoning to evaluate whether the knowledge base entails the query. It prints the results of this evaluation.
Command-line Interface: The script is intended to be run from the command line, taking a filename and a method as arguments. It then calls the main function with these arguments to execute the logic processing.
'''



import sys
from Reader import *
from sentence_transformers import *
from logic import *
from truthtable import *
from backward_chaining import *
from forward_chaining import *
import tkinter as tk
from truthtable_gui import TruthTableGUI  # Import the GUI module

def main(filename, method, use_gui=False):
    # Read File
    tell, query = read(filename)

    # Extract symbol
    symbols, sentences = extract_symbols_and_sentences(tell)

    # Create a dictionary to hold Symbol instances
    symbol_objects = {}

    # Create a Symbol instance for each unique symbol and store it in the dictionary
    for symbol in symbols:
        symbol_objects[symbol] = Symbol(symbol)

    knowledge_base = create_knowledge_base(sentences)  # Transform sentence into logical sentence
    query_sentence = parse(query)

    # Model Check
    is_Valid = model_check(knowledge_base, query_sentence)
    # Output the results
    print('\nResults:')
    if method == "TT":
        if use_gui:
            root = tk.Tk()
            app = TruthTableGUI(root, symbols, knowledge_base, query_sentence)
            root.mainloop()
        else:
            # Create a TruthTable instance
            truth_table = TruthTable(symbols, knowledge_base, query_sentence)
            entailed_symbols = truth_table.get_entailed_symbols()
            print(entailed_symbols)
            print(truth_table)
    elif method == "FC":
        # Forward Chaining
        fc = ForwardChaining(knowledge_base, query)
        fc_result = fc.solve()
        print(fc_result)
    elif method == "BC":
        # Backward Chaining
        bc = BackwardChaining(knowledge_base, query)
        bc_result = bc.solve()
        print(bc_result)

if __name__ == "__main__":
    filename = sys.argv[1]
    method = sys.argv[2]
    use_gui = '--gui' in sys.argv
    main(filename, method, use_gui)
