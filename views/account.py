import fastapi
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
router = fastapi.APIRouter()

templates = Jinja2Templates(directory='templates')

@router.get('/account',response_class=HTMLResponse)

def index(request:Request):
    vm = AccountViewModel(request)
    context = vm.to_dict()
    return templates.TemplateResponse('account/index.html',{"request":request,"data":context})

@router.get('/account/register')
def regsiter(request:Request):
    vm = RegisterViewModel(request)
    context = vm.to_dict()
    return templates.TemplateResponse('account/register.html',{"request":request,"data":context})

@router.post('/account/register')
async def register(request:Request):
        vm = RegisterViewModel(request)
        print(request)
        await vm.load()
        # if vm.error:
        #     context = vm.to_dict()
        #     return templates.TemplateResponse('account/register.html',{"request":request,"data":context})
        print("redirct")
        context = vm.to_dict()
        return templates.TemplateResponse('account/register.html',{"request":request,"data":context})
        


@router.get('/account/login')
def login(request:Request):
    vm = LoginViewModel(request)
    context = vm.to_dict()
    return templates.TemplateResponse('account/login.html',{"request":request,"data":context})

@router.get('/account/logout')
def logout(request:Request):
    return {}

