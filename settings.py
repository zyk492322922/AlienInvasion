class Settings():
	""" 游戏全局设置类 """

	def __init__(self):
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230,230,230)
		#self.ship_speed_step = 1.5

		# 子弹设置
		self.bullet_speed_factor = 1  # 子弹飞行速度
		self.bullet_width = 3
		self.bullet_height = 3
		self.bullet_color = 60,60,60
		self.bullet_allowed = 5    # 限制子弹数量