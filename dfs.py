# 중복순열 dfs

arr = [True, False]

def dfs(ans: list, m: int, depth: int):
    if depth == m:
        print(ans)
        return ans
    else:
        for d in arr:
            ans[depth] = d
            dfs(ans, m, depth+1)

for i in range(1, 4):
    m = i
    ans = [0] * m
    dfs(ans, m, 0)
    print()