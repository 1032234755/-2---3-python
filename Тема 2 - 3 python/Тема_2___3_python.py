
import sympy as sp
import numpy as np

# Коэффициенты уравнения параболы
a, b, c = 1, -3, 2

# Заданная точка
x0, y0 = 1, 0

# Проверка принадлежности точки параболе
def is_point_on_parabola(a, b, c, x0, y0):
    return y0 == a * x0**2 + b * x0 + c

is_on_parabola = is_point_on_parabola(a, b, c, x0, y0)
print(f"Точка ({x0}, {y0}) {'принадлежит' if is_on_parabola else 'не принадлежит'} параболе.")

# Нахождение координат фокуса параболы
def focus_of_parabola(a, b, c):
    # Координаты вершины параболы
    x_vertex = -b / (2 * a)
    y_vertex = a * x_vertex**2 + b * x_vertex + c
    
    # Координаты фокуса параболы
    x_focus = x_vertex
    y_focus = y_vertex + 1 / (4 * a)
    
    return x_focus, y_focus

x_focus, y_focus = focus_of_parabola(a, b, c)
print(f"Координаты фокуса параболы: ({x_focus:.4f}, {y_focus:.4f})")

# Нахождение расстояния до директрисы
def distance_to_directrix(a, b, c, x0, y0):
    # Координаты вершины параболы
    x_vertex = -b / (2 * a)
    y_vertex = a * x_vertex**2 + b * x_vertex + c
    
    # Уравнение директрисы: y = y_vertex - 1 / (4 * a)
    y_directrix = y_vertex - 1 / (4 * a)
    
    # Расстояние от точки до прямой y = y_directrix
    return abs(y0 - y_directrix)

distance_directrix = distance_to_directrix(a, b, c, x0, y0)
print(f"Расстояние от точки до директрисы параболы = {distance_directrix:.4f}")
