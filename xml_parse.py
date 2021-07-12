# XML parser ver 1.1

# https://webformyself.com/rukovodstvo-po-parsingu-xml-python/
# https://docs.python.org/3/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
import urllib.request # для сохранения
import os # для папок os.mkdir("hello")
import log # мой модуль логирования



def file_save(url):
    """Сохранение."""
    global file_name
    global folder_name
    
    id_word = url.rfind("/") # ищем индекс символа с конца    
    file_name = url[id_word+1:] #срез
    file_name = folder_name + "/" + file_name    
    urllib.request.urlretrieve(url, filename = file_name) # сохраняем на диск



def sum_objects():
    """
    Подсчитывает общее количество объектов.
    """
    sum_id = 0    
    for elem in root:        
        for subelem in elem.iter('Id'):
            log.log_message(("ID: " + subelem.text))
            sum_id = sum_id + 1
            
    log.log_message(("Общее количество элементов: " + str(sum_id)))



def iter_all():
    """
    Главная функция. Прогоняет весь xml.
    """
    global folder_name
    global id_name
    
    for elem in root:        
        try:
            for subelem in elem.iter('Id'):
                log.log_message((""))
                log.log_message(("ID: " + subelem.text))
                id_name = subelem.text

            for subelem in elem.iter('Title'):
                folder_name = id_name + ' - ' + subelem.text # имя папки
                log.log_message(("Title: " + folder_name))
                os.mkdir(folder_name) # создать папку
                
            for subelem in elem.iter('Image'):        
                for k, v in (subelem.attrib).items():
                    log.log_message((v))
                    file_save(v)

        except Exception:
            logging.exception("-- белочка сломалась в цикле --", exc_info=True)



# глобальные переменные
folder_name = ''
file_name = ''
id_name = ''

print("XML parser ver 1.1")
xml_file = input("Введите имя файла (например file.xml): ")
##xml_file = "NEW AVITO_6_mini_2.xml"
tree = ET.parse(xml_file)
root = tree.getroot()

log.log_config() # настройка модуля лога
log_text = "========== НОВЫЙ ЗАПУСК ==========================="
log.log_message(log_text)

try:
    sum_objects()
    iter_all()
except Exception:
    logging.exception("--- белочка сломалась ---", exc_info=True)
    
log.log_message((""))
log.log_message(("Готово"))
