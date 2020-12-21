import sys
import logging
import log.config_server_log
import log.config_client_log
import inspect


if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func_to_log):
    def log_saver(*args, **kwargs):
        LOGGER.debug(
            f"Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}.\n"
            f"Вызов из модуля {func_to_log.__module__}.\n"
            f"Вызов из функции {inspect.stack()[1][3]}\n"
        )
        return func_to_log(*args, **kwargs)
    return log_saver


'''
# Реализация в виде класса
class Log:
    """Класс-декоратор"""
    def __call__(self, func_to_log):
        def log_saver(*args, **kwargs):
            """Обертка"""
            ret = func_to_log(*args, **kwargs)
            LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                         f'Вызов из модуля {func_to_log.__module__}. Вызов из'
                         # f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
                         f'Вызов из функции {inspect.stack()[1][3]}')
            return ret
        return log_saver
'''

