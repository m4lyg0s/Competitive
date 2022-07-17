# https://atcoder.jp/contests/abc197/tasks/abc197_b
h, w, x, y = map(int, input().split())

grid = []
for i in range(h):
    s = input()
    s = list(s)
    grid.append(s)

x -= 1
y -= 1

ans = 0

for i in range(1, h):
    if 0 <= x-i < h:
        if grid[x-i][y] == "#":
            break
        else:
            ans += 1

for i in range(1, h):
    if 0 <= x+i < h:
        if grid[x+i][y] == "#":
            break
        else:
            ans += 1

for i in range(1, w):
    if 0 <= y-i < w:
        if grid[x][y-i] == "#":
            break
        else:
            ans += 1

for i in range(1, w):
    if 0 <= y+i < w:
        if grid[x][y+i] == "#":
            break
        else:
            ans += 1

ans += 1
print(ans)
