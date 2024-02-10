import tkinter as tk

# Создаем класс War
class War:
    def init(self, root):
        self.root = root
        self.root.title("Война вирусов")

# Создаем окно приложения
root = tk.Tk()

# Создаем объект класса War
game = War()

# Функции для кнопок
def play_game():
    print("Игра началась!")

def show_rules():
    print("Правила игры: ...")

def exit_game():
    root.destroy()

# Создаем холст для отображения игрового поля
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Функция для отрисовки игрового поля
def draw_board():
    canvas.delete("all")
    # Отрисовываем сетку игрового поля
    for i in range(10):
        canvas.create_line(50 * i, 0, 50 * i, 500)
        canvas.create_line(0, 50 * i, 500, 50 * i)

# Функция для отрисовки кружка на ячейке
def draw_circle(x, y):
    canvas.create_oval(x * 50 + 10, y * 50 + 10, x * 50 + 40, y * 50 + 40, fill="blue")

# Функция для обработки кликов мыши
def handle_click(event):
    # Получаем координаты клика
    x = event.x // 50
    y = event.y // 50
    # Отображаем координаты клика в консоли
    print("Клик на ячейку", x, y)
    # Отрисовываем кружок на ячейке
    draw_circle(x, y)

# Привязываем функцию handle_click к событию клика мыши
canvas.bind("<Button-1>", handle_click)

# Отрисовываем игровое поле
draw_board()

# Запускаем главный цикл приложения
root.mainloop()