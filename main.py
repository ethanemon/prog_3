"""""
Для заданной матрицы размером 8 x 8 найти такие k, что элементы k-й
строки матрицы совпадают с элементами k-ого столбца.
Найти сумму элементов в тех строках, которые содержат хотя бы один
отрицательный элемент.
"""""

from __future__ import annotations
import random


def get_rand_matrix(w: int, h: int, mn: int, mx: int) -> list[list[int]]:
    return [
        [random.randint(mn, mx) for _ in range(w)] for _ in range(h)
        ]

def get_column(matrix: list[list[int]], col: int) -> list[int]:
    return [row[col] for row in matrix]


def get_k_elems(matrix: list[list[int]]) -> int:
    assert len(matrix) == len(matrix[0])
    res = []
    for k in range(len(matrix)):
        if matrix[k] == get_column(matrix, k):
            res.append(k)
    return res


def main() -> int:

    matrix = get_rand_matrix(8, 8, -10, 10)
    print("Matrix:", matrix)
    ks = get_k_elems(matrix)
    print("K:", ks)

    target_rows = []

    for row in matrix:
        for col in row:
            if col < 0:
                target_rows.append(row)
                break

    for row in target_rows:
        print(row, "->", sum(row))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

if __name__ == "__main__":
    raise SystemExit(main())