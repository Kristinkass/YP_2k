import tkinter as tk
def check_step(m, r, c, step):
    mas = [[0] * 12 for i in range(12)]
    k = 0
    p = 0
    for i in range(1, 11):
        for j in range(1, 11):
            mas[i][j] = m[k][p]
            if p < 9:
                p += 1
            else:
                p = 0
        if k < 9:
            k += 1
        else:
            k = 0
    row = r + 1
    col = c + 1
    if (mas[row - 1][col - 1] == step
            or mas[row - 1][col] == step
            or mas[row - 1][col + 1] == step
            or mas[row][col - 1] == step
            or mas[row][col + 1] == step
            or mas[row + 1][col - 1] == step
            or mas[row + 1][col] == step
            or mas[row + 1][col + 1] == step):
        return True
    return False

def start_the_game(menu):
    size_block = 46
    margin = 5
    screen = tk.Toplevel(menu)
    screen.title("Война вирусов")
    screen.resizable(False, False)
    canvas = tk.Canvas(screen, width=510, height=510)
    canvas.configure(bg='black')
    canvas.pack()

    mas = [[0] * 10 for i in range(10)]
    query = 0
    step = 'x'
    startX = True
    startO = True


    def on_click(event):
        nonlocal query, step, startX, startO
        col = event.x // (margin + size_block)
        row = event.y // (margin + size_block)

        if startX == True:
            if step == 'x' and col == 0 and row == 0:
                mas[row][col] = 'x'
                query += 1
                startX = False

        if startO == True:
            if step == 'o' and col == 9 and row == 9:
                mas[row][col] = 'o'
                query += 1
                startO = False

        if startX == False:
            if step == 'x' and check_step(mas, row, col, step):
                if mas[row][col] == 0: # Убитый "o"
                    mas[row][col] = 'x'
                    query += 1
                if mas[row][col] == 'o':
                    mas[row][col] = 's'  # убитый o
                    query += 1
        if startO == False:
            if step == 'o' and check_step(mas, row, col, step):
                if mas[row][col] == 0 or mas[row][col] == 'z':
                    mas[row][col] = 'o'
                    query += 1
                if mas[row][col] == 'x' or mas[row][col] == 'z':
                    mas[row][col] = 'z'  # убитый x
                    query += 1

        if query == 3:
            if step == 'x':
                step = 'o'
            elif step == 'o':
                step = 'x'
            query = 0

        draw_board()
    def draw_board():
        for row in range(10):
            for col in range(10):
                if mas[row][col] == 'x':
                    color = 'red'
                elif mas[row][col] == 'o':
                    color = 'green'
                elif mas[row][col] == 'z':
                    color = 'red'
                elif mas[row][col] == 's':
                    color = 'blue'
                else:
                    color = 'white'
                x0 = col * size_block + (col + 1) * margin
                y0 = row * size_block + (row + 1) * margin
                x1 = x0 + size_block
                y1 = y0 + size_block
                canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='')
                if color == 'red':
                    if mas[row][col] != 'z':
                        canvas.create_line(x0, y0, x1, y1, width=2, fill='white')
                        canvas.create_line(x1, y0, x0, y1, width=2, fill='white')
                    else:
                        canvas.create_line(x0, y0, x1, y1, width=2, fill='white')
                        canvas.create_line(x1, y0, x0, y1, width=2, fill='white')
                        canvas.create_oval(x0 + size_block // 2 - size_block // 4,
                                           y0 + size_block // 2 - size_block // 4,
                                           x1 - size_block // 2 + size_block // 4,
                                           y1 - size_block // 2 + size_block // 4,
                                           width=3, outline='white')
                elif color == 'green' and mas[row][col] != 's':
                    canvas.create_oval(x0 + size_block // 2 - size_block // 4,
                                       y0 + size_block // 2 - size_block // 4,
                                       x1 - size_block // 2 + size_block // 4,
                                       y1 - size_block // 2 + size_block // 4,
                                       width=3, outline='white')

    canvas.bind("<Button-1>", on_click)
    draw_board()
    menu.withdraw()  # Скрываем окно меню
    screen.protocol("WM_DELETE_WINDOW", lambda: close_game(screen, menu))
def close_game(game_screen, menu):
    game_screen.destroy()
    menu.deiconify()  # Восстанавливаем окно меню
def open_menu():
    menu = tk.Tk()
    menu.title("Меню игры")
    menu.geometry("510x510")
    menu.resizable(False, False)
    menu.configure(bg='black')
    menu.title_label = tk.Label(menu, text="Война вирусов", font=("Arial", 30), bg='white')
    menu.title_label.pack(pady=50)
    play_button = tk.Button(menu, text="Играть", command=lambda: start_the_game(menu), width=10, height=2)
    play_button.pack(pady=10)
    exit_button = tk.Button(menu, text="Выйти", command=menu.destroy, width=10, height=2)
    exit_button.pack(pady=10)
    menu.mainloop()
open_menu()

