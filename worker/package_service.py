import datetime
from typing import List, Optional

from data.package import Package
from data.release import Release




# This woker file is for return information about packages that can be found on site.

# Returning a count of release on site
def release_count()-> int:
    return 2_234_847

# Return a count of all packages found
def package_count()-> int:
    return 274_000
#  grabbing latest_releases from DB
def latest_releases(limit:int=5) -> List:
    return [
            {'id': 'fastapi', 'summary': "A great web framework"},
            {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
            {'id': 'httpx', 'summary': "Requests for an async world"},
        ][:limit]
    

#  Returning get_package_by_id from DB
def get_package_by_id(package_name:str) -> Optional[Package]:
    package = Package(
        package_name,"This is the summary", "Full details here!",
        "https://fastapi.tiangolo.com/","MIT","Craig Sexypants Bennett"
    )
    return package

# Finding latest_release_for_package for a singel package
def get_latest_release_for_package(package_name:str) -> Optional[Release]:
    return Release("1.2.0", datetime.datetime.now())




