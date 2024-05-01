# import curses

# def center_typing(stdscr):
#     curses.curs_set(1)  # Show the cursor
#     stdscr.clear()
#     stdscr.refresh()

#     text = ""
#     max_width = curses.COLS - 2  # Maximum width for visible content
#     center_column = curses.COLS // 2  # Center column for cursor positioning

#     while True:
#         stdscr.clear()

#         # Adjust visible content based on cursor position
#         if len(text) > max_width:
#             start_index = max(0, len(text) - max_width)
#             visible_text = text[start_index:]
#         else:
#             visible_text = text

#         # Display visible content
#         stdscr.addstr(0, center_column - len(visible_text) // 2, visible_text)

#         # Move cursor to the end of the text
#         stdscr.move(0, center_column + len(visible_text) // 2)

#         # Get user input
#         key = stdscr.getch()

#         # Handle input
#         if key == ord('\n'):  # Enter key to exit
#             break
#         elif key == curses.KEY_BACKSPACE:
#             text = text[:-1]  # Backspace to delete the last character
#         else:
#             text += chr(key)  # Add typed character to text

#     curses.curs_set(0)  # Hide the cursor after exiting

# def main(stdscr):
#     curses.wrapper(center_typing)

# if __name__ == "__main__":
#     main(None)

import random

items = ['A', 'B', 'C', 'D']
weights = [1, 2, 3, 4]

selected_items = []

# Perform weighted random selection for k times
for _ in range(20):
    selected_item = random.choices(items, weights, k=1)[0]
    selected_items.append(selected_item)
    index = items.index(selected_item)
    items.pop(index)
    weights.pop(index)

print("Selected items:", selected_items)
print("Remaining items:", items)
