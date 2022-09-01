import tkinter as tk
from random import randint
import time

CANVAS_SIZE = 600
RECT_SIZE = 600 // 20
BG_COLOR = '#ff9f68'

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.player_pos = [(0, 0)]
        self.direction = 'Right'
        self.score = 0
        self.canvas_width = CANVAS_SIZE
        self.apple_pos = self.place_apple()
        self.render_objects()
        self.canvas.bind_all('<KeyPress>', self.change_player_direction)
    
    def render_objects(self):
        #player
        rect_size = RECT_SIZE
        x = 0
        y = 0
        self.canvas.create_rectangle(x, y, x+rect_size,  y+rect_size, fill='#17b978', outline='#17b978', tag='snake')
        
        # score text
        self.canvas.create_text(560, 580, text=f"Score: {self.score}", tag="score", fill="#fff", font=10)
        pos_x, pos_y = self.apple_pos
        print(pos_x, pos_y)

        #apple
        self.canvas.create_rectangle(pos_x, pos_y, pos_x+RECT_SIZE, pos_y+RECT_SIZE, fill='#f85959', outline='#f85959', tag="apple")

    def change_player_direction(self, event):
        head_x_position, head_y_position = self.player_pos[0]
        if (event.keysym == 'Up' or event.keysym == 'w') and self.direction != 'Down':
            self.direction = 'Up'
            new_head_position = (head_x_position, head_y_position - RECT_SIZE)
            
        elif (event.keysym == 'Down' or event.keysym == 's') and self.direction != 'Up':
            self.direction = 'Down'
            new_head_position = (head_x_position, head_y_position + RECT_SIZE)

        elif (event.keysym == 'Right' or event.keysym == 'd') and self.direction != 'Left':
            self.direction = 'Right'
            new_head_position = (head_x_position + RECT_SIZE, head_y_position)

        elif (event.keysym == 'Left' or event.keysym == 'a') and self.direction != 'Right':
            self.direction = 'Left'
            new_head_position = (head_x_position - RECT_SIZE, head_y_position)

        self.player_pos = [new_head_position] + self.player_pos[:-1]
    def move(self):
        pos = self.player_pos
        apple_eaten = self.check_apple_eaten()
        if self.direction == 'Up':
            if pos[0][1] < 0:
                self.end_window()
            if apple_eaten:
                self.check_apple_collision()
        elif self.direction == 'Down':
            if pos[0][1] > CANVAS_SIZE:
                self.end_window()
            if apple_eaten:
                self.check_apple_collision()
        elif self.direction == 'Right':
            if pos[0][0] > CANVAS_SIZE:
                self.end_window()
            if apple_eaten:
                self.check_apple_collision()
        elif self.direction == 'Left':
            if pos[0][0] < 0:
                self.end_window()
            if apple_eaten:
                self.check_apple_collision()

    def place_apple(self):
        rect_size = RECT_SIZE
        field_size = self.canvas_width // rect_size + 1
        row = randint(0, field_size-3)
        col = randint(0, field_size-2)
        x = row * rect_size
        y = col * rect_size
        apple_pos_placed = (x, y)
        if apple_pos_placed not in self.player_pos:
            return apple_pos_placed
            
    def check_apple_collision(self):
        if self.player_pos[0] == self.apple_pos:
            self.score += 1
            self.player_pos.append(self.player_pos[-1])
            self.apple_pos = self.place_apple()
            pos_x, pos_y = self.apple_pos
            self.canvas.coords(self.canvas.find_withtag("apple"), pos_x, pos_y, pos_x+RECT_SIZE, pos_y+RECT_SIZE)

            score = self.canvas.find_withtag("score")
            self.canvas.itemconfigure(score, text=f"Score: {self.score}", tag="score")

    def check_apple_eaten(self):
        pos_player = self.player_pos
        apple_pos = self.apple_pos
        print(pos_player[0], apple_pos)
        if pos_player[0] == apple_pos:
            return True
        else:
            return False

    def end_window(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(CANVAS_SIZE // 2, CANVAS_SIZE // 2, text=f'Your final score is {self.score}', font="Verdana 16", fill='#fff')


game = Game()
while True:
    move = game.move()
    game.update()
    time.sleep(0.1)