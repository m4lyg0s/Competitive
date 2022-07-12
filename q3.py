# https://atcoder.jp/contests/abc191/tasks/abc191_b
n, x = map(int, input().split())
a_array = list(map(int, input().split()))

result = []

for i in range(n):
    if(a_array[i] != x):
        result.append(a_array[i])

print(*result)
