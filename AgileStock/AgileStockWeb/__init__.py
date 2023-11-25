"""
The flask application package.
"""

#Before running, ensure Python 3.11 is installed.
#A command can be run to begin the development server
#    cd .\pywebtwo
#    py -m runserver
#
#
# OUTPUT:
#    PS C:\Dev\python\PythonWebTESTFlaskWebProject1\pywebtwo> py -m runserver
#     * Serving Flask app 'FlaskWebProject1'
#     * Debug mode: off
#    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#     * Running on http://localhost:7000
#    Press CTRL+C to quit


from flask import Flask

app = Flask(__name__)

import AgileStockWeb.views
