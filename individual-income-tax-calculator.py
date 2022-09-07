print('  Tinh thue thu nhap ca nhan  ')
print('********************************')
mst = input('Ma so thue: ')
ho_ten = input('Ho ten doi tuong nop thue: ')
thu_nhap = int(input('Tong thu nhao trong nam: '))
nguoi_phu_thuoc = int(input('So nguoi phu thuoc: '))
print('--- Ket qua: ------------------')

giam_tru = (9000000 + 3600000)*12*nguoi_phu_thuoc
tien_chiu_thue = thu_nhap - giam_tru
bac1 = 60000000
bac2 = 120000000
bac3 = 216000000
bac4 = 384000000
bac5 = 624000000
bac6 = 960000000
thue1, thue2, thue3, thue4, thue5, thue6, thue7 = 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35
tien_thue = 0
if tien_chiu_thue>0 and tien_chiu_thue<=bac1:
    tien_thue = tien_chiu_thue*thue1
elif tien_chiu_thue<=bac2:
    tien_thue = bac1*thue1 + (tien_chiu_thue-bac1)*thue2
elif tien_chiu_thue<=bac3:
    tien_thue = bac1*thue1 + (bac2-bac1)*thue2 + (tien_chiu_thue-bac2)*thue3
elif tien_chiu_thue<=bac4:
    tien_thue = bac1*thue1 + (bac2-bac1)*thue2 + (bac3-bac2)*thue3 + (tien_chiu_thue-bac3)*thue4
elif tien_chiu_thue<=bac5:
    tien_thue = bac1*thue1 + (bac2-bac1)*thue2 + (bac3-bac2)*thue3 + (bac4-bac3)*thue4 + (tien_chiu_thue-bac4)*thue5
elif tien_chiu_thue<=bac6:
    tien_thue = bac1*thue1 + (bac2-bac1)*thue2 + (bac3-bac2)*thue3 + (bac4-bac3)*thue4 + (bac5-bac4)*thue5 + (tien_chiu_thue-bac5)*thue6
elif tien_chiu_thue>bac6:
    tien_thue = bac1*thue1 + (bac2-bac1)*thue2 + (bac3-bac2)*thue3 + (bac4-bac3)*thue4 + (bac5-bac4)*thue5 + (bac6-bac5)*thue6 + (tien_chiu_thue-bac6)*thue7

print('So tien giam tru: %.2f VND' %(giam_tru))
print('So tien chiu thue: %.2f VND' %(tien_chiu_thue))
print('Tien thue phai nop: %.2f VND' %(tien_thue))