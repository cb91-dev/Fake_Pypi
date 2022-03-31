import fastapi
from fastapi.templating import Jinja2Templates
router = fastapi.APIRouter()
templates = Jinja2Templates(directory='templates')