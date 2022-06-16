from __future__ import annotations
from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))

__all__ = ("Config", "app_config")


class Config(object):
    DEBUG = os.environ.get("DEBUG")
    CSRF_ENABLED = os.environ.get("CSRF_ENABLED")
    URL = os.environ.get("URL")


class DevelopmentConfig(Config):
    DEBUG = True



class TestConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

app_config = {
    "development": DevelopmentConfig,
    "testing": TestConfig,
    "production": ProductionConfig,
}