import tkinter as tk
import subprocess

class GameMenu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x600")  # Размер окна
        self.menu_visible = True
        self.instructions_visible = False
        self.master.config(bg="#E6E6FA")

        self.title_label = tk.Label(text="Война вирусов", font=("Helvetica", 39, "bold"), bg="#E6E6FA")
        self.title_label.pack(pady=50)

        self.start_button = tk.Button(text="Начать игру", font=("Helvetica", 24), command=self.start_singleplayer_game)
        self.start_button.pack(pady=10)

        self.instructions_button = tk.Button(text="Правила игры", font=("Helvetica", 24), command=self.toggle_instructions)
        self.instructions_button.pack(pady=10)

        self.quit_button = tk.Button(text="Выход", font=("Helvetica", 24), command=self.master.destroy)
        self.quit_button.pack(pady=10)

        self.instructions_label = tk.Label(text="За один ход каждый из игроков может выполнить на выбор любую комбинацию, включающую "
                                                "\nв себя 3 действия, состоящие из размножения вирусов или уничтожения вируса соперника:"
                                                "\nРазмножение вирусов: игрок ставит один свой символ – крестик или нолик – в незанятую"
                                                "\nклетку, Уничтожение вирусов соперника: игрок объявляет убитым один чужой"
                                                "\nсимвол (убитые крестики обводятся кружком, убитые нолики закрашиваются)", font=("Helvetica", 16), fg="#1a1a1a", width=80, height=8)
        self.return_button = tk.Button(text="Вернуться в меню", font=("Helvetica", 24), command=self.return_to_menu)

    def toggle_instructions(self):
        if self.menu_visible:
            # Код для отображения инструкций
            self.menu_visible = False
            self.instructions_visible = True
            self.hide_menu()
            self.instructions_label.pack(pady=50)
            self.return_button.pack()
            # Остальной код здесь...
        else:
            # Код для скрытия инструкций
            self.menu_visible = True
            self.instructions_visible = False
            self.show_menu()
            self.instructions_label.pack_forget()
            self.return_button.pack_forget()
            # Остальной код здесь...

    def start_singleplayer_game(self):
        # Скрыть меню
        self.hide_menu()

        # Запустить игру
        subprocess.call(["python", "best.py"])

        # Показать меню после окончания игры или закрытия файла
        self.show_menu()

    def hide_menu(self):
        self.title_label.pack_forget()
        self.start_button.pack_forget()
        self.instructions_button.pack_forget()
        self.quit_button.pack_forget()

    def show_menu(self):
        self.title_label.pack(pady=50)
        self.start_button.pack(pady=10)
        self.instructions_button.pack(pady=10)
        self.quit_button.pack(pady=10)

    def return_to_menu(self):
        # Код для возвращения в меню
        self.menu_visible = True
        self.instructions_visible = False
        self.show_menu()
        self.instructions_label.pack_forget()
        self.return_button.pack_forget()

root = tk.Tk()
menu = GameMenu(root)
root.mainloop()
