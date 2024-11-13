import tkinter as tk
import math

# Создание окна
root = tk.Tk()
root.title('Движущаяся точка на окружности')

# Размер окна
WIDTH = 600
HEIGHT = 600
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# Радиус окружности
RADIUS = 200

# Начальные параметры
speed = 0.05  
angle = 0  
direction = 1 

# Создание холста
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()

# Отображение окружности
canvas.create_oval(
    CENTER_X - RADIUS, CENTER_Y - RADIUS,
    CENTER_X + RADIUS, CENTER_Y + RADIUS,
    outline='black'
)

# Точка, которая будет двигаться
point = canvas.create_oval(
    CENTER_X + RADIUS, CENTER_Y, CENTER_X + RADIUS + 5, CENTER_Y + 5, fill='red'
)

def move_point():
    global angle

    # Изменение угла в зависимости от скорости и направления
    angle += speed * direction

    # Пересчитываем координаты точки
    x = CENTER_X + RADIUS * math.cos(angle)
    y = CENTER_Y + RADIUS * math.sin(angle)

    # Перемещаем точку на новые координаты
    canvas.coords(point, x - 5, y - 5, x + 5, y + 5)

    # Повторный вызов через 20 миллисекунд для создания анимации
    canvas.after(20, move_point)

# Запуск движения
move_point()

# Управление событиями для изменения скорости и направления
def change_speed(event):
    global speed
    if event.keysym == 'Up':
        speed += 0.01  # Увеличиваем скорость при нажатии на стрелку вверх
    elif event.keysym == 'Down':
        speed = max(0.01, speed - 0.01)  # Уменьшаем скорость при нажатии на стрелку вниз

def change_direction(event):
    global direction
    if event.keysym == 'Left':
        direction = -1  # Изменяем направление на против часовой стрелки
    elif event.keysym == 'Right':
        direction = 1  # Изменяем направление на по часовой стрелке

# Привязка событий для управления
root.bind('<Up>', change_speed)
root.bind('<Down>', change_speed)
root.bind('<Left>', change_direction)
root.bind('<Right>', change_direction)

# Запуск главного цикла
root.mainloop()
