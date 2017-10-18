import sys
import pygame
from bullet import Bullet
from alien import Alien


""" 该项目中所有动画方法都放在该文件中  方便统一管理 """

# 单独处理按下键盘事件
def check_keydown_event(event,ai_setting,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# 新建一个子弹
		fire_bullet(ai_setting,screen,ship,bullets)


# 创建一个子弹, 并加到编组bullets中
def fire_bullet(ai_setting,screen,ship,bullets):
	if len(bullets) <ai_setting.bullet_allowed:
		new_bullet = Bullet(ai_setting,screen,ship)
		bullets.add(new_bullet)

# 创建一行外星人, 并添加到编组aliens中
def create_aliens(ai_setting,screen,ship,aliens):
	# 计算一行可以有多少外星人
	alien = Alien(ai_setting,screen)
    # 获取每行可以创建多少外星人
	alien_number = get_alien_number(ai_setting,alien.rect.width)
	number_rows = get_alien_rows(ai_setting,ship.rect.height,alien.rect.height)
	print(number_rows)
	#  创建第一行外星人
	for row in range(number_rows-1):
		# print('row =='+str(row))
		for number in range(alien_number):
			# print('hang =='+str(number))
			# 循环创建一个外星人， 并加到当前行
			create_alien(ai_setting,screen,aliens,number,row)

# 创建外星人 算法
def create_alien(ai_setting,screen,aliens,alien_number, number_rows):
	# 创建一个外星人， 并加到当前行
	alien = Alien(ai_setting,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_rows
	aliens.add(alien)

# 计算每行可以创建外星人的个数
def get_alien_number(ai_setting,alien_width):
	avaliable_space_x = ai_setting.screen_width - 2*alien_width
	alien_number = int(avaliable_space_x / (2*alien_width))
	return alien_number


# 计算可以创建多少行外星人
def get_alien_rows(ai_setting,ship_height,alien_height):
	avaliable_space_y = ai_setting.screen_height - 3 * alien_height - ship_height
	number_rows = int(avaliable_space_y/(2 * alien_height))
	return number_rows


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
def  update_screen(ai_setting,screen,ship,bullets,aliens):
	# 填充颜色
	screen.fill(ai_setting.bg_color)
	for bullet in bullets:
		bullet.draw_bullet()
    # 绘制飞船位置
	ship.blitme()
	for alien in aliens:
		alien.blitme()
	# 让绘制的屏幕可见
	pygame.display.flip()


# 更新子弹信息
def update_bullet(bullets):
	# 子弹移动
	for bullet in bullets:
		# 删除已经超出屏幕的子弹
		if bullet.rect.bottom <= 0 :
			bullets.remove(bullet)
		else:
		 	bullet.moving()
	