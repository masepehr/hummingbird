"""
Test Hummingbird when no extra dependencies are installed.
"""
import unittest
import warnings

import numpy as np

from hummingbird.ml._utils import lightgbm_installed, xgboost_installed


class TestNoExtra(unittest.TestCase):
    """
    These tests are meant to be run on a clean container after doing
    `pip install hummingbird-ml` without any of the `extra` packages
    """

    # Test no LGBM returns false on lightgbm_installed()
    def test_lightgbm_installed_false(self):
        warnings.filterwarnings("ignore")
        assert not lightgbm_installed()

    # Test no XGB returns false on xgboost_installed()
    def test_xgboost_installed_false(self):
        warnings.filterwarnings("ignore")
        assert not xgboost_installed()

    # Test that we can import the converter successfully without installing [extra]
    def test_import_convert_no_extra(self):
        try:
            from hummingbird.ml import convert
        except Exception:  # TODO something more specific?
            self.fail("Unexpected Error on importing convert without extra packages")


if __name__ == "__main__":
    unittest.main()
