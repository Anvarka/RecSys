if __name__ == "__main__":
    from tkinter import *
    import random

    class My_Button(Button):
        s = 0

        def row_column_bt(self, i, l):
            row = l[i] // 3
            column = l[i] % 3
            self.grid(row=row, column=column)

        def move(self):
            row = l[self.s] // 3
            column = l[self.s] % 3
            row_null = l[8] // 3
            column_null = l[8] % 3
            if (abs(row_null - row) == 1 and column == column_null) or (
                    row == row_null and abs(column_null - column) == 1):
                self.grid(row=row_null, column=column_null)
                l[self.s], l[8] = l[8], l[self.s]
            if check(l):
                give_win()

    def check(b):
        if b == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            return True

    def give_win():
        root1 = Tk()
        b[8].grid(row=2, column=2)
        label = Label(root1, text="You win!")
        label.pack()
        root1.mainloop()

    def special_rand(l):
        j = 0
        while j < random.randint(100, 1500):
            for i in range(9):
                row = l[i] // 3
                column = l[i] % 3
                row_null = l[8] // 3
                column_null = l[8] % 3
                if (abs(row_null - row) == 1 and column == column_null) or (
                        row == row_null and abs(column_null - column) == 1):
                    b[i].grid(row=row_null, column=column_null)
                    l[i], l[8] = l[8], l[i]
                j += 1

    root = Tk()
    b = []
    img = []
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(9):
        img.append(PhotoImage(file=str(i) + ".gif").subsample(2))
        b.append(My_Button(root, image=img[i]))
        b[i].s = i
    special_rand(l)
    for i in range(8):
        b[i].configure(command=b[i].move)
        b[i].row_column_bt(i,l)

    root.mainloop()
