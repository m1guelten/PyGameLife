import pytest
from utils import calc_arr, func_next_step
arr_start = [[0] * 5 for i in range(5)]
arr_finish = [[0] * 5 for j in range(5)]


arr_test = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0]
]


def clear_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = 0


@pytest.mark.parametrize(
    ("arr", "start_i", "start_j", "result"),
    [(arr_test, 0, 0, 2), (arr_test, 0, 1, 1), (arr_test, 0, 2, 3), (arr_test, 0, 3, 1), (arr_test, 0, 4, 1),
     (arr_test, 1, 0, 3), (arr_test, 1, 1, 2), (arr_test, 1, 2, 4), (arr_test, 1, 3, 1), (arr_test, 1, 4, 1),
     (arr_test, 2, 0, 2), (arr_test, 2, 1, 1), (arr_test, 2, 2, 4), (arr_test, 2, 3, 1), (arr_test, 2, 4, 2),
     (arr_test, 3, 0, 1), (arr_test, 3, 1, 1), (arr_test, 3, 2, 4), (arr_test, 3, 3, 2), (arr_test, 3, 4, 3),
     (arr_test, 4, 0, 1), (arr_test, 4, 1, 1), (arr_test, 4, 2, 3), (arr_test, 4, 3, 1), (arr_test, 4, 4, 2),
     ]
)
def test_calc_arr(arr, start_i, start_j, result):
    assert result == calc_arr(arr, start_i, start_j)


def test_func_next_step_erase():
    arr_start[0][0] = 1
    assert func_next_step(arr_start) == arr_finish, "Перевірка зникнення клітини від самотності"


def test_func_next_step_new():
    clear_arr(arr_start)
    arr_start[3][2] = 1
    arr_start[2][2] = 1
    arr_start[2][3] = 1
    arr_finish[3][2] = 1
    arr_finish[2][2] = 1
    arr_finish[2][3] = 1
    arr_finish[3][3] = 1
    assert func_next_step(arr_start) == arr_finish, "Перевірка народження клітини поблизу 3 інших клітин"


def test_func_next_step_new_erase():
    clear_arr(arr_start)
    clear_arr(arr_finish)
    arr_start[3][1] = 1
    arr_start[2][1] = 1
    arr_start[1][1] = 1
    arr_finish[2][0] = 1
    arr_finish[2][1] = 1
    arr_finish[2][2] = 1

    assert func_next_step(arr_start) == arr_finish, "Перевірка народження нової клітини і зникнення інших"
