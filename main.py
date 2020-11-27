from tables import Tabla_simbolos, Tabla_tipos, Tabla_ambitos
import tkinter as tk					 
from tkinter import ttk 

# antlr generatio files
import antlr4 as antlr4
from antlr_gen.decafLexer import decafLexer
from antlr_gen.decafListener import decafListener
from antlr_gen.decafParser import decafParser
from antlr_gen.decafVisitor import decafVisitor
import sys

# import the custom visitor
from custom_visitor import EvalVisitor
# new vistor for the intermediate code generator
from i_code_visitor import NewVisitor

# ASM library
import asm_generation as asmlib

# 

# -------------------------------------------- instantiations  ---------------------------------------------- 


# -------------------------------------------- visitor ---------------------------------------------- 

def init_visitor():
    # abrir el archivo de prueba para tokens
    with open('test.txt', 'r') as myfile:
        data = myfile.read()

    actual_data = antlr4.InputStream(data)
    # mandar al lexer el input del inpuntstream
    lexer = decafLexer(actual_data)
    stream = antlr4.CommonTokenStream(lexer)
    parser = decafParser(stream)

    tree = parser.program()

    c_visitor = EvalVisitor()
    
    # generate the basic types
    c_visitor.t_tipos.generate_default_values()
    # generate the default ambito
    c_visitor.t_ambitos.generate_default(c_visitor.t_tipos.search_type('void'))

    # Traverse the tree
    c_visitor.visit(tree)

    # THE INTERMEDIATE CODE VISITOR

    i_visitor = NewVisitor()
    # insert the values extracted from the prev visitor 
    i_visitor.insert_tables(c_visitor.t_simbolos, c_visitor.t_tipos, c_visitor.t_ambitos)
    # visit the tree
    i_visitor.visitAll(tree)
    
    return c_visitor, i_visitor


# -------------------------------------------- root ---------------------------------------------- 

root = tk.Tk() 
root.title("yep") 
tabControl = ttk.Notebook(root) 
root.geometry("700x600")

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Codigo') 
tabControl.add(tab2, text ='Tablas de simbolos') 
tabControl.add(tab3, text ='Errores')
tabControl.add(tab4, text ='Codigo Intermedio')
tabControl.add(tab5, text = 'Codigo ARM ASM')
tabControl.pack(expand = 1, fill ="both") 

# -------------------------------------------- funcs ---------------------------------------------- 
def save_data(container):
    code_text = container.get('1.0', tk.END)
    # open file to save
    file = open('test.txt', 'w')
    file.write(code_text)

def save_asm(container):
    code_text = container.get('1.0', tk.END)
    file = open('asm.s', 'w')
    file.write(code_text)


def fill_tables(container, container_2, container_3, container_4):
    # clear the previous data in the container
    clear_input(container)
    clear_input(container_2)
    clear_input(container_3)

    # restart the values in the visitor]
    c_visitor, i_visitor = init_visitor()

    simbolos_str = "Tabla de Simbolos \n"
    tipos_str = "Tabla de Tipos \n"
    ambitos_str = "Tabla de Ambitos \n"

    simbolos_value = c_visitor.t_simbolos.return_table()
    tipos_value = c_visitor.t_tipos.return_table()
    ambitos_value = c_visitor.t_ambitos.return_table()

    # SIMBOLOS
    container.insert(tk.END, simbolos_str)
    container.insert(tk.END, simbolos_value)

    # TIPOS
    container.insert(tk.END, "\n")
    container.insert(tk.END, tipos_str)
    container.insert(tk.END, tipos_value)

    # AMBITOS
    container.insert(tk.END, "\n")
    container.insert(tk.END, ambitos_str)
    container.insert(tk.END, ambitos_value)

    # insert the errors found
    error_names = c_visitor.errors.error_names
    found_descriptions = c_visitor.errors.found_descriptions

    container_2.insert(tk.END, 'RESULTS:')

    for i in range(len(error_names)):
        # insert the error and description
        container_2.insert(tk.END, "\n")
        container_2.insert(tk.END, 'ERROR: ' + str(error_names[i]) + ' ' + 'LINE: ' + str(found_descriptions[i][0]) + ' ' + 'COLUMN: ' + str(found_descriptions[i][1]))

    # Container 3 the intermediate code generator
    # i_visitor = init_new_visitor(t1, t2, t3)
    container_3.insert(tk.END, i_visitor.conn())


    # ASM CODE INSERT
    assembly_generated = asmlib.main(i_visitor.conn())
    container_4.insert(tk.END, assembly_generated)


    

def clear_input(container):
    # container.delete(0, tk.END)
    container.delete("1.0", tk.END)

# -------------------------------------------- tab1---------------------------------------------- 
code_inserted = tk.Text(tab1)
code_inserted.grid(column=0, row=1)
# open and insert the test code found in the txt
with open('test.txt', 'r') as myfile:
    data = myfile.read()
# insert at the end
code_inserted.insert(tk.END, data)

# insert a button for saving the changes
save_button = tk.Button(tab1, text="Save Changes", command=lambda : save_data(code_inserted) )
save_button.grid(column = 0, row = 2)

# insert a button for new processing
reprocess_button = tk.Button(tab1, text="Reprocess", command=lambda: fill_tables(tables_result, errors_result, inter_code, asm_code) )
reprocess_button.grid(column = 0, row = 3)

# -------------------------------------------- tab2---------------------------------------------- 
tables_result = tk.Text(tab2)
tables_result.grid(column = 0, row = 1)

# -------------------------------------------- tab3 ----------------------------------------------
errors_result = tk.Text(tab3)
errors_result.grid(column = 0, row = 1)

# -------------------------------------------- tab4 ----------------------------------------------
inter_code = tk.Text(tab4)
inter_code.grid(column = 0, row = 1)

# -------------------------------------------- tab4 ----------------------------------------------
asm_code = tk.Text(tab5)
asm_code.grid(column = 0, row = 1)

asm_button = tk.Button(tab5, text="Save ASM", command=lambda : save_asm(asm_code) )
asm_button.grid(column = 0, row = 2)

root.mainloop() 
