from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

# clicing method (hamm clicing method se array ko reverse bhi kar sakte hai) by using indexing [start:end:-1]
a= val[3:4]
a= val[:-3]

a= val[::-1]

for i in range(0,len(a)):
    print(a[i], end=" ")

# print(val.typecode)

# print("\n")
# Methods of the array
# val.insert(1,10)  
# val.append(20)
# val[4]=100

# existing array can create the new array to write the one line of code

# copyarray= array(val.typecode,(x*3 for x in val))

# pop function are use to delete the index of value  
# copyarray.pop() 

# remove function can delete the actual value of the index
# copyarray.remove(12)
# for i in range(0,len(copyarray)):
#     print(copyarray[i], end=" ")

# for i in range(0,len(val)):
#     print(val[i], end=" ")

# for i in range(0,4):


#     # print("\n")

#     print(val[i], end=" ")
# print("\n")

# for x in val:
#     print(x, end=" ")

