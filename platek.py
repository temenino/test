from matplotlib import pyplot as plt
from math import sin, cos, asin, acos, pi

def polar(x, y):
    if x == 0 and y == 0: return [0, 0]
    r = (x * x + y * y) ** 0.5
    alpha = asin(y/r)
    return [r, alpha]

def xy_coordinates(r, alpha):
    x = r*sin(alpha)
    y = r*cos(alpha)
    return [x, y]

def rotation(teta, xy):
    pol = polar(xy[0], xy[1])
    r = pol[0]
    alpha = pol[1]
    alpha += teta
    xy_coor = xy_coordinates(r, alpha)
    new_x = xy_coor[0]
    new_y = xy_coor[1]
    return [new_x,new_y]

subline1 = rotation(pi/6, [1*cos(2*pi/3), 1*sin(2*pi/3)])
subline2 = rotation(pi/6, [1*cos(2*pi/3), -1*sin(2*pi/3)])

subline3 = rotation(pi/6, [1*cos(2*pi/3), -1*sin(2*pi/3)])
subline4 = rotation(pi/6, [1*cos(2*pi/3), 1*sin(2*pi/3)])

lines = [
        [[0, 0], [12, 0]],
        [[3, 0], [3+3*cos(pi/3), 3*sin(pi/3)]],
        [[3, 0], [3+3*cos(pi/3), -3*sin(pi/3)]],
        [[6, 0], [6+4*cos(pi/3), 4*sin(pi/3)]],
        [[6, 0], [6+4*cos(pi/3), -4*sin(pi/3)]],
        [[10, 0], [10+1*cos(pi/3), 1*sin(pi/3)]],
        [[10, 0], [10+1*cos(pi/3), -1*sin(pi/3)]],
        [[6+2*cos(pi/3), 2*sin(pi/3)], [subline1[0]+6+2*cos(pi/3), subline1[1]+2*sin(pi/3)]],
        [[6+2*cos(pi/3), 2*sin(pi/3)], [subline2[0]+6+2*cos(pi/3), subline2[1]+2*sin(pi/3)]],
        [[6+2*cos(pi/3), -2*sin(pi/3)], [subline3[0]+6+2*cos(pi/3), -subline3[1]-2*sin(pi/3)]],
        [[6+2*cos(pi/3), -2*sin(pi/3)], [subline4[0]+6+2*cos(pi/3), -subline4[1]-2*sin(pi/3)]]
        ]


for i in range(6):
    for l in lines:
        teta = i * pi/3
        l_begin = rotation(teta, l[0])
        l_end = rotation(teta, l[1])
        l_x = [l_begin[0], l_end[0]]
        l_y = [l_begin[1], l_end[1]]
        plt.plot(l_x, l_y, color='white', lineWidth=3)

ax = plt.gca()
ax.set_facecolor('black')
ax.set_aspect('equal', adjustable='box')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

fig = plt.gcf()
# fig = plt.figure()
fig.patch.set_facecolor('black')
fig.set_size_inches(5, 5)
# fig.set_figheight(5)
# fig.set_figwidth(5)

plt.show()
