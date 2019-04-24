# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import replace_escape_chars


class sgOffTheTee(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    week_rank = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    rank_last_week = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    name = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    rounds = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    average = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    total = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    measured_rounds = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )

class rbcHeritage(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    name = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    score = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    r1 = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    r2 = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    r3 = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    r4 = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    total = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    earnings = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    fedExPoints = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
   
    year = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )

class rbcHeritagePlayer(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ip = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    name = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    driveYards = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    driveAcc = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    gir = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    ppgGir = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    eagle = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    birdie = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    pars = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    bogey = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    dbl = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    toPar = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )

class expanded(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    rank = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    name = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    age = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    yardPerDrive = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    driveAcc = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    driveTotal = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    gir = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    puttAvg = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    savePCT = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )

class expanded2(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    rank = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    name = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    age = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    eagles = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    birdies = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    pars = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    bogeys = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    birdiesPerRound = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    holesPerEagle = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(replace_escape_chars,str.strip),
        output_processor= TakeFirst()
    )