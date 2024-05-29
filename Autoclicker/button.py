class Button():
	def __init__(self, pos, text_input, base_color, hovering_color):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)
