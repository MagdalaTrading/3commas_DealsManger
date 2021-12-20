import time
import datetime
import schedule
import importlib
import b_maxdeals


def run_maxdeals():
    importlib.reload(b_maxdeals)
    now = datetime.datetime.now()
    print("Updated at : " + now.strftime('%Y-%m-%d %H:%M:%S'))

schedule.every(10).seconds.do(run_maxdeals)

while True:

    schedule.run_pending()
    time.sleep(1)
