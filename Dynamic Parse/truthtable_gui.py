import tkinter as tk
from tkinter import ttk
from truthtable import TruthTable

class TruthTableGUI:
    def __init__(self, master, symbols, knowledgeBase, query):
        self.master = master
        self.master.title("Truth Table")
        self.truthtable = TruthTable(symbols, knowledgeBase, query)
        
        # Creating Treeview widget
        self.tree = ttk.Treeview(master)
        
        # Defining columns
        columns = [str(symbol) for symbol in self.truthtable.symbols]
        columns += [str(self.truthtable.knowledgeBase), str(self.truthtable.query)]
        
        self.tree["columns"] = columns
        self.tree["show"] = "headings"
        
        # Setting up columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        self.populate_table()
        
        self.tree.pack(expand=True, fill='both')
    
    def populate_table(self):
        for model, evaluations in self.truthtable.table:
            row = [str(model[symbol]) for symbol in self.truthtable.symbols]
            row += [str(evaluations[0])] + [str(self.truthtable.query.evaluate(model))]
            self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    from logic import Conjunction, Symbol, Implication  # Import other necessary logic components
    
    root = tk.Tk()
    
    # Example usage
    symbols = ['p', 'q']
    knowledgeBase = Conjunction(Implication(Symbol('p'), Symbol('q')), Symbol('p'))
    query = Symbol('q')
    
    app = TruthTableGUI(root, symbols, knowledgeBase, query)
    root.mainloop()
