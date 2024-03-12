# imperative

arr = [1, 43, -35, 3, -1, 123, 0]

max_value = arr[0]

idx = 1

while idx < len(arr):
    if arr[idx] > max_value:
        max_value = arr[idx]
    idx += 1

print(max_value)

#declarative
print(max(arr))