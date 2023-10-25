# dfs + elppa (ing)

import ap

arr = [True, False]
DEPTH = 5


def dfs(ans: list, depth: int, result: list):
    if depth == DEPTH:
        result.append(ans[:])
        return
    else:
        for d in arr:
            ans[depth] = d
            dfs(ans, depth+1, result)


if __name__ == "__main__":
    all_results = []
    ans = [0] * DEPTH
    dfs(ans, 0, all_results)
    
    
    
    # for result in all_results:
    #     for direction in result:
            
        # print()