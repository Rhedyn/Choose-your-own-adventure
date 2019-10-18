import time
import os
import textwrap
tw = textwrap.TextWrapper(width = 72, initial_indent=' ', subsequent_indent=' ')
print ('\n'*100)
window_x, window_y = 640, 480
window_strike = ('─'*79)
window_dstrike = ('═'*79)
player_name = input("Please enter your name:\n\n> ")
print ('\n'*100 + window_dstrike)
