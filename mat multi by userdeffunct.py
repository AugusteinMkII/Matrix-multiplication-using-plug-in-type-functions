


def some_function(word):
    space = ' ' # there is a single space between the quotes
    if space in word:
        return False
    # both letters 'A' and 'Z' are in upper case
    if not('A' <= word[0] <= 'Z'):
        return False
    for i in range(1, len(word)):
        # both letters 'a' and 'z' are in lower case
        if not('a' <= word[i] <= 'z'):
            return False
    return True


def minmax(a, b):
    if a <= b:
        return a, b
    return b, a

print(minmax(2200,23))


print(some_function('Riemann'))


####performing matrix multiplication
####step:1 intializing matrix C, which will be multiplication
####of mat A and mat B.
####step:2 considering the mat A and mat B, disintegrating
####rows and columns for readily multiply.
####step:3 dot product of mat A and B
####step:4

def initialize_mat(dim):
    C = [] ###initialize c as a list variable.
    for i in range(dim):##iterarte for dimension of mat
        C.append([])    ##for each iteration append in C empty list
        for j in range(dim):
            C[i].append(0) ## for each iteration append 0 in C[ith] list.
    return C
import numpy



def dot_product(u,v):
    dim = len(u)
    dot = 0
    for i in range(dim):
        dot = dot + u[i]*u[i]
    return dot

def row(A,i):
    #dim =len(A)
    row = []
    for k in range(len(A)):
        row.append(A[i][k])
    return row

def column(A,j):
    col = []
    for i in range(len(A)):
        col.append(A[j][i])
    return col

def mat_multiplication(A,B):
    dim = len(A)
    C = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A,i),column(B,j))
    return C

A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[12,13,14],[15,16,17], [18,19,20]]
print(mat_multiplication(A,B))



def unique(list):
    num = []
    for element in list:
        if element in num:
            num.append(element)
    return num
print(unique([1,2,3,1,3,2]))

def uniquee(L):
    L_uniq = [ ]
    for i in range(0, len(L)):
        if not(L[i] in L[i + 1: ]):
            L_uniq.append(L[i])
    return L_uniq

print(uniquee([1,2,3,3,2,1]))