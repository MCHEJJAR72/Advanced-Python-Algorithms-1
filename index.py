Algorithms, Binary Search & Linked Lists
Tasks Today:
In-Place Algorithms
     a) Syntax
     a) Out of Place Algorithm
     b) In-Class Exercise #1
Two Pointers
Linked Lists
Merge Sort
     a) Video on Algorithms
     b) How it Works
Exercises
     a) Exercise #1 - Reverse a List in Place Using an In-Place Algorithm
     b) Exercise #2 - Find Distinct Words
     c) Exercise #3 - Write a program to implement a Linear Search Algorithm.
In-Place Algorithms
Syntax
# var[i], var[i+1] = var[i + 1] var[i]
#sometimes known as a swap algo

def swap(alist, x, y, z):
    alist[x], alist[y], alist[z] = alist[z], alist[y], alist[x]
    return alist

mylist = [20,4,10]

print(f"before swap {mylist}")
print(mylist[0])
#swap(mylist, 2, 0, 1)
swap(mylist, 0,1,2)
print(f"after swap {mylist}")
print(mylist[0])
before swap [20, 4, 10]
20
after swap [10, 4, 20]
10
Out of Place Algorithm
#not swapping completely reversing but also copies to another place in memeory

mylistcop = mylist[::-1]
print(mylistcop)
print(mylist)

array = ["a", "b", "c", "d"]
newarray = ["a"] * len(array)
print("before", array)
length = len(array) - 1

for i in range(length):
    newarray[i] = array[length - i]
array = newarray
print("after", array)
[20, 4, 10]
[10, 4, 20]
before ['a', 'b', 'c', 'd']
after ['d', 'c', 'b', 'a']
In-Class Exercise #1
Write a function that takes in four arguments (list, index1, index2, index3), and swaps those three positions in the list passed in.

l_1 = [10, 4, 3, 8, 4, 2, 6]

def swapping(listf, i1, i2, i3):
    listf[i1], listf[i2], listf[i3] = listf[i3], listf[i2], listf[i1]
    return listf
swapping(l_1, 2, 1, 0)
print(l_1)
[3, 4, 10, 8, 4, 2, 6]
Two Pointers
Syntax
#alist[left], #alist[right] = #alist[right], alist[left]

def twopointers(alist):
    #create the pointers
    left = 0
    right = len(alist) - 1
    #setup a loop that works through our list and sqaps things one pair at a time
    while left <= right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1
    return alist
mylist2 = [1,2,3,4,12,9,8,4,11,22]
twopointers(mylist2)
[22, 11, 4, 8, 9, 12, 4, 3, 2, 1]
Video of Algorithms
Watch the video about algorithms.

https://www.youtube.com/watch?v=Q9HjeFD62Uk

https://www.youtube.com/watch?v=kPRA0W1kECg

https://www.youtube.com/watch?v=ZZuD6iUe3Pc

Sorting Algorithms
Bubble Sort
Worst Case: O(n^2) Time - O(1) Space

#best case: O(n) - linear
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
def bubblesort(array):
    issorted = False
    while not issorted:
        issorted = True
        for num in range(len(array) - 1):
            if array[num] > array[num+1]:
                swap(num, num + 1, array)
                issorted = False
    return array
bubblesort([22,55,88,44,1,100,34,66])
[1, 22, 34, 44, 55, 66, 88, 100]
Insertion Sort
Worst Case: O(n^2) time - O(1)space

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
def insertionsort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j - 1, array)
            j -= 1
    return array
insertionsort([22,55,88,44,1,100,34,66])
    
[1, 22, 34, 44, 55, 66, 88, 100]
Merge Sort
How it Works
#step 1 split everything into its own group
#step 2 from left to right merge the two groups together
#step 3 while mergin place each items in the correct position within the merged group
#steps 4 continue with steps 3-4 until only one group is left
from random import randint
#used to gen a random list of 5 numbers from 0 to 20
nums = [randint(0,20) for i in range(5)]
print(nums)

####
def mergesort(alist):
    print("splitting...", alist)
#step 1 divide the array into equal parts as much as possible
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        #recursively call mergesort to perform splits if needed THEN merge once the splits are done
        mergesort(lefthalf)
        mergesort(righthalf)
        
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        #step 3 while mergin place items in the correct positions
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("merging", alist)
    return alist

mergesort(nums)
[8, 19, 4, 5, 5]
splitting... [8, 19, 4, 5, 5]
splitting... [8, 19]
splitting... [8]
merging [8]
splitting... [19]
merging [19]
merging [8, 19]
splitting... [4, 5, 5]
splitting... [4]
merging [4]
splitting... [5, 5]
splitting... [5]
merging [5]
splitting... [5]
merging [5]
merging [5, 5]
merging [4, 5, 5]
merging [4, 5, 5, 8, 19]
[4, 5, 5, 8, 19]
Binary Search
The Binary Search algorithm works by finding the number in the middle of a given array and comparing it to the target. Given that the array is sorted

The worst case run time for this algorithm is O(log(n))
def binarysearchhelperfunction(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potmatch = array[middle]
        if target == potmatch:
            return f"The index is {middle}"
        elif target < potmatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1
def binarysearch(array, target):
    return binarysearchhelperfunction(array, target, 0, len(array) - 1)
binarysearch([22,44,55,66,88,100], 44)
'The index is 1'
Exercises
Exercise #1
Reverse the list below in-place using an in-place algorithm.
For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']
rwords = [word[::-1] for word in words]
#output: words = ['.', 'ecnetnes', 'a', 'si', 'siht']


def reversearray(arr, n):
     
    for i in range(0, int(n / 2)):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        
n = len(rwords)
reversearray(rwords, n)
print(*rwords)
. ecnetnes a si siht
Exercise #2
Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
Should output:
{'a': 5,
'abstract': 1,
'an': 3,
'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def wcounter(text):
    import re
    Latext = text.lower()
    thewords = {}

    words = re.findall(r'\b\w+\b', Latext)

    for word in words:
        if word not in thewords:
            thewords[word] = 1
        else:
            thewords[word] += 1
    return thewords
            
print(wcounter(a_text))
{'in': 1, 'computing': 1, 'a': 5, 'hash': 4, 'table': 2, 'map': 2, 'is': 1, 'data': 2, 'structure': 2, 'which': 2, 'implements': 1, 'an': 3, 'associative': 1, 'array': 2, 'abstract': 1, 'type': 1, 'that': 1, 'can': 2, 'keys': 1, 'to': 2, 'values': 1, 'uses': 1, 'function': 1, 'compute': 1, 'index': 1, 'into': 1, 'of': 1, 'buckets': 1, 'or': 1, 'slots': 1, 'from': 1, 'the': 1, 'desired': 1, 'value': 1, 'be': 1, 'found': 1}
Exercise #3
Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

Hint: Linear Searching will require searching a list for a given number.
nums_list = [10,23,45,70,11,15]
target = 70
#if number is not present return -1

def search(arr, N, x): 
  
    for i in range(0, N): 
        if (arr[i] == x): 
            return i 
    return -1

x = 70
N = len(nums_list)


y = search(nums_list, N, x)
print("the index is at", y)


#O(N) where N is the numbers of elements in the array 
the index is at 3