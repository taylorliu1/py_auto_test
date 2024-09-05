import pytest

if __name__ == '__main__':
    # report_path = Conf.get_report_path() + os.sep + "result"
    pytest.main(["-v", "testcase/PowerStore/Day0/VoD/test_longevity.py::Test_Setup", "--yaml", "config/conf.yml", "--json",
                 "config/config.json", "--alluredir", "report"])