# arr_old = [
#     [0,0,0,0,0],
#     [0,0,1,0,0],
#     [1,0,0,1,0],
#     [1,0,0,0,0],
#     [1,0,0,0,0],
# ]

def calc_arr(arr, i, j):
    if i == 0:
        k_up, k_down = len(arr) - 1, 1
    elif i == len(arr) - 1:
        k_up, k_down = len(arr) - 2, 0
    else:
        k_up, k_down = i - 1, i + 1

    if j == 0:
        k_left, k_right = len(arr[i]) - 1, 1
    elif j == len(arr[i]) - 1:
        k_left, k_right = len(arr[i]) - 2, 0
    else:
        k_left, k_right = j - 1, j + 1

    return (arr[k_up][k_left] + arr[k_up][j] + arr[k_up][k_right] +
            arr[i][k_left] + arr[i][k_right] +
            arr[k_down][k_left]+arr[k_down][j]+arr[k_down][k_right])


def func_next_step(arr):
    arr_new = [[0] * len(arr[0]) for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            res = calc_arr(arr, i, j)
            if arr[i][j] == 0:
                if res == 3:
                    arr_new[i][j] = 1
            else:
                arr_new[i][j] = 0 if res < 2 or res > 3 else 1

    return arr_new
