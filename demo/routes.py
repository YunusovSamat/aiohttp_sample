from . import views


def setup_routers(app):
    app.router.add_get('/', views.index, name='index')
    app.router.add_get('/signup', views.Signup.get, name='signup')
    app.router.add_post('/signup', views.Signup.post)
    app.router.add_get('/login', views.Login.get, name='login')
    app.router.add_post('/login', views.Login.post)
    app.router.add_get('/logout', views.Logout.get)
