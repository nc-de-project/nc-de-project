from src.transformation_lambda.transformation_lambda import (
    format_fact_sales_order,
)  # noqa E501
import logging

logger = logging.getLogger("TestLogger")
logger.setLevel(logging.INFO)


def test_should_split_the_date_and_time():
    json = {
        "sales_order": [
            {
                "sales_order_id": 1,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 9,
                "staff_id": 16,
                "counterparty_id": 18,
                "units_sold": 84754,
                "unit_price": 2.43,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-10",
                "agreed_payment_date": "2022-11-03",
                "agreed_delivery_location_id": 4,
            }
        ]
    }
    expected = [
        [
            1,
            "2022-11-03",
            "14:20:52",
            "2022-11-03",
            "14:20:52",
            16,
            18,
            84754,
            2.43,
            3,
            9,
            "2022-11-03",
            "2022-11-10",
            4,
        ]
    ]
    assert format_fact_sales_order(json) == expected


def test_should_work_for_multiple_dicts():
    json = {
        "sales_order": [
            {
                "sales_order_id": 1,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 9,
                "staff_id": 16,
                "counterparty_id": 18,
                "units_sold": 84754,
                "unit_price": 2.43,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-10",
                "agreed_payment_date": "2022-11-03",
                "agreed_delivery_location_id": 4,
            },
            {
                "sales_order_id": 2,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 3,
                "staff_id": 19,
                "counterparty_id": 8,
                "units_sold": 42972,
                "unit_price": 3.94,
                "currency_id": 2,
                "agreed_delivery_date": "2022-11-07",
                "agreed_payment_date": "2022-11-08",
                "agreed_delivery_location_id": 8,
            },
            {
                "sales_order_id": 3,
                "created_at": "2022-11-03T14:20:52.188",
                "last_updated": "2022-11-03T14:20:52.188",
                "design_id": 4,
                "staff_id": 10,
                "counterparty_id": 4,
                "units_sold": 65839,
                "unit_price": 2.91,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-06",
                "agreed_payment_date": "2022-11-07",
                "agreed_delivery_location_id": 19,
            },
        ]
    }
    expected = [
        [
            1,
            "2022-11-03",
            "14:20:52",
            "2022-11-03",
            "14:20:52",
            16,
            18,
            84754,
            2.43,
            3,
            9,
            "2022-11-03",
            "2022-11-10",
            4,
        ],
        [
            2,
            "2022-11-03",
            "14:20:52",
            "2022-11-03",
            "14:20:52",
            19,
            8,
            42972,
            3.94,
            2,
            3,
            "2022-11-08",
            "2022-11-07",
            8,
        ],
        [
            3,
            "2022-11-03",
            "14:20:52",
            "2022-11-03",
            "14:20:52",
            10,
            4,
            65839,
            2.91,
            3,
            4,
            "2022-11-07",
            "2022-11-06",
            19,
        ],
    ]

    assert format_fact_sales_order(json) == expected


def test_should_not_mutate_original_data():
    json = {
        "sales_order": [
            {
                "sales_order_id": 1,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 9,
                "staff_id": 16,
                "counterparty_id": 18,
                "units_sold": 84754,
                "unit_price": 2.43,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-10",
                "agreed_payment_date": "2022-11-03",
                "agreed_delivery_location_id": 4,
            },
            {
                "sales_order_id": 2,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 3,
                "staff_id": 19,
                "counterparty_id": 8,
                "units_sold": 42972,
                "unit_price": 3.94,
                "currency_id": 2,
                "agreed_delivery_date": "2022-11-07",
                "agreed_payment_date": "2022-11-08",
                "agreed_delivery_location_id": 8,
            },
            {
                "sales_order_id": 3,
                "created_at": "2022-11-03T14:20:52.188",
                "last_updated": "2022-11-03T14:20:52.188",
                "design_id": 4,
                "staff_id": 10,
                "counterparty_id": 4,
                "units_sold": 65839,
                "unit_price": 2.91,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-06",
                "agreed_payment_date": "2022-11-07",
                "agreed_delivery_location_id": 19,
            },
        ]
    }
    format_fact_sales_order(json)
    expected = {
        "sales_order": [
            {
                "sales_order_id": 1,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 9,
                "staff_id": 16,
                "counterparty_id": 18,
                "units_sold": 84754,
                "unit_price": 2.43,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-10",
                "agreed_payment_date": "2022-11-03",
                "agreed_delivery_location_id": 4,
            },
            {
                "sales_order_id": 2,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 3,
                "staff_id": 19,
                "counterparty_id": 8,
                "units_sold": 42972,
                "unit_price": 3.94,
                "currency_id": 2,
                "agreed_delivery_date": "2022-11-07",
                "agreed_payment_date": "2022-11-08",
                "agreed_delivery_location_id": 8,
            },
            {
                "sales_order_id": 3,
                "created_at": "2022-11-03T14:20:52.188",
                "last_updated": "2022-11-03T14:20:52.188",
                "design_id": 4,
                "staff_id": 10,
                "counterparty_id": 4,
                "units_sold": 65839,
                "unit_price": 2.91,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-06",
                "agreed_payment_date": "2022-11-07",
                "agreed_delivery_location_id": 19,
            },
        ]
    }
    assert json == expected


def test_should_remove_duplicates():
    json = {
        "sales_order": [
            {
                "sales_order_id": 1,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 9,
                "staff_id": 16,
                "counterparty_id": 18,
                "units_sold": 84754,
                "unit_price": 2.43,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-10",
                "agreed_payment_date": "2022-11-03",
                "agreed_delivery_location_id": 4,
            },
            {
                "sales_order_id": 2,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 3,
                "staff_id": 19,
                "counterparty_id": 8,
                "units_sold": 42972,
                "unit_price": 3.94,
                "currency_id": 2,
                "agreed_delivery_date": "2022-11-07",
                "agreed_payment_date": "2022-11-08",
                "agreed_delivery_location_id": 8,
            },
            {
                "sales_order_id": 3,
                "created_at": "2022-11-03T14:20:52.188",
                "last_updated": "2022-11-03T14:20:52.188",
                "design_id": 4,
                "staff_id": 10,
                "counterparty_id": 4,
                "units_sold": 65839,
                "unit_price": 2.91,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-06",
                "agreed_payment_date": "2022-11-07",
                "agreed_delivery_location_id": 19,
            },
            {
                "sales_order_id": 3,
                "created_at": "2022-11-03T14:20:52.188",
                "last_updated": "2022-11-03T14:20:52.188",
                "design_id": 4,
                "staff_id": 10,
                "counterparty_id": 4,
                "units_sold": 65839,
                "unit_price": 2.91,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-06",
                "agreed_payment_date": "2022-11-07",
                "agreed_delivery_location_id": 19,
            },
        ]
    }
    expected = [
        [
            1,
            "2022-11-03",
            "14:20:52",
            "2022-11-03",
            "14:20:52",
            16,
            18,
            84754,
            2.43,
            3,
            9,
            "2022-11-03",
            "2022-11-10",
            4,
        ],
        [
            2,
            "2022-11-03",
            "14:20:52",
            "2022-11-03",
            "14:20:52",
            19,
            8,
            42972,
            3.94,
            2,
            3,
            "2022-11-08",
            "2022-11-07",
            8,
        ],
        [
            3,
            "2022-11-03",
            "14:20:52",
            "2022-11-03",
            "14:20:52",
            10,
            4,
            65839,
            2.91,
            3,
            4,
            "2022-11-07",
            "2022-11-06",
            19,
        ],
    ]
    assert format_fact_sales_order(json) == expected


def test_should_log_a_warning_if_key_is_missing(caplog):
    with caplog.at_level(logging.ERROR):
        json = {"sales_order": [{"spam": "eggs"}]}
        format_fact_sales_order(json)
        assert "KeyError: missing key 'created_at'." in caplog.text
