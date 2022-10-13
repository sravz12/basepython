#variable length arguments
def func1(*num):
    print(type(num))
    for i in num:
        print(i)
print("call 1")
func1(10,20,30,40)
print("call 2")
func1(1,2,3,4)