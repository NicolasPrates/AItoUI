from app import app

from flask import render_template


@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template("admin/dashboard.html")


@app.route('/admin/profile')
def admin_profile():
    return "Admin Profile"


@app.route('/api')
def admin_json():
    return {
        'no_of_neurons': 3,
        'number of conections': 4,
        'name_of_the_network': "nome"
    }
