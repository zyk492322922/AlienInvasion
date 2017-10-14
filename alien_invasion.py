import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	""" 初始化游戏并创建一个屏幕对象 """
	pygame.init()
	ai_setting = Settings()  #获取全局配置参数
	screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
	pygame.display.set_caption('Alien Invasion')
	
    # 创建一艘飞船
	ship = Ship(screen)

	while True:
		# 循环监听鼠标和键盘事件
		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()
		gf.check_events(ship)

		ship.moving()
		# screen.fill(ai_setting.bg_color)
        # 绘制飞船位置
		# ship.blitme()
		# # 让绘制的屏幕可见
		# pygame.display.flip()
		gf.update_screen(ai_setting,screen,ship)




run_game()
