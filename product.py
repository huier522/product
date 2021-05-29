import os  # operating system

#讀取檔案
def read_file(filename):
    products = []  # 在第40行再建立一次才能不管檔案在不在，才能有空清單去存
    with open(filename, 'r', encoding='utf-8') as file:
        for product in file:
            if '商品,價格' in product:
                continue  # 繼續
            name, price = product.strip().split(',')
            products.append([name, price])
    return products

#使用者輸入
def user_input(products):
    while True:
        name = input('輸入「q」會結束記帳。請輸入要紀錄的商品名稱：')
        if name == 'q':
            print('結束記帳。')
            break
        price = int(input('請輸入剛紀錄的商品價格：'))
        products.append([name, price])
        spend += price
    return products

#印出所有購買紀錄
def print_products(products):
    for product in products:
        print(f'{product[0]}的價格是{product[1]}')

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('商品,價格\n')
        for product in products:
            file.write(f'{product[0]},{product[1]}\n')
    #只是寫入不用return        

def main():
    #檢查檔案在不在，存在就讀取檔案
    filename = 'products.csv'
    products = [] #防止當檔案不存時會沒有清單可以讀取問題
    if os.path.isfile(filename):
        print('檔案存在')
        products = read_file(filename)
    else:
        print('檔案不存在，請建立檔案！')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()
