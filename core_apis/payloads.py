from flask_restx import reqparse




# Server Test
server_test = reqparse.RequestParser()
server_test.add_argument('arg', type=str, help='Argument')

#Code
askGPT = reqparse.RequestParser()
askGPT.add_argument('code', type=str, help='Incomplete Code', required=True)