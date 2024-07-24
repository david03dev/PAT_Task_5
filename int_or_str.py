#Write a python code using lambda function to check every element of a list is an integer or string?

#given list
data = ["david","raj","2",3,4,5]
given_list = data

#initialize output list
res_list = []

#iter method to avoid attribute error
iterator = iter(data)

#Identify the element whether  Integer or not using lambda
result = lambda x : "Integer" if x.isnumeric() else "String"

#pass each element to lambda function to identify
for data in iterator:
    element = str(data)
    res_list.append(result(element))

#print the result
print("Given list is: ",given_list)
print("Types of each element is: ",res_list)
