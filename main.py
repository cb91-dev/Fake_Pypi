
import uvicorn
from fastapi import FastAPI
from views import home
from views import account
from views import packages
from fastapi.staticfiles import StaticFiles


app = FastAPI()


#Run application 
def main():
    config()
    uvicorn.run(app)

# Configure app
def config():
    config_routes()
    
# Loading routes
def config_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)
    
    

if __name__ == '__main__':
    main()
else:
    # Routes will always be loaded
    config()
