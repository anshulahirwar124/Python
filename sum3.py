list=[[1,3,5,6],[3,4,5],[3,4,7],[10,20,30]]
ans=[]
for i in range(len(list)):
    for j in range(len(list)):
        temp=0
        for j in list[i]:
            temp+=j
    ans.append(temp)
print(ans)