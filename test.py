from tkinter import *

# create a canvas
canvas = Canvas(width=300, height=300)
canvas.pack()

# draw a triangle with blue shading
canvas.create_polygon(150, 50, 50, 250, 250, 250,
                      fill='blue', outline='black')

# calculate midpoints of the sides of the triangle
midpoint1 = ((150+50)/2, (50+250)/2)
midpoint2 = ((150+250)/2, (50+250)/2)
midpoint3 = ((50+250)/2, (250+250)/2)

# draw an inverted triangle with white shading
canvas.create_polygon(midpoint1[0], midpoint1[1], midpoint2[0], midpoint2[1],
                      midpoint3[0], midpoint3[1], fill='white', outline='black')

# display the canvas
mainloop()