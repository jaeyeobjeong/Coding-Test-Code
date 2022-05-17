n = int(input())

books = {}
for i in range(n):
    book = input()
    if book in books.keys():
        books[book] += 1
    else:
        books[book] = 1

result = sorted(sorted(books.items()), key = (lambda k : k[1]), reverse=True)
print(result[0][0])