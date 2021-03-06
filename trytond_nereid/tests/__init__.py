# -*- coding: utf-8 -*-
"""
    __init__

    Nereid Tryton module test cases

    :copyright: (c) 2011-2013 by Openlabs Technologies & Consulting (P) Limited
    :license: GPLv3, see LICENSE for more details.
"""
import unittest

import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from test_auth import TestAuth
from test_address import TestAddress
from test_i18n import TestI18N
from test_static_file import TestStaticFile
from test_currency import TestCurrency
from test_routing import TestRouting
from test_translation import TestTranslation
from test_country import TestCountry
from test_website import TestWebsite


class TestNereid(ModuleTestCase):

    module = 'nereid'


def suite():
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestNereid)
    )
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestAuth)
    )
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestAddress)
    )
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestI18N)
    )
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestStaticFile)
    )
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestCurrency)
    )
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestRouting)
    )
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestTranslation),
    )
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestCountry)
    )
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestWebsite)
    )
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
