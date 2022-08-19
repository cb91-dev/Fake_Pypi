from importlib.resources import Package
from struct import pack
import fastapi
from fastapi.templating import Jinja2Templates
router = fastapi.APIRouter()
from fastapi import Request
templates = Jinja2Templates(directory='templates')
from viewmodels.packages.details_viewmodel import DetailsViewModel


@router.get('/project/{package_name}')
def details(package_name: str, request: Request):
    vm = DetailsViewModel(package_name,request)
    details = vm.to_dict()
    print(details)
    return templates.TemplateResponse('packages/details.html',{"request":request,"data":details})
 
 

