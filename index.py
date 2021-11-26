import seleniumConfig
from src.tongQuan import btn_XemChiTiet,btn_XemMXH
from src.donHang import TK_HoaDon
from src.CaLamViec import calamviec

def main():
    print("=======Main========")
    while(1):
        choose=input('Nhap chuong trinh: ')
        driver = seleniumConfig.login(5)
        print(driver)
        if(choose=='1'):
            ''' Tổng quan '''
            btn_XemChiTiet.btn_XemChiTiet(driver)
            btn_XemMXH.btn_XemMXH(driver)
            ''' Đơn Hàng '''
            TK_HoaDon.Hoa_Don(driver)
            ''' Ca làm việc '''
            calamviec.CaLamViec(driver)

if __name__ == "__main__":
    main()

