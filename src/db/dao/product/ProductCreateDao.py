from src.db.dao.BaseCrudDao import BaseCrudDao
from src.util.QueryStringFile import querycreatetableproduct


class ProductCreateDao(BaseCrudDao):

    def create_table(self):
        self.get_cursor().execute(querycreatetableproduct)
