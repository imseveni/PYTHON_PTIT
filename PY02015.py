while True:
    arr = list(map(int, input().split()))

    if arr[0] == arr[1] == arr[2] == arr[3] == 0:
        break

    count = 0
    while not(arr[0] == arr[1] == arr[2] == arr[3]):
        n0 = abs(arr[0] - arr[1])
        n1 = abs(arr[1] - arr[2])
        n2 = abs(arr[2] - arr[3])
        n3 = abs(arr[3] - arr[0])

        arr[0] = n0
        arr[1] = n1
        arr[2] = n2
        arr[3] = n3
        
        count += 1

    print(count)