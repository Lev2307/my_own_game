from tkinter import Tk, Canvas
from random import randint
from time import sleep

CANVAS_SIZE = 600
RECT_SIZE = 600 // 20
BG_COLOR = '#ff9f68'

class Board(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()

board = Board()
board.title('Snake Game')
board.resizable(0, 0)

class Apple:
    def __init__(self):
        self.canvas = board.canvas
        self.canvas_width = CANVAS_SIZE

apple = Apple()

class Player:
    def __init__(self):
        self.canvas = board.canvas
        self.tail = [[]]
        self.x = 0
        self.y = 0
        self.player = self.render_player()
        self.canvas_width = CANVAS_SIZE
        self.canvas.bind_all('<KeyPress>', self.move_player)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        self.apple = self.place_apple()
    
    def render_player(self):
        rect_size = RECT_SIZE
        x = 0
        y = 0
        return self.canvas.create_rectangle(x, y, x+rect_size,  y+rect_size, fill='#17b978', outline='#17b978')
    
    def move_player(self, event):
        if (event.keysym == 'Up' or event.keysym == 'w'):
            self.move_up()
            self.canvas.move(self.player, 0, self.y)

        elif (event.keysym == 'Down' or event.keysym == 's'):
            self.move_down()
            self.canvas.move(self.player, 0, self.y)

        elif (event.keysym == 'Right' or event.keysym == 'd'):
            self.move_right()
            self.canvas.move(self.player, self.x, 0)

        elif (event.keysym == 'Left' or event.keysym == 'a'):
            self.move_left()
            self.canvas.move(self.player, self.x, 0)

    def move_up(self):
        pos = self.canvas.coords(self.player)
        apple_eaten = self.check_apple_eaten()
        if pos[1] <= 0:
            self.end_window()
        if apple_eaten:
            print('Apple Eaten!')
        self.y = -RECT_SIZE

    def move_down(self):
        self.y = RECT_SIZE
        pos = self.canvas.coords(self.player)
        apple_eaten = self.check_apple_eaten()
        if pos[3] >= CANVAS_SIZE:
            self.end_window()
        if apple_eaten:
            print('Apple Eaten!')

    def move_right(self):
        self.x = RECT_SIZE
        pos = self.canvas.coords(self.player)
        apple_eaten = self.check_apple_eaten()
        if pos[2] >= CANVAS_SIZE:
            self.end_window()
        if apple_eaten:
            print('Apple Eaten!')

    def move_left(self):
        self.x = -RECT_SIZE
        pos = self.canvas.coords(self.player)
        apple_eaten = self.check_apple_eaten()
        if pos[0] <= 0:
            self.end_window()
        if apple_eaten:
            print('Apple Eaten!')

    def place_apple(self):
        rect_size = RECT_SIZE
        field_size = self.canvas_width // rect_size + 1
        row = randint(0, field_size-2)
        col = randint(0, field_size-2)
        x = row * rect_size
        y = col * rect_size
        print(x, y)
        return self.canvas.create_rectangle(x, y, x+rect_size, y+rect_size, fill='#f85959', outline='#f85959')

    def check_apple_eaten(self):
        pos_player = self.canvas.coords(self.player)
        pos_apple = self.canvas.coords(self.apple)
        print(pos_player, pos_apple)

    def end_window(self):
        self.canvas.delete(self.player)
        self.canvas.create_text(300, 300, text='You lost =/', font="Verdana 14", fill='#fff')

player = Player()
board.mainloop()