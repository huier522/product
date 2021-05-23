#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as file:
    for product in file:
        if '商品,價格' in product:
            continue #繼續
        name, price = product.strip().split(',')
        products.append([name, price])
print(products)

#使用者輸入
while True:
    name = input('輸入「q」會結束記帳。請輸入要紀錄的商品名稱：')
    if name == 'q':
        print('結束記帳。')
        break
    price = input('請輸入剛紀錄的商品價格：')
    products.append([name, price])

#印出所有購買紀錄
for product in products:
    print(f'{product[0]}的價格是{product[1]}')

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as file:
    file.write('商品,價格\n')
    for product in products:
        file.write(f'{product[0]},{product[1]}\n')
