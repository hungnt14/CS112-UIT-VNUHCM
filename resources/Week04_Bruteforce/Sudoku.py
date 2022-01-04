SIZE = 9

mat = [[int(j) for j in input().strip().split()] for i in range(0, SIZE)]

def calc(i, j):
    if (i == SIZE):
        return True

    if mat[i][j] != 0: 
        if calc(i + (j+1)//SIZE, (j+1) % SIZE):
            return True
    elif mat[i][j] == 0:
        validValues = [True for x in range(0, SIZE+1)]
        for i2 in range(0, SIZE):
            validValues[mat[i2][j]] = False
        for j2 in range(0, SIZE):
            validValues[mat[i][j2]] = False
        for i2 in range(i//3 * 3, (i//3+1) * 3):
            for j2 in range(j//3 * 3, (j//3+1) * 3):
                validValues[mat[i2][j2]] = False

        for x in range(1, SIZE+1):
            if validValues[x] == True:
                mat[i][j] = x
                if calc(i + (j+1)//SIZE, (j+1) % SIZE):
                    return True
        mat[i][j] = 0
    return False

#-------------------

if calc(0, 0) == False:
    print("None")
else:
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            print(mat[i][j], end=' ')
        print(end='\n')