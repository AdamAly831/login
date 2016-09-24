from system.core.router import routes

# ======================================================================================================================
#           Regester
# =====================================================================================================================
routes['GET']['/'] = 'Registrations#index'
routes['POST']['/'] = 'Registrations#not_allow'
routes['POST']['/register'] = 'Registrations#register'

# ======================================================================================================================
#           Login Controller Routes
# =====================================================================================================================

routes['POST']['/login'] = 'Logins#login'
routes['GET']['/logout'] = 'Success#logout'
routes ['POST'] ['/users'] = 'Users#register'
