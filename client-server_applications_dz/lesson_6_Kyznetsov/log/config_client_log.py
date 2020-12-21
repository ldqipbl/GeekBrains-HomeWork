"""Кофнфиг клиентского логгера"""
import sys
# sys.path.append('../')
import os
import logging as log
# from common.variables import LOGGING_LEVEL


# создаём формировщик логов (formatter):
CLIENT_FORMATTER = log.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'logs/client.log')

# создаём потоки вывода логов
STREAM_HANDLER = log.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
STREAM_HANDLER.setLevel(log.ERROR)

LOG_FILE = log.FileHandler(PATH, encoding='utf8')
LOG_FILE.setFormatter(CLIENT_FORMATTER)

# создаём регистратор и настраиваем его
LOGGER = log.getLogger('client')

LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)

LOGGER.setLevel(log.DEBUG) # LOGGING_LEVEL)


# отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
