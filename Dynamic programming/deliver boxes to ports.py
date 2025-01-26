boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]]
mw = 7
mb = 5
pc = 5
n = len(boxes)
def solve(i):
    if i > n - 1: return 0
    j = k = i
    b = w = count = 0
    while j < n and b < mb and w + boxes[j][1] <= mw:
        b += 1
        w += boxes[j][1]
        if j != i and boxes[j][0] != boxes[j - 1][0]:
            count += 1
            k = j
        j += 1
    trip = 2 + count + solve(j)
    if k != i:
        trip = min(trip, 1 + count + solve(k))
    return trip

print(solve(0))