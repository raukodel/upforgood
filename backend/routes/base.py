from flask import jsonify, Response
import simplejson as json

def returnResponse(status, data):
    response = Response(
        response=json.dumps(data.__dict__),
        status=status,
        mimetype='application/json'
    )

    return response