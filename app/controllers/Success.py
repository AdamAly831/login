from system.core.controller import *


class Success(Controller):
    def __init__(self, action):
        super(Success, self).__init__(action)
    def index(self):
        # type = session ['type']
        if session ['id']:
            name = session ['name']
            return self.load_view('success.html', name = name )
        else:
            return redirect('/')
    def logout(self):
        #logout 
        return redirect('/') 


       
 
 
 