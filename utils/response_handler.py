from flask import jsonify

def success_response(data, status_code=200):
    return jsonify({"status": "success", "data": data}), status_code

def error_response(message, status_code=400, additional_data=None):
    response = {"status": "error", "message": message}
    if additional_data:
        response.update(additional_data)
    return jsonify(response), status_code