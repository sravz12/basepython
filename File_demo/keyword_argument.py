#variable length argument **kargs -> keyword argument
def fun(**karg):
    print(type(karg))
    for k,v in karg.items:
        print(k,':',v)

fun(Name='anu',cls='BCA')