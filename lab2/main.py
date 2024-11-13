import tkinter as tk
import random
import math
import json

# Создание окна приложения
root = tk.Tk()
root.title('Дождь')

# Загрузка настроек из JSON файла
with open('start_param.json', 'r') as file:
    config = json.load(file)

# Извлечение параметров из файла конфигурации
num_drops = config['num_drops']
density = config['density']
speed_range = config['speed']
angle_range = config['angle']
size_range = config['size']

# Настройка холста для отображения дождя
canvas = tk.Canvas(root, width=800, height=500, bg='#e6e6fa')
canvas.pack()


class RainDrop:
    def __init__(self, speed=None, density_choice=None):
        self.speed = speed or random.uniform(speed_range['min'], speed_range['max'])
        self.density = density_choice or random.choice(density)
        self.start_pos = (random.uniform(0, 800), -200)
        self.angle = math.radians(random.uniform(angle_range['min'], angle_range['max']))
        self.rect = self.create_drop()

    def create_drop(self):
        x, y = self.start_pos
        rect_width = random.uniform(size_range['width']['min'], size_range['width']['max'])
        rect_height = random.uniform(size_range['height']['min'], size_range['height']['max'])
        drop = canvas.create_rectangle(
            x, y, x + rect_width, y + rect_height,
            fill=self.density, outline=''
        )
        return drop

    def move_drop(self):
        x_move = self.speed * math.sin(self.angle)
        y_move = self.speed * math.cos(self.angle)
        canvas.move(self.rect, x_move, y_move)

        # Если капля выходит за экран, сбрасываем её в верхнюю часть экрана
        if self.is_off_screen():
            self.reset_drop()

        # Рекурсивный вызов для продолжения анимации
        canvas.after(60, self.move_drop)

    def is_off_screen(self):
        x1, y1, x2, y2 = canvas.coords(self.rect)
        return y2 > canvas.winfo_height()

    def reset_drop(self):
        """Сбрасываем каплю в верхнюю часть экрана"""
        self.start_pos = (random.uniform(0, 800), -200)
        self.speed = random.uniform(speed_range['min'], speed_range['max'])
        self.density = random.choice(density)
        self.angle = math.radians(random.uniform(angle_range['min'], angle_range['max']))
        canvas.delete(self.rect)  # Удаляем старую каплю
        self.rect = self.create_drop()  


def simulate_rain():
    drops = []
    for _ in range(num_drops):
        drop = RainDrop()
        drops.append(drop)
        drop.move_drop()  # Начинаем движение для каждой капли

simulate_rain()

root.mainloop()
