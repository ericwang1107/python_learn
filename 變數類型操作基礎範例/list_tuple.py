#有序可變 list
grades=[10,20,45,60,70]
print(grades)
grades[1]=25
print(grades)
print(len(grades))
#有序不可變 tuple
grades2=(15,25,50,55,75)
print(grades2)
print(len(grades2))
#不可變故grades2[1]=77無效
#列表刪除 刪除grades[1]及grades[2]
grades[1:3]=[]
print(grades)
grades=grades+[70,"abcd"]
print(grades)

#巢狀列表 date=[[3,4,5],["a","b","c"]]
date=[[3,4,5],["a","b","c"]]
print(str(date[0][1])+":"+str(date[1][1]))