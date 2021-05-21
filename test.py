import schedule
import time

def do_some():
    print("Updated!")

schedule.every(3).seconds.do(do_some)

while True:
    schedule.run_pending()
    time.sleep(1) 