list=[5,3,2,1,4,8]
list_sum=0
for i in list:
    list_sum+=i
ans=[]
for i in list:
    ans.append(list_sum-i)
    
print(list)
print(ans)
