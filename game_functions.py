import sys
import pygame


""" 该项目中所有动画方法都放在该文件中  方便统一管理 """



def  check_events(ship):
	# 循环监听鼠标和键盘事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False

        
#  刷新屏幕信息
def  update_screen(ai_setting,screen,ship):
	# 填充颜色
	screen.fill(ai_setting.bg_color)
    # 绘制飞船位置
	ship.blitme()
	# 让绘制的屏幕可见
	pygame.display.flip()