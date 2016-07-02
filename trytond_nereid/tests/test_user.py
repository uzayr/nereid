# -*- coding: utf-8 -*-
"""
    Test User

    :copyright: (c) 2015 by Fulfil.IO Inc.
    :license: BSD, see LICENSE for more details.
"""
from decimal import Decimal
import unittest

import trytond.tests.test_tryton
from nereid.testing import NereidTestCase
from trytond.tests.test_tryton import POOL, USER, USER, CONTEXT


class TestUser(NereidTestCase):
    """
    Test User
    """

    def setUp(self):
        trytond.tests.test_tryton.install_module('nereid')
        self.nereid_website_obj = POOL.get('nereid.website')
        self.nereid_website_locale_obj = POOL.get('nereid.website.locale')
        self.nereid_permission_obj = POOL.get('nereid.permission')
        self.nereid_user_obj = POOL.get('nereid.user')
        self.company_obj = POOL.get('company.company')
        self.currency_obj = POOL.get('currency.currency')
        self.language_obj = POOL.get('ir.lang')
        self.party_obj = POOL.get('party.party')
        self.Country = POOL.get('country.country')
        self.Subdivision = POOL.get('country.subdivision')

    def setup_defaults(self):
        """
        Setup the defaults
        """
        usd, = self.currency_obj.create([{
            'name': 'US Dollar',
            'code': 'USD',
            'symbol': '$',
            'rates': [('create', [{'rate': Decimal('1')}])],
        }])
        eur, = self.currency_obj.create([{
            'name': 'Euro',
            'code': 'EUR',
            'symbol': 'E',
            'rates': [('create', [{'rate': Decimal('2')}])],
        }])
        self.party, = self.party_obj.create([{
            'name': 'Openlabs',
        }])
        self.company, = self.company_obj.create([{
            'currency': usd,
            'party': self.party,
        }])
        c1, = self.currency_obj.create([{
            'code': 'C1',
            'symbol': 'C1',
            'name': 'Currency 1',
            'rates': [('create', [{'rate': Decimal('10')}])],

        }])
        c2, = self.currency_obj.create([{
            'code': 'C2',
            'symbol': 'C2',
            'name': 'Currency 2',
            'rates': [('create', [{'rate': Decimal('20')}])],
        }])
        self.lang_currency, = self.currency_obj.create([{
            'code': 'C3',
            'symbol': 'C3',
            'name': 'Currency 3',
            'rates': [('create', [{'rate': Decimal('30')}])],
        }])
        self.currency_obj.create([{
            'code': 'C4',
            'symbol': 'C4',
            'name': 'Currency 4',
            'rates': [('create', [{'rate': Decimal('40')}])],
        }])
        self.website_currencies = [c1, c2]
        self.en_us, = self.language_obj.search([('code', '=', 'en_US')])
        self.es_es, = self.language_obj.search([('code', '=', 'es_ES')])
        self.usd, = self.currency_obj.search([('code', '=', 'USD')])
        self.eur, = self.currency_obj.search([('code', '=', 'EUR')])
        locale_en_us, locale_es_es = self.nereid_website_locale_obj.create([{
            'code': 'en_US',
            'language': self.en_us,
            'currency': self.usd,
        }, {
            'code': 'es_ES',
            'language': self.es_es,
            'currency': self.eur,
        }])
        self.nereid_website_obj.create([{
            'name': 'localhost',
            'company': self.company,
            'application_user': USER,
            'default_locale': locale_en_us.id,
            'currencies': [('add', self.website_currencies)],
        }])
        self.templates = {
            'home.jinja': '{{ "hell" }}',
        }

    def test_0010_user(self):
        "Test for User display_name deprecated field"

        with Transaction().start(DB_NAME, USER, CONTEXT):
            self.setup_defaults()
            app = self.get_app()

            user, = self.nereid_user_obj.create([{
                "display_name": "Fulfil.io",
                "party": self.party.id,
                "company": self.company.id,
            }])
            assert user.name == "Fulfil.io"
            assert user.display_name == "Fulfil.io"


def suite():
    "Nereid test suite"
    test_suite = unittest.TestSuite()
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestUser)
    )
    return test_suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
