from pyglet import *
from pyglet.window import key
from RectangleCollision import *


window = window.Window(width=800,height=600)
window.set_caption('Game')
keys = key.KeyStateHandler()
window.push_handlers(keys)


class player():
    px = 400
    py = 300
    pw = 101
    ph = 101
    pixels = 5
    dir = ''
    pimage = image.load('white.png')

class block1():
    bx = 200
    by = 0
    bw = 101
    bh = 101
    bimage = image.load('light green.png')
class block2():
    bx = 200
    by = 100
    bw = 101
    bh = 101
    bimage = image.load('light green.png')
class goal():
    gx = 0
    gy = 0
    gw = 101
    gh = 101
    gimage = image.load('dark green.png')
    WinText = image.load('you won text1.png')
    WinTextHide = True
@window.event
def on_draw():
    window.clear()
    class player_draw():
        player.pimage.blit(player.px,player.py)
    class block_draw():
        block1.bimage.blit(block1.bx,block1.by)
        block2.bimage.blit(block2.bx,block2.by)
    class goal_draw():
        goal.gimage.blit(goal.gx,goal.gy)
        if goal.WinTextHide == False:
            goal.WinText.blit(300,300)
    class collision_stuff():
        if collision.rectangle(player.px,player.py,goal.gx,goal.gy,player.pw,player.ph,goal.gw,goal.gh):
            goal.WinTextHide = False
        if collision.rectangle(player.px,player.py,block1.bx,block1.by,player.pw,player.ph,block1.bw,block1.bh):
            if player.dir == 'left':
                player.px += player.pixels
            if player.dir == 'right':
                player.px -= player.pixels
            if player.dir == 'up':
                player.py -= player.pixels
            if player.dir == 'down':
                player.py += player.pixels
        if collision.rectangle(player.px,player.py,block2.bx,block2.by,player.pw,player.ph,block2.bw,block2.bh):
            if player.dir == 'left':
                player.px += player.pixels
            if player.dir == 'right':
                player.px -= player.pixels
            if player.dir == 'up':
                player.py -= player.pixels
            if player.dir == 'down':
                player.py += player.pixels
def update(dt):
    class player_stuff():
        if player.px >= 700:
            player.px -= player.pixels
        if player.px <= 0:
            player.px += player.pixels
        if player.py == 500:
            player.py -= player.pixels
        if player.py == 0:
            player.py += player.pixels
        if goal.WinTextHide == True:
         class player_movment():
            if keys[key.A]:
                player.dir = 'left'
                player.px -= player.pixels
            elif keys[key.D]:
                player.dir = 'right'
                player.px += player.pixels
            elif keys[key.W]:
                player.dir ='up'
                player.py += player.pixels
            elif keys[key.S]:
                player.dir = 'down'
                player.py -= player.pixels

clock.schedule_interval(update, 1/120)

app.run()
