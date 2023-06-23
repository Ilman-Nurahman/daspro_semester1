import json
# buka file JSON
file_json = open("data_menu.json")
# prsing data JSON
data = json.loads(file_json.read())

class Kasir:
    def __init__(self, menu):
        self.data = menu
        print('===========================================================');
        print('Selamat Datang di kedai Spontan');
        print('===========================================================');
        for indexMenu in range(0, len(menu['menu'])):
            print(indexMenu+1, menu['menu'][indexMenu]);
        print('===========================================================');

    def choose_menu(self):
        pilihan = input('Pilih Menu berdasarkan angka : ');
        if pilihan == '1':
             for indexFood in range(0, len(self.data['food'])):
                print(indexFood+1, self.data['food'][indexFood]['name']);
        elif pilihan == '2':
            for indexDrink in range(0, len(self.data['drink'])):
                print(indexDrink+1, self.data['drink'][indexDrink]['name']);
        elif pilihan == '3':
            for indexDessert in range(0, len(self.data['dessert'])):
                print(indexDessert+1, self.data['dessert'][indexDessert]['name']);
        else:
            exit();
        
        self.data['choose'] = pilihan;
    
    def choose_menu_by_category(self):
        # find choose
        findIndexChoose = int(self.data['choose']);
        listFind = self.data['menu'][findIndexChoose-1];
        chooseMenu = input('Pilih Menu ' + listFind + ' berdasarkan angka : ');
        self.data['choose2'] = chooseMenu;
        # input portion
        choosePortion = int(input('berapa Porsi ? : '));
        self.data['porsi'] = choosePortion;
    
    def saveOrder(self):
        self.data['preOrder']['name'] = self.data['choose2'];
        self.data['preOrder']['price'] = self.data['porsi'];
        self.data['preOrder']['portion'] = self.data['porsi'];
        self.data['order'].append(self.data['preOrder']);

    def printStruck(self):
        print('print struk');

def call():
    database = Kasir(data)
    # print(database.__dict__['data']);
    database.choose_menu()
    database.choose_menu_by_category()
    database.saveOrder()
     # choose customer
    chooseCustomer = "Apakah anda ada pesanan lain klik y / n :"
    response = input(chooseCustomer);
    if response == 'y':
        call();
    else:
        database.printStruck()
call();