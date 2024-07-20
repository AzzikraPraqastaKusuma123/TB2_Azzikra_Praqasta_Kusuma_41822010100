-- create_table.sql
CREATE TABLE buku (
    id SERIAL PRIMARY KEY,
    judul VARCHAR(255) NOT NULL,
    penulis VARCHAR(255) NOT NULL,
    penerbit VARCHAR(255),
    tahun_terbit INT,
    konten TEXT,
    iktisar TEXT
);
