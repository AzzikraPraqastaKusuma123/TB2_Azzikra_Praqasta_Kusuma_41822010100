
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from buku import BukuDB

DATABASE_URL = "sqlite:///perpustakaan.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    BukuDB.metadata.create_all(engine)

def get_buku_by_id(buku_id):
    buku = session.query(BukuDB).filter(BukuDB.id == buku_id).first()
    return buku

def post_buku(buku):
    new_buku = BukuDB(
        judul=buku.judul,
        penulis=buku.penulis,
        penerbit=buku.penerbit,
        tahun_terbit=buku.tahun_terbit,
        konten=buku.konten,
        iktisar=buku.iktisar
    )
    session.add(new_buku)
    session.commit()
