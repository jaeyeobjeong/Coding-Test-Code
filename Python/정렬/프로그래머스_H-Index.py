citations = [10, 10, 10, 10, 10]
answer = 0
citations.sort(reverse=True)

while answer < citations[0]:
    citations.pop(0)
    answer += 1
    if not citations:
        break
print(answer)