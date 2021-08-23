import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        #加载飞机图片，飞机的png背景需要透明的，利用.convert_alpha() 转化，得到一个Surface对象
        #通过两张图片不断切换，增加玩家飞机的动态效果
        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()
        #为玩家飞机加载毁灭的图片
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/me_destroy_1.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_2.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_3.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_4.png").convert_alpha() \
            ])
        #获取Surface对象的矩形对象。每一个Surface对象都会有一个rect矩形对象，用来描述Surface对象的位置信息。
        self.rect = self.image1.get_rect()
        #把传进来的bg_size参数传给width和height，含义是指飞机可以移动的宽和高
        self.width, self.height = bg_size[0], bg_size[1]
        #玩家飞机初始化时出现在窗口的位置
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        #初始化玩家飞机的速度
        self.speed = 10
        #添加active属性，这个属性表示玩家状态
        self.active = True
        #检测碰撞时，False表示未开启无敌状态，True表示已开启
        self.invincible = False
        #把图片非透明的部分设置为mask，标记为mask然后返回
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        #因为窗口左上角坐标是(0,0) ，如果矩形对象上部分不大于0，就是说没有超过游戏窗口的顶端位置，则self.rect.top -= self.speed
        #就是每次移动10个像素的位置，即speed，然后往上和往左走是减，往下和往右走是加。
        if self.rect.top > 0:
            self.rect.top -= self.speed
        #小于等于0时，要超出游戏窗口的上方了，那么就 self.rect.top = 0 纠正它的位置，使得玩家飞机的矩形对象最高只能跑到这个位置
        else:
            self.rect.top = 0

    #向下走、向左、向右走同理，其中因为要留60像素的高度在下边显示生命值与补给品，所以玩家飞机处于不可以界面最下边
    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    #初始化位置
    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True
