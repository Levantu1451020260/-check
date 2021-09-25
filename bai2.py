A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
print("List C sau khi lưu trữ các số trùng bên list A,B: ", set(A) & set(B))
C= set(A) & set(B)
A=set(A)-set(C)
B=set(B)-set(C)
print("list A")
print("list B")