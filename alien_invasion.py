import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	""" 初始化游戏并创建一个屏幕对象 """
	pygame.init()
	ai_setting = Settings()  #获取全局配置参数
	screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
	pygame.display.set_caption('Alien Invasion')
	
    # 创建一艘飞船
	ship = Ship(screen)
	# 创建一个用户存储子弹的编组
	bullets = Group()

	while True:
		# 监听事件
		gf.check_events(ai_setting,screen,ship,bullets)

		# 飞船移动
		ship.moving()

		# 子弹移动
		for bullet in bullets:
			bullet.moving()

		# screen.fill(ai_setting.bg_color)
        # 绘制飞船位置
		# ship.blitme()
		# # 让绘制的屏幕可见
		# pygame.display.flip()
		gf.update_screen(ai_setting,screen,ship,bullets)




run_game()
