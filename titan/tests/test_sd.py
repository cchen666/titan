from titan.tests.utils import *

ENV_TITANRC = '/Users/cchen/.bash_profile'
ENV_TEST_VM_NAME = "cchen-tox-" + gen_random(5, 0, 9)

class TestSD:
    def setup(self):
        print("Setup")

    def teardown(self):
        print("teardown")

    def test_sd_list(self):
        test_command = "source " + ENV_TITANRC + ";" + "titan sd-list 2>/dev/null"
        r = commands.getstatusoutput(test_command)[0]
        assert r == 0, test_command
