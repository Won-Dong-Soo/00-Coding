import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('TicTacToe')

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
G = (50, 50, 50)
GR = (0,255,0)

# 폰트 설정
font = pygame.font.Font(None, 200)  # 기본 글꼴, 크기 200

# 보드 설정
rect_x1 = [420]
rect_y1 = [0]
rect_x = [510]
rect_y = [90]
rect_width = [1080, 240]
rect_height = [1080, 240]

for i in range(2):
    rect_x.append(rect_x[i] + 330)
    rect_y.append(rect_y[i] + 330)

# 오브젝트 생성
main_map = [[" " for _ in range(3)] for _ in range(3)]

# 전역 변수
x, y, turn, flag = 0, 0, 0, 0

def draw_text_with_border(text, font, text_color, border_color, x, y):
    text_surface = font.render(text, True, text_color)
    border_surface = font.render(text, True, border_color)

    # 테두리를 5픽셀씩 이동하며 그림
    screen.blit(border_surface, (x - 5, y))
    screen.blit(border_surface, (x + 5, y))
    screen.blit(border_surface, (x, y - 5))
    screen.blit(border_surface, (x, y + 5))

    # 원본 텍스트 그림
    screen.blit(text_surface, (x, y))

# 승자 확인
# s: 승자 확인을 위한 문자열
def check_winner(s):
    global flag
    for i in range(3):
        if main_map[i][0] == main_map[i][1] == main_map[i][2] == s or main_map[0][i] == main_map[1][i] == main_map[2][i] == s:
            return True
    if main_map[0][0] == main_map[1][1] == main_map[2][2] == s or main_map[0][2] == main_map[1][1] == main_map[2][0] == s:
        return True
    return False

# 게임 보드 업데이트
def update_board():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (rect_x1[0], rect_y1[0], rect_width[0], rect_height[0]))
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, WHITE, (rect_x[i], rect_y[j], rect_width[1], rect_height[1]))
            if main_map[i][j] == "O":
                pygame.draw.circle(screen, BLUE, (rect_x[i] + 120, rect_y[j] + 120), 120)
            elif main_map[i][j] == "X":
                pygame.draw.circle(screen, RED, (rect_x[i] + 120, rect_y[j] + 120), 120)

# 클릭 이벤트 처리
# pos: 클릭 좌표
def handle_click(pos):
    global x, y, turn
    x, y = pos
    for i in range(3):
        for j in range(3):
            if rect_x[i] <= x <= rect_x[i] + 240 and rect_y[j] <= y <= rect_y[j] + 240:
                if main_map[i][j] == " ":
                    main_map[i][j] = "O" if turn % 2 == 0 else "X"
                    turn += 1
                    return

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            handle_click(pygame.mouse.get_pos())

    update_board()

    if check_winner("O"):
        draw_text_with_border('BLUE WIN!', font, BLUE, G, 650, 500)
        flag = 1
    elif check_winner("X"):
        draw_text_with_border('RED WIN!', font, RED, G, 650, 500)
        flag = 1

    if flag == 1:
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    if turn == 9:
        if flag == 0:
            draw_text_with_border('DRAW!', font, GR, G, 750, 500)
            pygame.display.update()
            pygame.time.delay(2000)
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()