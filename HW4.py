#Austin Ryf - 11512650
#Intended for Windows

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []

# now define functions to push and pop values to the top of to/from the top of
# the stack (end of the list). Recall that `pass` in Python is a space
# holder: replace it with your code.

def opPop():
    return opstack.pop()

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
    pass

# dictPop pops the top dictionary from the dictionary stack.

def dictPush(): OR def dictPush(d):
    pass pass

# dictPush pushes a new dictionary to the dictstack. Note that, your interpreter
# will call dictPush only when Postscript “begin” operator is called. “begin”
# should pop the empty dictionary from the opstack and push it onto the dictstack
# by calling dictPush. You may either pass this dictionary (which you popped from
# opstack) to dictPush as a parameter or just simply push a new empty dictionary
# in dictPush.

def define(name, value):
    pass
    
# add name:value to the top dictionary in the dictionary stack. (Keep the ‘/’ in
# name when you add it to the top dictionary) Your psDef function should pop the
# name and value from operand stack and call the “define” function.

def lookup(name):
    pass

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
    op1 = opPop() # pop the top value off the operand stack
    op2 = opPop() # pop the top value off the operand stack

    if (op1.is_integer())

    opNew = op1 + op2

    opPush(opNew) # push (op1 / op2) onto the operand stack

def sub():
    op1 = opPop()
    op2 = opPop()
    opNew = op1 - op2

    opPush(opNew)

def mul():
    op1 = opPop()
    op2 = opPop()
    opNew = op1 * op2

    opPush(opNew)

def div():
    op1 = opPop()
    op2 = opPop()
    opNew = op1/op2

    opPush(opNew)

def eq():
    op1 = opPop()
    op2 = opPop()
    
    return op1 == op2

def lt():
    op1 = opPop()
    op2 = opPop()
    
    return op1 < op2

def gt():
    op1 = opPop()
    op2 = opPop()
    
    return op1 > op2
 

#--------------------------- 15% ------------------------------------- 