import pandas as pd
import fungsiatm as fn

dtype_dic = {'Rekening': int,
            'PIN': str,
            'Saldo': int
}
df = pd.read_csv("data.csv", index_col="PIN", dtype=dtype_dic)
tries = 0
while (tries < 3):
    try:
        pin = int(input("Masukkan PIN: "))
        saldo = df.loc[pin][1]
        rek = df.loc[pin][0]
        break
    except KeyError:
        if (tries < 2):
            print("PIN anda salah. Coba lagi. (" + str(2-tries) + " percobaan lagi).")
        else:
            print("Kartu ATM anda terblokir. Silahkan hubungi Bank terdekat.")
            exit()
        tries += 1
me = 0
while True:
    me = fn.menu()
    if me == 1:
        fn.cekSaldo(rek)
        if (fn.prompt() == 0):
            break
    elif me == 2:
        jumlahTarik = int(input("Masukkan jumlah saldo yang ingin ditarik: "))
        fn.tarikSaldo(rek, jumlahTarik)
        if (fn.prompt() == 0):
            break
    elif me == 3:
        jumlahDepo = int(input("Masukkan jumlah uang yang ingin dideposit: "))
        fn.deposit(rek, jumlahDepo)
        if (fn.prompt() == 0):
            break
    elif me == 4:
        rekTransfer = int(input("Rekening tujuan: "))
        jumlahTransfer = int(input("Masukkan jumlah uang yang ingin ditransfer: "))
        fn.transfer(rek, jumlahTransfer, rekTransfer)
        if (fn.prompt() == 0):
            break
    elif me == 5:
        pinbaru = input("Masukkan PIN baru: ")
        fn.gantiPIN(rek, pinbaru)
        if (fn.prompt() == 0):
            break
    else:
        print("Nomor menu tidak valid.")
        if (fn.prompt() == 0):
            break



