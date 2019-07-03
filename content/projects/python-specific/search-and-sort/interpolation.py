def intpolsearch(values,x ):
    "do an interpolation search to find number in a list"
    idx0 = 0
    idxn = (len(values) - 1)

    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:

# Find the mid point
        mid = idx0 +\
               int(((float(idxn - idx0)/( values[idxn] - values[idx0]))
                    * ( x - values[idx0])))

# Compare the value at mid point with search value
        if values[mid] == x:
            return "Found "+str(x)+" at index "+str(mid)

        if values[mid] < x:
            idx0 = mid + 1
            print("middle point: " + str(mid) + "now searching checking element: " + str(idx0))

    return "Searched element not in the list"
