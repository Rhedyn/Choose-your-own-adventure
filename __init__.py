import time
import os
import textwrap
os.system('mode con: cols=90 lines=30')
tw = textwrap.TextWrapper(width = 72, initial_indent=' ', subsequent_indent=' ')
print ('\n'*100)
window_strike = ('─'*79)
window_dstrike = ('═'*79)
window_pstrike = ('·'*79)
player_name = input("Please enter your name:\n\n> ")
print ('\n'*100 + window_dstrike)
