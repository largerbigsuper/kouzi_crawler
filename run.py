import time
import os
from scrapy import cmdline
from datetime import datetime


def crawlall():
    print('Crawlall! Current time is: %s' % datetime.now())
    cmdline.execute('scrapy crawlall'.split())
    os.system('scrapy crawlall')


if __name__ == "__main__":
    while True:
        crawlall()