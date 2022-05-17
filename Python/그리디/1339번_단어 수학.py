n = int(input())

word_lst = []
for _ in range(n):
    word_lst.append(input())

result = {}
for word in word_lst:
    for i, w in enumerate(word):
        if w not in result.keys():
            result[w] = 10 ** (len(word) - (i + 1))
        else:
            result[w] += 10 ** (len(word) - (i + 1))
answer = sorted(result.items(), key = lambda x : x[1], reverse=True)

output = 0
i = 9
for _, value in answer:
    output += i * value
    i -= 1

print(output)