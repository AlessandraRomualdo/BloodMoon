import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_RED_DARK, MENU_OPTION, C_RED_DARKEST


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option=0
        # Carregar a música do menu
        pygame.mixer_music.load('./asset/TheNorth.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # desenhar a imagem e os textos no menu
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(120, "Blood", C_RED_DARK, ((WIN_WIDTH / 2), 70))
            self.menu_text(120, "Moon", C_RED_DARK, ((WIN_WIDTH / 2), 140))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(50, MENU_OPTION[i], C_RED_DARKEST, ((WIN_WIDTH / 2), 300 + 45 * i))
                else:
                    self.menu_text(50, MENU_OPTION[i], C_RED_DARK, ((WIN_WIDTH / 2), 300 + 45 * i))
            pygame.display.flip()

            # mapeando os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
                # mover as opções do menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # seta pra baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option +=1
                        else:
                            menu_option =0
                    if event.key == pygame.K_UP: # seta pra cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # tecla enter
                        return MENU_OPTION[menu_option]


    # metodo para escrever e criar a imagem
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)