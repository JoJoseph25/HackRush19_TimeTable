#Num of student to binary
def int_to_bin(n):
   s = bin(n)[2:]
   s = '0'*(9-len(s))+s
   return s
#Binary to num of student
def bin_to_int(s):
   return int(s,2)

# Valid Encoding Check or return random valid encoding
import random
def search(dict,value):
   if value in dict.values():
       return value
   else:
       return dict[list(dict.keys())[random.randint(0,len(dict)-1)]]

# Search / Sort Chromosomes
def partition(A, p, r, L, R):
    pivot = int(A[r][L:R],2)
    i = p-1
    for j in range(p,r):
        if int(A[j][L:R], 2) <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
def quicksort(A, p, r, L, R):
    if p < r:
        q = partition(A, p, r, L, R)
        quicksort(A, p, q-1, L, R)
        quicksort(A, q+1, r, L, R)

B = ['01110', '11001', '01101', '01011', '11100', '11010', '00111', '10011','10101', '10110']

import copy

def search(arr, ptrn, L, R):
    found = []
    for s in arr:
        if s[L:R] == ptrn:
            found.append(s)
    return found

# print (search(B, '01', 0,2))

# # def sort(arr, L, R):
# temp = []
# for i in range(len(B)):
#     temp.append(B[i])
# quicksort(temp,0, len(B)-1, 0, 2 )

# print (B)
# print (temp)

# CourseCode to binary

def CourseCode_to_binary(Code,Discipline_encode,Level_encode,Last_Digits_encode):
    if len(Code.split())==2:
        Discipline,Num=Code.split()
    else:
        Discipline,Num,Extra=Code.split()
    Level=Num[:1]
    Last_Digit=Num[1:]
    Discipline_binary=Discipline_encode[Discipline]
    Level_binary=Level_encode[Level]
    Last_Digits_binary=Last_Digits_encode[Last_Digit]

    CourseCode_binary=Discipline_binary+Level_binary+Last_Digits_binary
    return CourseCode_binary
