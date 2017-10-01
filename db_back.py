#-*- coding:utf-8 -*-
import sys, os
import datetime

today_s = datetime.datetime.today().strftime('%Y%m%d')
week_ago_str = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime('%Y%m%d')

os.system('cp /root/apps/omegabiomics/db.sqlite3 /root/data/db_%s.sqlite3' % (today_s,))
os.system('cp -r /root/apps/omegabiomics/media /root/data/media_%s' % (today_s,))

os.system('rm -rf /root/data/db_%s.sqlite3' % (week_ago_str,))
os.system('rm -rf /root/data/media_%s' % (week_ago_str,))

