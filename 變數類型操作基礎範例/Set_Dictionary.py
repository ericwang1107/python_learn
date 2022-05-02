#集合
set1={3,4,5}
set2={5,6,7}
#交集
set3=set1&set2
#聯集
set4=set1|set2
#差集
set5=set1-set2
#反交集
set6=set1^set2
print (set3)
print (set4)
print (set5)
print (set6)
#set拆解(無序)
set1=set("測試拆解字串串")
print (set1)
#字典
dic={"apple":"蘋果","eric":"小花","Vicky":"喵喵"}
print(dic["eric"])
dic["eric"]="花花"
print(dic["eric"])
print("eric" not in dic)
print(len(dic))
#刪除
del dic["apple"]
print(len(dic))
#列表產生字典
dic2={x:x*2 for x in ["a","b","c"]}
print(dic2)
dic2={x:x*2 for x in [2,3,4]}
print(dic2)