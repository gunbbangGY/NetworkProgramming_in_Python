v = 20

def func1() :
    v = 10
    print("1, v = %d" %v)

def func2() :
    global v
    v = 30
    print("2, v = %d" %v)

func1()
func2()
print(v)
