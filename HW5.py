#Austin Ryf - 11512650
#Intended for Windows

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []

# now define functions to push and pop values to the top of to/from the top of
# the stack (end of the list). Recall that `pass` in Python is a space
# holder: replace it with your code.

def opPop():
    if (len(opstack) > 0):
        return opstack.pop()
    else:
        print("No values in operand stack")

def opPush(value):
    opstack.append(value)

# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations

dictstack = []

# now define functions to push and pop dictionaries on the dictstack, to define
# name, and to lookup a name

def dictPop():
    if (len(dictstack) > 0):
        return dictstack.pop()
    else:
        print("No dictionaries in dictionary stack")

# dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)

# dictPush pushes a new dictionary to the dictstack. Note that, your interpreter
# will call dictPush only when Postscript “begin” operator is called. “begin”
# should pop the empty dictionary from the opstack and push it onto the dictstack
# by calling dictPush. You may either pass this dictionary (which you popped from
# opstack) to dictPush as a parameter or just simply push a new empty dictionary
# in dictPush.

def define(name, value):
    if not dictstack:
        dictionary = dict()
        dictionary[name] = value
        #changed define to push a tuple
        dictPush((0, dictionary))

    else:
        (dictstack[-1][1])[name] = value


    
# add name:value to the top dictionary in the dictionary stack. (Keep the ‘/’ in
# name when you add it to the top dictionary) Your psDef function should pop the
# name and value from operand stack and call the “define” function.

scope = ""

def lookup(name, scope):
    actualName = '/' + name
    revd = reversed(dictstack)

    if (scope == 'dynamic'):
        for item in revd:
            (index, dictionary) = item

            if (actualName in dictionary):
                return (index, dictionary[actualName])

        else:
            return None

    elif (scope == 'static'):
        index = len(dictstack) - 1
        dictionary = list(dictstack)

        return staticRecursion(dictionary, actualName, index)


def staticRecursion(sDict, sName, sIndex):
    #if name is found return dict and index
    if (sName in dictstack[sIndex][1]):
        return (sIndex, dictstack[sIndex][1][sName])
    #if end of index return none
    elif (sIndex == dictstack[sIndex][0]):
        return None
    #otherwise iterate through
    else:
        next, _ = dictstack[sIndex]
        _ = sDict.pop(sIndex)
        return staticRecursion(sDict, sName, next)

# return the value associated with name.
# What is your design decision about what to do when there is no definition for
# name? If “name” is not defined, your program should not break, but should
# give an appropriate error message.

#--------------------------- 15% -------------------------------------
# Arithmetic and comparison operators: define all the arithmetic and
# comparison operators here -- add, sub, mul, div, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters and
# types of the parameters are correct.

def add():
    if (len(opstack) >= 2):
        op1 = opPop() # pop the top value off the operand stack
        op2 = opPop() # pop the top value off the operand stack

        opNew = op1 + op2
        opPush(opNew) # push (op1 + op2) onto the operand stack
       
    else:
        print("Not enough parameters in operand stack for add")
    
def sub():
    if (len(opstack) >= 2):
        op1 = opPop() # pop the top value off the operand stack
        op2 = opPop() # pop the top value off the operand stack

        opNew = op2 - op1
        opPush(opNew) # push (op1 - op2) onto the operand stack
       
    else:
        print("Not enough parameters in operand stack for sub")

def mul():
    if (len(opstack) >= 2):
        op1 = opPop() # pop the top value off the operand stack
        op2 = opPop() # pop the top value off the operand stack

        opNew = op1 * op2
        opPush(opNew) # push (op1 * op2) onto the operand stack
       
    else:
        print("Not enough parameters in operand stack for mul")

def div():
    if (len(opstack) >= 2):
        op1 = opPop() # pop the top value off the operand stack
        op2 = opPop() # pop the top value off the operand stack

        opNew = op2 / op1
        opPush(opNew) # push (op1 / op2) onto the operand stack
       
    else:
        print("Not enough parameters in operand stack for div")

def eq():
    op1 = opPop()
    op2 = opPop()
    opPush(op1 == op2) # push true if op1 == op2, else false

def lt():
    op1 = opPop()
    op2 = opPop()
    opPush(op1 > op2) # push true if op1 > op2, else false

def gt():
    op1 = opPop()
    op2 = opPop()
    opPush(op1 < op2) # push true if op1 < op2, else false

#--------------------------- 15% -------------------------------------
# Array operators: define the array operators length, get

def length():
    if (len(opstack) > 0):
        op = opPop()
        if (type(op) == list):
            opPush(len(op))
        else:
            opPush(op)

def get():
    if (len(opstack) > 0):
        num = opPop()
        currList = opPop()
        # if num is an int and currList is a list push the value at currList[num], else push both values back onto the stack
        if (type(num) == int and type(currList) == list):
                opPush(currList[num])
        else:
            opPush(currList)
            opPush(num)
            print("First value popped not an int or Second value popped not a list")
    else:
        print("Op stack is empty for get()")

    

#--------------------------- 15% -------------------------------------
# Boolean operators: define the boolean operators psAnd, psOr, psNot
# Remember that these take boolean operands only. Anything else is an error

def psAnd():
    op1 = opPop()
    op2 = opPop()
    # both ops true, push true, else false
    if (op1 == True and op2 == True):
        opPush(True)
    else:
        opPush(False)

def psOr():
    op1 = opPop()
    op2 = opPop()
    # either ops true, push true, else false
    if (op1 == True and op2 == False):
        opPush(True)
    elif (op1 == False and op2 == True):
        opPush(True)
    else:
        opPush(False)

def psNot():
    op = opPop()
    # push inverse of op
    if (op == True):
        opPush(False)
    elif (op == False):
        opPush(True)


#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, exch, pop, copy,
# clear, stack

def dup():
    op = opPop()
    # push popped op twice, essentially duplicating it
    opPush(op)
    opPush(op)

def exch():
    op1 = opPop()
    op2 = opPop()
    # swap op1 and op2
    opPush(op1)
    opPush(op2)

def pop():
    opPop()

def copy():
    num = opPop()
    # if num is an int and num is less than the stack size, add the values from len(opstack) to len(opstack) - num to the list again
    if (type(num) == int and num < len(opstack)):
        opstack.extend(opstack[len(opstack) - num:])
    else:
        print("The value popped was not an int or the value was bigger than the length of op stack")

def clear():
    while (len(opstack) > 0):
        opPop() # empty the stack

def stack():
    revo = reversed(opstack)
    revAndIterd = reversed(list(enumerate(dictstack)))

    print("==============")

    for item in revo:
        print(item)

    print("==============")

    for (index, item) in revAndIterd:
        curTopStack, dictionary = item
        print("----", index, "----", curTopStack, "----")
        if dictionary:
            for key in dictionary:
                print(key, dictionary[key])

    print("==============")

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in
# Python.
# Note: The psDef operator will pop the value and name from the opstack and
# call your own "define" operator (pass those values as parameters). Note that
# psDef()won't have any parameters.

def psDict():
    opPop()
    newDict = dict()
    opPush(newDict) # push an empty dict onto the op stack

def begin():
    if (len(opstack) > 0):
        op = opPop()
        if (type(op) == dict):
            dictPush(op) # pushes dict from op stack to dict stack
        else:
            opPush(op)
            print("Tried to push a non-dictionary on to the dict stack")
    else:
        print("Tried to pop a dictionary off of an empty op stack")

def end():
    if (len(dictstack) > 0):
        dictPop() # remove top dict from dict stack
    else:
        print("Tried to pop a dictionary off of an empty dict stack")

def psDef():
    value = opPop()
    name = opPop()

    if (type(name) == str):
        define(name, value) # if name is a string, define it in dict stack
    else:
        opPush(name)
        opPush(value)

#------------------------------- Parsing ---------------------------------------

import re
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c == '{':
            res.append(groupMatching2(it))
        else:
            res.append(c)
    return False

def parse(tokens):
    res = []
    it = iter(tokens)
    for c in it:
        if isinstance(c, list):
            res.append(parse(c))

        elif c == '}':
            return False

        elif c == '{':
            res.append(parse(groupMatching2(it)))

        elif c.isdigit():
            res.append(int(c))

        elif c.startswith('-'):
            res.append(int(c))

        elif c == "true" or c == "false":
            res.append(bool(c))

        elif c.startswith('['):
            newList = [int(num) for num in c[1:-1].split(' ')]
            res.append(newList)

        else:
            res.append(c)

    return res

#print(parse(['[1 2 3 4 5]', 'dup', 'length', '/n', 'exch', 'def', '/fact', '{', '0', 'dict',
#'begin', '/n', 'exch', 'def', 'n', '2', 'lt', '{', '1', '}', '{', 'n', '1', 'sub',
#'fact', 'n', 'mul', '}', 'ifelse', 'end', '}', 'def', 'n', 'fact', 'stack']))


#--------------------------- if, ifelse, for, and forall ---------------------------

def psIf():
    code = opPop()
    condition = opPop()

    if (condition == True):
        interpretSPS(code, scope)

def psIfElse():
    code2 = opPop()
    code1 = opPop()
    condition = opPop()

    if (condition == True):
        interpretSPS(code1, scope)

    else:
        interpretSPS(code2, scope)

def psFor():
    inputArray = opPop()
    stop = opPop()
    index = opPop()
    start = opPop()

    if index > 0:
	    for x in range(start, stop + 1, index):
		    opPush(x)
		    interpretSPS(inputArray, scope)

    elif index < 0:
	    for x in range(start, stop - 1, index):
		    opPush(x)
		    interpretSPS(inputArray, scope)

def psForAll():
    code = opPop()
    inputArray = opPop()

    for item in inputArray:
        opPush(item)
        interpretSPS(code, scope)
        


#---------------------------- Interperet SPS Code and Code Arrays -----------------------------

functionDict = {"add": add, "sub": sub, "mul": mul, "div": div, "eq": eq, "gt": gt, "lt": lt, "length": length, "get": get, "and": psAnd, "or": psOr, "not": psNot, 
                "dup": dup, "exch": exch, "pop": pop, "copy": copy, "clear": clear, "stack": stack, "dict": psDict, "begin": begin, "end": end, "def": psDef, 
                "if": psIf, "ifelse": psIfElse, "for": psFor, "forall": psForAll}

def dictHelper(funcName):
    if funcName in functionDict.keys():
        return True
    else:
        return False

def interpretSPS(code, scope):
    for token in code:
        if isinstance(token, int) or isinstance(token, float) or isinstance(token, bool):
            opPush(token)

        elif isinstance(token, str):
            if token.startswith('/'):
                opPush(token)

            elif dictHelper(token):
                functionDict[token]()

            else:
                (index, lookFor) = lookup(token, scope)

                if (lookFor != None):
                    if isinstance(lookFor, list):
                        dictPush((index, {}))
                        interpretSPS(lookFor, scope)
                        dictPop()
                    
                    else:
                        opPush(lookFor)
        
        elif isinstance(token, list):
            opPush(token)

        else:
            print("Invalid code array type")

def interpreter(s, scope):
    print()
    print("Scope is currently: ", scope)
    interpretSPS(parse(tokenize(s)), scope)
    print()


#--------------------- Testing ----------------------------

#----------------- Test #1 (Correct) ----------------------

def test1():
    input1 = """
        /x 4 def
        /g { x stack } def
        /f { /x 7 def g } def
        f
        """

    interpreter(input1, "static")

    opstack.clear()
    dictstack.clear()


    interpreter(input1, "dynamic")

    opstack.clear()
    dictstack.clear()

#----------------- Test #2 (Correct) ----------------------

def test2():
    input2 = """
        /m 50 def
        /n 100 def
        /egg1 {/m 25 def n} def
        /chic {
            /n 1 def
            /egg2 { n } def
            m n
            egg1
            egg2
            stack } def
        n
        chic
        """

    interpreter(input2, "static")

    opstack.clear()
    dictstack.clear()


    interpreter(input2, "dynamic")

    opstack.clear()
    dictstack.clear()

#----------------- Test #3 (Correct) ----------------------

def test3():
    input3 = """
        /x 10 def
        /A { x } def
        /C { /x 40 def A stack } def
        /B { /x 30 def /A { x } def C } def
        B
        """

    interpreter(input3, "static")

    opstack.clear()
    dictstack.clear()


    interpreter(input3, "dynamic")

    opstack.clear()
    dictstack.clear()

#----------------- Test #4 (Correct) ----------------------

def test4():
    input4 = """
        /x 43 def
        /Z { /y 57 def x y add stack} def
        Z
        """

    interpreter(input4, "static")

    opstack.clear()
    dictstack.clear()


    interpreter(input4, "dynamic")

    opstack.clear()
    dictstack.clear()

#----------------- Test #5 (Correct) ----------------------

def test5():
    input5 = """
        /a 500 def
        /b 25 def
        /C {a b div} def
        C stack
        """

    interpreter(input5, "static")

    opstack.clear()
    dictstack.clear()


    interpreter(input5, "dynamic")

    opstack.clear()
    dictstack.clear()

#----------------------------------------------------------

def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == '__main__':
    main()