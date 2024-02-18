##########################################################################
## Company: AgileStock
## Engineer(s): Robert Howell
##
## Create Date:    12/3/2023
## Project Name:    AgileStock
## Target Devices:    Web
## Tool versions:    Python 3.11
## Description:    Flask's entry point.
##
## Dependencies:
##   -module(s):
##      os
##      AgileStockWeb
##
##   -packages(s):
##      blinker==1.7.0
##      click==8.1.7
##      colorama==0.4.6
##      Flask==3.0.0
##      itsdangerous==2.1.2
##      Jinja2==3.1.2
##      MarkupSafe==2.1.3
##      PyMySQL==1.1.0
##      Werkzeug==3.0.1
##
## Revision: 1.0 - File Created
## Additional Comments: This script runs the AgileStockWeb application using a development server.
##
##########################################################################

from os import environ
from AgileStockWeb import app

if __name__ == "__main__":
    HOST = environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(environ.get("SERVER_PORT", "7000"))
        # TODO - If there's an error:
        # "An attempt was made to access a socket in a way forbidden by its access permissions"
        # change the port number.
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=False)
