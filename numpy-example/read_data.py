f = open('a.dat')

matrix = []
for line in f:
    #print(line)
    words = line.split()
    print(words)
    row_of_numbers = []
    for w  in words:
        row_of_numbers.append(float(w))
    print(row_of_numbers)
    matrix.append(row_of_numbers)

print(matrix)
