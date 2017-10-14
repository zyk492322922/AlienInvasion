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

		# 初始化默认不移动
		self.moving_right = False  
		self.moving_left = False


	def blitme(self):
		""" 在指定位置绘制飞船  """
		self.screen.blit(self.image,self.rect)

	# 检查飞机是否已经到达屏幕边缘
	def check_edge(self):
	 	if self.rect.left == self.screen_rect.left:
	 		self.moving_left = False
 		if self.rect.right == self.screen_rect.right:
 			self.moving_right = False

    # 飞机移动方法
	def moving(self):
		self.check_edge()
		if self.moving_right == True:
			self.rect.centerx += 1
		if self.moving_left == True:
			self.rect.centerx -= 1

   