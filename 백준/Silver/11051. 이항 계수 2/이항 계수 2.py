import sys

a,b = map(int, input().split())
pascal = [[1],[1,1]]
for i in range(2,a+1):
    pascal.append([1])
    for j in range(1,i):
        pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
    pascal[i].append(1)
print(pascal[a][b] % 10007)