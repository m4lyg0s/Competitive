# https://atcoder.jp/contests/abc201/tasks/abc201_b
n = int(input())

moutain = []
for i in range(n):
    s, t = map(str, input().split())
    t = int(t)
    moutain.append([s, t])
moutain.sort(key=lambda x: x[1], reverse=True)

print(moutain[1][0])
