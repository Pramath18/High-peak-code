def findMinimumDifference():
    
    startIndex=0
    endIndex=0
    result = +2147483647  
    arr.sort() # Sorting the array.
    #print(arr)
    # Find minimum value among 
    # all K size subarray. 

    for i in range(n-k+1):
        oldValue = result
        result = int(min(result, arr[i+k-1] - arr[i]))
        if(oldValue != result): 
            startIndex = i
            endIndex = i+k-1


    outputArr=[]
    for i in range(startIndex,endIndex+1):
        outputArr.append(arr[i])
    #print(disparr)
    f.write("\nThe Goodies selected for the distribution are :\n")
    for i in range(len(outputArr)):
        outputString = str(dict[outputArr[i]]+": "+str(outputArr[i])+"\n") #Displays the final output
        f.write(outputString)
    str1 = str("\nAnd the difference between the chosen goodie with highest price and the lowest price is: "+str(result)+"\n")
    f.write(str1)
    f.close()


# Driver code

k=int(input("Enter the Number of Employees:"))
f = open("output.txt","a")
with open('input.txt','r') as file:
    string = file.read()

array1 = list(string.split("\n"))
#print(array1)
namearray=[]
arr=[]
dict={}
for eve in array1:
    (key,val)=eve.split(": ")
    dict[int(val)] = key
    arr.append(int(val))
dup_value=arr  
#print(namearray)
#print(valuearray)
#print(dict)
n =len(arr)
findMinimumDifference() # function call
