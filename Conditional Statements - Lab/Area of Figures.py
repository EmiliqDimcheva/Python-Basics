import math

type_and_sizes_of_figure = input()

if type_and_sizes_of_figure == "square":
    a=float(input())
    s=(a * a)
    print(f"{s:.3f}")
elif type_and_sizes_of_figure == "triangle":
    b=float(input())
    a=float(input())
    s=(a * b / 2)
    print(f"{s:.3f}")
elif type_and_sizes_of_figure == "circle":
    r = float(input())
    r=(math.pi * r * r )
    print(f"{r:.3f}")
elif type_and_sizes_of_figure == "rectangle":
    p=float(input())
    a=float(input())
    p=(p * a)
    print(f"{p:.3f}")







