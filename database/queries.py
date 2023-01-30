"""Module containing Queries to interact with the database."""

import os
from typing import List

from sqlalchemy import delete
from sqlalchemy.orm import sessionmaker, Session

from structure import Expense, ExpenseItem, ENGINE, BASE



class Queries:

    def init_db(self):
        if not os.path.exists(os.path.join(os.getcwd(), ENGINE.url.database)):
            BASE.metadata.create_all(ENGINE)

    def add_expense(self, records:List[Expense]) -> None:
        s = self._create_session()
        with s:
            s.add_all(records)
            s.commit()

    def delete_expense(self, expense_id:int) -> None:
        s = self._create_session()
        with s:
            s.execute(delete(Expense).where(Expense.expense_id == expense_id))
            s.commit()

    def update_items(self, expense_id: int, records:List[ExpenseItem]) -> None:
        s = self._create_session()
        with s:
            thing = s.query(Expense).filter(Expense.expense_id == expense_id).first()
            thing.sub_items = records
            
            s.commit()

    def _create_session(self) -> Session:
        """Return an active session with the database."""
        session = sessionmaker(ENGINE)
        return session()

if __name__ == '__main__':
    Queries().delete_expense(1)