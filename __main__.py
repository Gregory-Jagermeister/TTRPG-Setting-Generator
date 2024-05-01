import random
import time
import curses
#from Modules.Utilities.util_loading_bar import curses_loading_bar
#from Modules.Utilities.util_menus import paginated_menu
#from Modules.Utilities.util_menus import select_continent
#from Modules.Civilisations.Civilisation import Civilisation
from src.Modules.Settlement.TradingPost import TradingPost
from src.Modules.Settlement.Village import Village
from src.Modules.Settlement.Town import Town
from src.Modules.Settlement.City import City
#from views.world_creation import world_creation

def main(stdscr):

    trading_post = TradingPost().generate()
    village = Village().generate()
    town = Town().generate()
    city = City().generate()
    with open("Test - Trading Post.txt", 'w') as f:
        f.write(trading_post.__str__())
    with open("Test - Village.txt", 'w') as f:
        f.write(village.__str__())
    with open("Test - Town.txt", 'w') as f:
        f.write(town.__str__())
    with open("Test - City.txt", 'w') as f:
        f.write(city.__str__())
    # curses.curs_set(0)
    # curses.start_color()
    # curses.use_default_colors()

    # stdscr.clear()
  
    # world = world_creation(stdscr)
    # curses.curs_set(0)
    
    #select_continent(stdscr,world.get_world_continents())
   
    #stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)