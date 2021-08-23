import pygame


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        #初始化子弹的位置，实例化这个子弹类时传进来的position就应该是飞机矩形对象的中央上方发射
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = False
        #判断这个子弹跟敌机是否发生碰撞，然后要进行一个完美检测，所以需要一个mask属性
        self.mask = pygame.mask.from_surface(self.image)

    #定义子弹的移动的方法
    def move(self):
        #子弹向上发射
        self.rect.top -= self.speed
        #子弹的位置小于0的话，active属性设置为False，说明需要重新绘制
        if self.rect.top < 0:
            self.active = False

    #当子弹的active属性为False的时候，初始化
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

#吃到补给包，设置不同表现的子弹
class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("images/bullet2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 14
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        self.rect.top -= self.speed
        
        if self.rect.top < 0:
            self.active = False
    
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

