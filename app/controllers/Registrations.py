from system.core.controller import *
from flask import flash, escape
# ======================================================================================================================
#           Regesitratin Controller
# =====================================================================================================================
class Registrations(Controller):
    def __init__(self, action):
        super(Registrations, self).__init__(action)
        # Note that we have to load the model before using it
        self.load_model('User')
# ======================================================================================================================
#            
# =====================================================================================================================
    def index (self):
        print 'method index', request.method
        return self.load_view('index.html')
# ======================================================================================================================
#            
# =====================================================================================================================
    def not_allow(self):
        print 'methods not_allow', request.method
        return redirect('/')
# ======================================================================================================================
#           Login Controller Routes
# =====================================================================================================================
# 
    def register(self):
        print "regester"
        post= request.form
        user_info = {}

        for key in post:
            session[key] = post[key]
            user_info[key] = escape(post[key])

        register_status = self.models['Users'].register_user(user_info)
        print "register stauss", register_status

        if register_status ['status']:
            session['id'] = register_status['user']['id']
            session['name'] = register_status['user']['first_name'] + " " + register_status['user']['last_name']
            return redirect('/success')
        else:
         # set flashed error messages here from the error message we return from the Model
            for key in register_status['errors']:
                flash(u'{}'.format(register_status['errors'][key]), key)
            return self.load_view('/')
