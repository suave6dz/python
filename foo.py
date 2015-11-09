
# comment

'''multiline commenets surrounded by triple single or double quotes.'''
''''python is interpreted language
idris is static type checking, python is dynamic
idris values are immutable wheras python has mutable state
idris is language of expressions, python is of commands
--command is a state transformer'''

def foo(n):
    return n + 3

print(foo(6))

print(print("Happy 200th birthday George Boole"))

print(None)

# state is set of all values at a point in computation

x = 5
# {(x,5)}
print (x)
# {(x,5)}
x = 6
# {(x,6)}
print (x)
# {(x,6)}
y = 7
print (y)
# 
d = {"x" : 5, "y" :7}
