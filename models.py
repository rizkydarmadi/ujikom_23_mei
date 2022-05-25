from flask_login import UserMixin
from .__init__ import db

i = 0
def mydefault():
    global i
    i += 1
    return i


class TBLAnggota(UserMixin, db.Model):
    no_anggota = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    nama = db.Column(db.String(60))
    wajib = db.Column(db.Integer)
    pokok = db.Column(db.Integer)
    saldo = db.Column(db.Integer)

    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(100))
    no_anggota = db.Column(db.Integer,db.ForeignKey(TBLAnggota.no_anggota),nullable=False)

class TBLSimpan(UserMixin, db.Model):
    no_simpan = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.DateTime(100),nullable=False)
    no_anggota = db.Column(db.Integer,db.ForeignKey(TBLAnggota.no_anggota),nullable=False)
    jml_simpan = db.Column(db.Integer)
    kode_kasir = db.Column(db.Integer)

class TBLKasir(UserMixin, db.Model):
    kode_kasir = db.Column(db.Integer, primary_key=True)
    nama_kasir = db.Column(db.String(60))
    password_kasir = db.Column(db.String(100))

class TBLPinjam(UserMixin, db.Model):
    no_pinjam = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.DateTime(100),nullable=False)
    no_anggota = db.Column(db.Integer,db.ForeignKey(TBLAnggota.no_anggota),nullable=False)
    jml_pinjam = db.Column(db.Integer)
    kode_kasir = db.Column(db.Integer,db.ForeignKey(TBLKasir.kode_kasir),nullable=False)
    