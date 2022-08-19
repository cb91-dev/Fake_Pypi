
import uvicorn
from pathlib import Path
from fastapi import FastAPI
from routes import home
from routes import account
from routes import packages
from fastapi.staticfiles import StaticFiles
from data import db_session

app = FastAPI()


#Run application 
def main():
    config(dev_mode=True)
    # noinspection PyTypeChecker
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)

# Configure app
def config(dev_mode:bool):
    config_routes()
    config_db(dev_mode)
    
    
#  Configure DB
def config_db(dev_mode: bool):
    './db/pypi.sqlite'
    file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
    db_session.global_init(file.as_posix())
    
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
    config(dev_mode=False)
