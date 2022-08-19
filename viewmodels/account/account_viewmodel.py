from viewmodels.shared.viewmodel_base import ViewModelBase
from worker import user_service
from fastapi import Request




class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.user = user_service.get_user_by_id(self.user_id)