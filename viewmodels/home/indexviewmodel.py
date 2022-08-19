from typing import List

from starlette.requests import Request

from worker import package_service, user_service
from viewmodels.shared.viewmodel_base import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.release_count: int = package_service.release_count()
        self.user_count: int = user_service.user_count()
        self.package_count: int = package_service.package_count()
        self.packages: List = package_service.latest_packages(limit=7)