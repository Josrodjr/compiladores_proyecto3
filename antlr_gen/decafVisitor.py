# Generated from ../decaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafParser import decafParser
else:
    from decafParser import decafParser

# This class defines a complete generic visitor for a parse tree produced by decafParser.

class decafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by decafParser#program.
    def visitProgram(self, ctx:decafParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#declaration.
    def visitDeclaration(self, ctx:decafParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#varDeclaration.
    def visitVarDeclaration(self, ctx:decafParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#structDeclaration.
    def visitStructDeclaration(self, ctx:decafParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#varType.
    def visitVarType(self, ctx:decafParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#methoDeclaration.
    def visitMethoDeclaration(self, ctx:decafParser.MethoDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#methodType.
    def visitMethodType(self, ctx:decafParser.MethodTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#parameter.
    def visitParameter(self, ctx:decafParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#parametertype.
    def visitParametertype(self, ctx:decafParser.ParametertypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#block.
    def visitBlock(self, ctx:decafParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#ifstmt.
    def visitIfstmt(self, ctx:decafParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#whilestmt.
    def visitWhilestmt(self, ctx:decafParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#returnstmt.
    def visitReturnstmt(self, ctx:decafParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#methodstmt.
    def visitMethodstmt(self, ctx:decafParser.MethodstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#blockstmt.
    def visitBlockstmt(self, ctx:decafParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#locationstmt.
    def visitLocationstmt(self, ctx:decafParser.LocationstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#expressionstmt.
    def visitExpressionstmt(self, ctx:decafParser.ExpressionstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#location.
    def visitLocation(self, ctx:decafParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#rel_op_expr.
    def visitRel_op_expr(self, ctx:decafParser.Rel_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#minusexpr.
    def visitMinusexpr(self, ctx:decafParser.MinusexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#cond_op_expr.
    def visitCond_op_expr(self, ctx:decafParser.Cond_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#literalexpr.
    def visitLiteralexpr(self, ctx:decafParser.LiteralexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#factoexpr.
    def visitFactoexpr(self, ctx:decafParser.FactoexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#methodexpr.
    def visitMethodexpr(self, ctx:decafParser.MethodexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#locexpr.
    def visitLocexpr(self, ctx:decafParser.LocexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#corchexpr.
    def visitCorchexpr(self, ctx:decafParser.CorchexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#p_arith_op_expr.
    def visitP_arith_op_expr(self, ctx:decafParser.P_arith_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#eq_op_expr.
    def visitEq_op_expr(self, ctx:decafParser.Eq_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#arith_op_expr.
    def visitArith_op_expr(self, ctx:decafParser.Arith_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#methodCall.
    def visitMethodCall(self, ctx:decafParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#arg.
    def visitArg(self, ctx:decafParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#p_arith_op.
    def visitP_arith_op(self, ctx:decafParser.P_arith_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#arith_op.
    def visitArith_op(self, ctx:decafParser.Arith_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#rel_op.
    def visitRel_op(self, ctx:decafParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#eq_op.
    def visitEq_op(self, ctx:decafParser.Eq_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#cond_op.
    def visitCond_op(self, ctx:decafParser.Cond_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#literal.
    def visitLiteral(self, ctx:decafParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#int_Literal.
    def visitInt_Literal(self, ctx:decafParser.Int_LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#char_Literal.
    def visitChar_Literal(self, ctx:decafParser.Char_LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#bool_Literal.
    def visitBool_Literal(self, ctx:decafParser.Bool_LiteralContext):
        return self.visitChildren(ctx)



del decafParser