import requests
import json

def execute_payment(total_amount, description, callback_url, return_url, cancellation_url, merchant_account_number, client_reference):

    url = "https://payproxyapi.hubtel.com/items/initiate"

    payload = {
        "totalAmount": total_amount,
        "description": description,
        "callbackUrl": callback_url,
        "returnUrl": return_url,
        "cancellationUrl": cancellation_url,
        "merchantAccountNumber": merchant_account_number,
        "clientReference": client_reference
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic d21yOFlXcjphYTEyOTYzMDkyY2Y0MWI2YTQxNjFlOGQyYWMxNDhhYw=="
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    return response.text


def checkStatus(pos_sales_id,clientReference):
    url = f"https://api-txnstatus.hubtel.com/transactions/{pos_sales_id}/status?clientReference={clientReference}"

    headers = {
        "accept": "application/json",
        "authorization": "Basic d21yOFlXcjphYTEyOTYzMDkyY2Y0MWI2YTQxNjFlOGQyYWMxNDhhYw=="
    }

    response = requests.get(url, headers=headers)

    print(response.text)
    return response.text