import sys
import logging
import log.config_server_log
import log.config_client_log
import inspect
import traceback


if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func_to_log):
    def log_saver(*args, **kwargs):
        LOGGER.debug(
            f"Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}.\n"
            f"Вызов из модуля {func_to_log.__module__}.\n"
            f"Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}\n"
            f"Вызов из функции {inspect.stack()[1][3]}\n", 
            stacklevel=2

        )
        return func_to_log(*args, **kwargs)
    return log_saver

