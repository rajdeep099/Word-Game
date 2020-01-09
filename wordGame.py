import turtle
import random
import time     

# game over
def gameOver():
    eleNum.append(eleNum[len(eleNum) - 1] + 1)
    if eleNum[len(eleNum) - 1] == l:
        time.sleep(0.5)
        turtle.clear()
        turtle.penup()
        turtle.setposition(-300, -60)
        turtle.pendown()
        turtle.color("Black")
        turtle.write('CONGRATS YOU WON !!!', font=('Roboto', 40, 'bold'))
        time.sleep(0.5)

        restart()


# draw man
def drawMan(val):
    turtle.color("Red")
    # head
    if val == 1:
        turtle.penup()
        turtle.setposition(40, 260)
        turtle.pendown()
        turtle.circle(20)

    # body
    elif val == 2:
        turtle.penup()
        turtle.setposition(50, 260)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(70)
        turtle.left(90)

    # right leg
    elif val == 3:
        turtle.penup()
        turtle.setposition(50, 190)
        turtle.right(55)
        turtle.pendown()
        turtle.forward(60)
        turtle.left(55)

    # left leg
    elif val == 4:
        turtle.penup()
        turtle.setposition(50, 190)
        turtle.right(125)
        turtle.pendown()
        turtle.forward(60)
        turtle.left(125)

    # right arm
    elif val == 5:
        turtle.penup()
        turtle.setposition(50, 245)
        turtle.right(55)
        turtle.pendown()
        turtle.forward(60)
        turtle.left(55)

    # left arm
    elif val == 6:
        turtle.penup()
        turtle.setposition(50, 245)
        turtle.right(125)
        turtle.pendown()
        turtle.forward(60)
        turtle.left(125)

        # replay option
        turtle.clear()
        turtle.penup()
        turtle.setposition(-130, -60)
        turtle.pendown()
        turtle.color("Black")
        turtle.write('YOU LOST !!!', font=('Roboto', 40, 'bold'))
        time.sleep(0.5)
        restart()
    turtle.color("Black")


# cross
def cross(chosed_val):
    if chosed_val == 'Q' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-300, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:

            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'W' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-250, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'E' and chosed_val not in characters:
        characters.append(chosed_val)

        turtle.penup()
        turtle.setposition(-200, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'R' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-150, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'T' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-100, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'Y' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-50, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'U' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(0, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'I' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(50, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'O' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(100, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'P' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(150, -100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'A' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-280, -165)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'S' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-230, -165)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'D' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-180, -165)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'F' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-130, -165)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'G' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-80, -165)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'H' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-30, -165)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'J' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(20, -165)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'K' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(70, -165)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'L' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(120, -165)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'Z' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-260, -230)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'X' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-210, -230)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'C' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-160, -230)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'V' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-110, -230)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'B' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-60, -230)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'N' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(-10, -230)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()

    elif chosed_val == 'M' and chosed_val not in characters:

        characters.append(chosed_val)
        turtle.penup()
        turtle.setposition(40, -230)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(56.56)
        turtle.left(45)

        if chosed_val not in word:
            count.append(count[len(count) - 1] + 1)
            val = (count[len(count) - 1])
            drawMan(val)
        else:
            positions = []
            for i in range(len(word)):
                if word[i] == chosed_val:
                    positions.append(i)
            for i in positions:
                turtle.penup()
                turtle.setposition(-190 + 60 * i, -28)
                turtle.pendown()
                turtle.write(chosed_val, font=("Roboto", 20, 'bold'))
                gameOver()


# button click
def btnClk(x, y):
    global chosed_val
    global state

    if state == 'drawing':
        pass

    if state == 'notRunning':
        if -130 < x < -30 and -20 < y < 20:
            turtle.Screen().bye()
        if 50 < x < 150 and -20 < y < 20:
            state = 'running'
            start()
        # if -50 < x < 50 and -335 < y < -300:   #   for replay
        #     turtle.clear()
        #     start()

    if state == 'running':

        if -140 < y < -100:
            if -300 < x < -260:
                chosed_val = 'Q'
                cross(chosed_val)

            elif -250 < x < -210:
                chosed_val = 'W'
                cross(chosed_val)

            elif -200 < x < -160:
                chosed_val = 'E'
                cross(chosed_val)

            elif -150 < x < -110:
                chosed_val = 'R'
                cross(chosed_val)

            elif -100 < x < -60:
                chosed_val = 'T'
                cross(chosed_val)

            elif -50 < x < -10:
                chosed_val = 'Y'
                cross(chosed_val)

            elif 0 < x < 40:
                chosed_val = 'U'
                cross(chosed_val)

            elif 50 < x < 90:
                chosed_val = 'I'
                cross(chosed_val)

            elif 100 < x < 140:
                chosed_val = 'O'
                cross(chosed_val)

            elif 150 < x < 190:
                chosed_val = 'P'
                cross(chosed_val)

        elif -205 < y < -165:
            if -280 < x < -240:
                chosed_val = 'A'
                cross(chosed_val)

            elif -230 < x < -190:
                chosed_val = 'S'
                cross(chosed_val)

            elif -180 < x < -140:
                chosed_val = 'D'
                cross(chosed_val)

            elif -130 < x < -90:
                chosed_val = 'F'
                cross(chosed_val)

            elif -80 < x < -40:
                chosed_val = 'G'
                cross(chosed_val)

            elif -30 < x < 10:
                chosed_val = 'H'
                cross(chosed_val)

            elif 20 < x < 60:
                chosed_val = 'J'
                cross(chosed_val)

            elif 70 < x < 110:
                chosed_val = 'K'
                cross(chosed_val)

            elif 120 < x < 160:
                chosed_val = 'L'
                cross(chosed_val)

        elif -270 < y < -230:
            if -260 < x < -220:
                chosed_val = 'Z'
                cross(chosed_val)

            elif -210 < x < -170:
                chosed_val = 'X'
                cross(chosed_val)

            elif -160 < x < -120:
                chosed_val = 'C'
                cross(chosed_val)

            elif -110 < x < -70:
                chosed_val = 'V'
                cross(chosed_val)

            elif -60 < x < -20:
                chosed_val = 'B'
                cross(chosed_val)

            elif -10 < x < 30:
                chosed_val = 'N'
                cross(chosed_val)

            elif 40 < x < 80:
                chosed_val = 'M'
                cross(chosed_val)


# main loop
def mainLoop():
    # draw hanger
    global state
    state = 'drawing'
    turtle.penup()
    turtle.pensize(4)
    turtle.setposition(-50, 100)
    turtle.pendown()
    turtle.forward(100)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(220)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.penup()
    turtle.setposition(-300, -100)

    # alphabetic characters
    top_line = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
    mid_line = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
    btm_line = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']

    # top line
    for i in range(10):
        turtle.pendown()
        turtle.begin_fill()

        turtle.fillcolor('light blue')
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)

        turtle.penup()
        turtle.setposition(-290 + 50 * i, -130)
        turtle.pendown()
        turtle.write(top_line[i], font=("Arial", 14, "bold"))
        turtle.penup()
        turtle.setposition(-300 + 50 * i, -100)
        turtle.pendown()

        turtle.end_fill()
        turtle.penup()
        turtle.forward(50)

    # mid line
    turtle.setposition(-280, -165)
    for i in range(9):
        turtle.pendown()
        turtle.begin_fill()

        turtle.fillcolor('light green')
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)

        turtle.penup()
        turtle.setposition(-270 + 50 * i, -195)
        turtle.pendown()
        turtle.write(mid_line[i], font=("Arial", 14, "bold"))
        turtle.penup()
        turtle.setposition(-280 + 50 * i, -165)
        turtle.pendown()

        turtle.end_fill()
        turtle.penup()
        turtle.forward(50)

    # bottom line
    turtle.setposition(-260, -230)
    for i in range(7):
        turtle.pendown()
        turtle.begin_fill()

        turtle.fillcolor('light blue')
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)

        turtle.penup()
        turtle.setposition(-250 + 50 * i, -260)
        turtle.pendown()
        turtle.write(btm_line[i], font=("Arial", 14, "bold"))
        turtle.penup()
        turtle.setposition(-260 + 50 * i, -230)
        turtle.pendown()

        turtle.end_fill()
        turtle.penup()
        turtle.forward(50)

    # button press-call
    state = 'running'
    turtle.onscreenclick(btnClk, 1)
    turtle.listen()


def start():
    turtle.clear()
    global state
    state = 'notRunning'

    # words that are consisted in the game
    alphabets = ['ABSOLUTE', 'ENERGY', 'DATABASE', 'BUILDING', 'SPROUT', 'ESCAPE', 'AUDIENCE', 'DAILY', 'CALENDAR',
                 'SPACE', 'FAMILY', 'DIABETES', 'ATTACK', 'LAUNCH', 'BACTERIA', 'SOLUTION', 'FATHER', 'MOTHER',
                 'BIRTHDAY', 'GARDEN', 'COMPUTER', 'GREEN', 'CEREMONY']
    n = random.randint(0, len(alphabets) - 1)

    global count
    count = [0]

    global word
    word = alphabets[n]
    word = [str(i) for i in word]
    global l
    l = len(word)
    global eleNum
    eleNum = [0]

    global characters
    characters = []

    # blank spaces
    turtle.penup()
    turtle.setposition(-200, -30)

    for i in range(l):
        turtle.pendown()
        turtle.forward(40)
        turtle.penup()
        turtle.forward(20)

    mainLoop()


# Play button
def restart():
    global state
    state = 'notRunning'
    turtle.color("Black")
    turtle.clear()
    turtle.penup()
    turtle.setposition(-130, 20)
    choices = ['QUIT', 'PLAY']
    choiceColours = ['Red', "Green"]
    turtle.pendown()
    for j in range(2):
        turtle.begin_fill()
        turtle.fillcolor(choiceColours[j])
        for i in range(2):
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(40)
            turtle.right(90)
        turtle.penup()
        turtle.end_fill()
        turtle.setposition(-100 + 175 * j, -10)
        turtle.pd()
        turtle.color("White")
        turtle.write(choices[j], font=("Arial", 14, "bold"))
        turtle.pu()
        turtle.setposition(-130, 20)
        turtle.color("Black")
        turtle.forward(180)
        turtle.pd()

    turtle.onscreenclick(btnClk, 1)
    turtle.mainloop()


if __name__ == '__main__':
    turtle.clear()
    turtle.setup(800, 700)
    turtle.title("HANG-MAN")
    turtle.Screen().bgpic("C:\\Users\\Lenovo\\Desktop\\wall\\original.gif")
    turtle.speed(0)
    turtle.pensize(4)
    turtle.hideturtle()
    restart()
    turtle.mainloop()
