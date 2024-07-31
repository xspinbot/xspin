from db.repository import BaseRepository
from db.schemas import ReferallsTable


class ReferallsTableRepository(BaseRepository):
    table = ReferallsTable