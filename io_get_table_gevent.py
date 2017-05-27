import gevent
from gevent import monkey
monkey.patch_all()
import logging
import os
from time import time

import get_info
import table_crawler_selenium as crawler
import kill_old_tables
import get_index

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

def main():
    ts = time()
    info_list = get_info.get_info()
    yy = info_list[0]
    mm = info_list[1]
    c_list = info_list[2]
    
    tablespath = "/var/www/html/tables/"
    kill_old_tables.kill_old_tables(c_list, tablespath)
    
    jobs = [gevent.spawn(crawler.gettable, yy, mm, classname) for classname in c_list]
    gevent.wait(jobs)
    get_index.get_index(tablespath)
    print('Took {}s'.format(time() - ts))

if __name__ == '__main__':
    main()

