#!/usr/bin/env python3

from flask import render_template
import connexion

# Create application instance
app = connexion.App(__name__, specification_dir='./')

# load configuration of endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    """
    return 'Welcome.'


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)