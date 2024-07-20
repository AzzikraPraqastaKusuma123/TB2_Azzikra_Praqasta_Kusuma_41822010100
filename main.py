
import logging
from fastapi import HTTPException
from buku import Buku
from database_setup import get_buku_by_id, post_buku, create_tables

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

create_tables()

try:
    buku = get_buku_by_id(1)
    if buku:
        logger.info(f"Buku ditemukan: {buku.judul} by {buku.penulis}")
    else:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
except HTTPException as e:
    logger.error(f"HTTPException: {e.detail}")
