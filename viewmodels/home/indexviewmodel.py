from typing import List

from fastapi import Request
from worker import package_service, user_service
from viewmodels.shared.viewmodel_base import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        
        self.package_count: int = package_service.release_count() 
        self.release_count: int = user_service.user_count()
        self.user_count:int = package_service.package_count()
        self.packages: List = package_service.latest_releases(limit=5)
    #     {
    #     "packages_count":274_000,
    #     "release_count":2_234_847,
    #     "user_count":73_874,
    #     'packages': [
    #         {'id': 'fastapi', 'summary': "A great web framework"},
    #         {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
    #         {'id': 'httpx', 'summary': "Requests for an async world"},
    #     ]
    # }
