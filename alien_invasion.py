import sys
import pygame
from settings import Settings

def run_game():
	""" 初始化游戏并创建一个屏幕对象 """
	pygame.init()
	ai_setting = Settings()  #获取全局配置参数
	screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
	pygame.display.set_caption('Alien Invasion')
	

	while True:
		# 循环监听鼠标和键盘事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(ai_setting.bg_color)
		# 让绘制的屏幕可见
		pygame.display.flip()




run_game()
