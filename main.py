from flask import Blueprint, render_template
from .__init__ import create_app,db
from flask_login import login_required

main = Blueprint('main',__name__)

@main.route('/')
@login_required
def index():
	return render_template('anggota.html')

app = create_app()
if __name__ == '__main__':
	db.create_all(app=create_app())
	app.run(debug=True)