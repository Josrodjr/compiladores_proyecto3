# Generated from ../decaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafParser import decafParser
else:
    from decafParser import decafParser

# This class defines a complete listener for a parse tree produced by decafParser.
class decafListener(ParseTreeListener):

    # Enter a parse tree produced by decafParser#program.
    def enterProgram(self, ctx:decafParser.ProgramContext):
        pass

    # Exit a parse tree produced by decafParser#program.
    def exitProgram(self, ctx:decafParser.ProgramContext):
        pass


    # Enter a parse tree produced by decafParser#declaration.
    def enterDeclaration(self, ctx:decafParser.DeclarationContext):
        pass

    # Exit a parse tree produced by decafParser#declaration.
    def exitDeclaration(self, ctx:decafParser.DeclarationContext):
        pass


    # Enter a parse tree produced by decafParser#varDeclaration.
    def enterVarDeclaration(self, ctx:decafParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by decafParser#varDeclaration.
    def exitVarDeclaration(self, ctx:decafParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by decafParser#structDeclaration.
    def enterStructDeclaration(self, ctx:decafParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by decafParser#structDeclaration.
    def exitStructDeclaration(self, ctx:decafParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by decafParser#varType.
    def enterVarType(self, ctx:decafParser.VarTypeContext):
        pass

    # Exit a parse tree produced by decafParser#varType.
    def exitVarType(self, ctx:decafParser.VarTypeContext):
        pass


    # Enter a parse tree produced by decafParser#methoDeclaration.
    def enterMethoDeclaration(self, ctx:decafParser.MethoDeclarationContext):
        pass

    # Exit a parse tree produced by decafParser#methoDeclaration.
    def exitMethoDeclaration(self, ctx:decafParser.MethoDeclarationContext):
        pass


    # Enter a parse tree produced by decafParser#methodType.
    def enterMethodType(self, ctx:decafParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by decafParser#methodType.
    def exitMethodType(self, ctx:decafParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by decafParser#parameter.
    def enterParameter(self, ctx:decafParser.ParameterContext):
        pass

    # Exit a parse tree produced by decafParser#parameter.
    def exitParameter(self, ctx:decafParser.ParameterContext):
        pass


    # Enter a parse tree produced by decafParser#parametertype.
    def enterParametertype(self, ctx:decafParser.ParametertypeContext):
        pass

    # Exit a parse tree produced by decafParser#parametertype.
    def exitParametertype(self, ctx:decafParser.ParametertypeContext):
        pass


    # Enter a parse tree produced by decafParser#block.
    def enterBlock(self, ctx:decafParser.BlockContext):
        pass

    # Exit a parse tree produced by decafParser#block.
    def exitBlock(self, ctx:decafParser.BlockContext):
        pass


    # Enter a parse tree produced by decafParser#ifstmt.
    def enterIfstmt(self, ctx:decafParser.IfstmtContext):
        pass

    # Exit a parse tree produced by decafParser#ifstmt.
    def exitIfstmt(self, ctx:decafParser.IfstmtContext):
        pass


    # Enter a parse tree produced by decafParser#whilestmt.
    def enterWhilestmt(self, ctx:decafParser.WhilestmtContext):
        pass

    # Exit a parse tree produced by decafParser#whilestmt.
    def exitWhilestmt(self, ctx:decafParser.WhilestmtContext):
        pass


    # Enter a parse tree produced by decafParser#returnstmt.
    def enterReturnstmt(self, ctx:decafParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by decafParser#returnstmt.
    def exitReturnstmt(self, ctx:decafParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by decafParser#methodstmt.
    def enterMethodstmt(self, ctx:decafParser.MethodstmtContext):
        pass

    # Exit a parse tree produced by decafParser#methodstmt.
    def exitMethodstmt(self, ctx:decafParser.MethodstmtContext):
        pass


    # Enter a parse tree produced by decafParser#blockstmt.
    def enterBlockstmt(self, ctx:decafParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by decafParser#blockstmt.
    def exitBlockstmt(self, ctx:decafParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by decafParser#locationstmt.
    def enterLocationstmt(self, ctx:decafParser.LocationstmtContext):
        pass

    # Exit a parse tree produced by decafParser#locationstmt.
    def exitLocationstmt(self, ctx:decafParser.LocationstmtContext):
        pass


    # Enter a parse tree produced by decafParser#expressionstmt.
    def enterExpressionstmt(self, ctx:decafParser.ExpressionstmtContext):
        pass

    # Exit a parse tree produced by decafParser#expressionstmt.
    def exitExpressionstmt(self, ctx:decafParser.ExpressionstmtContext):
        pass


    # Enter a parse tree produced by decafParser#location.
    def enterLocation(self, ctx:decafParser.LocationContext):
        pass

    # Exit a parse tree produced by decafParser#location.
    def exitLocation(self, ctx:decafParser.LocationContext):
        pass


    # Enter a parse tree produced by decafParser#rel_op_expr.
    def enterRel_op_expr(self, ctx:decafParser.Rel_op_exprContext):
        pass

    # Exit a parse tree produced by decafParser#rel_op_expr.
    def exitRel_op_expr(self, ctx:decafParser.Rel_op_exprContext):
        pass


    # Enter a parse tree produced by decafParser#minusexpr.
    def enterMinusexpr(self, ctx:decafParser.MinusexprContext):
        pass

    # Exit a parse tree produced by decafParser#minusexpr.
    def exitMinusexpr(self, ctx:decafParser.MinusexprContext):
        pass


    # Enter a parse tree produced by decafParser#cond_op_expr.
    def enterCond_op_expr(self, ctx:decafParser.Cond_op_exprContext):
        pass

    # Exit a parse tree produced by decafParser#cond_op_expr.
    def exitCond_op_expr(self, ctx:decafParser.Cond_op_exprContext):
        pass


    # Enter a parse tree produced by decafParser#literalexpr.
    def enterLiteralexpr(self, ctx:decafParser.LiteralexprContext):
        pass

    # Exit a parse tree produced by decafParser#literalexpr.
    def exitLiteralexpr(self, ctx:decafParser.LiteralexprContext):
        pass


    # Enter a parse tree produced by decafParser#factoexpr.
    def enterFactoexpr(self, ctx:decafParser.FactoexprContext):
        pass

    # Exit a parse tree produced by decafParser#factoexpr.
    def exitFactoexpr(self, ctx:decafParser.FactoexprContext):
        pass


    # Enter a parse tree produced by decafParser#methodexpr.
    def enterMethodexpr(self, ctx:decafParser.MethodexprContext):
        pass

    # Exit a parse tree produced by decafParser#methodexpr.
    def exitMethodexpr(self, ctx:decafParser.MethodexprContext):
        pass


    # Enter a parse tree produced by decafParser#locexpr.
    def enterLocexpr(self, ctx:decafParser.LocexprContext):
        pass

    # Exit a parse tree produced by decafParser#locexpr.
    def exitLocexpr(self, ctx:decafParser.LocexprContext):
        pass


    # Enter a parse tree produced by decafParser#corchexpr.
    def enterCorchexpr(self, ctx:decafParser.CorchexprContext):
        pass

    # Exit a parse tree produced by decafParser#corchexpr.
    def exitCorchexpr(self, ctx:decafParser.CorchexprContext):
        pass


    # Enter a parse tree produced by decafParser#p_arith_op_expr.
    def enterP_arith_op_expr(self, ctx:decafParser.P_arith_op_exprContext):
        pass

    # Exit a parse tree produced by decafParser#p_arith_op_expr.
    def exitP_arith_op_expr(self, ctx:decafParser.P_arith_op_exprContext):
        pass


    # Enter a parse tree produced by decafParser#eq_op_expr.
    def enterEq_op_expr(self, ctx:decafParser.Eq_op_exprContext):
        pass

    # Exit a parse tree produced by decafParser#eq_op_expr.
    def exitEq_op_expr(self, ctx:decafParser.Eq_op_exprContext):
        pass


    # Enter a parse tree produced by decafParser#arith_op_expr.
    def enterArith_op_expr(self, ctx:decafParser.Arith_op_exprContext):
        pass

    # Exit a parse tree produced by decafParser#arith_op_expr.
    def exitArith_op_expr(self, ctx:decafParser.Arith_op_exprContext):
        pass


    # Enter a parse tree produced by decafParser#methodCall.
    def enterMethodCall(self, ctx:decafParser.MethodCallContext):
        pass

    # Exit a parse tree produced by decafParser#methodCall.
    def exitMethodCall(self, ctx:decafParser.MethodCallContext):
        pass


    # Enter a parse tree produced by decafParser#arg.
    def enterArg(self, ctx:decafParser.ArgContext):
        pass

    # Exit a parse tree produced by decafParser#arg.
    def exitArg(self, ctx:decafParser.ArgContext):
        pass


    # Enter a parse tree produced by decafParser#p_arith_op.
    def enterP_arith_op(self, ctx:decafParser.P_arith_opContext):
        pass

    # Exit a parse tree produced by decafParser#p_arith_op.
    def exitP_arith_op(self, ctx:decafParser.P_arith_opContext):
        pass


    # Enter a parse tree produced by decafParser#arith_op.
    def enterArith_op(self, ctx:decafParser.Arith_opContext):
        pass

    # Exit a parse tree produced by decafParser#arith_op.
    def exitArith_op(self, ctx:decafParser.Arith_opContext):
        pass


    # Enter a parse tree produced by decafParser#rel_op.
    def enterRel_op(self, ctx:decafParser.Rel_opContext):
        pass

    # Exit a parse tree produced by decafParser#rel_op.
    def exitRel_op(self, ctx:decafParser.Rel_opContext):
        pass


    # Enter a parse tree produced by decafParser#eq_op.
    def enterEq_op(self, ctx:decafParser.Eq_opContext):
        pass

    # Exit a parse tree produced by decafParser#eq_op.
    def exitEq_op(self, ctx:decafParser.Eq_opContext):
        pass


    # Enter a parse tree produced by decafParser#cond_op.
    def enterCond_op(self, ctx:decafParser.Cond_opContext):
        pass

    # Exit a parse tree produced by decafParser#cond_op.
    def exitCond_op(self, ctx:decafParser.Cond_opContext):
        pass


    # Enter a parse tree produced by decafParser#literal.
    def enterLiteral(self, ctx:decafParser.LiteralContext):
        pass

    # Exit a parse tree produced by decafParser#literal.
    def exitLiteral(self, ctx:decafParser.LiteralContext):
        pass


    # Enter a parse tree produced by decafParser#int_Literal.
    def enterInt_Literal(self, ctx:decafParser.Int_LiteralContext):
        pass

    # Exit a parse tree produced by decafParser#int_Literal.
    def exitInt_Literal(self, ctx:decafParser.Int_LiteralContext):
        pass


    # Enter a parse tree produced by decafParser#char_Literal.
    def enterChar_Literal(self, ctx:decafParser.Char_LiteralContext):
        pass

    # Exit a parse tree produced by decafParser#char_Literal.
    def exitChar_Literal(self, ctx:decafParser.Char_LiteralContext):
        pass


    # Enter a parse tree produced by decafParser#bool_Literal.
    def enterBool_Literal(self, ctx:decafParser.Bool_LiteralContext):
        pass

    # Exit a parse tree produced by decafParser#bool_Literal.
    def exitBool_Literal(self, ctx:decafParser.Bool_LiteralContext):
        pass



del decafParser