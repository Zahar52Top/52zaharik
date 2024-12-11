position_x = event.pos[0]

if pick_random == REAL_PLAYER:
  pg.draw.circle (screen, RED, (position_x, int (DISC_SIZE / 2)), DISC_RADIUS) pg.display.update()

if event.type == pg. MOUSEBUTTONDOWN:
    pg.draw.rect(screen, WHITE, (0, 0, width, DISC_SIZE))

if pick_random == REAL_PLAYER:
    position_x = event.pos[0]
    col = int(math.floor(position_x / DISC_SIZE))

if is_valid_position(grid, col):
    row = get_next_open_row(grid, col) grid[row][col] = REAL_PLAYER_ PIECE

if search_win_move (grid, REAL_ PLAYER_PIECE): label_my_font.

render ("Player 1 wins!", 1, RED
screen.blit(label, (10, 10)) game_over = True
pick_random += 1
pick_random pick_random % 2
draw_grid(grid)


if pick_random == AI_PLAYER and not game_over:
    col, minimax_score = minimax(grid, 5, -math.inf, math.inf, True)

if is_valid_position(grid, col):
    row = get_next_open_row(grid, col)
    grid[row][col] = AI_PLAYER_PIECE

if search_win_move (grid, AI_PLAYER_PIECE):
    label = my_font.render("Player 2 wins!", 1, YELLOW)
    screen.blit(label, (10, 10))

game_over = True
draw_grid(grid)
pick_random += 1
pick_random = pick_random % 2
if game_over:
    pg.time.wait(2500)

cells for chips of a different color (Fig. 8):
    def draw_grid(grid):
        for c in range(COLUMNS):
            for r in range(ROWS):
                pg.draw.rect(screen, BLUE, (c * DISC_SIZE, r * DISC_SIZE + DISC_SIZE, DISC_SIZE, DISC_ SIZE))
                pg.draw.circle (screen, WHITE, (int(c *DISC_SIZE + DISC_SIZE / 2), int(r * DISC_SIZE + DISC_SIZE + DISC_SIZE / 2)), DISC_ RADIUS)

for c in range (COLUMNS):
    for r in range(ROWS):
        for r in range(ROWS):

if grid[r] [c] == REAL_PLAYER_PIECE:
        pg.draw.circle(screen, RED, (int(c * DISC_SIZE + DISC_SIZE / 2),
            height int(r * DISC_SIZE + DISC_SIZE / 2)), DISC_RADIUS)

elif grid[r] [c] == AI_PLAYER_PIECE:
    pg.draw.circle(screen, YELLOW, (int(c * DISC_SIZE + DISC_SIZE / 2),
        height int(r * DISC_SIZE + DISC_SIZE / 2)), DISC_RADIUS):
             pg.display.update()

if is_valid_position(grid, col):
    row = get_next_open_row(grid, col)
    grid[row][col] = REAL_PLAYER_PIECE