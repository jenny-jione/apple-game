# 중복순열 dfs

arr = [True, False]

def dfs(ans: list, m: int, depth: int, result: list):
    if depth == m:
        print(ans)
        result.append(ans[:])
        return ans
    else:
        for d in arr:
            ans[depth] = d
            dfs(ans, m, depth+1, result)


if __name__ == "__main__":

    result = []

    # for i in range(1, 4):
    #     m = i
    #     ans = [0] * m
    #     dfs(ans, m, 0, result)
    
    # print(result)
    
    m = 5
    ans = [0] * m
    dfs(ans, m, 0, result)