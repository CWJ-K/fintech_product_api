import time
from multiprocessing import Process

import pytest
import requests
import uvicorn
from fastapi.testclient import (
    TestClient,
)
from sqlalchemy import engine

from api.main import (
    app,
    get_mysql_financialdata_conn,
)

from api import config 
from loguru import logger

client = TestClient(app)


def test_get_mysql_financialdata_conn():
    logger.info('start test: test_get_mysql_financialdata_conn')
    conn = get_mysql_financialdata_conn()
    
    assert isinstance(
        conn, engine.Connection
    )


def test_read_root():
    logger.info('start test: test_read_root')
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "Hello": "World"
    }

def test_taiwan_stock_price():
    logger.info('start test: test_taiwan_stock_price')
    response = client.get(
        "/taiwan_stock_price",
        params=dict(
            stock_id="0050",
            start_date="2022-06-13",
            end_date="2022-06-13",
        ),
    )
    assert response.status_code == 200

    assert response.json() == {
        "data": [
            {
                "StockID": "0050",
                "TradeVolume": 18437079,
                "Transaction": 32400,
                "TradeValue": 2280313744,
                "Open": 124.1,
                "Max": 124.25,
                "Min": 123.45,
                "Close": 123.55,
                "Change": -3.55,
                "Date": "2022-06-13",
            }
        ]
    }


@pytest.fixture(scope="module")
def setUp():
    proc = Process(
        target=uvicorn.run,
        args=(app,),
        kwargs={
            "host": config.API_HOST,
            "port": config.API_PORT,
            "log_level": "info",
        },
        daemon=True,
    )
    proc.start()
    time.sleep(1)
    return 1


def test_index(setUp):
    logger.info('start test: test_index')
    response = requests.get(
        f"http://{config.API_HOST}:{config.API_PORT}"
    )
    assert response.json() == {
        "Hello": "World"
    }


def test_TaiwanStockPriceID(setUp):
    logger.info('start test: test_TaiwanStockPriceID')
    payload = {
        "stock_id": "0050",
        "start_date": "2022-06-13",
        "end_date": "2022-06-13",
    }

    res = requests.get(
        f"http://{config.API_HOST}:{config.API_PORT}/taiwan_stock_price",
        params=payload,
    )
    resp = res.json()["data"]
    assert resp == [
        {
            "StockID": "0050",
            "TradeVolume": 18437079,
            "Transaction": 32400,
            "TradeValue": 2280313744,
            "Open": 124.1,
            "Max": 124.25,
            "Min": 123.45,
            "Close": 123.55,
            "Change": -3.55,
            "Date": "2022-06-13",
        }
    ]