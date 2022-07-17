# https://atcoder.jp/contests/abc190/tasks/abc190_b
n, s, d = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    if(x < s and d < y):
        print("Yes")
        exit()
print("No")
