import numpy as np
import matplotlib.pyplot as plt

def make_circle(points):
    if len(points) == 0:
        return None
    elif len(points) == 1:
        return (points[0], 0)
    elif len(points) == 2:
        center = np.mean(points, axis=0)
        radius = np.linalg.norm(points[0] - points[1]) / 2
        return (center, radius)
    else:
        return welzl(points, [], 0)

def welzl(points, boundary, boundary_length):
    if len(points) == 0 or len(boundary) == 3:
        if len(boundary) == 0:
            return None
        elif len(boundary) == 1:
            return (boundary[0], 0)
        elif len(boundary) == 2:
            center = np.mean(boundary, axis=0)
            radius = np.linalg.norm(boundary[0] - boundary[1]) / 2
            return (center, radius)
        else:
            return circumcircle(boundary[0], boundary[1], boundary[2])

    point = points[0]
    circle = welzl(points[1:], boundary, boundary_length)

    if circle is not None and point_in_circle(point, circle):
        return circle

    new_boundary = boundary + [point]
    new_boundary_length = boundary_length + 1
    circle = welzl(points[1:], new_boundary, new_boundary_length)

    return circle

def circumcircle(a, b, c):
    d = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    ux = ((np.linalg.norm(a) ** 2) * (b[1] - c[1]) + (np.linalg.norm(b) ** 2) * (c[1] - a[1]) + (np.linalg.norm(c) ** 2) * (a[1] - b[1])) / d
    uy = ((np.linalg.norm(a) ** 2) * (c[0] - b[0]) + (np.linalg.norm(b) ** 2) * (a[0] - c[0]) + (np.linalg.norm(c) ** 2) * (b[0] - a[0])) / d
    center = np.array([ux, uy])
    radius = np.linalg.norm(center - a)
    return (center, radius)

def point_in_circle(point, circle):
    center, radius = circle
    return np.linalg.norm(point - center) <= radius

# Приклад використання
n = np.random.randint(1, 21)  # Випадкова кількість точок від 1 до 20
points = np.random.rand(n, 2)  # Генеруємо випадкову кількість точок
circle = make_circle(points)

#n = int(input("Введіть кількість точок: "))
#points = []
#for i in range(n):
#    x = float(input("Введіть координату x для точки {}: ".format(i+1)))
#    y = float(input("Введіть координату y для точки {}: ".format(i+1)))
#    points.append([x, y])
#points = np.array(points)

circle = make_circle(points)

plt.scatter(points[:, 0], points[:, 1], color='b')
# Візуалізуємо точки
if circle:
    center, radius = circle
    circle_plot = plt.Circle(center, radius, color='r', fill=False)
# Візуалізуємо коло
    plt.gca().add_patch(circle_plot)

plt.axis('equal')
plt.show()

if circle:
    center, radius = circle
    print("Радіус кола найменшого радіусу:", radius)

print("Згенеровані точки:")
for point in points:
    print(point)

if circle:
    center, radius = circle
    print("Координати центра кола:", center)