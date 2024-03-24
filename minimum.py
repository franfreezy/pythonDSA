arr=[3,16,1,6,2]

arr=[4,6,1,4,1,6]
arr.sort()

equal_elements=all(element==arr[0] for element in arr )
while equal_elements==False:
    print(arr)
    # get the max==last element after sort
    max_val=max(arr)
    min_val=min(arr)
    ##getting the prefix
    prefix=[]
    i=0






    while arr[i]!=max_val:
        prefix.append(arr[i])
        i+=1
    
    cost=max_val-prefix[-1]
    prefix=[cost+element for element in prefix ]

    count=arr.count(max_val)
    while count!=0:
        prefix.append(max_val)
        count-=1

    arr=prefix
    print(prefix) 
    print(cost)


