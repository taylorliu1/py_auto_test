
import sys
# sys.path.append(r"C:\Users\test\PycharmProjects\auto\py_auto_test")
from utils.conf.JsonUtil import JsonReader

import pytest
from utils.conf.YamlUtil import YamlReader


def pytest_addoption(parser):
    parser.addoption(
        "--yaml",
        action="store",
        # dest="environment",
        default='conf.yml',
        help="yaml config"
    )

    parser.addoption(
        "--json",
        action="store",
        # dest="environment",
        default='conf.json',
        help="json config"
    )

@pytest.fixture(scope="class")
def yaml(pytestconfig):
    return pytestconfig.getoption("yaml")

@pytest.fixture(scope="class")
def json(pytestconfig):
    return pytestconfig.getoption("json")

@pytest.fixture(scope="class")
def config(yaml):
    return YamlReader(yaml).data()

@pytest.fixture(scope="class")
def jsons(json):
    return JsonReader(json).data()
