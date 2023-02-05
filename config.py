#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", -1001342411240)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQAlMzYWr3AFQgzppOcTWe3Mh7VGCKGAnObs6tykVwyexB04GNElsS1o12aRSeTTuGamgNJMssiUls33QEUfTajt27zrUQCi0HQ-qCCI8D_IT6pDnlv2tgCnHwkcEYJ6vUgBxPZSdMkkfnQ4tiL93MA4Vxt2Gwd6FUrxD2qwUXOQRnXUFIBTYPi1ihcjkijBU3-iixEsQwOYISLuM3sJ10liG-CdITfVSAhdIYciegR4-BNIHGmeYs38GMbbhFA0dM0i0z7Orm7FsziOZ_r56YbWbWuOH8R3Re-7hntBrThvXP_nI47zmYxuC8zIZ-qleZiI-VhHRoBCHNA46VWf6xHlUvF4PAA")
    TO_CHANNEL = os.environ.get("TO_CHANNEL", "")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
