def selection_sort(list):
    for i in range(0,len(list)):
        x = list[i]
        for j in range(0,len(list)):
            if x < list[j]:
                list[i], list[j] = list[j], list [i]
                x= list [j]
    return list
print(selection_sort([-1, 3, 5, 0, 23,-23, 40, -10, -5]))