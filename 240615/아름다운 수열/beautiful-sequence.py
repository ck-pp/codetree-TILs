N = int(input())
N_list = []
for _ in range(N):
    N_list.append(int(input()))
# 1 8 5 7 9 10

M = int(input())
M_list = []
for _ in range(M):
    M_list.append(int(input()))
M_list.sort()
# 4 6 7

K = 0
K_idx = []
p = []
for idx in range(0, len(N_list)-len(M_list)+1):
    temp_p = sorted(N_list[idx:idx+3])
    flag = True
    for idx_m in range(1, len(M_list)):
        diff = M_list[0]-temp_p[0]
        if diff != M_list[idx_m]-temp_p[idx_m]:
            flag = False
            break
    if flag:
        K += 1
        K_idx.append(idx+1)

print(K)
for idx_k in K_idx:
    print(idx_k)