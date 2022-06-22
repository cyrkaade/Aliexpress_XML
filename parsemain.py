import time
import xml.etree.ElementTree as ET

#Get product details:

tree1 = ET.parse("ВашПуть/Intim_Ali_allfids_2.xml")

# Тут хотелось бы отметить, что возможно
# он не будет парсить документ Intim_Ali_allfids_2 т.к он неправильный изнутри. Нету резделения тэгов.

root1 = tree1.getroot()
tree2 = ET.parse("ВашПуть/p5s_full_stock.xml")
root2 = tree2.getroot()
# Парсим файлы
counting = 1

while counting < 250000: # Делаем цикл и проходи по всем элементам (50 в каждый отрезок времени)
    for i in range(counting, counting + 50):
        check = root2.find(f"./product[@prodID='{i}']")
        if check is not None: # Проверяем, есть ли продукт с данным айди
            br_price = root2.find(f"./product[@prodID='{i}']/price").attrib['BaseRetailPrice']
            bw_price = root2.find(f"./product[@prodID='{i}']/price").attrib['BaseWholePrice']
            r_price = root2.find(f"./product[@prodID='{i}']/price").attrib['RetailPrice']
            w_price = root2.find(f"./product[@prodID='{i}']/price").attrib['WholePrice'] # Берем аттрибуты

            check_editing = root1.find(f"./offers/offer[@id='{i}']")

            editing = root1.find(f".offers/offer[@id='{i}']/price")
            if check_editing is not None:
                editing.attrib['BaseRetailPrice'] = br_price
                editing.attrib['BaseWholePrice'] = bw_price
                editing.attrib['RetailPrice'] = r_price
                editing.attrib['WholePrice'] = w_price # Изменяем данные
                print('Updated')
    counting += 50
    time.sleep(0.1)

# Далее вставляем в личном кабинете алиэкспресса ваш YML файл.
