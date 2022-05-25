from flask import Blueprint,request,render_template,redirect,url_for,flash
from .models import TBLPinjam, TBLPinjam
from .__init__ import db
from datetime import date


pinjam = Blueprint('pinjam', __name__)

@pinjam.route('/pinjam', methods=['GET', 'POST'])
def add_pinjam():
    if request.method=='GET':
        pinjam = TBLPinjam.query.all()
        return render_template('pinjam.html',title='pinjam',pinjam=pinjam)
    else:
    
        no_pinjam = request.form.get('no_pinjam')
        no_anggota = request.form.get('no_anggota')
        jumlah_pinjam = request.form.get('jumlah_pinjam')
      

        new_pinjam = TBLPinjam(no_pinjam=int(no_pinjam),no_anggota=int(no_anggota),jml_pinjam=int(jumlah_pinjam),tanggal=date.today(),kode_kasir=123)
        db.session.add(new_pinjam)
        db.session.commit()


    return redirect(url_for('pinjam.add_pinjam'))

@pinjam.route('/pinjam/edit/<int:id>', methods=['GET', 'POST'])
def update_pinjam(id):
    if request.method=='GET':
        return render_template('pinjam_update.html',title='pinjam')
    else:
        pinjam = TBLPinjam.query.filter_by(no_pinjam=id).first()
    
        pinjam.no_pinjam = int(request.form.get('no_pinjam'))
        pinjam.nama_pinjam = request.form.get('nama_pinjam')
        pinjam.pinjaman_wajib = int(request.form.get('pinjaman_wajib'))
        pinjam.pinjaman_pokok = int(request.form.get('pinjaman_pokok'))
        pinjam.saldo = int(request.form.get('saldo'))

        db.session.commit()

    return redirect(url_for('pinjam.add_pinjam'))

@pinjam.route('/pinjam/hapus/<int:id>', methods=['GET', 'POST'])
def delete_pinjam(id):

    pinjam = TBLPinjam.query.filter_by(no_pinjam=id).first()
    db.session.delete(pinjam)
    db.session.commit()

    return redirect(url_for('pinjam.add_pinjam'))

    

