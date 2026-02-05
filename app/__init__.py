import json
from flask import Flask

app = Flask(__name__)

# Registra um filtro para o Jinja2 formatar JSON bonito
@app.template_filter('to_pretty_json')
def to_pretty_json(value):
    return json.dumps(value, indent=4, sort_keys=True)

from app import routes