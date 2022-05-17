from tkinter.messagebox import NO
import fastapi
from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
from infrastructure import cookie_auth
from worker import user_service
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


# LOGIN FUNCTIONS !!!!!!!!!!!!!!!!!!
# Taking a register of new users
@router.post('/account/register')
async def register(request:Request):
        vm = RegisterViewModel(request)
        print(request)
        await vm.load()
        
        #invalid inputs from user handled here
        if vm.error:
            context = vm.to_dict()
            return templates.TemplateResponse('account/register.html',{"request":request,"data":context})
        #making user account
        account = user_service.create_account(vm.name, vm.email, vm.password)
        
        response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
        print(cookie_auth)
        cookie_auth.set_auth(response, account.id)
        return response
        

# GETTING PAGE FOR LOGIN
@router.get('/account/login')
def login(request:Request):
    vm = LoginViewModel(request)
    context = vm.to_dict()
    return templates.TemplateResponse('account/login.html',{"request":request,"data":context})

@router.get('/account/logout')
def logout(request:Request):
    return {}

