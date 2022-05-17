import sys

n = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    sys.exit()
else:
    result = 0
    while boxes:
        if not boxes:
            break
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        result += 1
    print(result)