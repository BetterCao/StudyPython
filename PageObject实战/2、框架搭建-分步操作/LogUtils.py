import logging.config
from Config.BaseInfo import project_path

#读取日志的配置文件
logging.config.fileConfig(project_path+"\\Config\\Logger.conf")

#选择一个日志格式
logger = logging.getLogger("example02")

def error(message):
    #打印debug级别的信息
    logger.error(message)

def info(message):
    #打印info级别的信息
    logger.info(message)

def warning(message):
    #打印warning级别的信息
    logger.warning(message)