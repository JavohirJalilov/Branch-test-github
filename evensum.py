def even_sum_digit(l:list)->int:
    even = 0
    for i in l:
        if i%2 == 0:
            even += i
    return even
