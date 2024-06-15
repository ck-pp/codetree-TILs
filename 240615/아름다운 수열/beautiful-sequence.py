N = int(input())
N_list = []
for _ in range(N):
    N_list.append(int(input()))

M = int(input())
M_list = []
for _ in range(M):
    M_list.append(int(input()))
M_list.sort()

K = 0
K_idx = []
p = []
# if len(M_list) == 1:
#     K = len(N_list)
#     K_idx.extend([idx_k+1 for idx_k in range(len(N_list))])
# else:
for idx in range(0, len(N_list)-len(M_list)+1):
    temp_p = sorted(N_list[idx:idx+len(M_list)])
    diff = M_list[0]-temp_p[0]
    flag = True
    for idx_m in range(len(M_list)-1):
        if diff != M_list[idx_m]-temp_p[idx_m]:
            flag = False
            break
    if flag:
        K += 1
        K_idx.append(idx+1)

print(K)
for idx_k in K_idx:
    print(idx_k)