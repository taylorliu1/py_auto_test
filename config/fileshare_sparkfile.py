import os

import pytest

# from config import Conf

if __name__ == '__main__':
    # report_path = Conf.get_report_path() + os.sep + "result"
    pytest.main(["-v","testcase/PowerStore/Day0/share/test_share_spark.py::Test_Setup","--yaml","config/conf.yml","--json","config/config.json","--json","config/fileinfo.json""--alluredir", "report"])
