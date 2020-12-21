import sys
# sys.path.append('../')
import os
import logging as log
import logging.handlers as log_hand


# создаём формировщик логов (formatter):
SERVER_FORMATTER = log.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')


# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'logs/server.log')


# создаём потоки вывода логов
STREAM_HANDLER = log.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(log.ERROR)

LOG_FILE = log_hand.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)


# создаём регистратор и настраиваем его
LOGGER = log.getLogger('server')

LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)

LOGGER.setLevel(log.DEBUG)


# отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
