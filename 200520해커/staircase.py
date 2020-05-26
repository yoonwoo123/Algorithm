n = 4

for i in range(n-1, -1, -1):
    arr = [' ' for _ in range(i)] + ['#' for q in range(n-i)]
    print(''.join(arr))