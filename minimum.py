arr=[3,16,1,6,2]

arr=[4,6,1,4,1,6]
arr.sort()
print(len(arr))

prefix=[]
minimumu_cost=0
firstvalue=arr[0]
i=0
count=0
while firstvalue==arr[i]:
    
    prefix.append(arr[i])
    i+=1
    count+=1
prefix.append(arr[i])
next_val=arr[i]


cost=firstvalue-next_val

print(prefix) 
print(cost)
arr=[cost+element for element in arr]
print(arr)
