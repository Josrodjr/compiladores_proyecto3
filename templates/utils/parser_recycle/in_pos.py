from pythonds.basic import Stack

# import my own separator
# from pser import parse_input

operands = ["<=", ">=", ">", "<", "==", "=!", "&&", "||", "(", ")"]

new_prec = {
    "<=": 3,
    ">=": 3,
    ">": 3,
    "<": 3,
    "==": 3,
    "=!": 3,
    "&&": 2,
    "||": 2,
    "(": 1
}

def infixToPostfix(infixexpr):
    prec = new_prec
    # prec["*"] = 3
    # prec["/"] = 3
    # prec["+"] = 2
    # prec["-"] = 2
    # prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    # tokenList = parse_input(infixexpr)

    print(tokenList)

    for token in tokenList:
        # if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
        if token not in operands:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    # return " ".join(postfixList)
    return postfixList

# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(infixToPostfix("( Aasdf + B ) * C - ( D - E ) * ( F + G )"))
# print(infixToPostfix("( r2 > r1 && r1 == r2 ) || ( sucasa > ddfa )"))