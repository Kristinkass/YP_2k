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


def exit_game():
    root.destroy()


def start_game():
    root = Tk()
    root.title("Война вирусов на бумаге")
    root.geometry('1570x800')

    menu_visible = True
    instructions_visible = False

    def open_gw():
        game_window = Toplevel(root)
        game_window.title("Игровое окно")
        game_window.geometry('1570x800')

        game_window.image = PhotoImage(file='Fon2_out.png')
        bg_logo = Label(game_window, image=game_window.image)
        bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

        canvas = Canvas(game_window, width=1601, height=955)
        canvas.pack()

        for i in range(10):
            for j in range(10):
                canvas.create_rectangle(50 + 50 * i, 50 + 50 * j, 100 + 50 * i, 100 + 50 * j, fill='white')

        skip_button = Button(game_window, text="Пропуск хода", width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'))
        skip_button.place(relx=0.15, rely=0.9)

        play_again_button = Button(game_window, text="Играть снова", width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'))
        play_again_button.place(relx=0.5, rely=0.9)

        quit_button = Button(game_window, text="Выход", width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'), command=exit_game)
        quit_button.place(relx=0.85, rely=0.9)

    def show_rules():
        rules_window = Toplevel(root)
        rules_window.title("Правила игры")
        rules_window.geometry('1570x800')

        rules_window.image = PhotoImage(file='Fon2_out.png')
        bg_logo = Label(rules_window, image=rules_window.image)
        bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

        rules_text = """
        Правила игры:
        За один ход каждый из игроков может выполнить на выбор любую комбинацию, включающую "
        в себя 3 действия, состоящие из размножения вирусов или уничтожения вируса соперника:"
        Размножение вирусов: игрок ставит один свой символ – крестик или нолик – в незанятую"
        клетку, Уничтожение вирусов соперника: игрок объявляет убитым один чужой"
        символ (убитые крестики обводятся кружком, убитые нолики закрашиваются)
        """

        rules_label = Label(rules_window, text=rules_text, font=("Helvetica", 16))
        rules_label.pack(pady=20)

        return_button = Button(rules_window, text="Назад", width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'), command=rules_window.destroy)
        return_button.pack(pady=20)

    root.image = PhotoImage(file='Fon2_out.png')
    bg_logo = Label(root, image=root.image)
    bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

    btn_play = Button(root, text='Играть', width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'),
                      command=open_gw)
    btn_play.place(relx=0.5, rely=0.45, anchor=CENTER)

    btn_rules = Button(root, text='Правила', width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'),
                       command=show_rules)
    btn_rules.place(relx=0.5, rely=0.6, anchor=CENTER)

    btn_settings = Button(root, text='Настройки', width=12, bg='plum4', fg='white', font=('Century', 30, 'bold'))
    btn_settings.place(relx=0.5, rely=0.74, anchor=CENTER)

    btn_quit_game = Button(root, text='Выход', width=12, command=exit_game, bg='plum4', fg='white',
                           font=('Century', 30, 'bold'))
    btn_quit_game.place(relx=0.5, rely=0.88, anchor=CENTER)

    root.mainloop()


start_game()
