def fun1(fun):
    def fun2():
        fun()
        print("cs")
    return fun2()
def sc( ):
    print("hi")
fun1(sc)