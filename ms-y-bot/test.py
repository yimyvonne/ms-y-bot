import sched, time
import coloredlogs, logging

s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#     print("Doing stuff...")
#     # do your stuff
#     s.enter(60, 1, do_something, (sc,))
#
# s.enter(1, 1, do_something, (s,))
# s.run()

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", logger=logger)

testList = ["yvoniwai", "chelhihi", "waylaidbydays", 'paperkaraki', 'rainbowkammy', 'elfish_nam']

def func(newList):
    # refer to global variable 'total' inside function
    item = "paperkaraki"
    global testList
    testList = newList[newList.index(item)+1:]

def testRun():
    logger.info('Total = {}'.format(testList))
    try:
        func(testList)
    except ValueError:
        logger.warning('warning')
    logger.info('Total = {}'.format(testList))
    s.enter(10, 1, testRun, ())

s.enter(1, 1, testRun)
s.run()