import numpy as np


def prod_non_zero_diag(x):
    ans = np.prod(np.diagonal(x)[np.diagonal(x) > 0])
    return ans

def are_multisets_equal(x, y):
    np.sort(x)
    np.sort(y)
    return x.all() == y.all()


def max_after_zero(x):
    ans = np.max(x[1:][np.nonzero(x[:-1] == 0)])
    return ans


def convert_image(img, coefs):
    return np.dot(img, coefs)


def run_length_encoding(x):
    #Разностный массив
    raz = np.diff(x)
    #Добавим -1 тк без этого не сможем востановить первый элемент
    n = [-1]
    #Добавим индексы которые не равны 0
    n = np.append(n, np.nonzero(raz))
    #Прибавим ко всем 1 и получим массив индексов которые нам подходят
    n += 1
    a = x[n]
    n = np.append(n, len(x))
    b = np.diff(n)
    return [a, b]


def pairwise_distance(x, y):
    n = len(x)
    x = np.repeat(x, n, axis = 0)
    x.reshape((n * 2, n))
    #сделали таблицу n на n
    y = np.tile(y, (n, 1))
    #по сути тоже самое, что и repeat
    y.reshape((2 * n, n))
    #сделали таблицу n на n
    x -= y
    x = x ** 2
    #Это понятно, что типа по x минус и по y минус
    return np.vectorize(np.sqrt)(np.dot(x, np.array([1, 1])))