# gamemaps module

from pygame import image, surface, Color

moveimage = image.load('images/pimanmovemap.png')
dotimage = image.load('images/pimandotmap.png')


def checkMovePoint(p):
    global moveimage
    if p.x + p.movex < 0: p.x = p.x + 600
    if p.x + p.movex > 600: p.x = p.x - 600
    if moveimage.get_at((int(p.x + p.movex), int(p.y + p.movey - 80))) != Color('black'):
        p.movex = p.movey = 0


def checkDotPoint(x, y):
    global dotimage
    if dotimage.get_at((int(x), int(y))) == Color('black'):
        return 1
    if dotimage.get_at((int(x), int(y))) == Color('red'):
        return 2
    return False


def getPossibleDirection(g):
    global moveimage
    if g.x - 20 < 0:
        g.x = g.x + 600
    if g.x + 20 > 600:
        g.x = g.x - 600
    directions = [0, 0, 0, 0]
    if g.x + 20 < 600:
        if moveimage.get_at((int(g.x + 20), int(g.y - 80))) == Color('black'): directions[0] = 1
    if 600 > g.x >= 0:
        if moveimage.get_at((int(g.x), int(g.y - 60))) == Color('black'): directions[1] = 1
    if g.x - 20 >= 0:
        if moveimage.get_at((int(g.x - 20), int(g.y - 80))) == Color('black'): directions[2] = 1
    if 600 > g.x >= 0:
        if moveimage.get_at((int(g.x), int(g.y - 100))) == Color('black'): directions[3] = 1
    return directions
