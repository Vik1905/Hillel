# Task 3
# Для файла ideas_for_test/work_with_xml/groups.xml
# створіть функцію  пошуку по group/number і
# повернення значення timingExbytes/incoming
# результат виведіть у консоль через логер на рівні інфо

import  xml.etree.ElementTree as ET
import logging

# Налаштування логера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_incoming_timing(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    logging.info(f"Value of timingExbytes/incoming for group number {number.text}: {incoming.text}")

find_incoming_timing('xml_data/groups.xml')
