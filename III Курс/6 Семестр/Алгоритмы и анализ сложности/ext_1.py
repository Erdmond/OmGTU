def nearest_greater_to_right(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] + 1
        else:
            result[i] = -1
        stack.append(i)

        print([i + 1 for i in stack])
    return result

a = [14, 20, 21, 13, 5, 87, 9, 61, 3, 45, 10, 36]
ans = nearest_greater_to_right(a)

print("Массив: ", a)
print("Индексы: ", ans)
