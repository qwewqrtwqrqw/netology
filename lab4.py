import json
import xml.etree.ElementTree as ET

# Чтение данных из JSON-файла
with open('data.json', 'r') as file:
    data = json.load(file)

# Конвертация данных в XML
root = ET.Element("data")
for key, value in data.items():
    element = ET.SubElement(root, key)
    element.text = str(value)

tree = ET.ElementTree(root)

# Сохранение данных в новом XML-файле
tree.write("data.xml")