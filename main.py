import random
import time
import threading

# untuk mencatat skor
statBoard = {}
# status bermain apakah masih?
playContinue = True

def play(playerName):
    '''role permainan ada disini'''

    # share variabel playContinue dan statBoard
    global playContinue, statBoard

    # looping selama belum ada pemain yang ngeset
    # playContinue ke False
    while playContinue:

        # generate angka random untuk keluaran dadu
        dice = random.randint(1, 6)
        print('{}: dadu {} '.format(playerName, dice))

        # jika keluar dadu 6
        if dice == 6:

            # catat dan tally hasil player di statBoard
            statBoard[playerName] = statBoard.get(playerName,0) + 1
            print('>> {} {}x '.format(playerName, statBoard[playerName]))

            # jika sudah tercapai 3x
            if statBoard[playerName] == 3:

                # set playContinue ke False agar pemain yang lain
                # berhenti mengocok dadu karena sudah ada pemenang
                playContinue = False
                print('>> {} menang! '.format(playerName))

                # berhenti main sbg pemenang
                break

        # random delay ini [0.1s - 1.0s] mensimulasikan waktu
        # untuk menyiapkan dan mengocok dadu itu bervariasi
        time.sleep(random.randint(1,10)/10)

# ---- main program ------
print('Simulasi Game Dadu 2 Player')

# nama-nama pemain
nm1 = 'Gagah'
nm2 = 'Ayu'

# cetak role
print('''
Dua player ({} dan {}) masing-masing melempar
dadu bersamaan secara berulang. Jeda waktu antara
lemparan satu dengan lemparan berikutnya adalah acak
antara 0,1 s.d 1,0 detik. Pemain dinyatakan sebagai
pemenang bila dadunya telah mengeluarkan angka 6
sebanyak 3 kali'''.format(nm1, nm2))

# mulai
input('\n-- Tekan [Enter] untuk memulai..')

# definisikan thread
thread1 = threading.Thread(target=play, args=(nm1,))
thread2 = threading.Thread(target=play, args=(nm2,))

# urutan target start -- diacak
urutanStart = [thread1, thread2]
random.shuffle(urutanStart)

# start setiap thread target
for p in urutanStart:
    p.start()

# menunggu semua thread target selesai
# untuk join ke thread utama
for p in urutanStart:
    p.join()

# thread utama
print('-- Game selesai..')


# Contoh output
'''
Simulasi Game Dadu 2 Player

Dua player (Gagah dan Ayu) masing-masing melempar
dadu bersamaan secara berulang. Jeda waktu antara
lemparan satu dengan lemparan berikutnya adalah acak
antara 0,1 s.d 1,0 detik. Pemain dinyatakan sebagai
pemenang bila dadunya telah mengeluarkan angka 6
sebanyak 3 kali

-- Tekan [Enter] untuk memulai..
Ayu: dadu 2
Gagah: dadu 6
>> Gagah 1x
Ayu: dadu 2
Gagah: dadu 6
>> Gagah 2x
Ayu: dadu 6
>> Ayu 1x
Gagah: dadu 3
Ayu: dadu 2
Ayu: dadu 5
Ayu: dadu 2
Ayu: dadu 5
Ayu: dadu 5
Gagah: dadu 6
>> Gagah 3x
>> Gagah menang!
-- Game selesai..
'''
