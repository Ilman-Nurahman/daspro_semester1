menu = ['makanan','minuman', 'dessert'];
category_food = ['Chicken Lada Hitam', 'Nasi Gila', 'Chicken Crispy'];
food_price = [16000, 17000, 15000];

category_drink = ['Vanila Oreo', 'Taro Cheese', 'Green Tea'];
food_price = [16000, 17000, 15000];

category_dessert = ['Ice Cream', 'Pisang Coklat', 'Roti Bakar'];
food_price = [16000, 17000, 15000];

list_pesanan = [];
quantity_pesanan = [];
harga_item = [];

print('===========================================================');
print('Selamat Datang di kedai Spontan');
print('===========================================================');
print('1. ', menu[0]);
print('2. ', menu[1]);
print('3. ', menu[2]);
print('===========================================================');

pilihan1 = input('Pilih Menu berdasarkan angka, ketik 0 untuk selesai : ');

def pilihanStep1():
    return pilihan1;

def pilihMenu(params, type):
    if params == '1' :
        if type == 'step1':
            for a in range(0, len(category_food)):
                print(a+1, category_food[a]);
            stringMenu = 'Makanan';
            return stringMenu;
        else:
            print('aldi');
    elif params == '2' :
        for a in range(0, len(category_drink)):
            print(a+1, category_drink[a]);
        stringMenu = 'Minuman';
        return stringMenu;
    else:
        for a in range(0, len(category_dessert)):
            print(a+1, category_dessert[a]);
        stringMenu = 'Dessert';
        return stringMenu;


pilihan2 = input('Pilih Menu ' + pilihMenu(pilihan1, 'step1') + ' berdasarkan angka : ');
quantity = int(input('Kuantitas : '));
chooseCustomer = "Apakah anda ada pesanan lain klik y / n :"
response = input(chooseCustomer);

if response == pilihanStep1:
    pilihanStep1();