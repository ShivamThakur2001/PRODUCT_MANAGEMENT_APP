from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtPrintSupport import QPrinter 
from datetime import date,time
import sys
import sqlite3
import time

ui, _ = loadUiType("Product.ui")

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.REGISTER_BUTTON.clicked.connect(self.register)
        self.LOGIN.clicked.connect(self.login)
        self.LOGOUT.clicked.connect(self.loguot)
        self.BACK_1.clicked.connect(self.back_1)
        self.BACK_2.clicked.connect(self.back_2)
        self.BACK_3.clicked.connect(self.back_3)
        self.BACK_4.clicked.connect(self.back_4)
        self.ADD_PRODUCT.clicked.connect(self.add_button)
        self.ADD.clicked.connect(self.ADDITION)
        self.DELETE_PRODUCT.clicked.connect(self.delete_button)
        self.DELETE.clicked.connect(self.delete_product)
        self.ORDER_PRODUCT.clicked.connect(self.order)
        self.PLACE_ORDER.clicked.connect(self.order_product)
        self.ADD_TO_CART.clicked.connect(self.add_to_cart)
        self.GET_INVOICE.clicked.connect(self.printreceipt)
    
    ## REGISTERATION ##
    def register(self):
        na = self.NAME.text()
        e_mail = self.E_MAIL.text()
        mobile_no = self.MOBILE_NUMBER.text()
        if len(mobile_no) == 10:
            pass
        else:
            self.REGISTER_INFO.setText("INVALID NUMBER")
        pawd = self.REGISTER_PASSWORD.text()
        con_pawd = self.CONFIRM_PASSWORD.text()
        if pawd == con_pawd:
            pass
        else:
            self.REGISTER_INFO.setText("PASSWORD NOT MATCHED")
        con = sqlite3.connect("PRODUCT.db")
        cursor = con.execute("INSERT INTO register_info (name,email,mobile,password) values('"+ na +"','"+ e_mail +"',"+ str(mobile_no) +",'"+ pawd +"')")
        con.commit()
        self.tabWidget.setCurrentIndex(0)
        self.NAME.setText("")
        self.E_MAIL.setText("")
        self.MOBILE_NUMBER.setText("")
        self.REGISTER_PASSWORD.setText("")
        self.CONFIRM_PASSWORD.setText("")
        self.REGISTER_INFO.setText("REGISTER SUCCESSFULLY")
        con.close()

    ## LOGIN ##
    def login(self):
        un = self.USERNAME.text()
        passw = self.LOGIN_PASSWORD.text()
        con = sqlite3.connect("PRODUCT.db")
        cursor = con.execute("SELECT password FROM register_info WHERE name = '{}'".format(un))
        result = cursor.fetchall()
        inp_password = (result[0][0])
        if(inp_password == passw):
            self.USERNAME.setText("")
            self.LOGIN_PASSWORD.setText("")
            self.tabWidget.setCurrentIndex(1)
        else:
            self.LOGIN_ALERT.setText("INVALID PASSWORD")
        con.close()
    
    ## ADD PRODUCT ##
    def add_button(self):
        self.tabWidget.setCurrentIndex(2)
        self.PRODUCT_NAME.setText("")
        self.BRAND_NAME.setText("")
        self.PRODUCT_PRICE.setText("")
        self.PRODUCT_SKU.setText("")
        self.PRODUCT_USE.setText("")
        self.PRODUCT_DESCRIPTION.setText("")
        self.PRODUCT_CATEGORY.setText("")
    def ADDITION(self):
        pname = self.PRODUCT_NAME.text()
        bname = self.BRAND_NAME.text()
        pprice = self.PRODUCT_PRICE.text()
        psku = self.PRODUCT_SKU.text()
        puse = self.PRODUCT_USE.text()
        pdescription = self.PRODUCT_DESCRIPTION.text()
        pcategory = self.PRODUCT_CATEGORY.text()
        con = sqlite3.connect("PRODUCT.db")
        cursor = con.execute("INSERT INTO add_product(product_name, brand_name, product_category, product_price, product_sku, product_use, product_description) values('"+ pname +"','"+ bname +"','"+ pcategory +"','"+ str(pprice) +"','"+ str(psku) +"','"+ puse +"','"+ pdescription +"')")
        con.commit()
        con.close()
        self.tabWidget.setCurrentIndex(1)
        self.INFORMATION.setText("ADDED SUCCESSFULLY")

    ## DELETE BUTTON ##
    def delete_button(self):
        self.tabWidget.setCurrentIndex(3)
        self.DELETE_PRODUCT_NAME.setText("")
        self.DELETE_BRAND.setText("")
        self.DELETE_REASON.setText("")
    def delete_product(self):
        dname = self.DELETE_PRODUCT_NAME.text()
        dbrand = self.DELETE_BRAND.text()
        dreason = self.DELETE_REASON.text()
        con = sqlite3.connect("PRODUCT.db")
        cursor = con.execute("INSERT INTO delete_product(deleted_name,deleted_brand,deleted_reason) values ('"+ dname +"', '"+ dbrand +"','"+ dreason +"')")
        con.commit()
        cursor = con.execute("DELETE FROM add_product WHERE product_name = '{}' and brand_name = '{}'".format(dname,dbrand))
        con.commit()        
        con.close()
        self.tabWidget.setCurrentIndex(1)
        self.INFORMATION.setText("DELETED SUCCESSFULLY")
        
    ## ORDER PRODUCT ##
    def order(self):
        t = time.localtime()
        ot = time.strftime("%H:%M",t)
        con = sqlite3.connect("PRODUCT.db")
        cursor = con.execute("SELECT MAX(order_id) FROM order_product")
        result = cursor.fetchall()
        if result:
            try:   
                for data in result:
                    oid = int(data[0]) + 1
            except:
                oid = 1
        else:
            oid = 1
        self.ORDER_ID.setText(str(oid))
        self.ORDER_ID_2.setText(str(oid))
        self.DATE.setText(str(date.today()))
        self.TIME.setText(str(ot))
        self.tabWidget.setCurrentIndex(4)
        self.ORDER_PRODUCT_NAME.text()
        self.ORDER_BRAND.text()
        self.QUANTITY.text()
        self.PRODUCT_TABLE.setRowCount(0)
        self.PRODUCT_TABLE.clear()
    def add_to_cart(self):
        a = ""
        b = ""
        c = ""
        d = ""
        total=0
        self.PRODUCT_TABLE.setRowCount(0)
        self.PRODUCT_TABLE.clear()
        self.PRODUCT_TABLE.setColumnWidth(0,174)
        self.PRODUCT_TABLE.setColumnWidth(1,174)
        self.PRODUCT_TABLE.setColumnWidth(2,174)
        self.PRODUCT_TABLE.setColumnWidth(3,174)
        self.PRODUCT_TABLE.setColumnWidth(4,174)
        self.PRODUCT_TABLE.setColumnWidth(5,174)
        con = sqlite3.connect("PRODUCT.db")
        cursor = con.execute("SELECT product_name ,brand_name ,product_category,product_price FROM add_product WHERE product_name = '"+ self.ORDER_PRODUCT_NAME.text() +"' and brand_name = '"+ self.ORDER_BRAND.text() +"'")
        con.commit()
        result = cursor.fetchall()
        if result:
            for prod in result:
                a = str(prod[0])
                b = str(prod[1])
                c = str(prod[2])
                d = str(prod[3])
        temp = (int(self.QUANTITY.text()) * int(d))
        temp1 = int(self.QUANTITY.text())
        con.execute("INSERT INTO order_product (order_id,order_name,order_brand,order_category,order_quantity,order_price,total_price) values("+ self.ORDER_ID.text() +", '"+ a +"','"+ b +"','"+ c +"',"+ str(temp1) +",'"+ d +"',"+ str(temp) +")")
        con.commit()
        con = sqlite3.connect("PRODUCT.db")
        cursor = con.execute("SELECT order_name,order_brand,order_category,order_quantity,order_price,total_price FROM order_product WHERE order_id = "+ self.ORDER_ID.text() +"")
        result = cursor.fetchall()
        r = 0
        c = 0
        for row_number, row_data in enumerate(result):
            r += 1
            c = 0
            for column_number, data in enumerate(row_data):
                c += 1
        self.PRODUCT_TABLE.setColumnCount(c)
        for row_number, row_data in enumerate(result):
            self.PRODUCT_TABLE.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.PRODUCT_TABLE.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        self.PRODUCT_TABLE.verticalHeader().setVisible(False)
        self.PRODUCT_TABLE.horizontalHeader().setVisible(False)
        cursor = con.execute("SELECT * FROM order_product WHERE order_id = "+ self.ORDER_ID.text() +" ")
        result = cursor.fetchall()
        if result:
            for prod in result:
                total = total + int(prod[6])
        
        self.TAX.setText("%.2f" % (total*0.05))
        self.GRAND_TOTAL.setText("%.2f" % (total + (total * 0.05) ))
        self.GRAND_TOTAL_2.setText("%.2f"%(total + (total * 0.05)))
        self.ORDER_PRODUCT_NAME.setText("")
        self.ORDER_BRAND.setText("")
        self.QUANTITY.setText("")

    ## PLACE ORDER ##
    def order_product(self):
        self.INVOICE.setRowCount(0)
        self.INVOICE.clear()
        self.INVOICE.setColumnWidth(0,110)
        self.INVOICE.setColumnWidth(1,110)
        self.INVOICE.setColumnWidth(2,110)
        con = sqlite3.connect("PRODUCT.db")
        cursor = con.execute("SELECT order_name,order_quantity,total_price FROM order_product WHERE order_id = "+ self.ORDER_ID.text() +" ")
        result = cursor.fetchall()
        r = 0
        c = 0
        for row_number, row_data in enumerate(result):
            r += 1
            c = 0
            for column_number, data in enumerate(row_data):
                c += 1
        self.INVOICE.setColumnCount(c)
        for row_number, row_data in enumerate(result):
            self.INVOICE.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.INVOICE.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        self.INVOICE.verticalHeader().setVisible(False)
        self.INVOICE.horizontalHeader().setVisible(False)
        self.tabWidget.setCurrentIndex(5)

    ## PRINT ##
    def printreceipt(self):
        if(self.GRAND_TOTAL.text() != "0.00"):
            printer = QPrinter()
            painter = QPainter()
            painter.begin(printer)
            screen = self.PRINTAREA.grab()
            painter.drawPixmap(10,10,screen)
            painter.end()
    ## LOGOUT ##
    def loguot(self):
            self.tabWidget.setCurrentIndex(0)
    def back_4(self):
        self.order_product()
        self.tabWidget.setCurrentIndex(1)
    
    ## BACK TO OPERATION ##
    def back_1(self):
        self.tabWidget.setCurrentIndex(1)
    def back_2(self):
        self.tabWidget.setCurrentIndex(1)
    def back_3(self):
        self.tabWidget.setCurrentIndex(1)
    

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
