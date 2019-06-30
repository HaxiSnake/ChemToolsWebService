#coding: utf-8
bind = '10.7.51.19:4321'
#bind = 'unix:/tmp/chemistry_appserver.sock'
workers = 6
worker_class = 'sync'


timeout = 90
graceful_timeout = 20
keepalive = 2

debug = False

worker_connections = 1000
user = 'jiangdong'
group = 'jiangdong'

proc_name = 'chemistry-appserver'

loglevel = 'debug'
logfile = '/home/jiangdong/workspace/CTWS/chemistry/log/gunicorn.log'
accesslog = '-'
