import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

def line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2])

x = 0

# B
line(x,0,x,4)
line(x,4,x+1.5,3.5)
line(x+1.5,3.5,x,2.5)
line(x,2.5,x+1.5,2)
line(x+1.5,2,x,0)
x += 3

# A
line(x,0,x+1,4)
line(x+1,4,x+2,0)
line(x+0.5,2,x+1.5,2)
x += 3

# S
line(x+2,4,x,4)
line(x,4,x,2)
line(x,2,x+2,2)
line(x+2,2,x+2,0)
line(x+2,0,x,0)
x += 3

# U
line(x,4,x,1)
line(x,1,x+1,0)
line(x+1,0,x+2,1)
line(x+2,1,x+2,4)
x += 3

# N
line(x,0,x,4)
line(x,4,x+2,0)
line(x+2,0,x+2,4)
x += 3

# D
line(x,0,x,4)
line(x,4,x+1.5,3)
line(x+1.5,3,x+1.5,1)
line(x+1.5,1,x,0)
x += 3

# H
line(x,0,x,4)
line(x+2,0,x+2,4)
line(x,2,x+2,2)
x += 3

# A
line(x,0,x+1,4)
line(x+1,4,x+2,0)
line(x+0.5,2,x+1.5,2)
x += 3

# R
line(x,0,x,4)
line(x,4,x+1.5,3)
line(x+1.5,3,x,2.5)
line(x,2.5,x+1.5,0)
x += 3

# A
line(x,0,x+1,4)
line(x+1,4,x+2,0)
line(x+0.5,2,x+1.5,2)

plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.title("BASUNDHARA :D", fontsize=20)
plt.show()

