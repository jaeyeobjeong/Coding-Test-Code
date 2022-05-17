test_dict = {
    'first' : [[1,23],[323,542]],
    'second': [[23,112], [1234,234]],
    'third' : [[26,7], [23,123]],
}

for v in test_dict.values():
    for l in v:
        print(sum(l), end = '  ')
    print()

test_dict_sorted = sorted(test_dict, key = lambda x : sum(test_dict[x][1]), reverse = True)
print(test_dict_sorted)

test_dlst= list(test_dict.items())
print(test_dlst)

test_dlst.sort(key=lambda x: sum(x[1][1]), reverse=True)
print(test_dlst)

test_dlst.sort(key=lambda x: sum(x[1][0]), reverse=True)
print(test_dlst)

print(sum(0)) # TypeError: 'int' object is not iterable