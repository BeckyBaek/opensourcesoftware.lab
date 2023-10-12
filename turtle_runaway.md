#Turtle Runaway Game
This is a simple turtle-based game where a chaser turtle treis to catch
a runner turtle.  
import tkinter as tk
import turtle
import random
import time

# import
-타이머 기능을 표시하기 위해 import에 다음과 같은 구문을 추가함
-게임은 시작부터 경과된 시간을 측정하고 러너가 잡힐 때 타이머가 멈춤.
```python3
import time
```
# is_catched(self)
설명..
```python3
-is_catched 메서드는 Runner와 chaser 사이의 유클리드 거리를 계산합니다.
-잡기 조건은 거리가 일정 임계값보다 작을 때 발생하도록 조정되었습니다.
```
# class RunawayGame
```python3
- 러너가 채이서를 잡은 횟수를 추적하는 점수 기능이 포함되어 있습니다.
self.score = 0

```
### `self.start_time = time.time()`
```python3
-게임이 시작된 시간을 추적하기 위해 사용됩니다.
```
### score and Timer Handling
```python3
러너가 잡힌 경우 (is_catched가 True), 코드는 점수를 1 증가시키고 (self.score += 1), 게임이 시작된 이후의 경과 시간을 계산합니다 (elapsed_time = round(time.time() - self.start_time, 2)).
그런 다음 turtle 모듈 (self.drawer)을 사용하여 캔버스에 러너가 잡힌 상태, 현재 점수 및 경과 시간을 표시합니다.
```
### Game Over Handling
```python3
만약 러너가 잡힌 경우 stop_game() 메서드가 호출되며, 이 메서드는 게임을 종료하는 관련 동작을 수행하기를 기대합니다. 이 메서드의 구체적인 구현은 코드 스니펫에서 제공되지 않았습니다.
```
### Displaying Catch Status
```python3
러너가 잡혔는지 여부에 관계없이 코드는 캔버스에 잡힌 상태, 점수 및 경과 시간에 대한 정보를 업데이트합니다.
```
### Continuation of the Game Loop
```python3
마지막 라인 (self.canvas.ontimer(self.step, self.ai_timer_msec))은 일정한 시간이 지난 후에 step 메서드를 다시 호출하여 게임 루프가 계속되도록 합니다 (self.ai_timer_msec).
```
### stop_game(self):
-stop_game이라는 새로운 메서드가 추가되었습니다. 러너가 잡힐 때 메시지를 출력합니다.
-게임은 러너가 잡히면 중지되며, 이 메서드에서 추가 동작이나 초기화를 수행할 수 있습니다.

# class ManualMover
```python3
ManualMover 클래스의 run_ai 메서드는 앞으로 계속 이동하는 기본 동작이 포함되어 있습니다.
이로써 채이서는 특정 키가 눌리지 않는 한 계속해서 앞으로 이동합니다.

```

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2
        self.score = 0
        self.start_time = None

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()

        # Instantiate another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

    def is_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        distance = (dx**2 + dy**2)**0.5
        return distance < 20  # Adjust the threshold for catching

    def start(self, init_dist=400, ai_timer_msec=100):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        # TODO) You can do something here and follows.
        self.ai_timer_msec = ai_timer_msec
        self.start_time = time.time()
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        # TODO) You can do something here and follows.
        is_catched = self.is_catched()

        if is_catched:
            self.score += 1
            elapsed_time = round(time.time() - self.start_time, 2)
            self.drawer.undo()
            self.drawer.penup()
            self.drawer.setpos(0, 250)
            self.drawer.write(f'Is catched? Yes! Score: {self.score}, Time: {elapsed_time}', align="center", font=(
                "Arial", 20, "normal"))
            self.stop_game()
        else:
            elapsed_time = round(time.time() - self.start_time, 2)
            self.drawer.undo()
            self.drawer.penup()
            self.drawer.setpos(0, 250)
            self.drawer.write(f'Is catched? No. Score: {self.score}, Time: {elapsed_time}', align="center", font=(
                "Arial", 20, "normal"))

            # Note) The following line should be the last of this function to keep the game playing
            self.canvas.ontimer(self.step, self.ai_timer_msec)

    def stop_game(self):
        print(f"Game Over - Turtle is caught! Score: {self.score}")
        # Stop the game (optional: you might want to reset or exit the game here)


class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        # Default behavior: move forward
        self.forward(self.step_move)


class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)
        if mode == 0:
            self.forward(self.step_move)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)


if __name__ == '__main__':
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    # Change the follows to your turtle if necessary
    runner = RandomMover(screen)
    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser)
    game.start()
    screen.mainloop()
