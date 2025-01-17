import pygame

pygame.init()

font20 = pygame.font.Font('freesansbold.ttf', 20)
COLOR1 = (0, 0, 0)
COLOR2 = (255, 255, 255)
COLOR3 = (0, 255, 0)
W, H = 900, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 30


class Striker:  # paddle
    def __init__(self, posx, posy, w, h, speed, color):
        self.posx = posx
        self.posy = posy
        self.w = w
        self.h = h
        self.speed = speed
        self.color = color
        self.entityRect = pygame.Rect(posx, posy, w, h)
        self.entity = pygame.draw.rect(screen, self.color, self.entityRect)

    def display(self):
        self.entity = pygame.draw.rect(screen, self.color, self.entityRect)

    def update(self, yfac):
        self.posy = self.posy + self.speed * yfac

        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.h >= H:
            self.posy = H - self.h

        self.entityRect = (self.posx, self.posy, self.w, self.h)

    def scoredisp(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        textrect = text.get_rect()
        textrect.center = (x, y)

        screen.blit(text, textrect)

    def getrect(self):
        return self.entityRect


class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yfac = -1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1

    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yfac

        if self.posy <= 0 or self.posy >= H:
            self.yfac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= W and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0

    def reset(self):
        self.posx = W // 2
        self.posy = H // 2
        self.xFac *= -1
        self.firstTime = 1

    def boink(self):
        self.xFac *= -1

    def getrect(self):
        return self.ball


def main():
    running = True
    entity1 = Striker(20, 0, 10, 100, 10, COLOR3)
    entity2 = Striker(W - 30, 0, 10, 100, 10, COLOR3)
    ball = Ball(W // 2, H // 2, 7, 7, COLOR2)

    entities = [entity1, entity2]

    entity1score, entity2score = 0, 0
    entity1yfac, entity2yfac = 0, 0

    while running:
        screen.fill(COLOR1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    entity2yfac = -1
                if event.key == pygame.K_DOWN:
                    entity2yfac = 1
                if event.key == pygame.K_z:
                    entity1yfac = -1
                if event.key == pygame.K_s:
                    entity1yfac = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    entity2yfac = 0
                if event.key == pygame.K_z or event.key == pygame.K_s:
                    entity1yfac = 0

        for entity in entities:
            if pygame.Rect.colliderect(ball.getrect(), entity.getrect()):
                ball.boink()

        entity1.update(entity1yfac)
        entity2.update(entity2yfac)
        point = ball.update()

        if point == -1:
            entity1score += 1
        elif point == 1:
            entity2score += 1

        if point:
            ball.reset()

        entity1.display()
        entity2.display()
        ball.display()
        entity1.scoredisp("entity_1 : ",
                          entity1score, 100, 20, COLOR2)
        entity2.scoredisp("entity_2 : ",
                          entity2score, W - 100, 20, COLOR2)
        pygame.display.update()

        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
