import csv
import random

WIDTH = 18
HEIGHT = 9

# lines = []
# for i in range(HEIGHT):
#     tmp = []
#     for j in range(WIDTH):
#         tmp.append(str(random.randint(1, 9)))
#     lines.append(tmp)

# import csv
# with open('map.csv', 'w') as f:
#     wr = csv.writer(f)
#     for line in lines:
#         wr.writerow(line)

lines = []
with open('./map.csv', 'r') as f:
    rdr = csv.reader(f)
    for row in rdr:
        tmp_line = []
        for el in row:
            tmp_line.append(int(el))
        lines.append(tmp_line)

    
def get_grade(lines: list):
    space = 0
    for nl in lines:
        for n in nl:
            if n == 0:
                space += 1
    print('grade:', space)


def print_lines(lines: list):
    for line in lines:
        line_str = ''
        for el in line:
            if el == 0:
                line_str += ' '
            else:
                line_str += str(el)
        # print(line_str)


def pop_line(lines: list):
    result = []
    for line in lines:
        i = 0
        j = 1
        while(i<len(line) and j<=len(line)):
            if sum(line[i:j]) == 10:
                line[i:j] = [0 for e in line[i:j]]
                i = i+(j-i)
                j = i+1
            elif sum(line[i:j]) > 10:
                i += 1
                j = i+1
            else:
                j += 1
        result.append(line)
    return result


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
        

print('==')
print_lines(lines)
print('== pop1 (r) ==')
pop_r = pop_line(lines)
print_lines(pop_r)
get_grade(pop_r)
print('== pop2 (r-c) ==')
t = transpose(pop_r)
pop_rc = pop_line(t)
tt = transpose(pop_rc)
print_lines(tt)
get_grade(tt)

print('== pop3 (r-c-r) ==')
pop_rcr = pop_line(tt)
print_lines(pop_rcr)
get_grade(pop_rcr)

print('== pop4 (r-c-r-r) ==')
pop_rcrr = pop_line(pop_rcr)
print_lines(pop_rcrr)
get_grade(pop_rcrr)

print('== pop5 (r-c-r-r-r) ==')
pop_rcrrr = pop_line(pop_rcrr)
print_lines(pop_rcrrr)
get_grade(pop_rcrrr)
