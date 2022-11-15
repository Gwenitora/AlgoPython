x, y = 0, 0
x, y = x*200, y*200

draw.line(screen, (255, 0, 0), (x+20,y+180), (x+180,y+20), 15)
draw.line(screen, (255, 0, 0), (x+20,y+20), (x+180,y+180), 15)

x, y = 0, 1
x, y = x*200, y*200

draw.ellipse(screen, (0, 0, 255), (x+20, y+20, 160, 160), 10)