from typing import Optional
from urllib.request import Request
from fastapi import Request
class ViewModelBase:
    
    def __init__(self, request:Request):
        self.error: Optional[str] = None
        self.error: Optional[str] = None
        
        
    def to_dict(self) -> dict:
        return self.__dict__