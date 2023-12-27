from flask import Flask,request, jsonify

import Hubtel.hubtel

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! v2'

@app.route('/process_payment', methods=['POST'])
def process_payment():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Access the required fields
        total_amount = data.get('totalAmount')
        description = data.get('description')
        callback_url = data.get('callbackUrl')
        return_url = data.get('returnUrl')
        cancellation_url = data.get('cancellationUrl')
        merchant_account_number = data.get('merchantAccountNumber')
        client_reference = data.get('clientReference')


        result = Hubtel.hubtel.execute_payment(total_amount,description,callback_url,return_url,cancellation_url,merchant_account_number,client_reference)

        # Return a response (you can customize this based on your needs)
        response_data = {'status': 'success', 'message': 'Payment processed successfully'}
        return jsonify(result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        response_data = {'status': 'error', 'message': 'An error occurred'}
        return jsonify(response_data), 500  # Return a 500 Internal Server Error status

@app.route('/payment_status', methods=['POST'])
def payment_status():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Access the required fields
        pos_sales_id = data.get('pos_sales_id')
        clientReference = data.get('clientReference')



        result = Hubtel.hubtel.checkStatus(pos_sales_id,clientReference)

        # Return a response (you can customize this based on your needs)
        response_data = {'status': 'success', 'message': 'Payment processed successfully'}
        return jsonify(result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        response_data = {'status': 'error', 'message': 'An error occurred'}
        return jsonify(response_data), 500  # Return a 500 Internal Server Error status




if __name__ == '__main__':
    app.run()
