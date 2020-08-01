# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:  # We have broken down the array untill we have no elements, then we start the merging process
        mid = len(dataset) // 2
        leftarr = dataset[:mid]  # Breaking down
        rightarr = dataset[mid:]

        # TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while(i < len(leftarr) and j < len(rightarr)):
            if leftarr[i] < rightarr[j]:  # if leftarray value is less than rightarray value
                dataset[k] = leftarr[i]  # New dataset array has leftarr[i] value
                i += 1  # increment the index of i
            else:  # if rightarr > leftarr
                dataset[k] = rightarr[j]
                j += 1  # increment j value
            k += 1  # increment k value


        # TODO: if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # TODO: if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


# test the merge sort with data
print(items)
mergesort(items)
print(items)
