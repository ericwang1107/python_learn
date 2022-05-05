def fun1(p1=1,p2=2):
    return p1+p2
print(fun1(2,3))
print(fun1("abc","4"))
print(fun1())

#無限參數
def say(*msgs):
    #Tuple處理
    for msg in msgs:
        print(msg)
#call
say("a","b","c")

#呼叫函式以參數名稱對應
fun1(p2=9,p1=3)