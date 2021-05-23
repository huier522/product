products = []

while True:
    name = input('輸入「q」會結束記帳。請輸入要紀錄的商品名稱：')
    if name == 'q':
        print('結束記帳。')
        break
    price = input('請輸入剛紀錄的商品價格：')
    products.append([name, price])

for product in products:
    print(f'{product[0]}的價格是{product[1]}')

with open('products.csv', 'w', encoding='utf-8') as file:
    file.write('商品,價格\n')
    for product in products:
        file.write(f'{product[0]},{product[1]}\n')