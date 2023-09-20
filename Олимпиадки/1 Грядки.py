# k = 1, k = 2, k = 3, k = 20
# l = 7
# n = 5
# m = 10

k = int(input())
l = int(input())
n = int(input())
m = int(input())

s1 = 2 * l * k + (2 * m + 2 * n) * k + (2 * m + m * (k - 2)) * (k - 1)
print(s1)

s2 = 0
while k > 0:
    s2 += 2 * l + 2 * m + 2*n + 2 * m * (k - 1)
    k = k - 1
print(s2)
