import curses
import math
import textwrap

def calc_cols(max_rows, array):
    return int(math.ceil(len(array) / max_rows))

def paginated_menu(stdscr, continents, page_size=15):
    # Get the screen height and width
    screen_height, screen_width = stdscr.getmaxyx()

    # Calculate the maximum number of items that can fit on the screen
    max_items = screen_height - 5  # Subtract 5 to give room for navigation info and margin
    
    # Update page_size if necessary
    page_size = min(page_size, max_items)

    num_continents = len(continents)
    num_pages = -(-num_continents // page_size)  # Ceiling division for page count
    current_page = 0
    k = 0

    while k != ord('q'):
        stdscr.clear()

        start_index = current_page * page_size
        end_index = min(start_index + page_size, num_continents)

        # Iterate and display the items that fit in the current page
        for i in range(start_index, end_index):
            line_pos = (i % page_size) + 2
            if line_pos < screen_height - 2:  # Check against screen height
                stdscr.addstr(line_pos, 0, f"Continent {i + 1}: {continents[i].get_continent_name()}")
        
        # Display navigation info in a location that is always visible
        navigation_info_line = screen_height - 2  # Second-to-last line of the terminal
        navigation_info = f"Page {current_page + 1} / {num_pages} - 'n' for next, 'p' for previous, 'q' to quit"
        stdscr.addstr(navigation_info_line, 0, navigation_info)

        # It's important to call refresh after any changes!
        stdscr.refresh()

        # Wait for user input
        k = stdscr.getch()

        if k == ord('n') and current_page < num_pages - 1:
            current_page += 1
        elif k == ord('p') and current_page > 0:
            current_page -= 1

def select_continent(stdscr, continents, page_size=15):
    # Get the screen height for pagination
    screen_height, _ = stdscr.getmaxyx()
    max_items = screen_height - 6  # Account for offset and instructions line
    page_size = min(page_size, max_items)
    
    num_continents = len(continents)
    num_pages = (num_continents + page_size - 1) // page_size
    current_page = 0
    current_row = 0

    while True:
        stdscr.clear()
        page_start = current_page * page_size
        page_end = min(page_start + page_size, num_continents)
        stdscr.addstr(0, 0, "Select a continent to edit (Up/Down to navigate, Enter to select, PgUp/PgDn to change pages, 'q' to exit):\n\n")

        for idx in range(page_start, page_end):
            option = continents[idx].get_continent_name()
            if idx == current_row + page_start:
                stdscr.addstr(idx - page_start + 3, 0, f"{option}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(idx - page_start + 3, 0, f"{option}\n")

        navigation_info = f"Page {current_page + 1} of {num_pages} - PgUp/PgDn to change pages"
        stdscr.addstr(screen_height - 3, 0, navigation_info)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row = (current_row - 1) % page_size
        elif key == curses.KEY_DOWN:
            current_row = (current_row + 1) % page_size
        elif key in (curses.KEY_ENTER, 10, 13):
            # Enter key, adjust index according to page number
            select_edit_view(stdscr, continents[current_row + page_start])
            # After editing, reset the position variables
            current_page = 0
            current_row = 0
        elif key == curses.KEY_NPAGE:  # Page Down
            if current_page < num_pages - 1:
                current_page += 1
                current_row = 0  # Reset row selection when changing page
        elif key == curses.KEY_PPAGE:  # Page Up
            if current_page > 0:
                current_page -= 1
                current_row = 0  # Reset row selection when changing page
        elif key == 27:  # ESC key
            break
        elif key == ord('q'):
            break

def select_edit_view(stdscr, continent):
    screen_height, _ = stdscr.getmaxyx()
    options = ["Edit This Continent", "View this Continent","Return"]
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr("What would you like to do with: " + continent.name + "\n\n")
        for idx, option in enumerate(options):
            if idx == current_row:
                stdscr.addstr(idx + 3, 0, f"{option}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 3, 0, f"{option}\n")
        stdscr.addstr(screen_height - 3, 0,"Navigate with the 'UP' / 'DOWN' arrow keys - Press 'Enter' to Select")
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP:
            current_row = max(0, current_row - 1)
        elif key == curses.KEY_DOWN:
            current_row = min(len(options) - 1, current_row + 1)
        elif key in (curses.KEY_ENTER, 10, 13):  # Enter key
            if current_row == 0:
                edit_continent(stdscr, continent)
            elif current_row == 1:
                display_continent(stdscr, continent)
            elif current_row == 2:
                break

def display_con_climate(stdscr, continent):
    screen_height, screen_width = stdscr.getmaxyx()
    result = "----Climate Information----"
    prompt_string = "Welcome To the Continent of " + continent.name

    while True:
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(4, (screen_width - len(prompt_string))//2 , prompt_string, curses.color_pair(1))
        stdscr.addstr(6, (screen_width - len(result))//2 , result)
        count = 0
        return_prompt = "Return to menu"
        for region, details in continent.climate.items():
            climate_string = "The {} region is characterized by a {}, mainly due to its {}.".format(region.capitalize(), details['climate'], details['feature'])
            stdscr.addstr(count + 8, (screen_width - len(climate_string))//2, climate_string)
            count += 1
        stdscr.addstr((screen_height // 2) + 4, (screen_width - len(return_prompt))//2, return_prompt, curses.A_REVERSE)
        stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
        stdscr.refresh

        key = stdscr.getch()

        if key in (curses.KEY_ENTER, 10, 13):
            break

def display_con_races(stdscr, continent):
    screen_height, screen_width = stdscr.getmaxyx()
    result = "----Race Demographics----"
    prompt_string = "Welcome To the Continent of " + continent.name

    MAX_LINES = 6

    max_cols = calc_cols(MAX_LINES, continent.inhabiting_races)

    while True:
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(4, (screen_width - len(prompt_string))//2 , prompt_string, curses.color_pair(1))
        stdscr.addstr(6, (screen_width - len(result))//2 , result)
        count = 0
        start_pos = max(0, (screen_width - max_cols * 25) // 2)
        col_count = 0

        return_prompt = "Return to menu"
        for race, population in continent.inhabiting_races.items():
            race_string = "{:<15s} {:<3d}%".format(race, population)
            stdscr.addstr(count + 8, start_pos + col_count * 25, race_string)
            count += 1
            if count >= MAX_LINES:
                count = 0
                col_count += 1
            

        stdscr.addstr(MAX_LINES + 10, (screen_width - len(return_prompt))//2, return_prompt, curses.A_REVERSE)
        stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
        stdscr.refresh

        key = stdscr.getch()

        if key in (curses.KEY_ENTER, 10, 13):
            break

def display_con_resources(stdscr, continent):
    screen_height, screen_width = stdscr.getmaxyx()
    result = "----Natural Resources----"
    prompt_string = f"Welcome To the Continent of {continent.name}"

    MAX_COLS = 5
    lines_per_region = {}

    # Calculate the total number of lines required for each region
    for region in continent.nat_resources:
        resources = continent.nat_resources[region]
        total_lines = sum(len(textwrap.wrap(f"- {resource} (Rarity: {rarity})", width=(screen_width // MAX_COLS) - 2)) for resource, rarity in resources)
        lines_per_region[region] = total_lines

    current_offset = 0  # Offset to track which region is currently being displayed

    while True:
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(4, (screen_width - len(prompt_string)) // 2, prompt_string, curses.color_pair(2))
        stdscr.addstr(6, (screen_width - len(result)) // 2, result, curses.color_pair(2))

        count = 0

        # Display the data for the current region based on the offset
        current_region = list(continent.nat_resources.keys())[current_offset]
        region_string = f"In the {current_region.capitalize()} region:"
        stdscr.addstr(8, (screen_width - len(region_string)) // 2, region_string)

        resources = continent.nat_resources[current_region]
        for resource, rarity in resources:
            bullet = "- "
            resource_string = f"{bullet}{resource} (Rarity: {rarity})"
            wrapped_lines = textwrap.wrap(resource_string, width=(screen_width - 2))
            
            for i, line in enumerate(wrapped_lines):
                stdscr.addstr(9 + count + i, (screen_width - (len(region_string)+1)) // 2, line)

            count += len(wrapped_lines)

        # Display the scrollbar
        scrollbar = f"Region {current_offset + 1}/{len(continent.nat_resources)}"
        stdscr.addstr((screen_height // 2) + 4, (screen_width - len(scrollbar)) // 2, scrollbar, curses.A_REVERSE)

        stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN:
            current_offset = (current_offset + 1) % len(continent.nat_resources)
        if key == curses.KEY_UP:
            current_offset = (current_offset - 1) % len(continent.nat_resources)
        elif key in (curses.KEY_ENTER, 10, 13):
            break

def display_continent(stdscr, continent):
    screen_height, screen_width = stdscr.getmaxyx()
    options = ["Climate", "Races", "Natural Resources", "Back"]
    current_row = 0
    prompt_string = "Welcome To the Continent of " + continent.name
    curses.init_pair(1, curses.COLOR_BLUE, -1)  # Pair number 2

    while True:
        stdscr.clear()
        stdscr.refresh()

        stdscr.addstr(0 + 4, (screen_width - len(prompt_string))//2, prompt_string, curses.color_pair(1) | curses.A_BOLD)
        for idx, option in enumerate(options):
            if idx == current_row:
                stdscr.addstr(idx + 6, (screen_width-len(option))//2, f"{option}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 6, (screen_width-len(option))//2, f"{option}\n")

        stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP:
            current_row = max(0, current_row - 1)
        elif key == curses.KEY_DOWN:
            current_row = min(len(options) - 1, current_row + 1)
        elif key in (curses.KEY_ENTER, 10, 13):  # Enter key
            if current_row == 0:
                display_con_climate(stdscr, continent)
            elif current_row == 1:
                display_con_races(stdscr, continent)
            elif current_row == 2:
                display_con_resources(stdscr, continent)
            elif current_row == 3:
                break

def edit_continent(stdscr, continent):
    options = ["Edit name", "Edit climate", "Edit inhabiting races", "Edit natural resources", "Back"]
    current_row = 0
    while True:
        stdscr.clear()
        stdscr.addstr("Editing: " + continent.name + "\n\n")
        for idx, option in enumerate(options):
            if idx == current_row:
                stdscr.addstr(idx + 3, 0, f"{option}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 3, 0, f"{option}\n")
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row = max(0, current_row - 1)
        elif key == curses.KEY_DOWN:
            current_row = min(len(options) - 1, current_row + 1)
        elif key in (curses.KEY_ENTER, 10, 13):  # Enter key
            if current_row == 0:
                continent.edit_name(stdscr)
            # Implement similar conditionals for other options...
            elif current_row == len(options) - 1:
                break
        elif key == 27:  # ESC key
            break