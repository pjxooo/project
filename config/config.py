import configparser
import logging
from logging.handlers import TimedRotatingFileHandler

cf = configparser.ConfigParser()
cf.read('config.ini',encoding='utf-8')
if len(cf.sections()) == 0:
    raise Exception('配置文件解析异常')
logFile = cf.get('file', 'logFile')
logger=logging.getLogger()
logger.setLevel(logging.INFO)

def init():
    log_format=logging.Formatter(fmt="%(asctime)s %(levelname)s : %(message)s",datefmt='%Y-%m-%d %H:%M:%S')
    # 在控制台打印日志
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(log_format)
    logger.addHandler(streamHandler)

    timedRotatingFileHandler=TimedRotatingFileHandler(filename="log/all.log",when='H',interval=1,encoding='utf-8')
    timedRotatingFileHandler.setFormatter(log_format)


    logger.addHandler(timedRotatingFileHandler)


