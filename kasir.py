from flask import Blueprint,request,render_template,redirect,url_for,flash
from .models import TBLKasir
from .__init__ import db

kasir = Blueprint('kasir', __name__)

@kasir.route('/kasir', methods=['GET', 'POST'])
def add_kasir():
    if request.method=='GET':
        kasir = TBLKasir.query.all()
        return render_template('kasir.html',title='kasir',kasir=kasir)
    else:
    
        kode_kasir = request.form.get('kode_kasir')
        nama_kasir = request.form.get('nama_kasir')
        password_kasir = request.form.get('password_kasir')
      
        new_kasir = TBLKasir(nama_kasir=nama_kasir,kode_kasir=kode_kasir,password_kasir=password_kasir)
        db.session.add(new_kasir)
        db.session.commit()

    return redirect(url_for('kasir.add_kasir'))

@kasir.route('/kasir/edit/<int:id>', methods=['GET', 'POST'])
def update_kasir(id):
    if request.method=='GET':
        return render_template('kasir_update.html',title='kasir')
    else:
        kasir = TBLKasir.query.filter_by(kode_kasir=id).first()
            
        kasir.nama_kasir = request.form.get('nama_kasir')
        kasir.password_kasir = int(request.form.get('password_kasir'))
        kasir.kode_kasir = int(id)

        db.session.commit()

    return redirect(url_for('kasir.add_kasir'))

@kasir.route('/kasir/hapus/<int:id>', methods=['GET', 'POST'])
def delete_kasir(id):

    kasir = TBLKasir.query.filter_by(kode_kasir=id).first()
    db.session.delete(kasir)
    db.session.commit()

    return redirect(url_for('kasir.add_kasir'))

    

