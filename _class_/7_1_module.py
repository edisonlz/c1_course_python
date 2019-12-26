构建一个模块的层级包


util/__init__.py
    /dateutil/
    /dateutil/__init__.py
    /dateutil/dateutil.py
    /dateutil/timeutil.py

引用报的语法
from util.dateutil.dateutil import date_to_string
from util.dateutil.timeutil import time_to_string
import time

time_to_string(time.time())


