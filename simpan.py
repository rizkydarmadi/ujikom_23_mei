from flask import Blueprint,request,render_template,redirect,url_for,flash
from .models import TBLSimpan
from .__init__ import db
from datetime import date

simpan = Blueprint('simpan', __name__)

@simpan.route('/simpan', methods=['GET', 'POST'])
def add_simpan():
    if request.method=='GET':
        simpan = TBLSimpan.query.all()
        return render_template('simpan.html',title='simpan',simpan=simpan)
    else:
    
        no_simpan = request.form.get('no_simpan')
        no_anggota = request.form.get('no_anggota')
        jumlah_simpan = request.form.get('jumlah_simpan')
      
        new_simpan = TBLSimpan(no_simpan=int(no_simpan),no_anggota=int(no_anggota),jml_simpan=int(jumlah_simpan),tanggal=date.today(),kode_kasir=123)
        db.session.add(new_simpan)
        db.session.commit()

    return redirect(url_for('simpan.add_simpan'))

@simpan.route('/simpan/edit/<int:id>', methods=['GET', 'POST'])
def update_simpan(id):
    if request.method=='GET':
        return render_template('simpan_update.html',title='simpan')
    else:
        simpan = TBLSimpan.query.filter_by(no_simpan=id).first()
            
        simpan.no_anggota = request.form.get('no_anggota')
        simpan.jml_simpan = int(request.form.get('jumlah_simpan'))

        db.session.commit()

    return redirect(url_for('simpan.add_simpan'))

@simpan.route('/simpan/hapus/<int:id>', methods=['GET', 'POST'])
def delete_simpan(id):

    simpan = TBLSimpan.query.filter_by(no_simpan=id).first()
    db.session.delete(simpan)
    db.session.commit()

    return redirect(url_for('simpan.add_simpan'))

    

