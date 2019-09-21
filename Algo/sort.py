
### Sorting algorithms


"""""""""""
Bubble sort
"""""""""""
''' O(n^2) '''
def bubble_sort(A): 
    for k in range(len(A)-1,0,-1):       
        flag = 1   
        # swap each pair of adjacent elements if they are not in increasing order
        for i in range(k):
            if A[i] > A[i+1]:   
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                flag = 0
        # if we go through a pass without swapping, the array is already sorted
        if flag == 1:               
            break
    return A


"""""""""""""""
Selection sort
"""""""""""""""
''' O(n^2)'''
def selection_sort(A):
    # move the sorted-unsorted sublists boundary one element to the right at a time
    for i in range(len(A)-1):                   
        # find index of minimum element of unsorted sublist
        iMin = i
        for j, num in enumerate(A[i+1:]):                
            if num < A[iMin]:
                iMin = i+j+1
        # swap minimum element with the unsorted left most element
        if iMin != i:
            temp = A[i]
            A[i] = A[iMin]
            A[iMin] = temp
        print(A)
    return A


"""""""""""""""
Insertion sort
"""""""""""""""
''' O(n^2) '''
def insertion_sort(A):
    for iUnsorted in range(1,len(A)):
        val = A[iUnsorted]   
        for iSorted in range(iUnsorted-1, -1, -1):
            # shift numbers greater than val to the right
            if A[iSorted] > val:
                A[iSorted+1] = A[iSorted]
                if iSorted==0:
                    A[0] = val
            else:
                A[iSorted+1] = val    
                break
    return A


""""""""""
Merge sort
"""""""""
''' O(nLogn) '''

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
    # when one sublist exhaust first, fill A with all the remaining elements of the other sublist
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