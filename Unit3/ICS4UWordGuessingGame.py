import pygame
pygame.init()
screen = pygame.display.set_mode((780, 600))
clock = pygame.time.Clock()
running = True

# font
title_font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 32)

# text
title_text = title_font.render('Guess a Word Game', True, (0, 0, 0))
button_text = button_font.render('Start Game', True, (0, 0, 0))

# button
button_rect = pygame.Rect(0, 0, 200, 50)
button_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

running = True

def start_game():
    # set up the game
    word = "ABCDEF"
    remain_time = max(len(word), 5)
    # set up the game
    characters = [[letter, True] for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    # character buttons setting
    button_size = 100
    button_gap = 10
    buttons = []
    for i in range(26):
        x = button_gap + (button_size + button_gap) * (i % 7)
        y = button_gap + (button_size + button_gap) * (i // 7)
        rect = pygame.Rect(x, y, button_size, button_size)
        buttons.append(rect)

    # textbox setting
    textbox_width = screen.get_width() - 2 * button_gap
    textbox_height = 100
    textbox_x = button_gap
    textbox_y = button_gap + 4 * (button_size + button_gap)
    textbox_rect = pygame.Rect(textbox_x, textbox_y, textbox_width, textbox_height)

    # remain time setting
    remain_time_rect = pygame.Rect(button_gap + 5 * (button_size + button_gap), button_gap + 3 * (button_size + button_gap), 2 * button_size + button_gap, button_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(buttons):
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        # click the button
                        if characters[i][1]:
                            characters[i][1] = False
                            if characters[i][0] not in word:
                                remain_time -= 1
                                characters[i][1] = False
                                if remain_time == -1:
                                    # failed
                                    fail_text = title_font.render("You Failed!", True, (255, 0, 0))
                                    fail_text_rect = fail_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
                                    screen.fill("white")
                                    screen.blit(fail_text, fail_text_rect)
                                    pygame.display.flip()
                                    pygame.time.wait(3000)
                                    running = False
        # win
        if all([not characters[ord(letter) - ord('A')][1] for letter in word]):
            success_text = title_font.render("You Win!", True, (0, 255, 0))
            success_text_rect = success_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.fill("white")
            screen.blit(success_text, success_text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
        screen.fill("white")

        # display characters buttons
        for i, rect in enumerate(buttons):
            if characters[i][1]:
                pygame.draw.rect(screen, (200, 200, 200), rect)
                letter = chr(ord('A') + i)
                letter_text = button_font.render(letter, True, (0, 0, 0))
                letter_text_rect = letter_text.get_rect(center=rect.center)
                screen.blit(letter_text, letter_text_rect)

        # display textbox
        pygame.draw.rect(screen, (200, 200, 200), textbox_rect)

        # create a text surface
        show_word = "".join([letter if not characters[ord(letter) - ord('A')][1] else "_" for letter in word])
        textbox_text = button_font.render(f"Guess the Word: {show_word}", True, (0, 0, 0))
        screen.blit(textbox_text, (textbox_rect.x + 50, textbox_rect.y + 10))

        # display remain times
        pygame.draw.rect(screen, (200, 200, 200), remain_time_rect)

        # create two text surfaces
        remain_time_text1 = button_font.render("Wrong Guesses:", True, (0, 0, 0))
        remain_time_text2 = button_font.render(str(remain_time) + " Left", True, (0, 0, 0))

        # calculate the position of the two text surfaces
        text1_pos = remain_time_text1.get_rect(center=(remain_time_rect.centerx, remain_time_rect.centery - remain_time_text1.get_height() // 2))
        text2_pos = remain_time_text2.get_rect(center=(remain_time_rect.centerx, remain_time_rect.centery + remain_time_text2.get_height() // 2))

        # display the two text surfaces
        screen.blit(remain_time_text1, text1_pos)
        screen.blit(remain_time_text2, text2_pos)

        pygame.display.flip()

        clock.tick(60)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the button is clicked
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                start_game()

    screen.fill("white")

    # create title
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, screen.get_height() // 4))

    # create button
    pygame.draw.rect(screen, (200, 200, 200), button_rect)
    screen.blit(button_text, (button_rect.x + 50, button_rect.y + 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()