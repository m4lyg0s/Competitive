# https://atcoder.jp/contests/abc188/tasks/abc188_b
n = int(input())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))
result = 0

for i in range(n):
    result += a_array[i] * b_array[i]

if(result):
    print('No')
else:
    print('Yes')
