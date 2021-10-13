from IPython.display import Image, display, display_png
import os, sys, inspect

cmd_folder = os.path.realpath(
    os.path.dirname(
        os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class Matter(object):
    def is_valid(self):
        return True

    def is_not_valid(self):
        return False

    def is_also_valid(self):
        return True

    # graph object is created by the machine
    def show_graph(self,img_name, **kwargs):
        self.get_graph(**kwargs).draw(img_name+'.png', prog='dot')
        display(Image(img_name+'.png'))
