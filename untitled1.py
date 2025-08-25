import time
import matplotlib.pyplot as plt
start=time.time()
def linearsearch(a, key):
    n = len(a)
    for i in range(n):
        if a[i] == key:
            return i;
        return -1
a = [13,24,35,46,57,68,79]
start = time.time()
print("the array elements are:",a)
k = int(input("enter the key element to search:"))
i = linearsearch(a,k)
if i == -1:
    print("search unsuccessful")
else:
    print("search successful key found at location:",i+1)
end = time.time()
print("runetime of the program is",end-start)
x=list(range(1,1000))
plt.plot(x ,[y for y in x] )
plt.title("linear search- Time complexity is O(n)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()


    
    