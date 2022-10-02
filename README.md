# Cryptomus Python SDK

Python SDK module for working with the Cryptomus API

## Installation and connection

PyPi derictory - [Tap Here](https://pypi.org/project/cryptomus/)

Installation using [pip](https://pip.pypa.io/en/stable/installation/):

```bash
$ pip install cryptomus
```

## Documentation

**Methods for working with api**: https://doc.cryptomus.com/ <br>

## Authorization

`PAYOUT_KEY` or `PAYMENT_KEY`, also `MERCHANT_UUID` required to use SDK details in [documentation](https://doc.cryptomus.com/general/request).

```python
from cryptomus import Client

PAYMENT_KEY = 'uQ4LFWCBE3dT84uQnt7ycL7p9Wc...gMPI8lzKl7Ct2I43R6SSC3gVDS3rkGX'
MERCHANT_UUID = 'c26b80a8-9549-4b66-bb53-774f12809249'

payment = Client.payment(PAYMENT_KEY, MERCHANT_UUID)

```

```python
from cryptomus import Client

PAYMENT_KEY = 'uQ4LFWCBE3dT84uQnt7ycL7p9Wc...gMPI8lzKl7Ct2I43R6SSC3gVDS3rkGX'
MERCHANT_UUID = 'c26b80a8-9549-4b66-bb53-774f12809249'

payout = Client.payout(PAYMENT_KEY, MERCHANT_UUID)
```

## Payout methods

### Payout request

```python
data = {
    'amount': '15',
    'currency': 'USD',
    'network': 'TRON',
    'order_id': '555321',
    'address': 'TXguLRFtrAFrEDA17WuPfrxB84jVzJcNNV',
    'is_subtract': '1',
    'url_callback': 'https://example.com/callback'
}

result = payout.create(data)
```

Output:

```python
 {
    "uuid": "a7c0caec-a594-4aaa-b1c4-77d511857594",
    "amount": "15",
    "currency": "TRX",
    "network": "tron",
    "address": "TJ...",
    "txid": None,
    "status": "process",
    "is_final": False,
    "balance": 129
}
```

### Info

```python
data = {
    "uuid": "a7c0caec-a594-4aaa-b1c4-77d511857594",
    "order_id": "12345"
}

result = payout.info(data)
```

Output:

```python
{
  "uuid": "a7c0caec-a594-4aaa-b1c4-77d511857594",
  "amount": "3.00000000",
  "currency": "TRX",
  "network": "tron",
  "address": "TJZ...",
  "txid": None,
  "status": "process",
  "is_final": False,
  "balance": "129.00000000"
}
```

## Payment methods

### Payment services

```python
result = payment.services()
```

Output:

```python
{
  {                                #[0]
    "network": "TRON",
    "currency": "TRX",
    "is_available": True,
    "limit": {
      "min_amount": "1.00000000",
      "max_amount": "10.00000000"
    },
    "commission": {
      "fee_amount": "0.00",
      "percent": "0.00"
    }
  },
  { ... },                       #[1]
  { ... }                        #[2] and so on
}
```

### Payment create

```python
data = {
    'amount': '16',
    'currency': 'USD',
    'network': 'ETH',
    'order_id': '555123',
    'url_return': 'https://example.com/return',
    'url_callback': 'https://example.com/callback',
    'is_payment_multiple': False,
    'lifetime': '7200',
    'to_currency': 'ETH'
};

result = payment.create(data)
```

Output:

```python
{
  "uuid": "8b03432e-385b-4670-8d06-064591096795",
  "amount": "16",
  "order_id": "test_19",
  "currency": "TRX",
  "comments": None,
  "network": "tron",
  "address": "TW...",
  "from": None,
  "txid": None,
  "payment_status": "check",
  "url":  "https://pay.cryptomus.com/pay/8b03432e-385b-4670-8d06-064591096795",
  "expired_at": 1650980953,
  "status": "check",
  "is_final": False
}
```

### Info

```python
data = {
    "uuid": "a7c0caec-a594-4aaa-b1c4-77d511857594",
    "order_id": "12345"
}

result = payment.info(data)
```

Output:

```python
{
  "uuid": "8b03432e-385b-4670-8d06-064591096795",
  "order_id": "test_10",
  "amount": "16.00000000",
  "payment_amount": "0.000000",
  "currency": "TRX",
  "comments": None,
  "network": "tron",
  "address": "TW...",
  "from": None,
  "txid": None,
  "payment_status": "check",
  "url": "https://pay.cryptomus.com/pay/8b03432e-385b-4670-8d06-064591096795",
  "expired_at": 1650980953,
  "status": "paid",
  "is_final": True
}
```

### Payment History

```python
page = 3
result = payment.history(page)
```

Output:

```python
{
  "items": [
    {     #    [0]
      "uuid": "87094a43-5fe4-4629-b2fd-c37e8e2af76c",
      "order_id": "1650956609",
      "amount": "16.00000000",
      "payment_amount": "0.01200000",
      "currency": "ETH",
      "comments": None,
      "network": "eth",
      'address': '0xa30b82321a83922b792eef731d84b5d655449225', 
      'from': None, 
      'txid': None, 
      'payment_status': 'cancel', 
      'url': 'https://pay.cryptomus.com/pay/3347cd9e-4b63-4605-b269-c45b51d03f8d', 
      'expired_at': 1663952410, 
      'status': 'cancel', 
      'is_final': True},
    { ... }, # [1]
    { ... }, # [2] and so on ...
    ], 
  'paginate': {
      'count': 3, 
      'hasPages': False, 
      'nextCursor': None, 
      'previousCursor': None, 
      'perPage': 15}
}
```

### Balance

```python
result = payment.balance()
```

Output:

```python
[
    {
        "balance": {
            "merchant": [
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "24.00000000",
                    "currency_code": "TRX",
                    "balance_usd": "24.00",
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "MATIC",
                    "balance_usd": "0.00",
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "LTC",
                    "balance_usd": "0.00",
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "BUSD",
                    "balance_usd": "0.00",
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "1.00000000",
                    "currency_code": "BTC",
                    "balance_usd": "19328.00",
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "USDT",
                    "balance_usd": "0.00",
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "ETH",
                    "balance_usd": "0.00",
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "DASH",
                    "balance_usd": "0.00",
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "BNB",
                    "balance_usd": "0.00",
                },
            ],
            "user": [
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "BTC",
                    "balance_usd": None,
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "USDT",
                    "balance_usd": None,
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "LTC",
                    "balance_usd": None,
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "TRX",
                    "balance_usd": None,
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "ETH",
                    "balance_usd": None,
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "DASH",
                    "balance_usd": None,
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "MATIC",
                    "balance_usd": None,
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "BNB",
                    "balance_usd": None,
                },
                {
                    "uuid": "abcdabcd-abcd-1234-1234-abcdabcd",
                    "balance": "0.00000000",
                    "currency_code": "BUSD",
                    "balance_usd": None,
                },
            ],
        }
    }
]


```

### Resend notifications 

```python
data = {
    "uuid": "a7c0caec-a594-4aaa-b1c4-77d511857594",
    "order_id": "12345"
}

result = payment.resend_notification(data)
```

Output:

```python
bool(True)
```

### Wallet create

```python
data = {
    'network': 'TRON',
    'currency': 'USDT',
    'order_id': '5535321',
    'url_callback': 'https://example.com/callback'
}

result = payment.create_wallet(data)
```

Output:

```python
{
  "uuid": "9f64a7ce-...",
  "order_id": "24",
  "currency": "USDT",
  "network": "tron",
  "address": "TK8..."
}
```

### Exceptions

All methods can throw RequestBuilderException.

## Requirements

* **Python 3** or higher
* extension  **requests**
