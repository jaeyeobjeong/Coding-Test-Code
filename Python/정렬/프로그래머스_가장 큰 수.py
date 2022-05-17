def solution(numbers):
    numbers = list(map(str, numbers))
    # lambda x : x * 3은 num 인자 각각의 문자열을 3번 반복한다는 뜻이다.
    # x * 3을 하는 이유? num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

lst = [303030, 333]
lst.sort()
print(lst)