def bubblesort(list):

# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1): #scan through ever-shortening list
        for idx in range(iter_num):     #for each item in list,
            if list[idx]>list[idx+1]:   #check it against its neighbour
                temp = list[idx]        #and swap if item on left is bigger
                list[idx] = list[idx+1]
                list[idx+1] = temp

    return list

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(bubblesort(unsorted_list))
