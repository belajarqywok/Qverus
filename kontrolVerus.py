#!/bin/env python3

'''

follow : @qywok_exploiter_357

'''

import os
import sys
import json
import requests
class Dompet:
    def __init__(self,add):
        # mengambil API
        self.getData=json.loads(requests.get("https://luckpool.net/verus/miner/"+str(add)).content)
        self.vrscToUsd=json.loads(requests.get("https://luckpool.net/verus/market").content)
        self.payments=json.loads(requests.get("https://luckpool.net/verus/payments/"+str(add)).content)
    def hashrate(self):
        rate=str(self.getData["hashrateString"])
        self.a_kekuatan=""
        kekuatan=["KH","MH","GH"]
        satKekuatan=["lemah","sedang","kuat"]
        if rate[len(rate)-len(rate):len(rate)]=="0.00 H":
            self.a_kekuatan+="offline"
        else:
            for b_kekuatan in range(len(kekuatan)):
                if(rate[len(rate)-2:len(rate)]==kekuatan[b_kekuatan]):
                    for t_kekuatan in range(len(kekuatan)):
                        if(kekuatan[b_kekuatan]==kekuatan[t_kekuatan]):
                            self.a_kekuatan+=satKekuatan[t_kekuatan]
        return self.a_kekuatan
    def estimatedLuck(self):
        self.colLuck=""
        if(self.getData["estimatedLuck"]=="DEAD"):
            self.colLuck+="\33[31;1m"
        else:
            self.colLuck+="\33[36;1m"
        return self.colLuck
    ############################################# payment ##############################################
    def pembayaranTerkini(self):
        self.terkini=""
        lengthMinIndex=89
        lengthMinMoney=10
        length=0
        while length<=9:
            if(len(self.payments[0])==lengthMinIndex):
                if(len(self.payments[0][len(self.payments[0])-lengthMinMoney:len(self.payments[0])])==lengthMinMoney):
                    self.terkini+=self.payments[0][len(self.payments[0])-lengthMinMoney:len(self.payments[0])]
                    break
            else:
                lengthMinIndex+=1
                lengthMinMoney+=1
            length+=1
        return self.terkini
    def pembayaranWaktuItu(self):
        self.waktuItu=""
        lengthMinIndex=89
        lengthMinMoney=10
        length=0
        while length<=9:
            if(len(self.payments[1])==lengthMinIndex):
                if(len(self.payments[1][len(self.payments[1])-lengthMinMoney:len(self.payments[1])])==lengthMinMoney):
                    self.waktuItu+=self.payments[1][len(self.payments[1])-lengthMinMoney:len(self.payments[1])]
                    break
            else:
                lengthMinIndex+=1
                lengthMinMoney+=1
            length+=1
        return self.waktuItu
    def pembayaranKapanTau1(self):
        self.kapanTau1=""
        lengthMinIndex=89
        lengthMinMoney=10
        length=0
        while length<=9:
            if(len(self.payments[2])==lengthMinIndex):
                if(len(self.payments[2][len(self.payments[2])-lengthMinMoney:len(self.payments[2])])==lengthMinMoney):
                    self.kapanTau1+=self.payments[2][len(self.payments[2])-lengthMinMoney:len(self.payments[2])]
                    break
            else:
                lengthMinIndex+=1
                lengthMinMoney+=1
            length+=1
        return self.kapanTau1
    def pembayaranKapanTau2(self):
        self.kapanTau2=""
        lengthMinIndex=89
        lengthMinMoney=10
        length=0
        while length<=9:
            if(len(self.payments[3])==lengthMinIndex):
                if(len(self.payments[3][len(self.payments[3])-lengthMinMoney:len(self.payments[3])])==lengthMinMoney):
                    self.kapanTau2+=self.payments[3][len(self.payments[3])-lengthMinMoney:len(self.payments[3])]
                    break
            else:
                lengthMinIndex+=1
                lengthMinMoney+=1
            length+=1
        return self.kapanTau2
    def pembayaranKapanTau3(self):
        self.kapanTau3=""
        lengthMinIndex=89
        lengthMinMoney=10
        length=0
        while length<=9:
            if(len(self.payments[4])==lengthMinIndex):
                if(len(self.payments[4][len(self.payments[4])-lengthMinMoney:len(self.payments[4])])==lengthMinMoney):
                    self.kapanTau3+=self.payments[4][len(self.payments[4])-lengthMinMoney:len(self.payments[4])]
                    break
            else:
                lengthMinIndex+=1
                lengthMinMoney+=1
            length+=1
        return self.kapanTau3
    def pembayaranEntahKapan(self):
        self.entahKapan=""
        lengthMinIndex=89
        lengthMinMoney=10
        length=0
        while length<=9:
            if(len(self.payments[5])==lengthMinIndex):
                if(len(self.payments[5][len(self.payments[5])-lengthMinMoney:len(self.payments[5])])==lengthMinMoney):
                    self.entahKapan+=self.payments[5][len(self.payments[5])-lengthMinMoney:len(self.payments[5])]
                    break
            else:
                lengthMinIndex+=1
                lengthMinMoney+=1
            length+=1
        return self.entahKapan
    def pembayaranGatauKapan(self):
        self.gatauKapan=""
        lengthMinIndex=89
        lengthMinMoney=10
        length=0
        while length<=9:
            if(len(self.payments[6])==lengthMinIndex):
                if(len(self.payments[6][len(self.payments[6])-lengthMinMoney:len(self.payments[6])])==lengthMinMoney):
                    self.gatauKapan+=self.payments[6][len(self.payments[6])-lengthMinMoney:len(self.payments[6])]
                    break
            else:
                lengthMinIndex+=1
                lengthMinMoney+=1
            length+=1
        return self.gatauKapan
    ##################################################################################################################
try:
    namaDompet=sys.argv[1]
    cekDompet=Dompet(namaDompet)
    resWarna=""
    resKekuatan=["lemah","sedang","kuat"]
    warnaKekuatan=["\33[33;1m","\33[32;1m","\33[36;1m"]
    for resKekuatan1 in range(len(resKekuatan)):
        if(cekDompet.hashrate()==resKekuatan[resKekuatan1]):
            for resKekuatan2 in range(len(resKekuatan)):
                if(resKekuatan[resKekuatan1]==resKekuatan[resKekuatan2]):
                    resWarna+=warnaKekuatan[resKekuatan2]
    if __name__ == "__main__":
        print("\33[37;1m -------------------------------------------------------- ")
        print("\33[37;1m|__________ "+"\33[32;1m"+str(cekDompet.getData["address"])+"\33[37;1m __________|")
        print("\33[37;1m|________________________________________________________|")
        print("\33[37;1m| > |"+"\33[37;1m immature : "+"\33[1;33m"+str(cekDompet.getData["immature"]))
        print("\33[37;1m| > |"+"\33[37;1m balance : "+"\33[0;36m"+str(cekDompet.getData["balance"]))
        print("\33[37;1m| > |"+"\33[37;1m paid : "+"\33[0;32m"+str(cekDompet.getData["paid"])+"\33[36;1m [ Dollar( US ) : $"+str(float(cekDompet.getData["paid"]*cekDompet.vrscToUsd["price_usd"]))+" ] "+"\33[33;1m[ Bitcoin : "+str(float(cekDompet.getData["paid"]*cekDompet.vrscToUsd["price_btc"]))+"btc ]")
        print("\33[37;1m|--------------------------------------------------------|")
        print("\33[37;1m| > |"+"\33[37;1m hashrate : "+""+str(cekDompet.getData["hashrateString"])+"\33[37;1m [ "+str(resWarna)+cekDompet.hashrate()+"\33[37;1m ]")
        print("\33[37;1m| > |"+"\33[37;1m shares : "+""+str(cekDompet.getData["shares"]))
        print("\33[37;1m| > |"+"\33[37;1m efficiency : "+""+str(cekDompet.getData["efficiency"]))
        print("\33[37;1m| > |"+"\33[37;1m estimatedLuck : "+str(cekDompet.estimatedLuck())+str(cekDompet.getData["estimatedLuck"]))
        print("\33[37;1m|--------------------------------------------------------|")
        print("\33[37;1m| > |"+"\33[37;1m pembayaran/payments : ")
        print("\33[37;1m|")
        print("\33[37;1m| #+--+> |"+"\33[37;1m pembayaran terkini : "+"\33[36;1m"+str(cekDompet.pembayaranTerkini())+" [ $"+str(float(float(cekDompet.pembayaranTerkini())*cekDompet.vrscToUsd["price_usd"]))+" ]")
        print("\33[37;1m| #+--+> |"+"\33[37;1m pembayaran waktu itu : "+"\33[32;1m"+str(cekDompet.pembayaranWaktuItu())+" [ $"+str(float(float(cekDompet.pembayaranWaktuItu())*cekDompet.vrscToUsd["price_usd"]))+" ]")
        print("\33[37;1m| #+--+> |"+"\33[37;1m pembayaran kapan tau : "+"\33[33;1m"+str(cekDompet.pembayaranKapanTau1())+" [ $"+str(float(float(cekDompet.pembayaranKapanTau1())*cekDompet.vrscToUsd["price_usd"]))+" ]")
        print("\33[37;1m| #+--+> |"+"\33[37;1m pembayaran kapan tau : "+"\33[36;1m"+str(cekDompet.pembayaranKapanTau2())+" [ $"+str(float(float(cekDompet.pembayaranKapanTau2())*cekDompet.vrscToUsd["price_usd"]))+" ]")
        print("\33[37;1m| #+--+> |"+"\33[37;1m pembayaran kapan tau : "+"\33[32;1m"+str(cekDompet.pembayaranKapanTau3())+" [ $"+str(float(float(cekDompet.pembayaranKapanTau3())*cekDompet.vrscToUsd["price_usd"]))+" ]")
        print("\33[37;1m| #+--+> |"+"\33[37;1m pembayaran entah kapan : "+"\33[33;1m"+str(cekDompet.pembayaranEntahKapan())+" [ $"+str(float(float(cekDompet.pembayaranEntahKapan())*cekDompet.vrscToUsd["price_usd"]))+" ]")
        print("\33[37;1m| #+--+> |"+"\33[37;1m pembayaran gatau kapan : "+"\33[36;1m"+str(cekDompet.pembayaranGatauKapan())+" [ $"+str(float(float(cekDompet.pembayaranGatauKapan())*cekDompet.vrscToUsd["price_usd"]))+" ]")
except KeyboardInterrupt:
    os.system("clear")
    print("\ntekan CTRL + C lagi untuk keluar\n")
    sys.exit(0)
except KeyError:
    print("[ ! ] DATA TIDAK DIKETAHUI.......")


