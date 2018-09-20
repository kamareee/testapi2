
from flask_restful import Api, Resource, reqparse


class UserData(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('serviceID', type=str)
        json = parser.parse_args()
        service_id = json.get('serviceID')

        final_response = {'serviceID': str(service_id),
                          'Message': 'Got the service ID {}'.format(service_id)}

        return {"status": 'OK', "body": final_response}
