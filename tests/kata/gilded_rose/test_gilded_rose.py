# -*- coding: utf-8 -*-

from coding_challenge.kata.gilded_rose.gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == 'foo'


def test_generic_quality_degradation_and_sell_in_decrement():
    regular_item = Item("Regular Item", 2, 6)
    gilded_rose = GildedRose([regular_item])

    gilded_rose.update_quality()
    assert regular_item.sell_in == 1
    assert regular_item.quality == 5

    gilded_rose.update_quality()
    assert regular_item.sell_in == 0
    assert regular_item.quality == 4

    # quality degrades twice as fast once sell_in date has passes
    gilded_rose.update_quality()
    assert regular_item.sell_in == -1
    assert regular_item.quality == 2

    gilded_rose.update_quality()
    assert regular_item.sell_in == -2
    assert regular_item.quality == 0


def test_generic_quality_never_more_than_50():
    regular_item = Item("Regular Item", 1, 51)
    gilded_rose = GildedRose([regular_item])

    gilded_rose.update_quality()
    assert regular_item.quality == 50


def test_generic_quality_never_negative():
    regular_item = Item("Regular Item", 0, 0)
    gilded_rose = GildedRose([regular_item])

    gilded_rose.update_quality()
    assert regular_item.quality == 0


def test_aged_brie_quality_increases_over_time():
    aged_brie = Item('Aged Brie', 2, 0)
    gilded_rose = GildedRose([aged_brie])

    gilded_rose.update_quality()
    assert aged_brie.sell_in == 1
    assert aged_brie.quality == 1

    gilded_rose.update_quality()
    assert aged_brie.sell_in == 0
    assert aged_brie.quality == 2

    gilded_rose.update_quality()
    assert aged_brie.sell_in == -1
    assert aged_brie.quality == 4

    gilded_rose.update_quality()
    assert aged_brie.sell_in == -2
    assert aged_brie.quality == 6


def test_sulfuras_never_ages_and_no_quality_degradation():
    sulfuras = Item('Sulfuras, Hand of Ragnaros', 1, 10)
    gilded_rose = GildedRose([sulfuras])

    gilded_rose.update_quality()
    assert sulfuras.sell_in == 1
    assert sulfuras.quality == 10

    gilded_rose.update_quality()
    assert sulfuras.sell_in == 1
    assert sulfuras.quality == 10


def test_backstage_passes_quality_rules():
    passes = Item('Backstage passes to a TAFKAL80ETC concert', 20, 0)
    gilded_rose = GildedRose([passes])

    gilded_rose.update_quality()
    assert passes.sell_in == 19
    assert passes.quality == 1

    passes.sell_in = 10
    gilded_rose.update_quality()
    assert passes.sell_in == 9
    assert passes.quality == 3

    passes.sell_in = 5
    gilded_rose.update_quality()
    assert passes.sell_in == 4
    assert passes.quality == 6

    passes.sell_in = 1
    gilded_rose.update_quality()
    assert passes.sell_in == 0
    assert passes.quality == 9

    gilded_rose.update_quality()
    assert passes.sell_in == -1
    assert passes.quality == 0


def test_conjured_quality_degradation_twice_as_fast():
    conjured = Item("Conjured Mana Cake", 2, 11)
    gilded_rose = GildedRose([conjured])

    gilded_rose.update_quality()
    assert conjured.sell_in == 1
    assert conjured.quality == 9

    gilded_rose.update_quality()
    assert conjured.sell_in == 0
    assert conjured.quality == 7

    gilded_rose.update_quality()
    assert conjured.sell_in == -1
    assert conjured.quality == 3

    gilded_rose.update_quality()
    assert conjured.sell_in == -2
    assert conjured.quality == 0