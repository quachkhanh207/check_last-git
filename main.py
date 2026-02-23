from product_manager import *

products = []

def show_menu():
    print("1. Thêm sản phẩm")
    print("2. Xóa sản phẩm")
    print("3. Tìm sản phẩm theo ID")
    print("0. Thoát")


while True:
    show_menu()
    choice = input("Chọn chức năng: ")

    if choice == "1":
        product = {
            "id": input("Mã sản phẩm: "),
            "name": input("Tên sản phẩm: "),
            "brand": input("Thương hiệu: "),
            "price": int(input("Giá: ")),
            "quantity": int(input("Số lượng: "))
        }
        add_product(products, product)

    elif choice == "2":
        pid = input("Nhập ID cần xóa: ")
        if delete_product(products, pid):
            print("Đã xóa.")
        else:
            print("Không tìm thấy.")

    elif choice == "3":
        pid = input("Nhập ID cần tìm: ")
        product = find_product_by_id(products, pid)
        print(product if product else "Không có sản phẩm.")
        break

    elif choice == "0":
        break