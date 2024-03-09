from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from _dovizAppForm import Ui_MainWindow
import json
import requests

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCevir.clicked.connect(self.cevir)
        self.ui.btnConvert.clicked.connect(self.convert)
        self.ui.btnExit.clicked.connect(self.close)
        

    def cevir(self):
        url = "https://api.apilayer.com/exchangerates_data/latest?symbols="
        payload = {}
        headers= {"apikey": ""} 

        miktar_str = self.ui.txtMiktar.text()
        bozulan_doviz = self.ui.txtSatilan.text()
        alinan_doviz = self.ui.txtAlnan.text()

        # Boşluk kontrolü
        if not miktar_str or not bozulan_doviz or not alinan_doviz:
            self.ui.lblSonuc.setText(" alanları doldurun.")
            return

        # Hata kontrolü
        try:
            miktar = int(miktar_str)
        except ValueError:
            self.ui.lblSonuc.setText("geçersiz bir sayı.")
            return

        response = requests.request("GET", url+alinan_doviz+"&base="+bozulan_doviz, headers=headers, data = payload)
        status_code = response.status_code
        result = json.loads(response.text)
        try:
            sonuc = str(float(miktar) * float(result["rates"][alinan_doviz]))
            self.ui.lblSonuc.setText(sonuc + " " + alinan_doviz)
        except KeyError:
            self.ui.lblSonuc.setText("para birimi yok.")
            return
    def convert(self):
        
        url = "https://api.apilayer.com/exchangerates_data/latest?symbols="
        payload = {}
        headers= {"apikey": ""}

        #USD-TRY

        usd=self.ui.lblUsd.text()
        slot1=self.ui.lblSlot1.text()

        response = requests.request("GET", url+slot1+"&base="+usd, headers=headers, data = payload)
        status_code = response.status_code
        result =json.loads(response.text)
        self.ui.lblUsdTry.setText(str(float(result["rates"][slot1])))

        #EUR-TRY

        eur=self.ui.lblEur.text()
        slot2=self.ui.lblSlot2.text()

        response = requests.request("GET", url+slot2+"&base="+eur, headers=headers, data = payload)
        status_code = response.status_code
        result =json.loads(response.text)
        self.ui.lblEurTry.setText(str(float(result["rates"][slot2])))

        #GBP-TRY

        gbp=self.ui.lblGbp.text()
        slot3=self.ui.lblSlot3.text()

        response = requests.request("GET", url+slot3+"&base="+gbp, headers=headers, data = payload)
        status_code = response.status_code
        result =json.loads(response.text)
        self.ui.lblGbpTry.setText(str(float(result["rates"][slot3])))
    
    
    def close(self):
        quitmessage=QMessageBox.question(self,"Close","Are you sure ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if quitmessage==QMessageBox.Yes:
            quit()


def app():

    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()