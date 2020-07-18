from flask import Response
import simplejson as json

from models.base import Object

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

def returnResponse(status, message, data):
    returnObj = Object()
    returnObj.message = message
    returnObj.data = data

    response = Response(
        response = json.dumps(returnObj.reprJSON(), cls=ComplexEncoder),
        status = status,
        mimetype = 'application/json'
    )

    return response