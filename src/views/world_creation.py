import curses
import random
from World.World import World

def display_world_name(stdscr, input_str):
    display_prompt(stdscr, "Type your World's Name ('r' for random Name, 'q' to quit): ", input_str)

def display_continent_amount(stdscr, input_str):
    display_prompt(stdscr, "How many Continents should this World have? ('r' for random, number to specify): ", input_str)

def display_mixed_races(stdscr, input_str): # NEW: Add a function for the new view
    display_prompt(stdscr, "Should civilizations be of mixed race? (Type 'yes' or 'no'): ", input_str)

def display_prompt(stdscr, prompt, input_str):
    stdscr.clear()
    stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
    screen_height, screen_width = stdscr.getmaxyx()
    center_column = screen_width // 2
    display_centered_text(stdscr, prompt, input_str, screen_height // 2 - 2, center_column)
    stdscr.refresh()

def display_centered_text(stdscr, text, input_str, y, center_column):
    stdscr.addstr(y, (center_column - len(text) // 2), text)
    underline = "_" * len(input_str)
    stdscr.addstr(y + 3, (center_column - len(underline) // 2), underline)
    stdscr.addstr(y + 2, (center_column - len(input_str) // 2), input_str)
    stdscr.move(y + 2, center_column + len(input_str) // 2)

def process_input(stdscr, current_view, inputs_map):
    user_input = inputs_map[current_view]
    ch = stdscr.getch()
    if ch == ord('\n'):
        return user_input, True  # Return input and signal to proceed
    elif ch == 8 and user_input:  # Handle backspace
        inputs_map[current_view] = user_input[:-1]
    elif ch >= 32 and ch <= 126:  # Handle regular character input
        inputs_map[current_view] += chr(ch)
    return None, False

def world_creation(stdscr):
    states = ['WORLD_NAME', 'MIXED_RACES', 'CONTINENT_AMOUNT']  # NEW: List of states
    current_state_idx = 0
    inputs = {'WORLD_NAME': '', 'MIXED_RACES': '', 'CONTINENT_AMOUNT': ''}  # NEW: Inputs
    
    while current_state_idx < len(states):
        current_view = states[current_state_idx]
        display_func = globals()[f'display_{current_view.lower()}']
        display_func(stdscr, inputs[current_view])
        
        input_result, should_proceed = process_input(stdscr, current_view, inputs)
        
        if should_proceed:
            if current_view == 'MIXED_RACES':
                result = inputs['MIXED_RACES'].lower() == 'yes'  # Convert to boolean
                inputs['MIXED_RACES'] = result  # Store the boolean value
                #current_state_idx += 1  # Move to the next state
            if current_view == 'CONTINENT_AMOUNT':
                continent_input = inputs['CONTINENT_AMOUNT'].lower()
                if continent_input.isdigit() and int(continent_input) > 0:
                    world = World(inputs['WORLD_NAME']).generate_world(int(inputs['CONTINENT_AMOUNT']), stdscr, is_mixed= inputs['MIXED_RACES'])
                    return world
                elif continent_input == 'r':
                    # Add your logic for random continent amount generation here, e.g.:
                    random_amount = random.randint(1, 4)
                    world = World(inputs['WORLD_NAME']).generate_world(random_amount, stdscr, is_mixed= inputs['MIXED_RACES'])
                    return world
                else:
                    display_error(stdscr, "Invalid number of continents! Please try again.")
                    continue
            
            if not validate_input(current_view, input_result):
                display_error(stdscr, "Invalid input! Please try again.")
                continue  # Don't advance the state if validation fails
            current_state_idx += 1  # Move to the next state

    return None  # In case the loop exits normally without world generation

def validate_input(view, result):
    if view == 'WORLD_NAME':
        return bool(result)  # Ensure world name is not empty
    elif view == 'MIXED_RACES':
        response = result.lower()
        return response in ['yes', 'no']  # Keep this check to ensure the response is valid
    elif view == 'CONTINENT_AMOUNT':
        return result.isdigit() or result.lower() == 'r'  # Validate continent amount or 'r' for random
    return False  # Fallback for unexpected view

def display_error(stdscr, message):
    stdscr.clear()
    stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
    display_centered_text(stdscr, message, "", stdscr.getmaxyx()[0] // 2, stdscr.getmaxyx()[1] // 2)
    stdscr.refresh()
    stdscr.getch()  # Wait for user ack
