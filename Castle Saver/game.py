from tkinter import *
import random

# Шаблон окна
window = Tk()

w = 600
h = 600

window.geometry(str(w)+'x'+str(h))

# Холст игрового поля
canvas = Canvas(window, width=w, height=h)
canvas.place(in_ = window, x =0 , y=0)

# Фон для игры
bg_photo = PhotoImage(file='bg_2.png')


class Knigth:
    def __init__(self):
        # Координаты центра рыцаря
        self.x = 70
        self.y = h // 2
        # Скорость рыцаря
        self.v = 0 
        # Изображение рыцаря
        self.photo = PhotoImage(file='knight.png')

    # Движение вверх
    def up(self, event):
        self.v = -3

    # Движение вниз
    def down(self, event):
        self.v = 3

    # Остановка
    def stop(self, event):
        self.v = 0

class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100, 500)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file='dragon.png')


knight = Knigth()

dragons = []
for i in range(10):
    dragons.append(Dragon())


def game():
    canvas.delete('all')
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v

    current_dragon = 0
    dragon_to_kill = -1

    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

        if ((dragon.x-knight.x)**2) + ((dragon.y-knight.y)**2) <= (96)**2:
            dragon_to_kill = current_dragon
        
        current_dragon +=1

        if dragon.x <=0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text="Поражение!", font='Verdana 42', fill='red')
        
    if dragon_to_kill >=0:
        del dragons[dragon_to_kill]

    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w//2, h//2, text="Победа!", font='Verdana 42', fill='red')
    else:
        window.after(5, game)


game()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.mainloop()