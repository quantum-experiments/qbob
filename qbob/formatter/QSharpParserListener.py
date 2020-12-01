# Generated from QSharpParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QSharpParser import QSharpParser
else:
    from QSharpParser import QSharpParser

# This class defines a complete listener for a parse tree produced by QSharpParser.
class QSharpParserListener(ParseTreeListener):

    # Enter a parse tree produced by QSharpParser#program.
    def enterProgram(self, ctx:QSharpParser.ProgramContext):
        pass

    # Exit a parse tree produced by QSharpParser#program.
    def exitProgram(self, ctx:QSharpParser.ProgramContext):
        pass


    # Enter a parse tree produced by QSharpParser#namespace.
    def enterNamespace(self, ctx:QSharpParser.NamespaceContext):
        pass

    # Exit a parse tree produced by QSharpParser#namespace.
    def exitNamespace(self, ctx:QSharpParser.NamespaceContext):
        pass


    # Enter a parse tree produced by QSharpParser#qualifiedName.
    def enterQualifiedName(self, ctx:QSharpParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by QSharpParser#qualifiedName.
    def exitQualifiedName(self, ctx:QSharpParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by QSharpParser#OpenElement.
    def enterOpenElement(self, ctx:QSharpParser.OpenElementContext):
        pass

    # Exit a parse tree produced by QSharpParser#OpenElement.
    def exitOpenElement(self, ctx:QSharpParser.OpenElementContext):
        pass


    # Enter a parse tree produced by QSharpParser#TypeElement.
    def enterTypeElement(self, ctx:QSharpParser.TypeElementContext):
        pass

    # Exit a parse tree produced by QSharpParser#TypeElement.
    def exitTypeElement(self, ctx:QSharpParser.TypeElementContext):
        pass


    # Enter a parse tree produced by QSharpParser#CallableElement.
    def enterCallableElement(self, ctx:QSharpParser.CallableElementContext):
        pass

    # Exit a parse tree produced by QSharpParser#CallableElement.
    def exitCallableElement(self, ctx:QSharpParser.CallableElementContext):
        pass


    # Enter a parse tree produced by QSharpParser#openDirective.
    def enterOpenDirective(self, ctx:QSharpParser.OpenDirectiveContext):
        pass

    # Exit a parse tree produced by QSharpParser#openDirective.
    def exitOpenDirective(self, ctx:QSharpParser.OpenDirectiveContext):
        pass


    # Enter a parse tree produced by QSharpParser#attribute.
    def enterAttribute(self, ctx:QSharpParser.AttributeContext):
        pass

    # Exit a parse tree produced by QSharpParser#attribute.
    def exitAttribute(self, ctx:QSharpParser.AttributeContext):
        pass


    # Enter a parse tree produced by QSharpParser#access.
    def enterAccess(self, ctx:QSharpParser.AccessContext):
        pass

    # Exit a parse tree produced by QSharpParser#access.
    def exitAccess(self, ctx:QSharpParser.AccessContext):
        pass


    # Enter a parse tree produced by QSharpParser#declarationPrefix.
    def enterDeclarationPrefix(self, ctx:QSharpParser.DeclarationPrefixContext):
        pass

    # Exit a parse tree produced by QSharpParser#declarationPrefix.
    def exitDeclarationPrefix(self, ctx:QSharpParser.DeclarationPrefixContext):
        pass


    # Enter a parse tree produced by QSharpParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:QSharpParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by QSharpParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:QSharpParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by QSharpParser#underlyingType.
    def enterUnderlyingType(self, ctx:QSharpParser.UnderlyingTypeContext):
        pass

    # Exit a parse tree produced by QSharpParser#underlyingType.
    def exitUnderlyingType(self, ctx:QSharpParser.UnderlyingTypeContext):
        pass


    # Enter a parse tree produced by QSharpParser#typeDeclarationTuple.
    def enterTypeDeclarationTuple(self, ctx:QSharpParser.TypeDeclarationTupleContext):
        pass

    # Exit a parse tree produced by QSharpParser#typeDeclarationTuple.
    def exitTypeDeclarationTuple(self, ctx:QSharpParser.TypeDeclarationTupleContext):
        pass


    # Enter a parse tree produced by QSharpParser#typeTupleItem.
    def enterTypeTupleItem(self, ctx:QSharpParser.TypeTupleItemContext):
        pass

    # Exit a parse tree produced by QSharpParser#typeTupleItem.
    def exitTypeTupleItem(self, ctx:QSharpParser.TypeTupleItemContext):
        pass


    # Enter a parse tree produced by QSharpParser#namedItem.
    def enterNamedItem(self, ctx:QSharpParser.NamedItemContext):
        pass

    # Exit a parse tree produced by QSharpParser#namedItem.
    def exitNamedItem(self, ctx:QSharpParser.NamedItemContext):
        pass


    # Enter a parse tree produced by QSharpParser#callableDeclaration.
    def enterCallableDeclaration(self, ctx:QSharpParser.CallableDeclarationContext):
        pass

    # Exit a parse tree produced by QSharpParser#callableDeclaration.
    def exitCallableDeclaration(self, ctx:QSharpParser.CallableDeclarationContext):
        pass


    # Enter a parse tree produced by QSharpParser#typeParameterBinding.
    def enterTypeParameterBinding(self, ctx:QSharpParser.TypeParameterBindingContext):
        pass

    # Exit a parse tree produced by QSharpParser#typeParameterBinding.
    def exitTypeParameterBinding(self, ctx:QSharpParser.TypeParameterBindingContext):
        pass


    # Enter a parse tree produced by QSharpParser#parameterTuple.
    def enterParameterTuple(self, ctx:QSharpParser.ParameterTupleContext):
        pass

    # Exit a parse tree produced by QSharpParser#parameterTuple.
    def exitParameterTuple(self, ctx:QSharpParser.ParameterTupleContext):
        pass


    # Enter a parse tree produced by QSharpParser#parameter.
    def enterParameter(self, ctx:QSharpParser.ParameterContext):
        pass

    # Exit a parse tree produced by QSharpParser#parameter.
    def exitParameter(self, ctx:QSharpParser.ParameterContext):
        pass


    # Enter a parse tree produced by QSharpParser#characteristics.
    def enterCharacteristics(self, ctx:QSharpParser.CharacteristicsContext):
        pass

    # Exit a parse tree produced by QSharpParser#characteristics.
    def exitCharacteristics(self, ctx:QSharpParser.CharacteristicsContext):
        pass


    # Enter a parse tree produced by QSharpParser#characteristicsExpression.
    def enterCharacteristicsExpression(self, ctx:QSharpParser.CharacteristicsExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#characteristicsExpression.
    def exitCharacteristicsExpression(self, ctx:QSharpParser.CharacteristicsExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#callableBody.
    def enterCallableBody(self, ctx:QSharpParser.CallableBodyContext):
        pass

    # Exit a parse tree produced by QSharpParser#callableBody.
    def exitCallableBody(self, ctx:QSharpParser.CallableBodyContext):
        pass


    # Enter a parse tree produced by QSharpParser#specialization.
    def enterSpecialization(self, ctx:QSharpParser.SpecializationContext):
        pass

    # Exit a parse tree produced by QSharpParser#specialization.
    def exitSpecialization(self, ctx:QSharpParser.SpecializationContext):
        pass


    # Enter a parse tree produced by QSharpParser#specializationName.
    def enterSpecializationName(self, ctx:QSharpParser.SpecializationNameContext):
        pass

    # Exit a parse tree produced by QSharpParser#specializationName.
    def exitSpecializationName(self, ctx:QSharpParser.SpecializationNameContext):
        pass


    # Enter a parse tree produced by QSharpParser#specializationGenerator.
    def enterSpecializationGenerator(self, ctx:QSharpParser.SpecializationGeneratorContext):
        pass

    # Exit a parse tree produced by QSharpParser#specializationGenerator.
    def exitSpecializationGenerator(self, ctx:QSharpParser.SpecializationGeneratorContext):
        pass


    # Enter a parse tree produced by QSharpParser#providedSpecialization.
    def enterProvidedSpecialization(self, ctx:QSharpParser.ProvidedSpecializationContext):
        pass

    # Exit a parse tree produced by QSharpParser#providedSpecialization.
    def exitProvidedSpecialization(self, ctx:QSharpParser.ProvidedSpecializationContext):
        pass


    # Enter a parse tree produced by QSharpParser#specializationParameterTuple.
    def enterSpecializationParameterTuple(self, ctx:QSharpParser.SpecializationParameterTupleContext):
        pass

    # Exit a parse tree produced by QSharpParser#specializationParameterTuple.
    def exitSpecializationParameterTuple(self, ctx:QSharpParser.SpecializationParameterTupleContext):
        pass


    # Enter a parse tree produced by QSharpParser#specializationParameter.
    def enterSpecializationParameter(self, ctx:QSharpParser.SpecializationParameterContext):
        pass

    # Exit a parse tree produced by QSharpParser#specializationParameter.
    def exitSpecializationParameter(self, ctx:QSharpParser.SpecializationParameterContext):
        pass


    # Enter a parse tree produced by QSharpParser#type_rule.
    def enterType_rule(self, ctx:QSharpParser.Type_ruleContext):
        pass

    # Exit a parse tree produced by QSharpParser#type_rule.
    def exitType_rule(self, ctx:QSharpParser.Type_ruleContext):
        pass


    # Enter a parse tree produced by QSharpParser#arrowType.
    def enterArrowType(self, ctx:QSharpParser.ArrowTypeContext):
        pass

    # Exit a parse tree produced by QSharpParser#arrowType.
    def exitArrowType(self, ctx:QSharpParser.ArrowTypeContext):
        pass


    # Enter a parse tree produced by QSharpParser#ExpressionStatement.
    def enterExpressionStatement(self, ctx:QSharpParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#ExpressionStatement.
    def exitExpressionStatement(self, ctx:QSharpParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#ReturnStatement.
    def enterReturnStatement(self, ctx:QSharpParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#ReturnStatement.
    def exitReturnStatement(self, ctx:QSharpParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#FailStatement.
    def enterFailStatement(self, ctx:QSharpParser.FailStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#FailStatement.
    def exitFailStatement(self, ctx:QSharpParser.FailStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#LetStatement.
    def enterLetStatement(self, ctx:QSharpParser.LetStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#LetStatement.
    def exitLetStatement(self, ctx:QSharpParser.LetStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#MutableStatement.
    def enterMutableStatement(self, ctx:QSharpParser.MutableStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#MutableStatement.
    def exitMutableStatement(self, ctx:QSharpParser.MutableStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#SetStatement.
    def enterSetStatement(self, ctx:QSharpParser.SetStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#SetStatement.
    def exitSetStatement(self, ctx:QSharpParser.SetStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#SetUpdateStatement.
    def enterSetUpdateStatement(self, ctx:QSharpParser.SetUpdateStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#SetUpdateStatement.
    def exitSetUpdateStatement(self, ctx:QSharpParser.SetUpdateStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#SetWithStatement.
    def enterSetWithStatement(self, ctx:QSharpParser.SetWithStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#SetWithStatement.
    def exitSetWithStatement(self, ctx:QSharpParser.SetWithStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#IfStatement.
    def enterIfStatement(self, ctx:QSharpParser.IfStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#IfStatement.
    def exitIfStatement(self, ctx:QSharpParser.IfStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#ElifStatement.
    def enterElifStatement(self, ctx:QSharpParser.ElifStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#ElifStatement.
    def exitElifStatement(self, ctx:QSharpParser.ElifStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#ElseStatement.
    def enterElseStatement(self, ctx:QSharpParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#ElseStatement.
    def exitElseStatement(self, ctx:QSharpParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#ForStatement.
    def enterForStatement(self, ctx:QSharpParser.ForStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#ForStatement.
    def exitForStatement(self, ctx:QSharpParser.ForStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#WhileStatement.
    def enterWhileStatement(self, ctx:QSharpParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#WhileStatement.
    def exitWhileStatement(self, ctx:QSharpParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#RepeatStatement.
    def enterRepeatStatement(self, ctx:QSharpParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#RepeatStatement.
    def exitRepeatStatement(self, ctx:QSharpParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#UntilStatement.
    def enterUntilStatement(self, ctx:QSharpParser.UntilStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#UntilStatement.
    def exitUntilStatement(self, ctx:QSharpParser.UntilStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#WithinStatement.
    def enterWithinStatement(self, ctx:QSharpParser.WithinStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#WithinStatement.
    def exitWithinStatement(self, ctx:QSharpParser.WithinStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#ApplyStatement.
    def enterApplyStatement(self, ctx:QSharpParser.ApplyStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#ApplyStatement.
    def exitApplyStatement(self, ctx:QSharpParser.ApplyStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#UsingStatement.
    def enterUsingStatement(self, ctx:QSharpParser.UsingStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#UsingStatement.
    def exitUsingStatement(self, ctx:QSharpParser.UsingStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#BorrowingStatement.
    def enterBorrowingStatement(self, ctx:QSharpParser.BorrowingStatementContext):
        pass

    # Exit a parse tree produced by QSharpParser#BorrowingStatement.
    def exitBorrowingStatement(self, ctx:QSharpParser.BorrowingStatementContext):
        pass


    # Enter a parse tree produced by QSharpParser#scope.
    def enterScope(self, ctx:QSharpParser.ScopeContext):
        pass

    # Exit a parse tree produced by QSharpParser#scope.
    def exitScope(self, ctx:QSharpParser.ScopeContext):
        pass


    # Enter a parse tree produced by QSharpParser#DiscardSymbol.
    def enterDiscardSymbol(self, ctx:QSharpParser.DiscardSymbolContext):
        pass

    # Exit a parse tree produced by QSharpParser#DiscardSymbol.
    def exitDiscardSymbol(self, ctx:QSharpParser.DiscardSymbolContext):
        pass


    # Enter a parse tree produced by QSharpParser#SymbolName.
    def enterSymbolName(self, ctx:QSharpParser.SymbolNameContext):
        pass

    # Exit a parse tree produced by QSharpParser#SymbolName.
    def exitSymbolName(self, ctx:QSharpParser.SymbolNameContext):
        pass


    # Enter a parse tree produced by QSharpParser#SymbolTuple.
    def enterSymbolTuple(self, ctx:QSharpParser.SymbolTupleContext):
        pass

    # Exit a parse tree produced by QSharpParser#SymbolTuple.
    def exitSymbolTuple(self, ctx:QSharpParser.SymbolTupleContext):
        pass


    # Enter a parse tree produced by QSharpParser#updateOperator.
    def enterUpdateOperator(self, ctx:QSharpParser.UpdateOperatorContext):
        pass

    # Exit a parse tree produced by QSharpParser#updateOperator.
    def exitUpdateOperator(self, ctx:QSharpParser.UpdateOperatorContext):
        pass


    # Enter a parse tree produced by QSharpParser#qubitInitializer.
    def enterQubitInitializer(self, ctx:QSharpParser.QubitInitializerContext):
        pass

    # Exit a parse tree produced by QSharpParser#qubitInitializer.
    def exitQubitInitializer(self, ctx:QSharpParser.QubitInitializerContext):
        pass


    # Enter a parse tree produced by QSharpParser#ItemAccessExpression.
    def enterItemAccessExpression(self, ctx:QSharpParser.ItemAccessExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#ItemAccessExpression.
    def exitItemAccessExpression(self, ctx:QSharpParser.ItemAccessExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#BitwiseXorExpression.
    def enterBitwiseXorExpression(self, ctx:QSharpParser.BitwiseXorExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#BitwiseXorExpression.
    def exitBitwiseXorExpression(self, ctx:QSharpParser.BitwiseXorExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#DoubleExpression.
    def enterDoubleExpression(self, ctx:QSharpParser.DoubleExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#DoubleExpression.
    def exitDoubleExpression(self, ctx:QSharpParser.DoubleExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#TupleExpression.
    def enterTupleExpression(self, ctx:QSharpParser.TupleExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#TupleExpression.
    def exitTupleExpression(self, ctx:QSharpParser.TupleExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#RangeExpression.
    def enterRangeExpression(self, ctx:QSharpParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#RangeExpression.
    def exitRangeExpression(self, ctx:QSharpParser.RangeExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#CompareExpression.
    def enterCompareExpression(self, ctx:QSharpParser.CompareExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#CompareExpression.
    def exitCompareExpression(self, ctx:QSharpParser.CompareExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#OrExpression.
    def enterOrExpression(self, ctx:QSharpParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#OrExpression.
    def exitOrExpression(self, ctx:QSharpParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#InterpStringExpression.
    def enterInterpStringExpression(self, ctx:QSharpParser.InterpStringExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#InterpStringExpression.
    def exitInterpStringExpression(self, ctx:QSharpParser.InterpStringExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#BoolExpression.
    def enterBoolExpression(self, ctx:QSharpParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#BoolExpression.
    def exitBoolExpression(self, ctx:QSharpParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#OpenRangeExpression.
    def enterOpenRangeExpression(self, ctx:QSharpParser.OpenRangeExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#OpenRangeExpression.
    def exitOpenRangeExpression(self, ctx:QSharpParser.OpenRangeExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#AndExpression.
    def enterAndExpression(self, ctx:QSharpParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#AndExpression.
    def exitAndExpression(self, ctx:QSharpParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#ResultExpression.
    def enterResultExpression(self, ctx:QSharpParser.ResultExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#ResultExpression.
    def exitResultExpression(self, ctx:QSharpParser.ResultExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#NegationExpression.
    def enterNegationExpression(self, ctx:QSharpParser.NegationExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#NegationExpression.
    def exitNegationExpression(self, ctx:QSharpParser.NegationExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#UpdateExpression.
    def enterUpdateExpression(self, ctx:QSharpParser.UpdateExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#UpdateExpression.
    def exitUpdateExpression(self, ctx:QSharpParser.UpdateExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#CallExpression.
    def enterCallExpression(self, ctx:QSharpParser.CallExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#CallExpression.
    def exitCallExpression(self, ctx:QSharpParser.CallExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#BitwiseOrExpression.
    def enterBitwiseOrExpression(self, ctx:QSharpParser.BitwiseOrExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#BitwiseOrExpression.
    def exitBitwiseOrExpression(self, ctx:QSharpParser.BitwiseOrExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#LeftOpenRangeExpression.
    def enterLeftOpenRangeExpression(self, ctx:QSharpParser.LeftOpenRangeExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#LeftOpenRangeExpression.
    def exitLeftOpenRangeExpression(self, ctx:QSharpParser.LeftOpenRangeExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#ExponentExpression.
    def enterExponentExpression(self, ctx:QSharpParser.ExponentExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#ExponentExpression.
    def exitExponentExpression(self, ctx:QSharpParser.ExponentExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#MultiplyExpression.
    def enterMultiplyExpression(self, ctx:QSharpParser.MultiplyExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#MultiplyExpression.
    def exitMultiplyExpression(self, ctx:QSharpParser.MultiplyExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#ConditionalExpression.
    def enterConditionalExpression(self, ctx:QSharpParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#ConditionalExpression.
    def exitConditionalExpression(self, ctx:QSharpParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#UnwrapExpression.
    def enterUnwrapExpression(self, ctx:QSharpParser.UnwrapExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#UnwrapExpression.
    def exitUnwrapExpression(self, ctx:QSharpParser.UnwrapExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#ControlledExpression.
    def enterControlledExpression(self, ctx:QSharpParser.ControlledExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#ControlledExpression.
    def exitControlledExpression(self, ctx:QSharpParser.ControlledExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#IntegerExpression.
    def enterIntegerExpression(self, ctx:QSharpParser.IntegerExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#IntegerExpression.
    def exitIntegerExpression(self, ctx:QSharpParser.IntegerExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#ShiftExpression.
    def enterShiftExpression(self, ctx:QSharpParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#ShiftExpression.
    def exitShiftExpression(self, ctx:QSharpParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx:QSharpParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx:QSharpParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#PauliExpression.
    def enterPauliExpression(self, ctx:QSharpParser.PauliExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#PauliExpression.
    def exitPauliExpression(self, ctx:QSharpParser.PauliExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#BitwiseAndExpression.
    def enterBitwiseAndExpression(self, ctx:QSharpParser.BitwiseAndExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#BitwiseAndExpression.
    def exitBitwiseAndExpression(self, ctx:QSharpParser.BitwiseAndExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#AddExpression.
    def enterAddExpression(self, ctx:QSharpParser.AddExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#AddExpression.
    def exitAddExpression(self, ctx:QSharpParser.AddExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#StringExpression.
    def enterStringExpression(self, ctx:QSharpParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#StringExpression.
    def exitStringExpression(self, ctx:QSharpParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#RightOpenRangeExpression.
    def enterRightOpenRangeExpression(self, ctx:QSharpParser.RightOpenRangeExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#RightOpenRangeExpression.
    def exitRightOpenRangeExpression(self, ctx:QSharpParser.RightOpenRangeExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#ArrayExpression.
    def enterArrayExpression(self, ctx:QSharpParser.ArrayExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#ArrayExpression.
    def exitArrayExpression(self, ctx:QSharpParser.ArrayExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#MissingExpression.
    def enterMissingExpression(self, ctx:QSharpParser.MissingExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#MissingExpression.
    def exitMissingExpression(self, ctx:QSharpParser.MissingExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#BigIntegerExpression.
    def enterBigIntegerExpression(self, ctx:QSharpParser.BigIntegerExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#BigIntegerExpression.
    def exitBigIntegerExpression(self, ctx:QSharpParser.BigIntegerExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#NewArrayExpression.
    def enterNewArrayExpression(self, ctx:QSharpParser.NewArrayExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#NewArrayExpression.
    def exitNewArrayExpression(self, ctx:QSharpParser.NewArrayExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#AdjointExpression.
    def enterAdjointExpression(self, ctx:QSharpParser.AdjointExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#AdjointExpression.
    def exitAdjointExpression(self, ctx:QSharpParser.AdjointExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#EqualsExpression.
    def enterEqualsExpression(self, ctx:QSharpParser.EqualsExpressionContext):
        pass

    # Exit a parse tree produced by QSharpParser#EqualsExpression.
    def exitEqualsExpression(self, ctx:QSharpParser.EqualsExpressionContext):
        pass


    # Enter a parse tree produced by QSharpParser#boolLiteral.
    def enterBoolLiteral(self, ctx:QSharpParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by QSharpParser#boolLiteral.
    def exitBoolLiteral(self, ctx:QSharpParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by QSharpParser#resultLiteral.
    def enterResultLiteral(self, ctx:QSharpParser.ResultLiteralContext):
        pass

    # Exit a parse tree produced by QSharpParser#resultLiteral.
    def exitResultLiteral(self, ctx:QSharpParser.ResultLiteralContext):
        pass


    # Enter a parse tree produced by QSharpParser#pauliLiteral.
    def enterPauliLiteral(self, ctx:QSharpParser.PauliLiteralContext):
        pass

    # Exit a parse tree produced by QSharpParser#pauliLiteral.
    def exitPauliLiteral(self, ctx:QSharpParser.PauliLiteralContext):
        pass


    # Enter a parse tree produced by QSharpParser#stringContent.
    def enterStringContent(self, ctx:QSharpParser.StringContentContext):
        pass

    # Exit a parse tree produced by QSharpParser#stringContent.
    def exitStringContent(self, ctx:QSharpParser.StringContentContext):
        pass


    # Enter a parse tree produced by QSharpParser#interpStringContent.
    def enterInterpStringContent(self, ctx:QSharpParser.InterpStringContentContext):
        pass

    # Exit a parse tree produced by QSharpParser#interpStringContent.
    def exitInterpStringContent(self, ctx:QSharpParser.InterpStringContentContext):
        pass



del QSharpParser