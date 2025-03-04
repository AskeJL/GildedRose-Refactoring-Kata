# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        brie = "Aged Brie"
        backstagepass = "Backstage passes to a TAFKAL80ETC concert"
        HandOfRagnaros = "Sulfuras, Hand of Ragnaros"
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros":
                updateRegularItem(item)
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        updateBackstagepass(item)
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
             updateSellIn(item)

def updateBrie(item):
    
def updateRegularItem(item):
    if item.quality > 0:
        item.quality = item.quality - 1
    
def updateBackstagePass(item):
    if item.sell_in < 11:
        if item.quality < 50:
            item.quality = item.quality + 1
        if item.sell_in < 6:
            if item.quality < 50:
                item.quality = item.quality + 1

def updateSellIn(item):
    if item.name != "Sulfuras, Hand of Ragnaros":
        item.sell_in = item.sell_in - 1
    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
