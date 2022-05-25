from flask import Blueprint,request,render_template,redirect,url_for,flash
from .models import TBLAnggota
from .__init__ import db

anggota = Blueprint('anggota', __name__)

@anggota.route('/anggota', methods=['GET', 'POST'])
def add_anggota():
    if request.method=='GET':
        anggota = TBLAnggota.query.all()
        return render_template('anggota.html',title='Anggota',anggota=anggota)
    else:
    
        no_anggota = request.form.get('no_anggota')
        nama_anggota = request.form.get('nama_anggota')
        simpanan_wajib = request.form.get('simpanan_wajib')
        simpanan_pokok = request.form.get('simpanan_pokok')
        saldo = request.form.get('saldo')

        new_anggota = TBLAnggota(nama=nama_anggota,wajib=int(simpanan_wajib),pokok=int(simpanan_pokok),saldo=int(saldo),no_anggota=int(no_anggota))
        db.session.add(new_anggota)
        db.session.commit()

    return redirect(url_for('anggota.add_anggota'))

@anggota.route('/anggota/edit/<int:id>', methods=['GET', 'POST'])
def update_anggota(id):
    if request.method=='GET':
        return render_template('anggota_update.html',title='Anggota')
    else:
        anggota = TBLAnggota.query.filter_by(no_anggota=id).first()
    
        anggota.no_anggota = int(request.form.get('no_anggota'))
        anggota.nama_anggota = request.form.get('nama_anggota')
        anggota.simpanan_wajib = int(request.form.get('simpanan_wajib'))
        anggota.simpanan_pokok = int(request.form.get('simpanan_pokok'))
        anggota.saldo = int(request.form.get('saldo'))

        db.session.commit()

    return redirect(url_for('anggota.add_anggota'))

@anggota.route('/anggota/hapus/<int:id>', methods=['GET', 'POST'])
def delete_anggota(id):

    anggota = TBLAnggota.query.filter_by(no_anggota=id).first()
    db.session.delete(anggota)
    db.session.commit()

    return redirect(url_for('anggota.add_anggota'))

    

