# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone

import datetime

from getriddb.models import Inventoryitem

# Create your tests here.

class InventoryitemMethodTests(TestCase):

    def test_customerpayout_never_negative(self):
        """
        self.customerpayout = float(self.item_profit/2) should be half of the item profit
        """
        #time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
