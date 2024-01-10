# Ввод списка товаров и их цен в разных магазинах
products = []
shops = []

n = int(input("Введите количество товаров: "))
for i in range(n):
    product = input("Введите название товара: ")
    price_shop = []

    for j in range(len(shops)):
        price = float(input(f"Введите цену товара {product} в магазине {shops[j]}: "))
        price_shop.append(price)

    products.append((product, price_shop))

    new_shop = input("Введите название нового магазина: ")
    shops.append(new_shop)

# Вычисление общей стоимости покупок в каждом магазине
total_prices = []
for i in range(len(shops)):
    total_price = 0
    for j in range(n):
        total_price += products[j][1][i]
    total_prices.append(total_price)

# Вывод списка магазинов и общей стоимости покупок в каждом магазине
print("Список магазинов и общая стоимость покупок:")
for i in range(len(shops)):
    print(f"{shops[i]}: {total_prices[i]}")

# Поиск магазина, в котором пользователь может сэкономить больше всего денег
max_savings = max(total_prices) - min(total_prices)
max_savings_shop = shops[total_prices.index(max(total_prices))]

print(f"Вы можете сэкономить больше всего денег в магазине {max_savings_shop} - сумма сэкономленных денег составляет {max_savings}")