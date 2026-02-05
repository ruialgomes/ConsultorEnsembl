from flask import render_template, request, jsonify
from app import app
from app.services import EnsemblService

@app.route('/', methods=['GET', 'POST'])
def index():
    variant_data = None
    if request.method == 'POST':
        rsid = request.form.get('rsid').strip()
        if rsid:
            variant_data = EnsemblService.get_variant_data(rsid)
    return render_template('index.html', variant=variant_data)

@app.route('/api/variant/<rsid>')
def api_variant(rsid):
    data = EnsemblService.get_variant_data(rsid)
    return jsonify(data)