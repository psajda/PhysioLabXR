import unittest

from rena.MainWindow import MainWindow
from rena.interfaces import InferenceInterface


class TestCase(unittest.TestCase):
    def test_recording_tab_file_finder(self):
        # create the app
        # main window init
        inference_interface = InferenceInterface()
        window = MainWindow(inference_interface=inference_interface)
        window.hide()  # no need to display the window when unit testing
        window.recording_tab.SelectDataDirBtn.click()
        # TODO complete the test case

if __name__ == '__main__':
    unittest.main()
