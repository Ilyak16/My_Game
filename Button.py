import pygame

class ImageButton:
    def __init__(self,x, y, width, height, text, image_path, image_hover_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image_hover = self.image
        if image_hover_path:
            self.image_hover = pygame.image.load(image_hover_path)
            self.image_hover = pygame.transform.scale(self.image_hover, (width, height))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.sound_path = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False
    def Draw(self, screen):
        current_image = self.image_hover if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)
        font = pygame.font.SysFont(None, 45)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    def check_hover(self,mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))