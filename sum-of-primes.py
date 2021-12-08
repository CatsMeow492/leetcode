def sumprimes(n):
    sum1 = 0
    for i in range(0,len(n)): # First loop through the entire array
        num = n[i]  
        if (num > 1 and all(num%j != 0 for j in range(2, int(num**0.5)+1))): # Only start this loop if array[i] is greater than one and num / j has a remainder for the entire range which is half num plus 1
                sum1 = sum1 + num
    print(sum1)
    return(sum1)

                
x = sumprimes([3,3,1,13])
print(x)