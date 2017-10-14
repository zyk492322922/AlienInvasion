import pygame

class Ship():
	"""  飞机模型类 """

	def __init__(self,screen):

		self.screen = screen
		#加载飞船图片并获取其外接矩形
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

        # 设置图像在屏幕底部居中
		self.rect.centerx = self.screen_rect.centerx   # 飞船中心x坐标是整个屏幕的中心的x坐标
		self.rect.bottom = self.screen_rect.bottom     #  飞船下边缘和整个屏幕下边缘对齐


	def blitme():
		""" 在指定位置绘制飞船  """
		self.screen.blit(self.image,self.rect)

