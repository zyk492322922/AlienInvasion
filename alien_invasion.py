import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
	""" 初始化游戏并创建一个屏幕对象 """
	pygame.init()
	ai_setting = Settings()  #获取全局配置参数
	screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
	pygame.display.set_caption('Alien Invasion')
	
    # 创建一艘飞船
	ship = Ship(screen)
	# 创建一个用来存储子弹的编组
	bullets = Group()
    
    # 创建一个存放外星人的编组
	aliens = Group()

	gf.create_aliens(ai_setting,screen,ship,aliens)

	while True:
		# 监听事件
		gf.check_events(ai_setting,screen,ship,bullets)

		# 飞船移动
		ship.moving()

		# 子弹移动 更新子弹信息
		gf.update_bullet(bullets)

        # 绘制飞船位置
		# # 让绘制的屏幕可见
		gf.update_screen(ai_setting,screen,ship,bullets,aliens)




run_game()
