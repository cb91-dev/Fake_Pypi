from viewmodels.shared.viewmodel_base import ViewModelBase
from data.user import User
from fastapi import Request



class AccountViewModel(ViewModelBase):
    def __init__(self,request: Request):
        super().__init__(request)
        self.user = User('Craig','mail@mail.com','84fdv189v1v')
    pass