import csv

WIDTH = 18
HEIGHT = 9

lines = []
with open('./map.csv', 'r') as f:
    rdr = csv.reader(f)
    for row in rdr:
        tmp_line = []
        for el in row:
            tmp_line.append(int(el))
        lines.append(tmp_line)

height = len(lines)
width = len(lines[0])


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


def transpose(lines: list):
    result = []
    height = len(lines)
    width = len(lines[0])
    for i in range(width):
        line = []
        for j in range(height):
            s = lines[j][i]
            line.append(s)
        result.append(line)
    return result


def pop_line_dir(lines: list, dir: bool):
    result = []
    if dir:
        for i in range(height):
            row = []
            for j in range(width):
                row.append(lines[i][j])
            result.append(pop_line(row))
        return result
    
    else:
        for i in range(width):
            col = []
            for j in range(height):
                col.append(lines[j][i])
            result.append(pop_line(col))
        return transpose(result)


def print_lines(lines: list):
    for line in lines:
        line_str = ''
        for el in line:
            if el == 0:
                line_str += ' '
            else:
                line_str += str(el)
        print(line_str)


def get_grade(lines: list):
    space = 0
    for nl in lines:
        for n in nl:
            if n == 0:
                space += 1
    print('grade:', space)


def show_result(lines: list, msg: str):
    print(f'== {msg} ==')
    print('-------------------')
    print_lines(lines)
    print('-------------------')
    get_grade(lines)
    print()
            

# result = pop_line_dir(lines[:], True)
# result2 = pop_line_dir(lines[:], False)

# r = pop_line_dir(lines[:], True)
# show_result(r, 'r')
# rc = pop_line_dir(r, False)
# show_result(rc, 'rc')
# rcr = pop_line_dir(rc, True)
# show_result(rcr, 'rcr')
# rcrc = pop_line_dir(rcr, False)
# show_result(rcrc, 'rcrc')
# rcrcc = pop_line_dir(rcrc, False)
# show_result(rcrcc, 'rcrcc')
