# -*- coding: utf-8 -*-
from collections import namedtuple
from enum import Enum
from typing import List


class ItemName(str, Enum):
    aged_brie = 'Aged Brie'
    backstage_passes = 'Backstage passes to a TAFKAL80ETC concert'
    sulfuras = 'Sulfuras, Hand of Ragnaros'
    conjured = 'Conjured Mana Cake'


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemQualityParameter:
    lower_limit: int = 0
    modifier: int
    upper_limit: int = 50

    @staticmethod
    def get_quality_parameter(item: Item) -> 'ItemQualityParameter':
        parameter = ItemQualityParameter()
        parameter.lower_limit = 0
        parameter.upper_limit = 50

        if item.name == ItemName.aged_brie:
            parameter.modifier = ItemQualityParameter.get_aged_brie_modifier(item)
        elif item.name == ItemName.sulfuras:
            parameter.modifier = ItemQualityParameter.get_sulfuras_modifier(item)
            parameter.lower_limit = 80
            parameter.upper_limit = 80
        elif item.name == ItemName.backstage_passes:
            parameter.modifier = ItemQualityParameter.get_backstage_passes_modifier(item)
        elif item.name == ItemName.conjured:
            parameter.modifier = ItemQualityParameter.get_conjured_item_modifier(item)
        else:
            parameter.modifier = ItemQualityParameter.get_generic_item_modifier(item)
        return parameter

    @staticmethod
    def get_generic_item_modifier(item: Item) -> int:
        if item.sell_in < 0:
            return -2
        return -1

    @staticmethod
    def get_aged_brie_modifier(item: Item) -> int:
        if item.sell_in < 0:
            return 2
        return 1

    @staticmethod
    def get_sulfuras_modifier(item: Item) -> int:
        return 0

    @staticmethod
    def get_backstage_passes_modifier(item: Item) -> int:
        if item.sell_in < 0:
            return item.quality * -1
        if item.sell_in < 6:
            return 3
        if item.sell_in < 11:
            return 2
        return 1

    @staticmethod
    def get_conjured_item_modifier(item: Item) -> int:
        if item.sell_in < 0:
            return -4
        return -2


class GildedRose(object):

    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != ItemName.sulfuras:
                item.sell_in = item.sell_in - 1

            parameter = ItemQualityParameter.get_quality_parameter(item)
            item.quality += parameter.modifier

            if item.quality > parameter.upper_limit:
                item.quality = parameter.upper_limit
            elif item.quality < parameter.lower_limit:
                item.quality = parameter.lower_limit
