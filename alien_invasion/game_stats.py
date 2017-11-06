class GameStats():
	def __init__(self,ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		#游戏启动时处于活动状态
		self.game_active = True

	def reset_stats(self):
		#定好可用船的数量
		self.ships_left = self.ai_settings.ship_limit
