import psycopg2

from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from tkinter import scrolledtext
from tkinter import messagebox as msg
from secrets import randbelow
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("PROLAB")
        self.minsize(1800,900)
       # self.initUi()
       # self.initUI()
        # self.scrollText()

       # self.msgButton()
        # setup font options
        font_1 = font.Font(family='Arial', size=12)

        style = ttk.Style()
        style.configure('.', font=font_1)  # style for frame label text

        tabControl = ttk.Notebook(self)

        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Anasayfa")

        self.tab6 = ttk.Frame(tabControl)
        tabControl.add(self.tab6, text="Hammadde Ekle")

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text ="Hammadde Satın Alma")

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Ürün Üretme")

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text="Müşteri Ürün Satım")

        self.tab5 = ttk.Frame(tabControl)
        tabControl.add(self.tab5, text="Ürün Kar-Satış Geçmişi")



        tabControl.pack(expan =1, fill = "both")
        self.suppliersMaterial = []
        self.materialProductionCost = IntVar().get()
        self.stringConc = StringVar().get()
        self.connectDb()
        self.addingWidgets()
        self.addingWidgets2()
        self.Tab6()
        self.Tab2()
        self.Tab3()
        self.Tab4()
        self.Tab5()


    #Message Boxes
    # def msgButton(self):
    #     self.btn = ttk.Button(self, text="Open message box", command = self.infoMsgBox)
    #     self.btn.grid(column =0, row = 0)
    #
    # def infoMsgBox(self):
    #     msg.showerror("Python Message Info", "ERROR")

    #tabs

    def connectDb(self):
        # connect to the db
        self.con = psycopg2.connect(
            host="localhost",
            database='prolab3',
            user='postgres',
            password='112233',
        )

        self.cur = self.con.cursor()
        # execute
        # cur.execute("insert into customers (customer_name, adress) values (%s, %s)", ("Ali", "Istanbul") )

        self.cur.execute('SELECT "customer_id", "customer_name", "adress" FROM "customers"')

        self.rows = self.cur.fetchall()

        self.myCustomers = []
        for r in self.rows:
            self.myCustomers.append(r[1])

        self.cur.execute('SELECT "firm_id", "firm_name", "country", "city" FROM "suppliers"')

        self.suppliers = self.cur.fetchall()
        print(self.suppliers)
        self.cur.execute('SELECT DISTINCT "materiel_name" FROM "materials"')

        self.suppMaterials = self.cur.fetchall()

        self.suppMaterialsName = []
        for r in self.suppMaterials:
            self.suppMaterialsName.append(r[0])

        self.cur.execute('SELECT "material_id", "material_name", "stock", "price" FROM "manufacturers_materials"')

        self.myMaterials = self.cur.fetchall()

        self.cur.execute('SELECT "id", "location", "distance" FROM "shipping_costs"')

        self.shippingCosts = self.cur.fetchall()

        self.myMaterialsName = []
        for r in self.myMaterials:
            self.myMaterialsName.append(r[1])

        self.cur.execute('SELECT * FROM "products"')
        self.myProducts = self.cur.fetchall()

        self.myProductsName = []
        for r in self.myProducts:
            self.myProductsName.append(r[1])

        # print(type(rows))
        # for r in suppliers:
        #     print(f"id {r[0]} name {r[1]}")

        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

        # close the connection
       # self.con.close()
        #

    def clickMe(self):

        self.label.configure(text="Sectin")
        self.label.configure(foreground = "green")

    def infoMsgBox(self):
        msg.showerror("Hata", "Stok Yetersiz!")

    def infoMsgBox2(self):
        msg.showinfo("Eklendi", "Hammadde basarili bir sekilde eklendi")

    def addCustomer(self):

        self.l.delete('0', 'end')

        self.cur = self.con.cursor()

        self.cur.execute("insert into customers (customer_name,adress) values (%s, %s)", (self.custName.get(), self.custAddress.get()))

        self.cur.execute('SELECT "customer_id", "customer_name", "adress" FROM "customers"')
        self.rows = self.cur.fetchall()

        self.myCustomers = []
        for r in self.rows:
            self.myCustomers.append(r[1])

        self.combo6['values'] = self.myCustomers
        self.combo8['values'] = self.myCustomers
        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

        # close the connection
       # self.con.close()
        #

        for r in self.rows:
            self.l.insert(r[0], f"{r[1]}" + " / " f"{r[2]}")

    def addSupplier(self):


        self.cur = self.con.cursor()

        self.cur.execute("INSERT INTO suppliers (firm_name,country,city) VALUES (%s, %s, %s)", (self.suppName.get(), self.suppCountry.get(), self.suppCity.get()))

        # supps = self.cur.fetchall()
        # print(supps)
        # id = supps[0][0]
        # self.cur.execute("INSERT INTO materials (materiel_name,production_date,expire_date,quantity,price,firm_name) VALUES (%s, %s, %s, %s, %s, %s)",
        #                  (self.suppMaterial.get(), self.suppDate.get(), self.suppExpire.get(), self.suppStock.get(), self.suppPrice.get(), id))

        # self.cur.execute("insert into customers (customer_name,adress) values (%s, %s)",
        #                  (self.custName.get(), self.custAddress.get()))

        self.cur.execute('SELECT "firm_id", "firm_name", "country", "city" FROM "suppliers"')
        self.suppliers = self.cur.fetchall()
        self.l27.delete('0', 'end')
        for r in self.suppliers:
            self.l27.insert(r[0], f"{r[1]}" + " / " f"{r[2]}" + " / " f"{r[3]}")
        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

        # close the connection
        # self.con.close()
        #

    def addSupplierMaterial(self):
        self.cur = self.con.cursor()

        self.cur.execute("INSERT INTO materials (materiel_name,production_date,expire_date,quantity,price,firm_name) VALUES (%s, %s, %s, %s, %s, %s)",
                         (self.suppMaterial.get(), self.suppDate.get(), self.suppExpire.get(), self.suppStock.get(), self.suppPrice.get(), self.deleteSupp))
        self.infoMsgBox2()
        self.cur.execute('SELECT "firm_id", "firm_name", "country", "city" FROM "suppliers"')
        self.suppliers = self.cur.fetchall()
        self.l27.delete('0', 'end')
        for r in self.suppliers:
            self.l27.insert(r[0], f"{r[1]}" + " / " f"{r[2]}" + " / " f"{r[3]}")
        # commit the changes
        self.cur.execute('SELECT DISTINCT "materiel_name" FROM "materials"')

        self.suppMaterials = self.cur.fetchall()

        self.suppMaterialsName = []
        for r in self.suppMaterials:
            self.suppMaterialsName.append(r[0])

        self.combo11['values'] = self.suppMaterialsName


        self.con.commit()

        # close the cursor
        self.cur.close()

        # close the connection
        # self.con.close()

    def addShipping(self):
        self.l333.delete('0', 'end')

        self.cur = self.con.cursor()

        self.cur.execute("insert into shipping_costs (location,distance) values (%s, %s)",
                         (self.shippingLoc.get(), self.shippingCost.get()))

        self.cur.execute('SELECT "id", "location", "distance" FROM "shipping_costs"')

        self.shippingCosts = self.cur.fetchall()
        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

        # close the connection
        # self.con.close()
        #

        for r in self.shippingCosts:
            self.l333.insert(r[0], f"{r[1]}" + " / " f"{r[2]}")
    def deleteSupplier(self):
        self.l27.delete('0', 'end')

        self.cur = self.con.cursor()

        self.cur.execute(f"DELETE FROM suppliers WHERE (firm_id = '{self.deleteSupp}')")

        self.cur.execute('SELECT "firm_id", "firm_name", "country", "city" FROM "suppliers"')
        self.suppliers = self.cur.fetchall()

        for r in self.suppliers:
            self.l27.insert(r[0], f"{r[1]}" + " / " f"{r[2]}" + " / " f"{r[3]}")
        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()
    def deleteCustomer(self):
        self.l.delete('0', 'end')

        self.cur = self.con.cursor()

        self.cur.execute(f"DELETE FROM customers WHERE (customer_id = '{self.selected_customer_index}')")

        self.cur.execute('SELECT "customer_id", "customer_name", "adress" FROM "customers"')
        self.rows = self.cur.fetchall()
        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

        # close the connection
        # self.con.close()
        #

        for r in self.rows:
            self.l.insert(r[0], f"{r[1]}" + " / " f"{r[2]}")

    def UpdateCustomer(self):
        self.l.delete('0', 'end')

        self.cur = self.con.cursor()

        self.cur.execute(
            f"UPDATE customers SET customer_name='{self.custName.get()}',adress='{self.custAddress.get()}' WHERE (customer_id = '{self.selected_customer_index}')")

        self.cur.execute('SELECT "customer_id", "customer_name", "adress" FROM "customers"')
        self.rows = self.cur.fetchall()

        self.myCustomers = []
        for r in self.rows:
            self.myCustomers.append(r[1])

        self.combo6['values'] = self.myCustomers
        self.combo8['values'] = self.myCustomers
        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

        # close the connection
        # self.con.close()
        #

        for r in self.rows:
            self.l.insert(r[0], f"{r[1]}" + " / " f"{r[2]}")
    def updateSupplier(self):
        self.cur = self.con.cursor()

        self.cur.execute(f"UPDATE suppliers SET firm_name='{self.suppName.get()}',country='{self.suppCountry.get()}',city='{self.suppCity.get()}' WHERE (firm_id = '{self.deleteSupp}')")



        self.cur.execute('SELECT "firm_id", "firm_name", "country", "city" FROM "suppliers"')
        self.suppliers = self.cur.fetchall()
        self.l27.delete('0', 'end')
        for r in self.suppliers:
            self.l27.insert(r[0], f"{r[1]}" + " / " f"{r[2]}" + " / " f"{r[3]}")
        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

        # close the connection
        # self.con.close()
        #

    def onclick_event(self):
        # curselection() returns a tuple of indexes selected in listbox
        selection = self.l.curselection()


        if len(selection) > 0:
            # print("Clicked indexes: {0}".format(selection))
            # print(self.rows[selection[0]])
            self.selected_customer_index = self.rows[selection[0]][0]
            print(self.rows[selection[0]])

        # rows=[{23, "GG"},{44,"SA"}]

        # cur = con.cursor()
        #
        # #insert
        #
        # #
        # # commit the changes
        # con.commit()
        #
        # # close the cursor
        # cur.close()

    def onclick_event2(self):
        selection = self.l2.curselection()


        if len(selection) > 0:
            # print("Clicked indexes: {0}".format(selection))
            # print(self.rows[selection[0]])
            self.supplierSelectIndex = self.suppliersMaterial[selection[0]][0]
            self.supplierSelect = self.suppliersMaterial[selection[0]]
            print(self.suppliersMaterial[selection[0]])
            print(self.suppliersMaterial[selection[0]][0])

            # stok*fiyatim+fiyat*adet/stok+adet+Kargo parasi
        # self.shippingCostForMaterial

        self.cur = self.con.cursor()

        if self.supplierSelect[9].lower() == "türkiye":
            self.cur.execute(f"SELECT id, location, distance FROM shipping_costs WHERE location = '{self.supplierSelect[10]}'")

            distance = self.cur.fetchall()
            self.shippingCostForMaterial = distance[0][2] * 0.5
            print(self.quantity.get())
            ff = int(self.quantity.get())
            self.label202.configure(text=f"Kargo Parasi ile Yeni Fiyat: {ff * self.supplierSelect[5] + self.shippingCostForMaterial } TL")


        else:
            #yurdisi ise
            self.cur.execute(f"SELECT id, location, distance FROM shipping_costs WHERE location = '{self.supplierSelect[10]}'")
            distance = self.cur.fetchall()

            self.shippingCostForMaterial = distance[0][2] * 1
            self.label202.configure(text=f"Kargo Parasi ile Yeni Fiyat: {self.supplierSelect[5] + self.shippingCostForMaterial} TL")


        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

    def onclick_event4(self):
        selection = self.l27.curselection()

        if len(selection) > 0:
            self.deleteSupp = self.suppliers[selection[0]][0]
            # print("Clicked indexes: {0}".format(selection))
            # print(self.rows[selection[0]])
            print(self.suppliers[selection[0]])

    def addMaterialToFirm(self):
        self.l38.delete('0', 'end')

        self.cur = self.con.cursor()
        # firm id hard kodlu olmus duzelt

        self.cur.execute(f"INSERT INTO manufacturers_materials (material_name,stock,price,firm_name) VALUES ('{self.current_material}','0',0,'1')")

        self.cur.execute('SELECT "material_id", "material_name", "stock", "price" FROM "manufacturers_materials"')

        self.myMaterials = self.cur.fetchall()

        for r in self.myMaterials:
            self.l38.insert(r[0], f"Hammadde: {r[1]}" + "      Stok/ " f"{r[2]}")

        self.myMaterialsName = []

        for r in self.myMaterials:
            self.myMaterialsName.append(r[1])

        self.combo71['values'] = self.myMaterialsName
        self.combo5['values'] =self.myMaterialsName

        self.l3.delete('0', 'end')
        for r in self.myMaterials:
            self.l3.insert(r[0], f"Hammadde: {r[1]}" + "      Stok/ " f"{r[2]}")

        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

        # close the connection
        # self.con.close()
        #


    def searchMaterial(self):
        self.l2.delete('0', 'end')

        self.cur = self.con.cursor()

        #self.cur.execute("insert into customers (customer_name,adress) values (%s, %s)", (self.custName.get(), self.custAddress.get()))

        self.cur.execute(f"SELECT * FROM materials LEFT OUTER JOIN suppliers ON materials.firm_name = suppliers.firm_id WHERE materiel_name = '{self.material.get()}' ORDER BY price")
        self.suppliersMaterial = self.cur.fetchall()
        print(self.suppliersMaterial)
        for r in self.suppliersMaterial:
            self.l2.insert(r[0], f"Hammadde:{r[1]}" + f" Fiyat:{r[5]}  Stok: {r[4]} "f" Uretim Tarihi:{r[2]} " +  f" Omru: {r[3]}" + f" {r[8]}/{r[9]}/{r[10]}")

        self.cur.execute(f"SELECT * FROM manufacturers_materials WHERE manufacturers_materials.material_name = '{self.material.get()}'")
        self.stockWillChange = self.cur.fetchall()

        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

    def buyMaterial(self):
        print(self.supplierSelect[5])
        print(self.stockWillChange[0][2])
        print(self.stockWillChange[0][3])
        print(self.supplierSelect)


        quantityToNum=int(self.quantity.get())
        print("HELLASODL JASDMKhASKMD has")
        print(quantityToNum)
        # stok*fiyatim+fiyat*adet/stok+adet+Kargo parasi simdilik kargo parasi yok 1 tane tablo eklenek/STOK KONTROLU YAPICAK
        cost = quantityToNum * self.supplierSelect[5] + self.shippingCostForMaterial
        ##cost = (float(self.stockWillChange[0][2]) * float(self.stockWillChange[0][3]) + float(self.supplierSelect[5])* quantityToNum)/(float(self.stockWillChange[0][2]) + float(quantityToNum)) + self.shippingCostForMaterial  #SHIPPING COST FOR NOW
        print(cost)
        self.cur = self.con.cursor()
        self.cur.execute(
            f"SELECT * FROM manufacturers_materials WHERE manufacturers_materials.material_name = '{self.material.get()}'")
        self.stockWillChange = self.cur.fetchall()

        myTotalStock = int(self.stockWillChange[0][2]) + quantityToNum

        self.cur.execute(f"SELECT * FROM materials  LEFT OUTER JOIN suppliers ON materials.firm_name = suppliers.firm_id WHERE (materials.material_id = '{self.supplierSelect[0]}')")

        checkStock = self.cur.fetchall()

        if quantityToNum > checkStock[0][4]:
            self.infoMsgBox()
        else:
            self.cur.execute(
                'UPDATE "manufacturers_materials" SET "stock"=(%s),"price"=(%s) WHERE ("material_id" = (%s))', (myTotalStock,cost,self.stockWillChange[0][0]))

            # leftStock = self.supplierSelect[4] - quantityToNum
            leftStock = checkStock[0][4] - quantityToNum

            self.cur.execute(
                'UPDATE "materials" SET "quantity"=(%s) WHERE ("material_id" = (%s))',
                (leftStock, self.supplierSelect[0]))

           # self.suppliersMaterial = self.cur.fetchall()
            self.l3.delete('0', 'end')
            self.l4.delete('0', 'end')
            self.cur.execute(f"SELECT * FROM materials LEFT OUTER JOIN suppliers ON materials.firm_name = suppliers.firm_id WHERE materiel_name = '{self.material.get()}' ORDER BY price")

            self.suppliersMaterial = self.cur.fetchall()
            print(self.suppliersMaterial)
            for r in self.suppliersMaterial:
                self.l4.insert(r[0], f"Hammadde:{r[1]}" + f" Fiyat:{r[5]}  Stok: {r[4]} "f"  Uretim Tarihi:{r[2]} " +  f" Omru: {r[3]}" + f" {r[8]}/{r[9]}/{r[10]}")

            self.cur.execute('SELECT "material_id", "material_name", "stock", "price" FROM "manufacturers_materials"')

            self.myMaterials = self.cur.fetchall()

            for r in self.myMaterials:
                self.l3.insert(r[0], f"Hammadde: {r[1]}" + "      Stok/ " f"{r[2]}" + f" Birim Basina Maliyeti:  {round(float(r[3]),2)}")


        # commit the changes
        self.con.commit()

        # close the cursor
        self.cur.close()

    def display_selected_item_index(self):
        print(self.combo5.current())
        self.currentSelectedMaterial = self.myMaterials[self.combo5.current()]

    def display_selected_item_index2(self):
        print(self.combo6.current())
        self.currentSelectedCustomer = self.rows[self.combo6.current()]
        print(self.currentSelectedCustomer)
    def display_selected_item_index3(self):
        print(self.combo7.current())
        self.currentSelectedProduct = self.myProducts[self.combo7.current()]
        print(self.currentSelectedProduct)
    def display_selected_item_index4(self):
        print(self.combo8.current())
        self.current_customer = self.rows[self.combo8.current()]
        print(self.current_customer[0])
    def display_selected_item_index5(self):
        print(self.combo9.current())
        self.current_product = self.myProducts[self.combo9.current()]
        print(self.current_product)

    def display_selected_item_index6(self):
        print(self.combo11.current())
        self.current_material = self.suppMaterials[self.combo11.current()][0]
        print(self.current_material)

    def addMaterial(self):
        self.cur = self.con.cursor()

        self.cur.execute(f"SELECT * FROM manufacturers_materials WHERE (manufacturers_materials.material_id = '{self.currentSelectedMaterial[0]}')")

        tempSelectedMat= self.cur.fetchall()
        totalQuant = self.addQuantity.get() * self.addProductQuantity.get()
        # queryden cekip kontrol et onceden cektigin queryle degil
        if totalQuant > int(tempSelectedMat[0][2]):
            self.infoMsgBox()
        else:
            self.stringConc += self.materialProduction.get() + f"^{self.addQuantity.get()}"
            self.materialProductionCost += float(self.currentSelectedMaterial[3]) * totalQuant
            print(self.materialProductionCost)
            currentStock = int(tempSelectedMat[0][2]) - totalQuant
            print(currentStock)


            self.cur.execute(
                'UPDATE "manufacturers_materials" SET "stock"=(%s) WHERE ("material_id" = (%s))',
                (currentStock, self.currentSelectedMaterial[0]))

            self.cur.execute('SELECT "material_id", "material_name", "stock", "price" FROM "manufacturers_materials"')

            self.myMaterials = self.cur.fetchall()

            self.l40.delete('0', 'end')

            for r in self.myMaterials:
                self.l40.insert(r[0], f"Hammadde: {r[1]}" + "      Stok/ " f"{r[2]}")


            print(self.materialProductionCost)

            print(self.stringConc)
            self.label30.configure(text=self.stringConc)
        self.con.commit()

        # close the cursor
        self.cur.close()

    def produceProduct(self):


        self.cur = self.con.cursor()

        self.cur.execute(
            "select * from products where product_name = '{0}'".format(self.productName.get().lower()))

        rows = self.cur.fetchall()
        print(rows)
        if len(rows) == 0:
            newStock = self.addProductQuantity.get()
            laborCost = self.addProductQuantity.get()
            totalCost = self.materialProductionCost + laborCost
            price = totalCost + totalCost * 0.2
            irand = randbelow(10)
            # firm nama degistir
            self.cur.execute(
                f"INSERT INTO products (product_name,components,expire_date,stock,labor_cost,total_cost,price,production_date,firm_name) VALUES ('{self.productName.get().lower()}','{self.stringConc}','{self.expire43.get()}','{newStock}','{int(laborCost)}','{int(totalCost)}','{int(price)}','{self.date43.get()}','1')")


        else:
            print("HELLLO")
            print(rows)
            print(rows[0][4])
            print(rows[0][0])
            newStock = rows[0][4] + self.addProductQuantity.get()
            laborCost = self.addProductQuantity.get()
            totalCost = self.materialProductionCost + laborCost
            price = totalCost + totalCost * 0.2
            print(newStock)
            print(laborCost)
            print(totalCost)
            print(price)

            self.cur.execute(
                'UPDATE "products" SET "stock"='f"{newStock}"',"labor_cost"='f"{laborCost}"',"total_cost"='f"{totalCost}"',"price"='f"{price}"' WHERE ("product_id" = 'f"{rows[0][0]}"')')
        self.stringConc =""
        self.label30.configure(text=self.stringConc)
        self.l55.delete('0', 'end')

        self.cur.execute('SELECT * FROM "products"')
        self.myProducts = self.cur.fetchall()
        self.myProductsName = []
        for r in self.myProducts:
            self.myProductsName.append(r[1])
        # insert combo7
        self.combo7['values'] = self.myProductsName
        self.combo9['values'] = self.myProductsName
        for r in self.myProducts:
            self.l55.insert(r[0], f"Urun: {r[1]}/{r[2]} Fiyat: {r[7]} Uretim Tarihi: {r[8]}" + " Omru: " f"{r[3]} Stok: {r[4]} Isci Maliyet: {r[5]} Total Maliyet: {r[6]} ")
        self.con.commit()
        # close the cursor
        self.cur.close()


    def sellProduct(self):
        print("hello")
        print(self.currentSelectedCustomer)
        print(self.currentSelectedProduct)
        print(self.quantityforsale.get())

        self.cur = self.con.cursor()

        self.cur.execute('SELECT * FROM "products" WHERE ("products"."product_id" = 'f"{self.currentSelectedProduct[0]}"')')

        self.temp = self.cur.fetchall()
        if self.quantityforsale.get() > self.temp[0][4]:
            self.infoMsgBox()
        else:
             newStock = self.temp[0][4] - self.quantityforsale.get()
             profit = self.temp[0][7] - self.temp[0][6]
             self.cur.execute('UPDATE "products" SET "stock"='f"{newStock}"' WHERE ("product_id" = 'f"{self.temp[0][0]}"')')

             self.cur.execute(f"INSERT INTO sold_products (purchased_product,quantity,amount_due,profit_from_sale,customer_name) VALUES ('{self.temp[0][1]}','{self.quantityforsale.get()}','{self.temp[0][7]}','{profit}','{self.currentSelectedCustomer[0]}')")

             self.cur.execute('SELECT * FROM "products"')

             row = self.cur.fetchall()
             self.l66.delete('0', 'end')
             for r in row:
                 self.l66.insert(r[0], f"Urun: {r[1]}/{r[2]} Fiyat: {r[7]}" + f" Stok: {r[4]} Isci Maliyet: {r[5]} Total Maliyet: {r[6]} ")

             self.cur.execute('SELECT * FROM "sold_products" LEFT OUTER JOIN "customers" ON "sold_products"."customer_name" = "customers"."customer_id"')
             self.l77.delete('0', 'end')
             product_sold = self.cur.fetchall()
             print("BURAYA BAK")
             print(product_sold)
             for r in product_sold:
                 self.l77.insert(r[0], f"Satis_Urun: {r[1]} Satilan Adet: {r[2]}" + " Odenen Miktar: " f"{r[3]}  Musteri Adi: {r[7]}")



        self.con.commit()
        # close the cursor
        self.cur.close()


    def customerHistory(self):
        self.cur = self.con.cursor()

        self.cur.execute('SELECT SUM(profit_from_sale) AS "Total Profit" FROM "sold_products" LEFT OUTER JOIN "customers"  ON "sold_products"."customer_name" = "customers"."customer_id" WHERE "sold_products"."customer_name" = 'f"{self.current_customer[0]}"'')

        rows = self.cur.fetchall()

        print(rows[0][0])
        self.label98.configure(text=f"{self.current_customer[1]} Musterisinden Elde Edilen Kar: {rows[0][0]} TL")

        self.cur.execute('SELECT * FROM "sold_products" LEFT OUTER JOIN "customers"  ON "sold_products"."customer_name" = "customers"."customer_id" WHERE "sold_products"."customer_name" = 'f"{self.current_customer[0]}"'')

        rows2 = self.cur.fetchall()
        print(rows2)
        self.l53.delete('0', 'end')
        for r in rows2:
            self.l53.insert(r[0], f" Musteri Adi: {r[7]} Satilan Urun: {r[1]} Satistan Kar: {r[4]} Satilan Adet: {r[2]}" + " Odenen Miktar: " f"{r[3]} ")

       # self.cur.execute('SELECT * FROM "sold_products" LEFT OUTER JOIN "customers" ON "sold_products"."customer_name" = "customers"."customer_id" WHERE "sold_products"."purchased_product" = 'f"{}"'')

        # self.cur.execute('SELECT * FROM "products" WHERE ("products"."product_id" = 'f"{self.currentSelectedProduct[0]}"')')

        self.con.commit()
        # close the cursor
        self.cur.close()

    def productHistory(self):
        self.cur = self.con.cursor()

        self.cur.execute(
            "SELECT SUM(profit_from_sale) FROM sold_products LEFT OUTER JOIN customers ON sold_products.customer_name = customers.customer_id WHERE sold_products.purchased_product = '{0}'".format(self.current_product[1]))

        rows = self.cur.fetchall()

        print(rows[0][0])
        self.label99.configure(text=f"{self.current_product[1]} Urununden Elde Edilen Kar: {rows[0][0]} TL")

        self.cur.execute(
            "SELECT * FROM sold_products LEFT OUTER JOIN customers ON sold_products.customer_name = customers.customer_id WHERE sold_products.purchased_product = '{0}'".format(self.current_product[1]))

        rows2 = self.cur.fetchall()
        print(rows2)
        self.l53.delete('0', 'end')
        for r in rows2:
            self.l53.insert(r[0], f"  Satilan Urun: {r[1]} Satistan Kar: {r[4]} Satilan Adet: {r[2]}" + " Odenen Miktar: " f"{r[3]} Musteri Adi: {r[7]} ")

        # self.cur.execute('SELECT * FROM "sold_products" LEFT OUTER JOIN "customers" ON "sold_products"."customer_name" = "customers"."customer_id" WHERE "sold_products"."purchased_product" = 'f"{}"'')

        # self.cur.execute('SELECT * FROM "products" WHERE ("products"."product_id" = 'f"{self.currentSelectedProduct[0]}"')')

        self.con.commit()
        # close the cursor
        self.cur.close()

    def totalProfit(self):
        self.cur = self.con.cursor()

        self.cur.execute("SELECT SUM(profit_from_sale) FROM sold_products")
        rows = self.cur.fetchall()
        print("TOPLAM KAR")
        print(rows[0][0])

        self.label100.configure(text=f"Suana Kadar Elde Edilen Toplam Kar: {rows[0][0]}")
        self.con.commit()
        # close the cursor
        self.cur.close()

    def addingWidgets(self):

        labelFrame = ttk.LabelFrame(self.tab1, text="Musterilerim")
        labelFrame.grid(column = 0, row = 0, padx=8, pady = 40)

        self.l = Listbox(labelFrame, width=50, height= 15, selectmode = SINGLE, font=30)
        self.l.pack(side="left", fill="y")
        self.l.bind('<<ListboxSelect>>', lambda event: self.onclick_event())
        for r in self.rows:
            self.l.insert(r[0], f"{r[1]}" + " / " f"{r[2]}")


       # self.l.grid(column = 0, row=0, sticky="w")

        scrollbar = Scrollbar(labelFrame, orient="vertical")
        scrollbar.config(command=self.l.yview)
        scrollbar.pack(side="right", fill="y")
        self.l.config(yscrollcommand=scrollbar.set)

        labelFrame = ttk.LabelFrame(self.tab1, text="Kargo Ucretleri")
        labelFrame.place(x= 1120, y = 50)

        self.l333 = Listbox(labelFrame, width=50, height=15, selectmode=SINGLE, font=30)
        # self.l333.bind('<<ListboxSelect>>', lambda event: self.onclick_event())
        for r in self.shippingCosts:
            self.l333.insert(r[0], f"{r[1]}" + " / Mesafe: " f"{r[2]}")

        self.l333.grid(column=0, row=0, sticky="w")


        self.button = ttk.Button(self.tab1, text="Ekle", command = self.addCustomer)
        self.button.place(x=594, y= 220)
        self.button2 = ttk.Button(self.tab1, text="Sil", command=self.deleteCustomer)
        self.button2.place(x=594, y= 260)
        self.button3 = ttk.Button(self.tab1, text="Guncellle", command=self.UpdateCustomer)
        self.button3.place(x=594, y=300)

        labelFrame2 = ttk.LabelFrame(self.tab1, text="Tedarikcilerim")
        labelFrame2.grid(column=0, row=1, padx=8, pady=40)

        self.l27 = Listbox(labelFrame2, width=50, height=20, selectmode=SINGLE, font=30)
        self.l27.bind('<<ListboxSelect>>', lambda event: self.onclick_event4())
        self.l27.pack(side="left", fill="y")

        for r in self.suppliers:
            self.l27.insert(r[0], f"{r[1]}" + " / " f"{r[2]}" + " / " f"{r[3]}")

        self.l27.grid(column=0, row=0, sticky="w")

        self.button3 = ttk.Button(self.tab1, text="Ekle", command=self.addSupplier)
        self.button3.place(x=550, y=480)
        self.button4 = ttk.Button(self.tab1, text="Sil", command=self.deleteSupplier)
        self.button4.place(x=550, y=520)

        self.button5 = ttk.Button(self.tab1, text="Tedarikci Urun Ekle", command=self.addSupplierMaterial)
        self.button5.place(x=550, y=670)

        self.button6 = ttk.Button(self.tab1, text="Guncelle", command=self.updateSupplier)
        self.button6.place(x=550, y=560)



    def addingWidgets2(self):
        labelFrame = ttk.LabelFrame(self.tab1, text="Musteri Ekleme Bolumu",)
        labelFrame.place(x= 590, y=80)

        self.custName = StringVar()
        self.custAddress = StringVar()
        self.name = StringVar()
        self.Adress = StringVar()

        self.suppName = StringVar()
        self.suppCountry = StringVar()
        self.suppCity = StringVar()

        self.suppMaterial = StringVar()
        self.suppStock = IntVar()
        self.suppDate = StringVar()
        self.suppExpire = StringVar()
        self.suppPrice = IntVar()

        self.shippingLoc = StringVar()
        self.shippingCost = IntVar()

        self.label0 = ttk.Label(labelFrame, text="Musteri Adi Soyadi")
        self.label0.grid(column = 0, row=0, sticky = "w")

        self.textbox = ttk.Entry(labelFrame, width = 40, textvariable = self.custName)
        self.textbox.grid(column = 1, row =0 )

        self.label1 = ttk.Label(labelFrame, text="Musteri Adresi")
        self.label1.grid(column=0, row=1, sticky="w", pady=10)

        self.textbox2 = ttk.Entry(labelFrame, width=40, textvariable=self.custAddress)
        self.textbox2.grid(column=1, row=1)



        labelFrame2 = ttk.LabelFrame(self.tab1, text="Tedarikci Ekleme Bolumu", )
        labelFrame2.place(x=700, y=450)

        #onchange event

        self.label2 = ttk.Label(labelFrame2, text="Tedarikci Adi ")
        self.label2.grid(column=0, row=0, sticky="w")

        self.textbox = ttk.Entry(labelFrame2, width=40, textvariable=self.suppName)
        self.textbox.grid(column=1, row=0)

        self.label3 = ttk.Label(labelFrame2, text="Ulke")
        self.label3.grid(column=0, row=1, sticky="w", pady=10)

        self.textbox2 = ttk.Entry(labelFrame2, width=40, textvariable=self.suppCountry)
        self.textbox2.grid(column=1, row=1)

        self.label4 = ttk.Label(labelFrame2, text="Sehir")
        self.label4.grid(column=0, row=2, sticky="w", pady=10)

        self.textbox3 = ttk.Entry(labelFrame2, width=40, textvariable=self.suppCity)
        self.textbox3.grid(column=1, row=2)

        labelFrame2 = ttk.LabelFrame(self.tab1, text="Kargo Fiyat Bilgisi Ekle", )
        labelFrame2.place(x=1120, y=450)

        # onchange event

        self.label2 = ttk.Label(labelFrame2, text="Ulke/Sehir ")
        self.label2.grid(column=0, row=0, sticky="w")

        self.textbox = ttk.Entry(labelFrame2, width=40, textvariable=self.shippingLoc)
        self.textbox.grid(column=1, row=0)

        self.label3 = ttk.Label(labelFrame2, text="Kargo Fiyati")
        self.label3.grid(column=0, row=1, sticky="w", pady=10)

        self.textbox2 = ttk.Entry(labelFrame2, width=40, textvariable=self.shippingCost)
        self.textbox2.grid(column=1, row=1)

        self.button6 = ttk.Button(labelFrame2, text="Ekle", command=self.addShipping)
        self.button6.grid(column=2, row=1, padx=10)

        labelFrame3 = ttk.LabelFrame(self.tab1, text="Tedarikci Urunu", )
        labelFrame3.place(x=700, y=600)

        # onchange event

        self.label3 = ttk.Label(labelFrame3, text="Hammadesi  ")
        self.label3.grid(column=0, row=0, sticky="w")

        self.textbox = ttk.Entry(labelFrame3, width=40, textvariable=self.suppMaterial)
        self.textbox.grid(column=1, row=0)

        self.label3 = ttk.Label(labelFrame3, text="Stoğu")
        self.label3.grid(column=0, row=1, sticky="w", pady=10)

        self.textbox2 = ttk.Entry(labelFrame3, width=40, textvariable=self.suppStock)
        self.textbox2.grid(column=1, row=1)

        self.label4 = ttk.Label(labelFrame3, text="Uretim Tarihi")
        self.label4.grid(column=0, row=2, sticky="w", pady=10)

        self.textbox3 = ttk.Entry(labelFrame3, width=40, textvariable=self.suppDate)
        self.textbox3.grid(column=1, row=2)

        self.label4 = ttk.Label(labelFrame3, text="Raf Ömrü")
        self.label4.grid(column=0, row=3, sticky="w", pady=10)

        self.textbox3 = ttk.Entry(labelFrame3, width=40, textvariable=self.suppExpire)
        self.textbox3.grid(column=1, row=3)

        self.label4 = ttk.Label(labelFrame3, text="Fiyatı")
        self.label4.grid(column=0, row=4, sticky="w", pady=10)

        self.textbox3 = ttk.Entry(labelFrame3, width=40, textvariable=self.suppPrice)
        self.textbox3.grid(column=1, row=4)





        # label = ttk.Label(labelFrame, text = "Enter your name:")
        # label.grid(column = 0, row = 0, sticky = "w")
        #
        # textedit = Entry(labelFrame, width = 20)
        # textedit.grid(column =1, row=0)

    def Tab2(self):
        labelFrame = ttk.LabelFrame(self.tab2, text="En dusuk Fiyata Satan Tedarikciler")
        labelFrame.grid(column = 1, row = 0, padx=8, pady = 40)

        self.l2 = Listbox(labelFrame, width=80, height= 15, selectmode = SINGLE, font=30)
        self.l2.bind('<<ListboxSelect>>', lambda event: self.onclick_event2())
        self.l2.pack(side="left", fill="y")
       # self.l2.grid(column = 0, row=0, sticky="w")
        scrollbar = Scrollbar(labelFrame, orient="vertical")
        scrollbar.config(command=self.l2.yview)
        scrollbar.pack(side="right", fill="y")
        self.l2.config(yscrollcommand=scrollbar.set)


        self.label202 = ttk.Label(self.tab2, text="")
        self.label202.place(x=1510, y=180)

        self.button = ttk.Button(self.tab2, text="Satin Al", command = self.buyMaterial)
        self.button.grid(column=2, row=0)


        labelFrame2 = ttk.LabelFrame(self.tab2, text="Hammadde Al")
        labelFrame2.grid(column=0, row=0, padx=8, pady=40)

        self.material = StringVar()
        self.label = ttk.Label(labelFrame2, text="Hammadde Sec")
        self.label.grid(column=0, row=0)
        self.combo71 = ttk.Combobox(labelFrame2, width = 15, textvariable = self.material)


        self.combo71['values'] =self.myMaterialsName

        self.combo71.grid(column = 0, row =1, pady=10)

        self.button = ttk.Button(labelFrame2, text ="Arat", command = self.searchMaterial)
        self.button.grid(column = 1, row =1)

        self.quantity = IntVar()


        self.label = ttk.Label(labelFrame2, text="Adet")
        self.label.grid(column=0, row=2, sticky="w")

        self.textbox = ttk.Entry(labelFrame2, width=20, textvariable=self.quantity)
        self.textbox.grid(column=0, row=3, padx=10)


        labelFrame3 = ttk.LabelFrame(self.tab2, text="Stogumdaki Hammaddelerin Durumu")
        labelFrame3.grid(column=0, row=1, padx=8, pady=40)

        self.l3 = Listbox(labelFrame3, width=50, height=20, selectmode=SINGLE, font=30)

        for r in self.myMaterials:
            self.l3.insert(r[0], f"Hammadde: {r[1]}" + "      Stok/ " f"{r[2]}")

        self.l3.grid(column=0, row=0, sticky="w")

        labelFrame4 = ttk.LabelFrame(self.tab2, text="Tedarikci Stok Durumu")
        labelFrame4.grid(column=1, row=1, padx=30, pady=40)

        self.l4 = Listbox(labelFrame4, width=80, height=20, selectmode=SINGLE, font=30)


        self.l4.grid(column=0, row=0, sticky="w")

    def Tab3(self):
        labelFrame = ttk.LabelFrame(self.tab3, text="Urun Uret")
        labelFrame.grid(column=0, row=0, padx=8, pady=60)

        self.materialProduction = StringVar()

        self.addQuantity = IntVar()
        self.expire43 = IntVar()
        self.date43 = StringVar()
        self.addProductQuantity = IntVar()
        self.productName = StringVar()

        self.label = ttk.Label(labelFrame, text="Stogundan Hammadde Sec")
        self.label.grid(column=0, row=4)

        self.combo5 = ttk.Combobox(labelFrame, width=15, textvariable=self.materialProduction)
        self.combo5['values'] = self.myMaterialsName
        self.combo5.bind("<<ComboboxSelected>>", lambda event: self.display_selected_item_index())
        self.combo5.grid(column=0, row=5, pady=10)

        self.button = ttk.Button(labelFrame, text="Ekle", command=self.addMaterial)
        self.button.grid(column=1, row=6)

        self.name = StringVar()
        self.Adress = StringVar()

        self.label = ttk.Label(labelFrame, text="Adet")
        self.label.grid(column=0, row=6, sticky="w")
        self.textbox = ttk.Entry(labelFrame, width=20, textvariable=self.addQuantity)
        self.textbox.grid(column=0, row=7, padx=10)

        self.label = ttk.Label(labelFrame, text="Olusacak Urun:")
        self.label.grid(column=0, row=8, sticky="w")

        self.label = ttk.Label(labelFrame, text="Raf Omru")
        self.label.grid(column=0, row=10, sticky="w")
        self.textbox = ttk.Entry(labelFrame, width=20, textvariable=self.expire43)
        self.textbox.grid(column=0, row=11, padx=10)

        self.label = ttk.Label(labelFrame, text="Uretim Tarihi")
        self.label.grid(column=0, row=12, sticky="w")
        self.textbox = ttk.Entry(labelFrame, width=20, textvariable=self.date43)
        self.textbox.grid(column=0, row=13, padx=10)




        self.label = ttk.Label(labelFrame, text="Adet")
        self.label.grid(column=0, row=2, sticky="w")
        self.textbox = ttk.Entry(labelFrame, width=20, textvariable=self.addProductQuantity)
        self.textbox.grid(column=0, row=3, padx=10, pady=5)


        self.label = ttk.Label(labelFrame, text="Urunun Adini Gir")
        self.label.grid(column=0, row=0, sticky="w")

        self.textbox = ttk.Entry(labelFrame, width=20, textvariable=self.productName)
        self.textbox.grid(column=0, row=1, padx=10)

        self.label30 = ttk.Label(labelFrame, text="")
        self.label30.grid(column=0, row=9, sticky="w")

        self.button = ttk.Button(labelFrame, text="Uret", command=self.produceProduct)
        self.button.grid(column=1, row=10)

        labelFrame2 = ttk.LabelFrame(self.tab3, text="Hammadde Stogumun Durumu")
        labelFrame2.grid(column=0, row=1, padx=8, pady=40)

        self.l40 = Listbox(labelFrame2, width=50, height=20, selectmode=SINGLE, font=30)

        self.l40.grid(column=0, row=0, sticky="w")

        labelFrame3 = ttk.LabelFrame(self.tab3, text="Urunlerimin Durumu")
        labelFrame3.grid(column=1, row=1, padx=8, pady=40)

        self.l55 = Listbox(labelFrame3, width=90, height=20, selectmode=SINGLE, font=30)

        self.l55.grid(column=0, row=0, sticky="w")

    def Tab4(self):
        labelFrame = ttk.LabelFrame(self.tab4, text="Musteri Sec")
        labelFrame.grid(column=0, row=0, padx=8, pady=60)

        self.customer_name = StringVar()
        self.product_name = StringVar()
        self.myfruit = StringVar()
        self.quantityforsale = IntVar()
        self.combo6 = ttk.Combobox(labelFrame, width=25, textvariable=self.customer_name)
        self.label = ttk.Label(labelFrame, text="Musteri")
        self.label.grid(column=0, row=0)

        self.combo6['values'] = self.myCustomers
        self.combo6.bind("<<ComboboxSelected>>", lambda event: self.display_selected_item_index2())
        self.combo6.grid(column=0, row=1, pady=10)

        # self.button = ttk.Button(labelFrame, text="Sec", command=self.clickMe)
        # self.button.grid(column=1, row=1)

        self.label = ttk.Label(labelFrame, text="Urun")
        self.label.grid(column=0, row=2)

        self.combo7 = ttk.Combobox(labelFrame, width=15, textvariable=self.product_name)
        self.combo7.bind("<<ComboboxSelected>>", lambda event: self.display_selected_item_index3())
        self.combo7['values'] = self.myProductsName

        self.combo7.grid(column=0, row=3, pady=10)

        # self.button = ttk.Button(labelFrame, text="Sec", command=self.clickMe)
        # self.button.grid(column=1, row=2)

        self.name = StringVar()
        self.Adress = StringVar()

        self.label = ttk.Label(labelFrame, text="Adet")
        self.label.grid(column=0, row=4, sticky="w")
        self.textbox = ttk.Entry(labelFrame, width=20, textvariable=self.quantityforsale)
        self.textbox.grid(column=0, row=5, padx=10)

        self.button = ttk.Button(labelFrame, text="Sat", command=self.sellProduct)
        self.button.grid(column=1, row=5)

        labelFrame2 = ttk.LabelFrame(self.tab4, text="Urun Stok Durumum")
        labelFrame2.grid(column=0, row=1, padx=8, pady=60)

        self.l66 = Listbox(labelFrame2, width=70, height=20, selectmode=SINGLE, font=30)

        self.l66.grid(column=0, row=0, sticky="w")

        labelFrame3 = ttk.LabelFrame(self.tab4, text="Urun Satis Kaydi")
        labelFrame3.grid(column=1, row=1, padx=8, pady=60)

        self.l77 = Listbox(labelFrame3, width=85, height=20, selectmode=SINGLE, font=30)

        self.l77.grid(column=0, row=0, sticky="w")

    def Tab5(self):

        self.selected_customer = StringVar()
        self.selected_product = StringVar()

        labelFrame = ttk.LabelFrame(self.tab5, text="Satis Sonuclari")
        labelFrame.grid(column=0, row=0, padx=8, pady=40)

        self.l53 = Listbox(labelFrame, width=90, height=30, selectmode=SINGLE, font=30)

        self.l53.grid(column=0, row=0, sticky="w")

        labelFrame2 = ttk.LabelFrame(self.tab5, text="Elde Ettigim Kar Degerleri")
        labelFrame2.place(x=1030, y=50)

        self.label = ttk.Label(labelFrame2, text="Musteri Bazinda Kar")
        self.label.grid(column=0, row=1)
        self.combo8 = ttk.Combobox(labelFrame2, width=65, textvariable=self.selected_customer)
        self.combo8['values'] = self.myCustomers
        self.combo8.bind("<<ComboboxSelected>>", lambda event: self.display_selected_item_index4())
        self.combo8.grid(column=0, row=2, pady=10)

        self.button = ttk.Button(labelFrame2, text="Arat", command=self.customerHistory)
        self.button.grid(column=1, row=2)
        self.label98 = ttk.Label(labelFrame2, text="")
        self.label98.grid(column=0, row=3, sticky="w")

        self.label = ttk.Label(labelFrame2, text="Urun Bazinda Kar")
        self.label.grid(column=0, row=4, pady=5)
        self.combo9 = ttk.Combobox(labelFrame2, width=65, textvariable=self.selected_product)
        self.combo9['values'] = self.myProductsName
        self.combo9.bind("<<ComboboxSelected>>", lambda event: self.display_selected_item_index5())
        self.combo9.grid(column=0, row=5, pady=5)

        self.button = ttk.Button(labelFrame2, text="Arat", command=self.productHistory)
        self.button.grid(column=1, row=5)
        self.label99 = ttk.Label(labelFrame2, text="")
        self.label99.grid(column=0, row=6, sticky="w")

        self.label = ttk.Label(labelFrame2, text="Tum Satislardan Elde Edilen Toplam Kar")
        self.label.grid(column=0, row=7, pady=10)
        self.button = ttk.Button(labelFrame2, text="Hesapla", command=self.totalProfit)
        self.button.grid(column=1, row=7)
        self.label100 = ttk.Label(labelFrame2, text="")
        self.label100.grid(column=0, row=8, sticky="w")


    def Tab6(self):
        labelFrame60 = ttk.LabelFrame(self.tab6, text="Hammadde Al")
        labelFrame60.grid(column=0, row=0, padx=8, pady=40)

        self.material = StringVar()
        self.label = ttk.Label(labelFrame60, text="Hammadde Sec")
        self.label.grid(column=0, row=0)
        self.combo11 = ttk.Combobox(labelFrame60, width=15, textvariable=self.material)

        self.combo11['values'] = self.suppMaterialsName
        self.combo11.bind("<<ComboboxSelected>>", lambda event: self.display_selected_item_index6())
        self.combo11.grid(column=0, row=1, pady=10)

        self.button = ttk.Button(labelFrame60, text="Ekle", command=self.addMaterialToFirm)
        self.button.grid(column=1, row=1)

        labelFrame33 = ttk.LabelFrame(self.tab6, text="Stogumdaki Hammaddelerin Durumu")
        labelFrame33.grid(column=0, row=1, padx=8, pady=40)

        self.l38 = Listbox(labelFrame33, width=60, height=25, selectmode=SINGLE, font=30)

        for r in self.myMaterials:
            self.l38.insert(r[0], f"Hammadde: {r[1]}" + "      Stok/ " f"{r[2]}")

        self.l38.grid(column=0, row=0, sticky="w")


root = Root()
text = Text(root)
root.mainloop()