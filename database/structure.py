"""Module defining the structure of the database."""

import os
from sqlite3 import Connection

from sqlalchemy import (Column, ForeignKey, Integer, String, Float, Table, 
                        Boolean, create_engine, DATE, event)
from sqlalchemy.orm import declarative_base, relationship, backref, deferred

ENGINE = create_engine('sqlite:///test.db')
BASE = declarative_base()

@event.listens_for(ENGINE, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute('PRAGMA foreign_keys=ON;')
        cursor.close()


class Expense(BASE):
    """"""
    __tablename__ = 'expense'

    expense_id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    date = Column(DATE, nullable=False)
    amount = Column(Float, nullable=False)
    desc = Column(String(250))

    sub_items = relationship('ExpenseItem', backref='expense', passive_deletes=True)

class ExpenseItem(BASE):

    __tablename__ = 'expenseitem'
    item_id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    desc = Column(String(250))

    expense_id  = deferred(Column(Integer, ForeignKey('expense.expense_id', ondelete='CASCADE')))
    

if __name__ == '__main__':
    pass