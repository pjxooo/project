import time

from config.config import init
from config.config import logger

start = int(time.time())
init()

def getRunTimeInt():
    return (int(time.time()) - start)

def getRunTime():
    return '程序已经执行%d秒' % (int(time.time()) - start)


def writeInfo(msg):
    logger.info('%s\t(%s)' % (msg, getRunTime()))


def writeError(msg):
    logger.error('%s\t(%s)' % (msg, getRunTime()))
