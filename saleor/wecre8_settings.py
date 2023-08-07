# flake8: noqa
import logging
import sentry_sdk
import os
from saleor.settings import *

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    traces_sample_rate=0.1,
    _experiments={
        "profiles_sample_rate": 0.1,
    },
)

TIME_ZONE = CELERY_TIMEZONE = "Asia/Riyadh"
'''
CITIES_LIGHT_INCLUDE_CITY_TYPES = [
    "PPL",
    "PPLA",
    "PPLA2",
    "PPLA3",
    "PPLA4",
    "PPLC",
    "PPLF",
    "PPLG",
    "PPLL",
    "PPLR",
    "PPLS",
    "STLMT",
]
CITIES_LIGHT_APP_NAME = "provinces"
CITIES_LIGHT_TRANSLATION_LANGUAGES = ["ar"]
CITIES_LIGHT_INCLUDE_COUNTRIES = ["SA", "AE", "OM", "BH", "QA", "KW"]

INSTALLED_APPS += [
    #"cities_light",
    "django_celery_results",
]
'''
SENTRY_OPTS.update(
    {
        "send_default_pii": True,  # type: ignore
    }
)

logging.basicConfig(
    level=logging.WARNING,
    format=" %(levelname)s %(name)s: %(message)s",
)
