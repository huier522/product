product = []

while True:
    name = input('輸入「q」會結束記帳。請輸入要紀錄的商品名稱：')
    if name == 'q':
        print('結束記帳。')
        break
    price = input('請輸入剛紀錄的商品價格：')
    product.append([name, price])
print(product)
