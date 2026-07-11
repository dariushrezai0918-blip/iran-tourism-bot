import time
import schedule

def job():
    print("ربات در حال اجراست...")

schedule.every(1).minutes.do(job)

print("Scheduler Started")

while True:
    schedule.run_pending()
    time.sleep(1)
