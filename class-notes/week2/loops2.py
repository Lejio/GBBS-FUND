
# a = [1,2,3,4,5,6,7,8,9,10]


a = [8, 17, 15, 5, 9, 19, 11, 3, 4, 18, 2, 14, 12, 13, 1, 10, 16, 20, 7, 6]

# %

# print(a[0] == 11)

# 27 mod 9 = 0
# 65 mod 8 = 1

# 5 mod 2 

# b = 5
# print(a[b])


# for i in range(len(a)):
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# Big O Notation: describes how fast an algorithm runs 

# y=x

# In big o notation, it means that in the worse case, the size of the input is directly proportional to the time it takes to run the

# O(n) - Linear Time Complexity

# O(n^2) - Quadratic Time Complexity

# O(log(n)) - Logarithmic Time Complexity

# O(1) - Constant Time Complexity
for i in range(len(a)):
    
    if a[i]==20:
        print(i)
