import pytest
from typing import List

from bonus.models import LoyaltyModel, Order
from tests.utils import random_cards_generator


@pytest.fixture(scope="module")
def cards_fixture(django_db_blocker) -> List[LoyaltyModel]:
    objects_gen = []
    for i in range(30):
        objects_gen.append(LoyaltyModel(**random_cards_generator()))
    return LoyaltyModel.objects.bulk_create(objects_gen)

@pytest.fixture(scope="module")
def order_fixture(django_db_blocker) -> List[Order]:
    objects_gen = []
    for i in range(30):
        objects_gen.append(Order(**random_cards_generator()))
    return Order.objects.bulk_create(objects_gen)


class TestCardsModel:

    @pytest.fixture(autouse=True)
    def init_fixtures(self, cards_fixture):

        self.cards: List[LoyaltyModel] = cards_fixture

    def test_add_cards(self):
        pass