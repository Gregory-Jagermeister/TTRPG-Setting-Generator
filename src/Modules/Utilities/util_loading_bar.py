import time
import sys

def print_loading_bar(iteration, total, loading_string="Loading", bar_length=50):
    # Calculate the number of `=` characters to show
    filled_length = int(bar_length * iteration // total)

    # Create the bar string
    bar = '=' * filled_length + '-' * (bar_length - filled_length)

    # Print the loading bar along with the current progress
    sys.stdout.write(f'\r{loading_string}: [{bar}] {(100 * iteration // total)}%')
    sys.stdout.flush()

def curses_loading_bar(stdscr, iteration, total, loading_string="Loading", bar_length=50):
    # Make sure the bar doesn't exceed the screen width
    max_y, max_x = stdscr.getmaxyx()
    bar_length = min(bar_length, max_x - len(loading_string) - 10)  # Account for padding and percentage

    # Calculate the number of `=` characters to show
    filled_length = int(bar_length * iteration // total)

    # Create the bar string
    bar = '=' * filled_length + '-' * (bar_length - filled_length)

    # Prepare and display the loading bar and percentage
    progress_str = f'{loading_string}: [{bar}] {(100 * iteration // total)}%'
    
    # Center the loading bar horizontally
    start_x = (max_x - len(progress_str)) // 2

    stdscr.clear()
    stdscr.addstr(max_y // 2, start_x, progress_str)
    stdscr.refresh()