import csv

arr = [True, False]

def get_matrix():
    matrix = []
    with open('./map.csv', 'r') as f:
        rdr = csv.reader(f)
        for row in rdr:
            tmp_line = []
            for el in row:
                tmp_line.append(int(el))
            matrix.append(tmp_line)
    return matrix


def dfs(ans: list, depth: int, result: list):
    if depth == DEPTH:
        result.append(ans[:])
        return
    else:
        for d in arr:
            ans[depth] = d
            dfs(ans, depth+1, result)


def pop_line(line: list):
    i = 0
    j = 1
    while(i<len(line) and j<=len(line)):
        if sum(line[i:j]) == 10:
            line[i:j] = [0 for _ in line[i:j]]
            i += (j-i)
            j = i+1
        elif sum(line[i:j]) > 10:
            i += 1
            j = i+1
        else:
            j += 1
    return line


def transpose(matrix: list):
    result = []
    b = len(matrix)
    a = len(matrix[0])
    for i in range(a):
        row = []
        for j in range(b):
            row.append(matrix[j][i])
        result.append(row)
    return result


def pop_apple(matrix: list, dir_row: bool):
    h = len(matrix)
    w = len(matrix[0])
    result = []
    if dir_row:
        for i in range(h):
            row = []
            for j in range(w):
                row.append(matrix[i][j])
            result.append(pop_line(row))
        return result
    else:
        for j in range(w):
            col = []
            for i in range(h):
                col.append(matrix[i][j])
            result.append(pop_line(col))
        return transpose(result)


## show result
def print_matrix(matrix: list):
    for row in matrix:
        row_str = ''
        for el in row:
            if el == 0:
                row_str += ' '
            else:
                row_str += str(el)
        print(row_str)


def get_grade(matrix: list):
    space = 0
    for row in matrix:
        for element in row:
            if element == 0:
                space += 1
    print('grade:', space)


def show_result(matrix: list, msg: str):
    line_len = len(matrix[0]) + 1
    side = ((line_len - len(msg)) // 2) - 1
    line = '-' * side + ' ' + msg + ' ' + '-' * side
    print(line)
    print_matrix(matrix)
    get_grade(matrix)
    print('-' * line_len)
    print()
            

if __name__ == "__main__":
    all_results = []
    DEPTH = 5
    ans = [0] * DEPTH
    dfs(ans, 0, all_results)
    
    # for result in all_results:
    #     for direction in result:
    
    matrix = get_matrix()
    show_result(matrix, 'original')
    
    matrix1 = pop_apple(matrix[:], True)
    show_result(matrix1, 'row')
    matrix2 = pop_apple(matrix[:], False)
    show_result(matrix2, 'col')