def remove_duplicates(n):
    new_list = []

    for i in n:
        if i not in new_list:
            new_list.append(i)
    return new_list


print (remove_duplicates([1, 1, 2, 2, 3, 3]))