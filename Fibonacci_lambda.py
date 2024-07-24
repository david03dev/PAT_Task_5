
#Initialize the fibonacci series
fib = [0,1]

#Get length of the series
n = int(input("Enter the length of fibonacci series : "))

#calculate fibonacci next element using lambda function
res = lambda x : (fib[-1] + fib[-2])

#call lambda function and create fibonacci series
for i in range(1,n):
    fib.append(res(fib))

#print the results
print(fib)
