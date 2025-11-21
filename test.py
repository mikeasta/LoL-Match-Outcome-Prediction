A = list(input())
B = sorted(list(input()), reverse=True)  

b_idx = 0

for i in range(len(A)):
    if b_idx < len(B) and A[i] < B[b_idx]:
        A[i] = B[b_idx] 
        b_idx += 1  

res = ''.join(A)  
print(res)