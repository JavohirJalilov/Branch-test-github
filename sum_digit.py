def odd_sum_digit(l:list)->int:
    odd = 0
    for i in l:
        if i%2 == 1:
            odd += i
    return odd

# odd function

def even_sum_digit(l1:list)->int:
    even = 0
    for x in l1:
        if x%2 == 0:
            even += x
    return even