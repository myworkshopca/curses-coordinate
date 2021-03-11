import curses

def window(stdscr):

    #curses.curs_set(0)

    # get size of the screen.
    sh, sw = stdscr.getmaxyx()

    # ┌ 9484
    stdscr.addstr(3, 3, chr(9484))

    # paint the
    stdscr.addstr(2, 3, "3")
    stdscr.addstr(3, 2, "3")

    # paint the x axis scale
    for x in range(4, sw):
        # ─ 9472
        stdscr.addstr(3, x, chr(9472))
        # only paint the 10s scale.
        if x % 10 == 0:
            # conver the x-axis to string
            x_str = str(x)
            # paint the x axis scale.
            for i in range(0, len(x_str)):
                stdscr.addstr(3 - 1 - i, x, x_str[len(x_str) - 1 - i])
    # paint the ending 9658 - ►
    stdscr.addstr(3, sw - 1, chr(9658))

    # paint the y axis scale
    for y in range(4, sh):
        # │ 9474
        stdscr.addstr(y, 3, chr(9474))
        if y % 10 == 0:
            y_str = str(y)
            stdscr.addstr(y, 3 - len(y_str), y_str)
    # paint the ending ▼ 9660
    stdscr.addstr(sh - 1, 3, chr(9660))

    msg = "Python curses Coordinate System"
    stdscr.addstr(sh // 2 - 4, sw // 2 - len(msg) // 2, msg)
    msg = "Press arrow keys to move around, Press ESC or q to exit" 
    stdscr.addstr(sh // 2 - 2, sw // 2 - len(msg) // 2, msg)

    cursor_ch = chr(9608)
    y, x = sh // 2 - 6, sw // 2 
    stdscr.addstr(y, x, cursor_ch)
    # paint the coordinate message.
    stdscr.addstr(sh // 2, sw // 2 - 7, '(y={0}, x={1})'.format(y, x))
    ny, nx = y, x

    while True:

        user_key = stdscr.getch()

        # exit when user press ESC q or Q
        if user_key in [27, 113, 81]:
            break

        # decide the new head based on the direction
        if user_key in [curses.KEY_UP, 107]:
            # k (107) for up
            if y > 0:
                ny = y - 1
        elif user_key in [curses.KEY_DOWN, 106]:
            # j (106) for down
            if y < sh - 1:
                ny = y + 1
        elif user_key in [curses.KEY_RIGHT, 108]:
            # l (108) for right
            if x < sw - 1:
                nx = x + 1
        elif user_key in [curses.KEY_LEFT, 104]:
            # h (104) for left
            if x > 0:
                nx = x - 1

        # erase the previous location by paint the white space.
        stdscr.addstr(y, x, ' ')
        # paint the new location.
        stdscr.addstr(ny, nx, cursor_ch)
        y, x = ny, nx

        # paint the (y, x) coordinate the at the center of the screen
        # there are 2 steps:
        # - erase the previous painting with white space
        stdscr.addstr(sh // 2, sw // 2 - 7, ' ' * 15)
        # - paint the new coordinate.
        stdscr.addstr(sh // 2, sw // 2 - 7, '(y={0}, x={1})'.format(y, x))

curses.wrapper(window)
