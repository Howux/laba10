import json


def one():
    with open("products.json", "r", encoding="utf-8") as list:
        products = json.load(list)

    for position in products["products"]:
        print(f"\nНазвание: {position['name']}")
        print(f"Цена: {position['price']}")
        print(f"Вес: {position['weight']}")
        if position["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")


def two():
    with open("products.json", "r", encoding="utf-8") as list:
        products = json.load(list)

    list_of_products = products["products"]

    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Продукт в наличии: ").upper()

    if available == "ДА":
        available = True
    else:
        available = False

    new_products = {
        "name": name,
        "price": price,
        "weight": weight,
        "available": available
    }

    list_of_products.append(new_products)

    with open("products.json", "w", encoding="utf-8") as list:
        products = json.dump(products, list)

    with open("products.json", "r", encoding="utf-8") as list:
        products = json.load(list)

    for position in products["products"]:
        print(f"\nНазвание: {position['name']}")
        print(f"Цена: {position['price']}")
        print(f"Вес: {position['weight']}")
        if position["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")


def three():
    eng_words = []
    ru_words = []
    all_words = []
    lines = 0
    op = open("en-ru.txt", "r", encoding="utf-8-sig")

    with op as fp:
        en_ru = fp.readlines()

    for line in en_ru:
        eng_word = line.split(" - ")[0].strip()
        eng_words.append(eng_word)
        ru_word = line.split(" - ")[1].strip()
        ru_words.append(ru_word)
        lines += 1

    op.close()

    op = open("ru-en.txt", "w", encoding="utf-8-sig")

    with op as fp:
        for word in range(lines):
            fp.write(f"{ru_words[word]} - {eng_words[word]} \n")

    op.close()

    with open("ru-en.txt", "r", encoding="utf-8-sig") as fp:
        string = fp.readlines()

        for line in string:
            all_words.append(line)

    all_words.sort()

    with open("ru-en.txt", "w", encoding="utf-8-sig") as fp:
        for word in range(lines):
            fp.write(all_words[word])

# one()
# two()
# three()