import json
import pytest
import sys
import os
from models import db, app  
from models.account import Account

ACCOUNT_DATA = {}

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Configura la base de datos antes y después de todas las pruebas"""
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()

class TestAccountModel:
    """Modelo de Pruebas de Cuenta"""

    @classmethod
    def setup_class(cls):
        """Cargar los datos necesarios para las pruebas"""
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)
        print(f"ACCOUNT_DATA cargado: {ACCOUNT_DATA}")

    @classmethod
    def teardown_class(cls):
        """Desconectar de la base de datos"""
        print("Finalizó TestAccountModel")

    def setup_method(self):
        """Truncar las tablas antes de cada prueba"""
        with app.app_context():
            db.session.query(Account).delete()
            db.session.commit()

    def teardown_method(self):
        """Eliminar la sesión después de cada prueba"""
        with app.app_context():
            db.session.remove()

    def test_create_an_account(self):
        """Probar la creación de una sola cuenta"""
        data = ACCOUNT_DATA[0]
        with app.app_context():
            account = Account(**data)
            account.create()
            assert len(Account.all()) == 1

    def test_create_all_accounts(self):
        """Probar la creación de múltiples cuentas"""
        with app.app_context():
            for data in ACCOUNT_DATA:
                account = Account(**data)
                account.create()
            assert len(Account.all()) == len(ACCOUNT_DATA)
