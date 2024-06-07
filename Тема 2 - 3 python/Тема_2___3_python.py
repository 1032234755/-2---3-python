
import sympy as sp
import numpy as np

# ������������ ��������� ��������
a, b, c = 1, -3, 2

# �������� �����
x0, y0 = 1, 0

# �������� �������������� ����� ��������
def is_point_on_parabola(a, b, c, x0, y0):
    return y0 == a * x0**2 + b * x0 + c

is_on_parabola = is_point_on_parabola(a, b, c, x0, y0)
print(f"����� ({x0}, {y0}) {'�����������' if is_on_parabola else '�� �����������'} ��������.")

# ���������� ��������� ������ ��������
def focus_of_parabola(a, b, c):
    # ���������� ������� ��������
    x_vertex = -b / (2 * a)
    y_vertex = a * x_vertex**2 + b * x_vertex + c
    
    # ���������� ������ ��������
    x_focus = x_vertex
    y_focus = y_vertex + 1 / (4 * a)
    
    return x_focus, y_focus

x_focus, y_focus = focus_of_parabola(a, b, c)
print(f"���������� ������ ��������: ({x_focus:.4f}, {y_focus:.4f})")

# ���������� ���������� �� ����������
def distance_to_directrix(a, b, c, x0, y0):
    # ���������� ������� ��������
    x_vertex = -b / (2 * a)
    y_vertex = a * x_vertex**2 + b * x_vertex + c
    
    # ��������� ����������: y = y_vertex - 1 / (4 * a)
    y_directrix = y_vertex - 1 / (4 * a)
    
    # ���������� �� ����� �� ������ y = y_directrix
    return abs(y0 - y_directrix)

distance_directrix = distance_to_directrix(a, b, c, x0, y0)
print(f"���������� �� ����� �� ���������� �������� = {distance_directrix:.4f}")
