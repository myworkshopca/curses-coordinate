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

    # paint the x axis.
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

    for y in range(4, sh):
        # │ 9474
        stdscr.addstr(y, 3, chr(9474))
        if y % 10 == 0:
            y_str = str(y)
            stdscr.addstr(y, 3 - len(y_str), y_str)
    # paint the ending ▼ 9660
    stdscr.addstr(sh - 1, 3, chr(9660))

    while True:
        stdscr.addstr(sh - 10, sw - 50, 'Enter Y axis: ')
        # user input string.
        user_i = ''
        while True:
            key = stdscr.getch()
            if key >= 48 and key <= 57:
                user_i = user_i + chr(key)
                stdscr.addstr(chr(key))
            elif key == 10:
                break
            else:
                continue
        # set the y axis
        user_y = int(user_i)

        stdscr.addstr(sh - 9, sw - 50, 'Enter X axis: ')
        # reset the user input string
        user_i = ''
        while True:
            key = stdscr.getch()
            if key >= 48 and key <= 57:
                user_i = user_i + chr(key)
                stdscr.addstr(chr(key))
            elif key == 10:
                break
            else:
                continue

        # set the y axis
        user_x = int(user_i)

        # paint the user input.
        stdscr.addstr(user_y, user_x, "X")
        key = stdscr.getch()
        # exit when it is ESC
        if key == 27:
            break
        else:
            # start over.
            stdscr.addstr(sh - 10, sw - 50, ' ' * 30)
            stdscr.addstr(sh - 9, sw - 50, ' ' * 30)

curses.wrapper(window)
