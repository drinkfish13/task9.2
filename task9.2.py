# Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали.
import numpy as np
n =int(input())
print(np.diag(np.flip(np.arange(n)), k=0))
print('Cумма ее значений на диагонали: ',np.trace(np.diag(np.flip(np.arange(n)), k=0)))
