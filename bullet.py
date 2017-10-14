import pygame
from pygame.sprite import Sprite


# 飞船发射的子弹
class Bullet(Sprite):

	def __init__(self,ai_setting,screen,ship):
		super().__init__()
		self.screen = screen


 		#  在(0,0)处绘制一个子弹,然后在移动到正确的位置
		self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# 由于子弹是垂直方向移动，所以需要移动y轴
		self.y = float(self.rect.y)

		self.color = ai_setting.bullet_color
		self.speed_factor = ai_setting.bullet_speed_factor


	# 子弹移动
	def moving(self):
		""" 向上移动 """
		# 计算表示子弹位置的y值
		self.y -= self.speed_factor
		# 把计算的y值，赋值到矩形属性
		self.rect.y = self.y


	def draw_bullet(self):
		""" 在屏幕上绘制子弹 """
		pygame.draw.rect(self.screen,self.color,self.rect)


		

