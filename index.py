import json
import datetime
# buka file JSON
file_json = open("data_menu.json")
# prsing data JSON
data = json.loads(file_json.read())
dateOrderMerge = datetime.datetime.now().strftime("%d%m%Y %H%M%S")
dateOrderFormat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp ' + y     
    else :
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p

def totalBill(list):
    return sum(list); 

class Kasir:
    def __init__(self, menu):
        self.data = menu
        print('|=======================================================|');
        print('|               SELAMAT DATANG DI APLIKASI              |');
        print('|                     CAFE SPONTAN                      |');
        print('|=======================================================|');
        print('| No |','Menu','{: >45}'.format('|'));
        print('|=======================================================|');
        for indexMenu in range(0, len(menu['menu'])):
            print('|',indexMenu+1,' |',menu['menu'][indexMenu],'{: >42}'.format('|'));
        print('|=======================================================|');

    def choose_menu(self):
        pilihan = input('Pilih Menu berdasarkan angka : ');
        print('|=======================================================|');
        print('| No |','Detail Menu','                                     |');
        print('|=======================================================|');
        findMaxLengthForUi = [];
        lenStringMax = 0;
        if pilihan == '1':
            for indexFood in range(0, len(self.data['food'])):
                # get len padding for ui
                findMaxLengthForUi.append(self.data['food'][indexFood]['name']);
                lenStringMax = len(max(findMaxLengthForUi, key=len));
                getSpasi = lenStringMax - len(self.data['food'][indexFood]['name']) + 1;
                # ternary condition
                pembatas = ' |' if indexFood+1 < 10 else '|';
                # nested condition
                if max(findMaxLengthForUi, key=len) == self.data['food'][indexFood]['name'] :
                    print('|',indexFood+1,pembatas,self.data['food'][indexFood]['name'],'|',formatrupiah(self.data['food'][indexFood]['price']),'{: >16}'.format('|'));
                else :
                    print('|',indexFood+1,pembatas,self.data['food'][indexFood]['name'],'|'.rjust(getSpasi),formatrupiah(self.data['food'][indexFood]['price']),'{: >16}'.format('|'));
        elif pilihan == '2':
            for indexDrink in range(0, len(self.data['drink'])):
                # get len padding for ui
                findMaxLengthForUi.append(self.data['drink'][indexDrink]['name']);
                lenStringMax = len(max(findMaxLengthForUi, key=len));
                getSpasi = lenStringMax - len(self.data['drink'][indexDrink]['name']) + 1;
                # ternary condition
                pembatas = ' |' if indexDrink+1 < 10 else '|';
                # nested condition
                if max(findMaxLengthForUi, key=len) == self.data['drink'][indexDrink]['name'] :
                    print('|',indexDrink+1,pembatas,self.data['drink'][indexDrink]['name'],'|',formatrupiah(self.data['drink'][indexDrink]['price']),'{: >22}'.format('|'));
                else :
                    print('|',indexDrink+1,pembatas,self.data['drink'][indexDrink]['name'],'|'.rjust(getSpasi),formatrupiah(self.data['drink'][indexDrink]['price']),'{: >22}'.format('|'));
        elif pilihan == '3':
            for indexDessert in range(0, len(self.data['dessert'])):
                 # get len padding for ui
                findMaxLengthForUi.append(self.data['dessert'][indexDessert]['name']);
                lenStringMax = len(max(findMaxLengthForUi, key=len));
                getSpasi = lenStringMax - len(self.data['dessert'][indexDessert]['name']) + 1;
                # ternary condition
                pembatas = ' |' if indexDessert+1 < 10 else '|';
                # nested condition
                if max(findMaxLengthForUi, key=len) == self.data['dessert'][indexDessert]['name'] :
                    print('|',indexDessert+1,pembatas,self.data['dessert'][indexDessert]['name'],'|',formatrupiah(self.data['dessert'][indexDessert]['price']),'{: >19}'.format('|'));
                else :
                    print('|',indexDessert+1,pembatas,self.data['dessert'][indexDessert]['name'],'|'.rjust(getSpasi),formatrupiah(self.data['dessert'][indexDessert]['price']),'{: >19}'.format('|'));
        else:
            print('Pilih berdasarkan angka yang ada di tampilan !');
            call();
        
        print('|=======================================================|');
        self.data['choose'] = pilihan;
    
    def choose_menu_by_category(self):
        # find choose
        findIndexChoose = int(self.data['choose']);
        listFind = self.data['menu'][findIndexChoose-1];
        # choose menu
        chooseMenu = int(input('Pilih Menu ' + listFind + ' berdasarkan angka : '));
        self.data['choose2'] = str(chooseMenu);
        if chooseMenu < 16:
            # input portion
            choosePortion = int(input('berapa Porsi ? : '));
            self.data['porsi'] = choosePortion;
        else :
            print('Pilih berdasarkan angka yang ada di tampilan !');
            call();

    def saveOrder(self):
        # find choose by index
        self.data['preOrder'] = {};
        findIndexChoose = int(self.data['choose']);
        listFind = self.data['menu'][findIndexChoose-1];
        findIndexChoose = int(self.data['choose2']);

        if listFind == 'makanan' :
            listFindObject = self.data['food'][findIndexChoose-1];
            self.data['preOrder']['name'] = listFindObject['name'];
            self.data['preOrder']['price'] = listFindObject['price'];
            self.data['preOrder']['portion'] = self.data['porsi'];
        elif listFind == 'minuman' :
            listFindObject = self.data['drink'][findIndexChoose-1];
            self.data['preOrder']['name'] = listFindObject['name'];
            self.data['preOrder']['price'] = listFindObject['price'];
            self.data['preOrder']['portion'] = self.data['porsi'];
        elif listFind == 'dessert' :
            listFindObject = self.data['dessert'][findIndexChoose-1];
            self.data['preOrder']['name'] = listFindObject['name'];
            self.data['preOrder']['price'] = listFindObject['price'];
            self.data['preOrder']['portion'] = self.data['porsi'];
        else :
            print('Pilih berdasarkan angka yang ada di tampilan !');
            call();
        
        self.data['order'].append(self.data['preOrder']);

    def dataCustomer(self):
        listTotalBill = [];
        for indexOrder in range(0, len(self.data['order'])):
           list = self.data['order'][indexOrder]['price'] * self.data['order'][indexOrder]['portion'];
           listTotalBill.append(list);
           totalBill(listTotalBill);
        
        print('|=======================================================');
        print('| Total Bill anda adalah : ', formatrupiah(totalBill(listTotalBill)));
        print('|=======================================================');

        self.data['namaBiling'] = input('Nama Pemesan : ');
        self.data['tableNumber'] = input('Nomor Meja : ');
        self.data['nominal_payment'] = int(input('Masukan uang anda : '));
    
    def printStruck(self):
        listTotalItem = [];
        listTotalBill = [];
        # format struck pesanan (nomeja/inisial_kedai/dateandjam)
        codeStruck = self.data['tableNumber']+'CS'+dateOrderMerge;
        replaceSpasi = codeStruck.replace(" ", "");
        print('|======================================================');
        print('|            TERIMA KASIH TELAH MEMESAN DI             ');
        print('|                     CAFE SPONTAN                     ');
        print('|======================================================');
        print('|',"Date          : ", dateOrderFormat);
        print('|',"Receipt No    : ", replaceSpasi);
        print('|',"Customer Name : ", self.data['namaBiling']);
        print('|',"Table Number  : ", self.data['tableNumber']);
        print('=======================================================');
        for indexOrder in range(0, len(self.data['order'])):
            itemBill = self.data['order'][indexOrder]['price'] * self.data['order'][indexOrder]['portion'];
            listTotalItem.append(self.data['order'][indexOrder]['portion']);
            listTotalBill.append(itemBill);
            totalItem = sum(listTotalItem);
            print('|',self.data['order'][indexOrder]['portion'],' ',self.data['order'][indexOrder]['name'],' ',formatrupiah(itemBill));
        print('=======================================================');
        print('|','Total item : ', totalItem);
        print('|','Bill       : ', formatrupiah(totalBill(listTotalBill)));
        print('|','Cash       : ', formatrupiah(self.data['nominal_payment']));
        print('|','Change     : ', formatrupiah(self.data['nominal_payment'] - totalBill(listTotalBill)));
        print('=======================================================');
        print('|           TERIMA KASIH ATAS KUNJUNGAN ANDA !         ');
        print('=======================================================');

def call():
    database = Kasir(data)
    database.choose_menu()
    database.choose_menu_by_category()
    database.saveOrder()
     # asking customer
    chooseCustomer = "Apakah anda ada pesanan lain klik y / n :"
    response = input(chooseCustomer);
    if response == 'y':
        call();
    else:
        database.dataCustomer()
        database.printStruck()
call();