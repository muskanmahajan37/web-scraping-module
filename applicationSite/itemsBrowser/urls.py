from urllib.parse import urlparse
from uuid import uuid4
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')


def url_validation(url):
    validate = URLValidator()
    try:
        validate(url)
    except ValidationError:
        return False
    return True


