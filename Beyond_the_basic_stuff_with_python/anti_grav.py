# import antigravity
import webbrowser
# webbrowser.open('www.facebook.pl')

tupel = ("es")
tupel2 = ("es",)

kw = {'sep':'_'}
# **kw spread, ale key = parametr, a val to value paramatru
print('a','b','c',**kw)
print('a','b','c',*kw)

op = {
    "x":1,
    "y":2
}
op2 = {
    "y":2,
    "x":1
    
}

def div(x,y):
    return x/y

print(div(**op))
print(div(**op2))

def myMinFunction(*args):
    if len(args) == 1:
        values = args[0]
    else:
         values = args
    if len(values) == 0:
        raise ValueError('myMinFunction() args is an empty sequence')
        for i, value in enumerate(values):
            if i == 0 or value < smallestValue:
            smallestValue = value
    return smallestValue



