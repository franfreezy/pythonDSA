#minimum number of machines

arr1= [2, 94, 93, 91, 82, 25]
arr2= [77, 50, 98, 14, 66, 53]

n = 1
time=[[]]
machine_n = f"machine {n}"
print(machine_n, ":", n)
i=0
if len(arr1)==len(arr2):
    for i in range(len(arr1)):
        time[arr1[i]].append(arr2[i]) 
    
print(time)