def insert(lst, table_size):
    hash_list = [False] * table_size
    
    for item in lst:
        h1k = item % table_size
        h2k = 1 + (item % (table_size - 1))
        for i in range(table_size):
            hk = (h1k + i * h2k) % table_size
            if hash_list[hk] == False:
                hash_list[hk] = item
                break
        else:
            print("table is full")

    return hash_list

lst = [10, 22, 31, 4, 15, 28, 17, 88, 59]
size = 11
hash_list = insert(lst, size)
print(hash_list)