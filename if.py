from lib2to3.pytree import convert


var1=int(input("請輸入數字:"))
result=""
if var1%10==0:
    result="1"
elif var1%2==0:
    result="2"
else:
    result="3"
print(result)
