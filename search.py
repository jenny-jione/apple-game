# dfs + elppa (ing)

import ap

arr = [True, False]

def dfs(lines: list, m: int, depth: int):
    if depth == m:
        return
    else:
        for d in arr:
            # ans[depth] = d
            ap.pop_line_dir(lines, d)
            dfs(ans, m, depth+1)

for i in range(1, 2):
    m = i
    ans = [0] * m
    # lines = ap.
    dfs(ans, m, 0)
    print()