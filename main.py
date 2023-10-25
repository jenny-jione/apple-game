import csv

arr = [True, False]

def get_map():
    maps = []
    with open('./test.csv', 'r') as f:
        rdr = csv.reader(f)
        for row in rdr:
            tmp_line = []
            for el in row:
                tmp_line.append(int(el))
            maps.append(tmp_line)
    return maps


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
    DEPTH = 5
    ans = [0] * DEPTH
    dfs(ans, 0, all_results)
    