import os

import pytest

# from config import Conf

if __name__ == '__main__':
    # report_path = Conf.get_report_path() + os.sep + "result"
    pytest.main(["-v","testcase/PowerStore/Day0/iscsi/test_iscsi.py::Test_Clean","--yaml","config/conf.yml","--json","config/config.json","--alluredir", "report"])
