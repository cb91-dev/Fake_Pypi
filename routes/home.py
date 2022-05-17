
import fastapi
from fastapi.templating import Jinja2Templates
from fastapi import Request
router = fastapi.APIRouter()
from viewmodels.home.indexviewmodel import IndexViewModel
from viewmodels.shared.viewmodel_base import ViewModelBase
from fastapi.responses import HTMLResponse
templates = Jinja2Templates(directory='templates')


@router.get('/',response_class=HTMLResponse)

def index(request:Request):
    vm = IndexViewModel(request)
    context = vm.to_dict()
    return templates.TemplateResponse('home/index.html',{"request":request,"data":context})



@router.get('/about',response_class=HTMLResponse)

def about(request:Request):
    vm = ViewModelBase(request)
    context = vm.to_dict() 
    return templates.TemplateResponse('home/index.html',{"request":request,"data":context})