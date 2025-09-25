import tkinter as tk
import turtle
import random
import time

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2
        self.start_time = time.time()
        self.score = 0
        self.game_time = 60
        self.game_over = False
        self.caught_count = 0

        self.runner.shape("turtle")
        self.runner.color('blue')
        self.runner.penup()

        self.chaser.shape("turtle")
        self.chaser.color('red')
        self.chaser.penup()

        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

    def is_catched(self):
        if self.game_over:
            return False
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        caught = dx**2 + dy**2 < self.catch_radius2
        if caught:
            self.score += 10
            self.caught_count += 1
            self.runner.setpos(random.randint(-350, 350), random.randint(-350, 350))
            self.chaser.setpos(random.randint(-350, 350), random.randint(-350, 350))
            while self.is_catched(): 
                self.runner.setpos(random.randint(-350, 350), random.randint(-350, 350))
                self.chaser.setpos(random.randint(-350, 350), random.randint(-350, 350))
        return caught

    def get_remaining_time(self):
        elapsed = time.time() - self.start_time
        return max(0, self.game_time - elapsed)

    def start(self, init_dist=400, ai_timer_msec=100):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)
        self.start_time = time.time()
        self.game_over = False
        self.score = 0
        self.caught_count = 0

        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        if not self.game_over:
            self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
            self.chaser.run_ai(self.runner.pos(), self.runner.heading())
            
            self.is_catched()
            
            remaining_time = self.get_remaining_time()
            
            if remaining_time <= 0:
                self.game_over = True
         
            self.drawer.clear()
            self.drawer.penup()
            self.drawer.setpos(-350, 350)
            self.drawer.write(f'Time: {int(remaining_time)}s | Score: {self.score}', 
                            font=('Arial', 14, 'normal'))
            self.drawer.setpos(-350, 320)
            
            if self.game_over:
                self.drawer.write(f'GAME OVER! Final Score: {self.score}', 
                                font=('Arial', 16, 'bold'))
            else:
                self.drawer.write(f'Caught: {self.caught_count}', 
                                font=('Arial', 14, 'normal'))

        if not self.game_over:
            self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=15, step_turn=15):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.onkeypress(lambda: self.forward(self.step_move), 'w')
        canvas.onkeypress(lambda: self.backward(self.step_move), 's')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'a')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'd')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass 

class SmartRunner(turtle.RawTurtle):
    def __init__(self, canvas, step_move=12, step_turn=10):  
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        distance = self.distance(opp_pos)
        
        if distance < 100:
            escape_angle = self.towards(opp_pos) + 180
            current_angle = self.heading()
            angle_diff = (escape_angle - current_angle) % 360
            
            if angle_diff > 180:
                angle_diff -= 360
            
            if abs(angle_diff) < 30:
                self.forward(self.step_move + 5) 
            elif angle_diff > 0:
                self.right(min(self.step_turn, angle_diff))
            else:
                self.left(min(self.step_turn, -angle_diff))
        else: 
            mode = random.randint(0, 3)
            if mode == 0:
                self.forward(self.step_move)
            elif mode == 1:
                self.left(self.step_turn)
            elif mode == 2:
                self.right(self.step_turn)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Turtle Runaway Game")
    canvas = tk.Canvas(root, width=800, height=800)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("lightgreen")

    runner = SmartRunner(screen)
    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser)
    game.start()
    
    print("Game started! Use Arrow Keys or WASD to control the red turtle")
    print("Catch the blue turtle to score points!")
    
    screen.mainloop()