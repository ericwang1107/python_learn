#while迴圈
i=0
while i<10:
    print("變數i:",i,"i+1的話:",i+1)
    i+=1
print("while迴圈結束")
#for迴圈
arr=[10,20,40,50,5]
for i in arr:
    print("陣列arr成員:",i)
#產生連續數字列表range()
for j in range(6):
    print(j)
print("range第二參數使用")
for j in range(6,10):
    print(j)
print("range範例結束")
#break 跳脫迴圈 continue 跳至下一圈
#else 迴圈結束前執行 while及for都適用
i=0
n=0
while i<5:
    n+=i
    i+=1
else:
    n=99
print(n)
n=0
for j in [10,20,30]:
    n+=j
    print(n)
else:
    n=99
print(n)
#範例:找整數平方根
#break不會跑else
n=int(input("輸入整數:"))
for i in range(n):
    if n**0.5==i:
        print("平方根為:"+str(i))
        break;
else:
    print("沒有整數平方根")
    