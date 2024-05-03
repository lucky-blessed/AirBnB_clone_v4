!#/usr/bin/python3
"""API connector app.py"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/vi/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown_appcontent(code):
    """Teardown_appcontent"""
    storage.close()

    @app.errorhandler(404)
    def page_not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    if __name__ == "__main__":
        app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
                port=int(os.getenv('HBNB_API_PORT', '5000')),
                threded=True)
