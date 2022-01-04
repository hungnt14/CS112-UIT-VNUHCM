import os
import sys

# read data from input
sys.stdin = open('findpath.inp','r')

n, m, s, d = map(int, input().split())
EdgeList = []

for i in range(m):
    u, v = map(int, input().split())
    EdgeList.append((u, v))

# read data from output
sys.stdin = open('findpath.out','r')

AnsPath = list(map(int, input().split()))

for i in range(len(AnsPath) - 1):
    u = AnsPath[i]
    v = AnsPath[i + 1]
    if (u, v) not in EdgeList and (v, u) not in EdgeList:
        print("Incorrect!! X_X")
        exit()

print("Correct!! ^o^")


