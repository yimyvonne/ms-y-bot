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

def get_follower_number(string):
    follower_number_string = string

    # follower_number = float(follower_number_string[:len(
    #     follower_number_string) - 1]) * 1000 if 'k' in follower_number_string else follower_number_string
    # print(follower_number)

    # print((float(follower_number_string[:len(
    #     follower_number_string) - 1])*1000) > 2000)

    print(int("1234".replace(",", "")))

# s.enter(1, 1, testRun)
# s.run()
get_follower_number('22.2k')