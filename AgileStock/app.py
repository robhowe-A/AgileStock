"""
This script runs the AgileStockWeb application using a development server.
"""

from os import environ
from AgileStockWeb import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '7000'))
        #TODO - If there's an error: 
        #"An attempt was made to access a socket in a way forbidden by its access permissions"
        # change the port number.
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
