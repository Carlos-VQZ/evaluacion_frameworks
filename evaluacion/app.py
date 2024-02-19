import web
from mvc.controllers.login import Login

urls = (
    "/", "mvc.controllers.login.Login",
    "/index", "mvc.controllers.index.Index" 
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
