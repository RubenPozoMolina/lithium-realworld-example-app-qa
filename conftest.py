import configparser
import pytest


@pytest.fixture
def config():
    cfg = configparser.ConfigParser()
    cfg.read('./config/config.ini')
    yield cfg
