import os
import random
import sys

# defined function
def generateRandomNumber(LowerBound, UpperBound, Type):
    if Type == int:
        return random.randint(LowerBound, UpperBound)
    elif Type == float:
        return random.uniform(LowerBound, UpperBound)
    else:
        raise Exception("Invalid type of number: " + str(Type))

# create folder
if not os.path.exists("./test"):
    os.makedirs("test")

# set some constant
TEST_NUMBER = 10
MAX_N = 100000

for TEST_ID in range(TEST_NUMBER):
    # output file
    generated_input_filepath = "./test/findpath" + str(TEST_ID) + ".inp"
    sys.stdout = open(generated_input_filepath,'w')

    n = generateRandomNumber(1, MAX_N, int)
    m = generateRandomNumber(1, MAX_N, int)
    s = generateRandomNumber(0, n - 1, int)
    d = generateRandomNumber(0, n - 1, int)

    print(n, m, s, d)

    EdgeList = []

    for i in range(m):
        while True:
            u = generateRandomNumber(0, n - 1, int)
            v = generateRandomNumber(0, n - 1, int)

            if ((u, v) not in EdgeList and (v, u) not in EdgeList):
                EdgeList.append((u, v))
                break

    for edge in EdgeList:
        u, v = edge
        print(u, v)

    