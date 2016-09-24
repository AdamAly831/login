"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
#get the page oload 
# get get  regester to work
# get  the login to work

from system.core.controller import *
from flask import flash, escape
class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        # Note that we have to load the model before using it
        self.load_model('User')

    def index (self):
        return self.load_view('success.html')

    def login(self):
        print 'login workin'        
        post = request.form
        print post

        user_info = {
        'email': post ['email'],
        'password':post['password'],
        }

        user = self.models['User'].login_user(user_info)
        if not user:
            print "Incorrect login"
            return redirect('')
        else:
            session['id'] = user ['id']
            session['name'] = user['first_name'] + " " + user['last_name']
            session['type'] = 'login'
        return redirect('/success')

    def register(self):
        print "regester"
        post= request.form
        user_info = {}

        for key in post:
            session[key] = post[key]
            user_info[key] = escape(post[key])

        register_status = self.models['User'].register_user(user_info)
        print "register stauss", register_status

        if register_status ['status']:
            session['id'] = register_status['user']['id']
            session['name'] = register_status['user']['first_name'] + " " + register_status['user']['last_name']
            return redirect('/success')
        else:
         # set flashed error messages here from the error message we return from the Model
            for key in register_status['errors']:
                flash(u'{}'.format(register_status['errors'][key]), key)
            return redirect('/')
 

    # # This is how a method used to add a course would look
    # # We would set up a POST route for this method
    # def add(self):
    #     # in actuality, data for the new course would come 
    #     # from a form on our client
    #     course_details = {
    #         'title': 'Python',
    #         'description': 'Python is Amazing'
    #     }
    #     self.models['Logins'].add_course(course_details)
    #     return redirect('/')

    # # This is how a method used to update a course would look
    # # We would set up a POST route for this method
    # def update(self, course_id):
        
    #     self.models['Logins'].update_course(course_details)
    #     return redirect('/')

    #  # This is how a method used to delete a course would look
    #  # We would set up a POST route for this method
    #  def delete(self, course_id):
    #      self.models['Logins'].delete_course(course_id)
    #      return redirect('/')

        """
        
        This is an example of a controller method that will load a view for the client 

        """

        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
       
        #http://localhost:5000/welcome/new
     
 