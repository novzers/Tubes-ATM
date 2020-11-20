import pandas as pd
import time

def menu():
    print('''
-----------------------------
  /$$$$$$  /$$$$$$$$ /$$      /$$       /$$$$$$$                               /$$                              
 /$$__  $$|__  $$__/| $$$    /$$$      | $$__  $$                             | $$                              
| $$  \ $$   | $$   | $$$$  /$$$$      | $$  \ $$ /$$$$$$  /$$$$$$$   /$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$/$$$$ 
| $$$$$$$$   | $$   | $$ $$/$$ $$      | $$$$$$$//$$__  $$| $$__  $$ /$$__  $$| $$  /$$/ /$$__  $$| $$_  $$_  $$
| $$__  $$   | $$   | $$  $$$| $$      | $$____/| $$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$/ | $$  \ $$| $$ \ $$ \ $$
| $$  | $$   | $$   | $$\  $ | $$      | $$     | $$_____/| $$  | $$| $$  | $$| $$_  $$ | $$  | $$| $$ | $$ | $$
| $$  | $$   | $$   | $$ \/  | $$      | $$     |  $$$$$$$| $$  | $$|  $$$$$$$| $$ \  $$|  $$$$$$/| $$ | $$ | $$
|__/  |__/   |__/   |__/     |__/      |__/      \_______/|__/  |__/ \____  $$|__/  \__/ \______/ |__/ |__/ |__/
                                                                     /$$  \ $$                                  
                                                                    |  $$$$$$/                                  
                                                                     \______/                                   
-----------------------------
    Pilih menu:
    1. Cek Saldo
    2. Tarik Saldo
    3. Deposit Tunai
    4. Transfer Saldo
    5. Ganti PIN''')
    menu = int(input("Pilih nomor menu: "))
    return menu

def prompt():
    ask = input("Apakah anda ingin melanjutkan transaksi? (y/n) ")
    if (ask == 'y'):
        return 1
    else:
        print("Terima kasih telah menggunakan ATM Pengkom.")
        return 0

def cekSaldo(rek):
    saldo = df.loc[rek][1]
    time.sleep(1.1)
    print("Saldo anda sekarang Rp" + str(saldo) + ".")

def tarikSaldo(rek, jumlahTarik):
    saldo = df.loc[rek][1]
    saldo -= jumlahTarik
    time.sleep(1.1)
    if (saldo < 0):
        print("Gagal menarik uang. Jumlah uang yang ingin ditarik lebih besar dari saldo.")
    else:
        print("Berhasil menarik uang sebanyak Rp" + str(jumlahTarik) + ".")
        print("Sisa saldo anda sekarang Rp" + str(saldo) + ".")
        df.loc[rek][1] = saldo
        df.to_csv('data.csv')

def deposit(rek, jumlahDepo):
    saldo = df.loc[rek][1]
    saldo += jumlahDepo
    time.sleep(1.1)
    print("Berhasil mendeposit uang sebanyak Rp" + str(jumlahDepo) + ".")
    print("Sisa saldo anda sekarang Rp" + str(saldo) + ".")
    df.loc[rek][1] = saldo
    df.to_csv('data.csv')

def transfer(rek, jumlahTransfer, rekTransfer):
    try:
        saldor = df.loc[rekTransfer][1]
    except:
        print("Rekening yang anda masukkan tidak valid.")
        return 0
    saldoa = df.loc[rek][1]
    saldoa -= jumlahTransfer
    time.sleep(1.1)
    if (saldoa < 0):
        print("Gagal transfer uang. Jumlah uang yang ingin ditransfer lebih besar dari saldo.")
        saldoa += jumlahTransfer
    else:
        print("Berhasil transfer uang sebanyak Rp" + str(jumlahTransfer) + ".")
        print("Sisa saldo anda sekarang Rp" + str(saldoa) + ".")
        saldor += jumlahTransfer
        df.loc[rek][1] = saldoa
        df.loc[rekTransfer][1] = saldor
        df.to_csv('data.csv')


def gantiPIN(rek, pinbaru):
    if(len(pinbaru) == 6 and pinbaru.isnumeric()):
        df.loc[rek][0] = str(pinbaru)
        print("Berhasil mengubah PIN.")
        df.to_csv('data.csv')
    else:
        print("PIN baru yang anda masukkan tidak valid.")



df = pd.read_csv("data.csv", index_col="Rekening")