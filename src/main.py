"""
Daemon to start looping event Scheduler and print alive every 2 seconds.
"""
import sys, time
from apscheduler.schedulers.background import BackgroundScheduler
from config.app import app_config
from loguru import logger
from jobs.ping import ping

fmt = (
    "<green>[{time:YYYY-MM-DDTHH:mm:ssZ}]</green> | "
    "<cyan>{level}      </cyan>"
    "<bold>{message}</bold>"
)

logger.remove()
logger.add(app_config['job_log'], format=fmt, level="ERROR", backtrace=True, rotation="10 days", colorize=False, diagnose=True)
logger.add(sys.stdout, format=fmt, level="INFO", backtrace=False, colorize=True, diagnose=False)

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(ping, 'interval', seconds=3)
# ---------------------------------------------------------------------------- #
    #! ADD JOBS HERE

# ---------------------------------------------------------------------------- #
    scheduler.start()
    try:
        while True:
            time.sleep(2)
    except(KeyboardInterrupt, SystemExit):
        scheduler.shutdown()