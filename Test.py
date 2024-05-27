from flask import Flask, render_template, request

from flask import jsonify
from flask import jsonify

import atexit

app = Flask(__name__)

@app.route('/') #Render html page

def index():

    return render_template('123.html')

def cleanup(): #clean up GPIO pins

    print("Cleaning up GPIO")


if __name__ == '__main__':

    try:

        app.run(host='0E.0.0.0', port='5000', debug=True)

    except KeyboardInterrupt:

        print('Interrupted')

    finally:

        # Register the cleanup function

        atexit.register(cleanup)


