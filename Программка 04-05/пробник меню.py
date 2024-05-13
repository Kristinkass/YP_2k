from tkinter import *

def toggle_instructions():
    if menu_visible:
        menu_visible = False
        instructions_visible = True
        hide_menu()
        instructions_label.pack(pady=50)
        return_button.pack()
    else:
        menu_visible = True
        instructions_visible = False
        show_menu()
        instructions_label.pack_forget()
        return_button.pack_forget()


def show_menu():
    btn_play.pack()
    btn_rules.pack()
    btn_settings.pack()
    btn_quit_game.pack()


def hide_menu():
    btn_play.pack_forget()
    btn_rules.pack_forget()
    btn_settings.pack_forget()
    btn_quit_game.pack_forget()



def start_game():
    root = Tk()
    root.title("Война вирусов на бумаге")
    root.state('zoomed')

    def exit_game():
        root.destroy()

    menu_visible = True
    instructions_visible = False

    def open_gw():
        game_window = Toplevel(root)
        game_window.title("Игровое окно")
        game_window.state('zoomed')

        game_window.image = PhotoImage(file='Fon2_out.png')
        bg_logo = Label(game_window, image=game_window.image)
        bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

        canvas = Canvas(game_window, width=1601, height=955)
        canvas.pack()

        for i in range(10):
            for j in range(10):
                canvas.create_rectangle(50 + 50 * i, 50 + 50 * j, 100 + 50 * i, 100 + 50 * j, fill='white')

        skip_button = Button(game_window, text="Пропуск хода", width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'))
        skip_button.place(relx=0.07, rely=0.8)

        play_again_button = Button(game_window, text="Играть снова", width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'))
        play_again_button.place(relx=0.39, rely=0.8)

        quit_button = Button(game_window, text="Выход", width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'), command=exit_game)
        quit_button.place(relx=0.72, rely=0.8)

        rules_summary = """
        За один ход комбинация из 3 действий: размножения или уничтожения. 
        Убитые крестики обводятся кружком, а убитые нолики закрашиваются.
        Цель игры – уничтожить все символы противника.
        Любые действия возможны только в доступных клетках, которые расположены 
        по соседству со своей собственной клеткой.
        Можно пропустить полностью свой ход, но запрещается выполнять этот ход частично.
        """
        rules_label = Label(game_window, text=rules_summary, bg='thistle3', font=('Helvetica', 16))
        rules_label.place(relx=0.4, rely=0.07)

    def show_rules():
        rules_window = Toplevel(root)
        rules_window.title("Правила игры")
        rules_window.state('zoomed')

        rules_window.image = PhotoImage(file='Fon2_out.png')
        bg_logo = Label(rules_window, image=rules_window.image)
        bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

        rules_text = """
        Правила игры:
        Данная игра рассчитана на двух игроков, которая проходит на игровом поле размером 10 на 10 клеток. 
        Наиболее удобными обозначениями становятся классические «крестик» и «нолик», обозначающие символы у игроков. 
        Начало игры происходит из противоположных углов игрового поля. За один ход каждый из игроков может выполнить 
        на выбор любую комбинацию из 3 действий: размножение – игрок ставит один свой символ в незанятую клетку, 
        соседнюю со своим символом; уничтожение – игрок объявить убитым один символ противника, который находится 
        рядом с клеткой, занятой собственным символом. Убитые крестики обводятся кружком, а убитые нолики закрашиваются. 
        Цель игры – уничтожить все символы противника.
        Любые действия возможно только в доступных для игрока клетках, то есть в тех, которые расположены по "
        соседству со своей собственной клеткой!
        Игра заканчивается, когда один игрок уничтожает все символы противника или если отсутствует допустимый ход 
        для каждого игрока. Побеждает игрок, который уничтожает все символы противника. Если это не удаётся ни одному 
        из игроков, то игра заканчивается вничью.


        """

        rules_label = Label(rules_window, text=rules_text,bg='thistle3', font=("Helvetica", 16))
        rules_label.pack(pady=20)

        return_button = Button(rules_window, text="Назад", width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'), command=rules_window.destroy)
        return_button.place(relx=0.5, rely=0.88, anchor=CENTER)

    root.image = PhotoImage(file='Fon2_out.png')
    bg_logo = Label(root, image=root.image)
    bg_logo.place(x=0, y=0, relwidth=1, relheight=1)


    def start_game():
        root.withdraw()  # Скрываем главное окно
        open_gw()  # Открываем игровое окно

    btn_play = Button(root, text='Играть', width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'),
                      command=start_game)
    btn_play.place(relx=0.5, rely=0.5, anchor=CENTER)

    btn_rules = Button(root, text='Правила', width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'),
                       command=show_rules)
    btn_rules.place(relx=0.5, rely=0.68, anchor=CENTER)

    btn_quit_game = Button(root, text='Выход', width=12, command= exit_game, bg='plum4', fg='white',
                           font=('Century', 30, 'bold'))
    btn_quit_game.place(relx=0.5, rely=0.86, anchor=CENTER)

    root.mainloop()


start_game()