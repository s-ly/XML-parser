import logging # модуль логирования

def log_config():
    """
    Настройка логирования.
    Справка: https://webdevblog.ru/logging-v-python/
    level - уровень регистрации,
    filename - файл вывода,
    format - добавим дату и время.
    """
    logging.basicConfig(level=logging.DEBUG,
                        filename='app.log',
                        format='%(asctime)s - %(message)s')
def log_message(message):
    """
    Вывод (запись в файл) сообщения лога и на экран.
    """
    print(message)
    logging.debug(message)
    
##log_config()
##x = "42"
##y = "55"
##log_message("mes:" + x + y)
##try:
##    x = 10/0
##except Exception:
##    logging.exception("белочка сломалась", exc_info=True)
