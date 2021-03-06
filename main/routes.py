from account.views import Index, Login, Signup, Logout
from user_files.views import UserFiles


def setup_routers(app):
    app.router.add_get('/', Index.get, name='index')

    app.router.add_get('/signup', Signup.get, name='signup')
    app.router.add_post('/signup', Signup.post)

    app.router.add_get('/login', Login.get, name='login')
    app.router.add_post('/login', Login.post)
    app.router.add_patch('/login', Login.patch)
    app.router.add_delete('/login', Login.delete)

    app.router.add_get('/logout', Logout.get, name='logout')

    app.router.add_get('/user_files', UserFiles.get, name='user_files')
    app.router.add_post('/user_files', UserFiles.post)
    # app.router.add_post('/user_files', UserFiles.delete)

# https://drive.google.com/open?id=1h_UQIb9T1QF9dYzzw36uVMBjoc4wl_h5-ejFk84knXg
# https://drive.google.com/open?id=143RU9FaHV9KpZZOqYtLtNCZyoXSBlGIIWvsPxn5frGU#
# https://docs.google.com/spreadsheets/d/1h_UQIb9T1QF9dYzzw36uVMBjoc4wl_h5-ejFk84knXg/export
