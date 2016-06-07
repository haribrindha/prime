# prime
count=0
for num in range(2,10):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        	count=count+1
print(count)
            
