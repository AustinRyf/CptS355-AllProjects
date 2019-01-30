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
    dictionary = dict()
    dictionary[name] = value
        
    dictPush(dictionary)
    
# add name:value to the top dictionary in the dictionary stack. (Keep the ‘/’ in
# name when you add it to the top dictionary) Your psDef function should pop the
# name and value from operand stack and call the “define” function.

def lookup(name):
    actualName = '/' + name
    revd = reversed(dictstack)

    for dictionary in revd:
        if actualName in dictionary:
            return dictionary[actualName]

    print("Name is not defined")

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
        op1 = float(opPop()) # pop the top value off the operand stack
        op2 = float(opPop()) # pop the top value off the operand stack

        opNew = op1 + op2
        opPush(opNew) # push (op1 + op2) onto the operand stack
       
    else:
        print("Not enough parameters in operand stack for add")
    
def sub():
    if (len(opstack) >= 2):
        op1 = float(opPop()) # pop the top value off the operand stack
        op2 = float(opPop()) # pop the top value off the operand stack

        opNew = op2 - op1
        opPush(opNew) # push (op1 - op2) onto the operand stack
       
    else:
        print("Not enough parameters in operand stack for sub")

def mul():
    if (len(opstack) >= 2):
        op1 = float(opPop()) # pop the top value off the operand stack
        op2 = float(opPop()) # pop the top value off the operand stack

        opNew = op1 * op2
        opPush(opNew) # push (op1 * op2) onto the operand stack
       
    else:
        print("Not enough parameters in operand stack for mul")

def div():
    if (len(opstack) >= 2):
        op1 = float(opPop()) # pop the top value off the operand stack
        op2 = float(opPop()) # pop the top value off the operand stack

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
    while (len(opstack) > 0):
        op = opPop()
        print(op) # print the stack

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in
# Python.
# Note: The psDef operator will pop the value and name from the opstack and
# call your own "define" operator (pass those values as parameters). Note that
# psDef()won't have any parameters.

def psDict():
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

#------------------------- Test Cases ---------------------------------

#------- Part 1 TEST CASES--------------
def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True

#Comparison operators tests
def testEq():
    opPush(6)
    opPush(6)
    eq()
    if opPop() != True:
        return False
    return True

def testLt():
    opPush(3)
    opPush(6)
    lt()
    if opPop() != True:
        return False
    return True

def testGt():
    opPush(3)
    opPush(6)
    gt()
    if opPop() != False:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    if opPop() != 5:
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True

#boolean operator tests
def testPsAnd():
    opPush(True)
    opPush(False)
    psAnd()
    if opPop() != False:
        return False
    return True

def testPsOr():
    opPush(True)
    opPush(False)
    psOr()
    if opPop() != True:
        return False
    return True

def testPsNot():
    opPush(True)
    psNot()
    if opPop() != False:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True

def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv), \
                 ('eq',testEq),('lt',testLt),('gt', testGt), ('psAnd', testPsAnd),('psOr', testPsOr),('psNot', testPsNot), \
                 ('length', testLength),('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('copy', testCopy), \
                 ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')

if __name__ == '__main__':
    print(main_part1())