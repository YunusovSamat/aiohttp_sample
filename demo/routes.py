from . import views


def setup_routers(app):
    app.router.add_route('GET', '/', views.index)
    app.router.add_route('GET', '/post', views.post)
