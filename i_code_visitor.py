import antlr4 as antlr4
from antlr_gen.decafLexer import decafLexer
from antlr_gen.decafListener import decafListener
from antlr_gen.decafParser import decafParser
from antlr_gen.decafVisitor import decafVisitor
from antlr4.tree.Trees import Trees
import sys

import codecs

# we are reserving the registers available for the operations
from logic.registry_control import reg_controller
# for the labels of the registers we are using in the forks
from logic.jump_control import label_controller
# import the tables we are going to use to check
from tables import Tabla_simbolos, Tabla_tipos, Tabla_ambitos

class NewVisitor(decafVisitor):
    # declare the tables
    t_simbolos = 0
    t_tipos = 0
    t_ambitos = 0
    controller = reg_controller()
    l_controller = label_controller()

    # lines
    line = ''

    def visitAll(self, ctx):
        self.generate_var_declr()
        self.visitChildren(ctx)
        return 0

    # -------------------------------------------- DECLARATION ---------------------------------------------- 
    # METHOD
    def visitMethoDeclaration(self, ctx):
        name = ctx.ID().getText()
        # START
        self.line += str(name) + ":\n"
        self.line += "func start\n"
        # CHILDREN
        self.visitChildren(ctx)
        # END
        self.line += "func end\n"
        return 0

    # VARIABLE
    def visitVarDeclaration(self, ctx):
        return 0

    # STRUCT
    def visitStructDeclaration(self, ctx):
        return 0

    # -------------------------------------------- STATEMENT ---------------------------------------------- 
    # IF
    def visitIfstmt(self, ctx):
        reg = self.visit(ctx.expression())
        # in case it is not a reg
        if reg in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == reg:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the reg
            reg = str(scope_name)+"_"+str(reg)

        if reg in self.controller.registers:
            self.controller.free(reg)
        
        # GET IF STAMENT COMPLETE
        label = self.l_controller.reserve()
        self.line += "if " + str(reg) + " jump " + str(label) + "\n"

        # free the reg
        if reg in self.controller.registers:
            self.controller.free(reg)
        
        if ctx.else_block:
            # generate a new label for the jump
            else_label = self.l_controller.reserve()
            self.line += "else jump " + str(else_label) + "\n"
        # GENERATE CODE INSIDE IF BLOCK
        self.line += str(label) + ":\n"
        self.visit(ctx.if_block)
        self.line += "label end\n"
        # GENERATE CODE INSIDE ELSE BLOCK
        if ctx.else_block:
            self.line += str(else_label) + ":\n"
            self.visit(ctx.else_block)
            self.line += "label end\n"
        return 0

    # WHILE
    def visitWhilestmt(self, ctx):
        reg = self.visit(ctx.expression())
        # in case it is not a reg
        if reg in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == reg:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the reg
            reg = str(scope_name)+"_"+str(reg)

        if reg in self.controller.registers:
            self.controller.free(reg)

        # label for the code exec
        block_label = self.l_controller.reserve()
        self.line += "if " + str(reg) + " jump " + str(block_label) + "\n"
        
        # GENERATE CODE INSIDE IF BLOCK
        self.line += str(block_label) + ":\n"
        self.visit(ctx.condition)
        # jump back
        reg = self.visit(ctx.expression())
        self.line += "if " + str(reg) + " jump " + str(block_label) + "\n"
        self.line += "label end\n"

        if reg in self.controller.registers:
            self.controller.free(reg)
        
        return 0

    # RETURN
    def visitReturnstmt(self, ctx):
        if ctx.expression:
            # always returns in r1
            reg = self.visit(ctx.expression())
            # in case it is not a reg
            if reg in self.t_simbolos.simbolo:
                # found a operand in the sibol table alrady instantiated so we add the ambito
                i = 0
                for value in range(len(self.t_simbolos.simbolo)):
                    if self.t_simbolos.simbolo[value] == reg:
                        i = value
                # get the scope from the same table
                scope_location = self.t_simbolos.ambito[i]
                # get the scope name
                scope_name = self.t_ambitos.nombre[scope_location]
                # alter the reg
                reg = str(scope_name)+"_"+str(reg)
            # insert line
            # asign R1
            return_reg = self.controller.find_available()
            self.controller.reserve(return_reg)
            self.line += str(return_reg) + "=" + str(reg) + "\n" 
            self.line += "return " + str(return_reg) + "\n"
            # free the reg
            if reg in self.controller.registers:
                self.controller.free(reg)
            # free the return reg
            self.controller.free(return_reg)
        return 0

    # METHOD
    def visitMethodstmt(self, ctx):
        return 0

    # LOCATION
    def visitLocationstmt(self, ctx):
        left_operand = self.visit(ctx.left)
        right_operand = self.visit(ctx.right)
        # find if it exists in the table
        if left_operand in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == left_operand:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            left_operand = str(scope_name)+"_"+str(left_operand)

        # RIGHT OPERAND
        if right_operand in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == right_operand:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            right_operand = str(scope_name)+"_"+str(right_operand)

        self.line += str(left_operand) + "=" + str(right_operand) + "\n"
       
        # free the reg
        if right_operand in self.controller.registers:
            self.controller.free(right_operand)

        return 0

    # def visitExpressionstmt(self, ctx):
    #     self.visitChildren(ctx)
    #     return 0

    # -------------------------------------------- LOCATION ---------------------------------------------- 
    def visitLocation(self, ctx):
        value = ctx.getText()
        return value

    # -------------------------------------------- EXPRESSION ---------------------------------------------- 
    # def visitMethodexpr(self, ctx):
    #     self.visitChildren(ctx)
    #     return 0

    def visitP_arith_op_expr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if right == None:
            right = self.controller.pop()
        if left == None:
            left = self.controller.pop()
        # ALLOCATE A REGISTER
        if left in self.controller.registers:
            self.controller.free(left)
        
        # case it is a instantiated variable
        if left in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == left:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            left = str(scope_name)+"_"+str(left)

        # RIGHT OPERAND
        if right in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == right:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            right = str(scope_name)+"_"+str(right)
        
        reg = self.controller.find_available()
        self.controller.reserve(reg)
        # line
        self.line += str(reg) + "=" + str(left) + str(ctx.p_arith_op().getText()) + str(right) + "\n"
        return reg

    def visitArith_op_expr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if right == None:
            right = self.controller.pop()
        if left == None:
            left = self.controller.pop()
        # ALLOCATE A REGISTER
        # if the left is a register free it
        if left in self.controller.registers:
            self.controller.free(left)

        # case it is a instantiated variable
        if left in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == left:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            left = str(scope_name)+"_"+str(left)

        # RIGHT OPERAND
        if right in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == right:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            right = str(scope_name)+"_"+str(right)

        reg = self.controller.find_available()
        self.controller.reserve(reg)
        # line
        self.line += str(reg) + "=" + str(left) + str(ctx.arith_op().getText()) + str(right) + "\n"
        return reg

    def visitRel_op_expr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if right == None:
            right = self.controller.pop()
        if left == None:
            left = self.controller.pop()
        # ALLOCATE A REGISTER
        if left in self.controller.registers:
            self.controller.free(left)

        # case it is a instantiated variable
        if left in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == left:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            left = str(scope_name)+"_"+str(left)

        # RIGHT OPERAND
        if right in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == right:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            right = str(scope_name)+"_"+str(right)

        reg = self.controller.find_available()
        self.controller.reserve(reg)
        # line
        self.line += str(reg) + "=" + str(left) + str(ctx.rel_op().getText()) + str(right) + "\n"
        return reg

    def visitEq_op_expr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if right == None:
            right = self.controller.pop()
        if left == None:
            left = self.controller.pop()
        # ALLOCATE A REGISTER
        if left in self.controller.registers:
            self.controller.free(left)
        
        # case it is a instantiated variable
        if left in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == left:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            left = str(scope_name)+"_"+str(left)

        # RIGHT OPERAND
        if right in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == right:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            right = str(scope_name)+"_"+str(right)

        reg = self.controller.find_available()
        self.controller.reserve(reg)
        # line
        self.line += str(reg) + "=" + str(left) + str(ctx.eq_op().getText()) + str(right) + "\n"
        return reg

    def visitCond_op_expr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if right == None:
            right = self.controller.pop()
        if left == None:
            left = self.controller.pop()
        # ALLOCATE A REGISTER
        if left in self.controller.registers:
            self.controller.free(left)

        # case it is a instantiated variable
        if left in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == left:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            left = str(scope_name)+"_"+str(left)

        # RIGHT OPERAND
        if right in self.t_simbolos.simbolo:
            # found a operand in the sibol table alrady instantiated so we add the ambito
            i = 0
            for value in range(len(self.t_simbolos.simbolo)):
                if self.t_simbolos.simbolo[value] == right:
                    i = value
            # get the scope from the same table
            scope_location = self.t_simbolos.ambito[i]
            # get the scope name
            scope_name = self.t_ambitos.nombre[scope_location]
            # alter the left operand with the name of the scope
            right = str(scope_name)+"_"+str(right)
        
        reg = self.controller.find_available()
        self.controller.reserve(reg)
        # line
        self.line += str(reg) + "=" + str(left) + str(ctx.cond_op().getText()) + str(right) + "\n"
        return reg

    # -------------------------------------------- METHODCALL ---------------------------------------------- 
    def visitMethodCall(self, ctx):
        method_name = ctx.ID().getText()
        # get a free register 
        reg = self.controller.find_available()
        self.controller.reserve(reg)
        if ctx.arg():
            used_args = []
            for arg in ctx.arg():
                # add the param in a registry
                register_arg = self.controller.find_available()
                self.controller.reserve(register_arg)

                found_arg = arg.getText()
                # in case the arg is a instanced variable
                for value in range(len(self.t_simbolos.simbolo)):
                    if self.t_simbolos.simbolo[value] == found_arg:
                        i = value
                        # get the scope from the same table
                        scope_location = self.t_simbolos.ambito[i]
                        # get the scope name
                        scope_name = self.t_ambitos.nombre[scope_location]
                        # alter the left operand with the name of the scope
                        found_arg = str(scope_name)+"_"+str(found_arg)

                self.line += str(register_arg) + "=" + str(found_arg) + "\n"
                used_args.append(register_arg)
            for arg in used_args:
                # free the register
                self.controller.free(arg)
        # call the function
        self.line += str(reg) + "= func_call " + str(method_name) + "\n" 
        # free pointer register
        self.controller.free(reg)
        self.visitChildren(ctx)
        return 0

    # -------------------------------------------- LITERAL ---------------------------------------------- 
    def visitLiteral(self, ctx):
        value = self.visitChildren(ctx)
        return value

    def visitInt_Literal(self, ctx):
        value = ctx.NUM()
        return value

    def visitChar_Literal(self, ctx):
        value = ctx.CHAR()
        return value
    
    def visitBool_Literal(self, ctx):
        value = ctx.getText()
        if value == 'true':
            return 1
        if value == 'false':
            return 0

    # -------------------------------------------- other crappers ---------------------------------------------- 

    def insert_tables(self, t_simbolos, t_tipos, t_ambitos):
        self.t_simbolos = t_simbolos
        self.t_tipos = t_tipos
        self.t_ambitos = t_ambitos
    
    def __init__(self):
        self.t_simbolos = []
        self.t_tipos = []
        self.t_ambitos = []

    def clear_tables(self):
        self.t_simbolos = 0
        self.t_tipos = 0
        self.t_ambitos = 0

    def conn(self):
        return self.line

    def generate_var_declr(self):
        # DATA TAG
        self.line += "DATA START\n"
        # iterate over every value in the simbol table
        for value in range(len(self.t_simbolos.t_id)):
            # get the type of the variable 
            t_type = self.t_simbolos.tipo[value]
            var_type = self.t_tipos.nombre[t_type]
            # get the scope the variable is found in
            t_scope = self.t_simbolos.ambito[value]
            scope = self.t_ambitos.nombre[t_scope]
            # get the name of the variable we are instantiating
            name = self.t_simbolos.simbolo[value]

            # insert the var declaration 
            self.line += str(scope) + "_" + str(name) + ":" + str(var_type) + "\n"

        # TEXT TAG
        self.line += "TEXT START\n"