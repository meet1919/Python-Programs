import pygame
pygame.init()
from Grid import Grid

surface = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Tic Tac Toe')
#Icon
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

import threading

def create_thread(target):
    thread = threading.Thread(target = target)
    thread.daemon = True
    thread.start()

import socket

HOST = '127.0.0.1'
PORT = 65432
connection_established = False
conn, addr = None, None
                        #IPv4              #TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

def recieve_data():
    global turn
    while True:
        data = conn.recv(1024).decode()
        data = data.split('-')
        x, y = int(data[0]), int(data[1])
        if data[2] == 'Your Turn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'O')
        print(data)

def waiting_for_connection():
    global connection_established, conn, addr
    conn, addr = sock.accept()
    print('Client is connected')
    connection_established = True
    recieve_data()

create_thread(waiting_for_connection)

grid = Grid()
running = True
player = 'X'
turn = True
playing = 'True'

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and connection_established:
            if pygame.mouse.get_pressed()[0]:
                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    cellX, cellY = pos[0] // 100, pos[1] // 100
                    grid.get_mouse(cellX, cellY, player)
                    if grid.game_over:
                        playing = 'False'
                    send_data = '{}-{}-{}-{}'.format(cellX, cellY, 'Your Turn', playing).encode()
                    conn.send(send_data)
                    turn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
                playing = 'True'


    surface.fill((0, 0, 0))
    grid.draw(surface)
    pygame.display.flip()
