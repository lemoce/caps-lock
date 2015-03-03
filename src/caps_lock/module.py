import pygtk
pygtk.require('2.0')

import gtk
gtk.gdk.threads_init()
import gobject
import commands
import os
import sys

#CURRENT_DIR = '/home/27190057897/workspaces/python/caps-lock'
SEP_CHAR = os.sep
COMMAND = "xset q | grep LED"

def determine_path():
    """Borrowed from wxglade.py"""
    try:
        root = __file__
        if os.path.islink(root):
            root = os.path.realpath(root)
        return os.path.dirname(os.path.abspath(root))
    except:
        print "I'm sorry, but something is wrong."
        print "There is no __file__ variable. Please contact the author."
        sys.exit()

CURRENT_DIR = '%s%s%s' % (determine_path(), SEP_CHAR, 'data')
        
CAPS_MAP = {True: '%s%s%s' % (CURRENT_DIR, SEP_CHAR, 'caps_on.svg'),
            False: '%s%s%s' % (CURRENT_DIR, SEP_CHAR, 'caps_off.svg')}
NUM_MAP = {True: '%s%s%s' % (CURRENT_DIR, SEP_CHAR, 'num_on.svg'),
           False: '%s%s%s' % (CURRENT_DIR, SEP_CHAR, 'num_off.svg')}

def caps_status():
    caps = int(commands.getoutput(COMMAND)[65])
    if caps % 2 == 1:
        return True
    else:
        return False

def num_status():
    num = int(commands.getoutput(COMMAND)[65])
    if num / 2 == 1:
        return True
    else:
        return False

class KeyStatusChecker:

    def __init__(self):
        self.caps_icon = gtk.status_icon_new_from_file(CAPS_MAP[caps_status()])
        self.num_icon = gtk.status_icon_new_from_file(NUM_MAP[num_status()])
        self.caps_icon.set_visible(True)
        self.num_icon.set_visible(True)
        self.tick_interval = 1

    def update(self):
        self.caps_icon.set_from_file(CAPS_MAP[caps_status()])
        self.num_icon.set_from_file(NUM_MAP[num_status()])
        source_id = gobject.timeout_add(self.tick_interval*1000, self.update)

    def main(self):
        source_id = gobject.timeout_add(self.tick_interval*1000, self.update)
        gtk.main()



def main():
    app = KeyStatusChecker()
    app.main()

if __name__ == "__main__":
    main()
