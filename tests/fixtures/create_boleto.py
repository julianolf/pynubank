import pytest


@pytest.fixture()
def create_boleto_return():
    return {
        "data": {
            "viewer": {
                "id": "123123123"
            },
            "createTransferInBoleto": {
                "boleto": {
                    "id": "123123123",
                    "dueDate": "2020-06-16",
                    "barcode": "123123132123123123123",
                    "readableBarcode": "123131321231231.2313212312.2131231.21332123",
                    "amount": 1231.23
                }
            }
        }
    }
