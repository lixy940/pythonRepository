class Settings():

	def __init__ (self):
		self.screen_width = 800
		self.screen_height = 500
		self.bg_color =  (223, 223, 223)

		self.ship_speed_factor = 1
		self.ship_limit = 3

		self.bullet_speed_factor = 1 
		self.bullet_width = 2 
		self.bullet_height = 10 
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 4

		self.alien_speed_factor = 0.5

		self.fleet_drop_speed = 3
		self.fleet_direction = 1
