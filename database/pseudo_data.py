"""Module for creating fake data"""
from __future__ import annotations
import random
from typing import List
from datetime import datetime
import time

from faker import Faker
from faker.providers import BaseProvider

from structure import Expense, ExpenseItem
from queries import Queries


class PrepareFaker:

    class FakeCategory(BaseProvider):
        options = ['Food', 'Gas', 'Loans', 'Investment']
        def category(self):
            return random.choice(self.options)

    class FakeDate(BaseProvider):
        def random_date(self, seed):
            random.seed(seed)
            d = random.randint(1, int(time.time()))
            return datetime.fromtimestamp(d)

    def get_prepped_faker(self) -> Faker:
        fake = Faker()
        fake.add_provider(self.FakeCategory)
        fake.add_provider(self.FakeDate)
        return fake


class FakeExpense:
    def gen_fake(self, desired_records = 1) -> List[Expense]:
        fake = PrepareFaker().get_prepped_faker()
        records = []
        for _ in range(desired_records):
            data = Expense(
                category = fake.category(),
                date = fake.random_date(None),
                amount = fake.pydecimal(3, 2),
                desc = fake.text(),
            )
            records.append(data)
        
        return records

class FakeSubItem:
    def gen_fake(self, desired_records = 1) -> List[ExpenseItem]:
        fake = PrepareFaker().get_prepped_faker()
        records = []
        for _ in range(desired_records):
            data = ExpenseItem(
                category = fake.category(),
                amount = fake.pydecimal(3, 2),
                desc = fake.text(),
                                 
            )
            records.append(data)
        
        return records

# data that will be collected

# Expense category
# expense amount
# expense description
# sub-class

def create_fake_records():
    Queries().init_db()
    Queries().add_expense(FakeExpense().gen_fake(3))
    Queries().update_items(1, FakeSubItem().gen_fake(3))

if __name__ == '__main__':
    create_fake_records()
    pass