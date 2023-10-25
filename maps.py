import csv

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

def show_map(maps: list):
    h = len(maps)
    w = len(maps[0])
    
    for i in range(h):
        row = ''
        for j in range(w):
            row += str(maps[i][j])
        print(row)

def show_map_transpose(maps: list):
    h = len(maps)
    w = len(maps[0])
    
    for j in range(w):
        row = ''
        for i in range(h):
            row += str(maps[i][j])
        print(row)


if __name__ == "__main__":
    maps = get_map()
    show_map(maps)
    show_map_transpose(maps)
    print('==')
