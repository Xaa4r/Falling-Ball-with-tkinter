import tkinter as tk
import random

class Ball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x+20, y+20, fill='red')
        self.speed = random.uniform(1, 2)
        
    def fall(self):
        coords = self.canvas.coords(self.id)
        if coords[3] < 500:
            self.canvas.move(self.id, 0, self.speed)
        else:
            self.canvas.delete(self.id)

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, height=500, width=500)
        self.canvas.pack()
        self.balls = []
        self.score = 0
        self.text = tk.StringVar()
        self.text.set('Score: 0')
        tk.Label(root, textvariable=self.text).pack()
        tk.Button(root, text='Quit', command=root.quit).pack(side='left', padx=10, pady=10)
        self.canvas.after(100, self.spawn_balls)
        self.canvas.after(100, self.animate)
        
    def spawn_balls(self):
        if len(self.balls) < 5:
            x = random.randint(0, 480)
            y = -20
            self.balls.append(Ball(self.canvas, x, y))
        self.canvas.after(5000, self.spawn_balls)
        
    def animate(self):
        for ball in self.balls:
            ball.fall()
        self.canvas.after(100, self.animate)
        
    def add_score(self, event):
        for ball in self.balls:
            coords = self.canvas.coords(ball.id)
            if coords[0] <= event.x <= coords[2] and coords[1] <= event.y <= coords[3]:
                self.canvas.delete(ball.id)
                self.balls.remove(ball)
                self.score += 1
                self.text.set('Score: {}'.format(self.score))
                if self.score == 20:
                    tk.Label(self.root, text='You Won!').pack()
                    self.root.destroy()
                return
        tk.Label(self.root, text='Game Over!').pack()
        self.root.destroy()
        
root = tk.Tk()
game = Game(root)
root.bind_all('<Button-1>', game.add_score)
root.mainloop()