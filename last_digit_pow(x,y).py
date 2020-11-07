def last_digit(n1, n2):
    if n2 == 0:
        return 1
    elif n1 == 0:
        return 0
    last_dig = [[0,0,0,0], [1,1,1,1], [2,4,8,6], [3,9,7,1], [4,6,4,6],
                [5,5,5,5], [6,6,6,6], [7,9,3,1], [8,4,2,6], [9,1,9,1]]
    return last_dig[n1%10][(n2 - 1) % 4]


n1, n2 = 12, 30
# n1, n2 = 6, 21

print(last_digit(n1, n2))
