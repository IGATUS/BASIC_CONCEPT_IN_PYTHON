def dec(func):
    def inner(*args):
        list1=[]
        list1=args[1:]
        for i in list1:
            if i==0:
                return 'indeterminate form'
            else:
                return func(*args)
    return inner
@dec
def div1(a,b):
    return a/b
@dec
def div2(a,b,c):
    return a/b/c
print(div1(4,2))
print(div2(4,0,2))