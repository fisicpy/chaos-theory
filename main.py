import pygame
import random

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
pygame.font.init()

CIRCLE_RADIUS = 5
FPS = 500

def get_coords_center_line(x1, y1, x2, y2):
	x3 = int((x1 + x2) / 2)
	y3 = int((y1 + y2) / 2)
	return x3, y3


class Point:
	def __init__(self, surface, x, y, radius, color):
		self.surface = surface
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color

	def draw(self):
		pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

	def new_x(self, val):
		self.x = val

	def new_y(self, val):
		self.y = val

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y


main_points = [
	Point(display, 400, 70, CIRCLE_RADIUS, (255, 255, 255)),
	Point(display, 150, 530, CIRCLE_RADIUS, (255, 255, 255)),
	Point(display, 650, 530, CIRCLE_RADIUS, (255, 255, 255)),


]

points = [
	Point(display, 400, 70, CIRCLE_RADIUS, (255, 255, 255))
]

input()

if __name__ == "__main__":
	run_game = True
	while run_game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run_game = False

		display.fill((0, 0, 0))

		pressed = pygame.mouse.get_pressed()
		x, y = pygame.mouse.get_pos()
		if pressed[0]:
			print(x, y)
			
		random_main_point = random.choice(main_points)
		x, y = get_coords_center_line(points[-1].get_x(), points[-1].get_y(), random_main_point.get_x(), random_main_point.get_y())
		points.append(Point(display, x, y, CIRCLE_RADIUS, (255, 255, 255)))

		for point in main_points:
			point.draw()

		for point in points:
			point.draw()
					
		pygame.display.flip()

