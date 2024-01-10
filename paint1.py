import simple_draw as sd
sd.resolution = (1200, 600)

def bubble(point, step):
    radius = 10
    for _ in range(6):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)
for _ in range(50):
   point = sd.random_point()
   bubble(point=point, step=2)
sd.pause()