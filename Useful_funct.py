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
