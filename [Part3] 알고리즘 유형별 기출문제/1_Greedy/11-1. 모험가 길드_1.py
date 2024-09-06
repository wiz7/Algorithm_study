n = int(input())
data = list(map(int, input().split()))
data.sort()

min_scary_value = 0
result = 0

while min_scary_value < n:
    min_scary_value = min(data)
    n -= min_scary_value
    data = data[min_scary_value:]
    result += 1

print(result)
