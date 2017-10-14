import sys
import pygame
from bullet import Bullet


""" 该项目中所有动画方法都放在该文件中  方便统一管理 """

# 单独处理按下键盘事件
def check_keydown_event(event,ai_setting,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key ==pygame.K_SPACE:
		# 创建一个子弹, 并加到编组bullets中
		new_bullet = Bullet(ai_setting,screen,ship)
		bullets.add(new_bullet)


# 单独处理松开键盘事件
def check_keyup_event(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


# 循环监听鼠标和键盘事件
def  check_events(ai_setting,screen,ship,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event,ai_setting,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)

        

# 刷新屏幕信息
def  update_screen(ai_setting,screen,ship,bullets):
	# 填充颜色
	screen.fill(ai_setting.bg_color)
	for bullet in bullets:
		bullet.draw_bullet()
    # 绘制飞船位置
	ship.blitme()
	# 让绘制的屏幕可见
	pygame.display.flip()