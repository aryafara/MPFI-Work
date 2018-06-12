#Multi-window display and tool functionality









#Controller class is an idea credited to this example: https://gist.github.com/MalloyDelacroix/2c509d6bcad35c7e35b1851dfc32d161
#essentially automates hooking sockets to other windows
#My implementation will in the future have a general method and perhaps a garbage collector
class Controller(dict):
    def __init__(self):
        super(Controller,self).__init__()
        '''
        reasoning for using dict:
            get/set methods
            beats using a stack with pairs due to how every menu is connected to main
            makes new menus easy to implement
        '''
        #self['main'] = mainWindow()
    
    def show_playBar(self,filename):
        #self['play'] = playBar(filename)
        self['play'].switch_window.connect(self['main']._show)
        #self['play'].show()
    
    def show_window(self,window:'Window Class', wargs = None): #generalized show fn for the windows#
        if window.__class__.__name__ in self or window:
            pass
        #here 
        else:
            self[window.__class__.__name__] = window(wargs)
            self[window.__class__.__name__].connect_to_main.connect(self['main']._show)
            #self[window].show()
