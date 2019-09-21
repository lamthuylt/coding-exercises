# Sorting algorithms

## Bubble sort

#### Algorithm
This algorithm consists in repeatedly scanning through the list, comparing each pair of adjacent elements, and swapping them if they are in the wrong order. By this way, larger/smaller elements bubble up to the top of the list, which is the origin of the name "Bubble sort". This procedure is repeated until no more swap is required, meaning that the list is sorted. 

#### Illustration
<figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif" alt="{{ include description }}">
  Red is current pair of adjacent elements. Black is sorted sublist. (source: https://en.wikipedia.org/wiki/Bubble_sort)
</figure>

#### Implementation
```python
def bubble_sort(arr):
    for k in range(len(arr)-1,0,-1):       
        flag = 1   
        # swap each pair of adjacent elements if they are not in increasing order
        for i in range(k):
            if arr[i] > arr[i+1]:   
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                flag = 0
        # if we go through a pass without swapping, the array is already sorted
        if flag == 1:               
            break
    return arr
```

#### Analysis
* Time complexity: O(n^2)
* Space complexity: O(1)
 


## Selection sort

#### Algorithm
This algorithm divides the list into 2 sublists: one sublist of already sorted elements, which is built up from left to right, and one sublist of remaining elements to be sorted. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest element of the unsorted sublist, swapping it with the left most element of the unsorted sublist, and moving the sublist boundary one element to the right.

#### Illustration
<figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif" alt="{{ include description }}">
  Red is current min. Yellow is sorted list. Blue is current item. (source: https://en.wikipedia.org/wiki/Selection_sort)
</figure>

#### Implementation
```python
def selection_sort(arr):
    # move the sorted-unsorted sublists boundary one element to the right at a time
    for i in range(len(arr)-1):                   
        # find index of minimum element of unsorted sublist
        iMin = i
        for j, num in enumerate(arr[i+1:]):                
            if num < arr[iMin]:
                iMin = i+j+1
        # swap minimum element with the unsorted left most element
        if iMin != i:
            temp = arr[i]
            arr[i] = arr[iMin]
            arr[iMin] = temp
        print(arr)
    return arr
```

#### Analysis
* Time complexity: O(n^2)
* Space complexity: O(1)



## Insertion sort

#### Algorithm
Insertion sort divides the list into 2 sublists: sorted sublist, which initially contains the first element in the list and is built up from left to right, and unsorted sublist, which initially contains the remaining elements. The algorithm proceeds by picking one element from the unsorted sublist at a time, finding the location it belongs within the sorted sublist, and inserting it there. The procedure repeats until the unsorted sublist is empty.  

#### Illustration
<figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" alt="{{ include description }}">
  The sorted sublist (black) initially contains the first element in the list. With each iteration, one element (red) is picked from the unsorted sublist and inserted inplace into the sorted sublist (source: https://en.wikipedia.org/wiki/Insertion_sort)
</figure>

#### Implementation
```python
def insertion_sort(arr):
    for iUnsorted in range(1,len(arr)):
        val = arr[iUnsorted]   
        for iSorted in range(iUnsorted-1, -1, -1):
            # shift numbers greater than val to the right
            if arr[iSorted] > val:
                arr[iSorted+1] = arr[iSorted]
                if iSorted==0:
                    arr[0] = val
            else:
                arr[iSorted+1] = val    
                break
    return arr
```

#### Analysis
* Time complexity: O(n^2) (the number of comparisons and shifts of insertion sort is much less than bubble sort and selection sort)
* Space complexity: O(1) 


## Merge sort

#### Algorithm
This algorithm is broken down into 2 following steps:
1. **Bottom up split**: divide the input list into 2 (almost) equal sublists - left and right, then repeat the splitting process on each sublist over again until each sublist contains one element (a list of one element is considered sorted).
2. **Top down merge**: repeatedly merge sublists to produce new sorted sublists until there is only one sorted sublist remaining. This will be the original list in sorted order.

#### Illustration
<figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif" alt="{{ include description }}">
  First divide the list into sublists of one element. Then compare each element of adjacent sublists to sort and merge the two adjacent sublists, and repeat this process until all the sublists are sorted and merged. (source: https://en.wikipedia.org/wiki/Merge_sort)
</figure>

#### Implementation
```python
def merge(L,R):
    # merge two sorted sublists (Left and Right) into one sorted list
    nL = len(L)
    nR = len(R)
    A = []
    i = j = 0
    # compare each pair of element of the two sublists to sort and merge them 
    while i<nL and j<nR:
        if L[i] <= R[j]:
            A.append(L[i])
            i += 1
        else:
            A.append(R[j])
            j += 1
    # when one sublist exhausts first, fill A with all the remaining elements of the other sublist
    if i == nL:
        A.extend(R[j:])
    elif j == nR:                
        A.extend(L[i:])        
    return A   
        
def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    else:
        mid = int(n/2)
        L = merge_sort(A[:mid])
        R = merge_sort(A[mid:])
        return merge(L,R)
```

#### Analysis
* Time complexity: O(nLogn)
* Space complexity: O(n) (suppose that )