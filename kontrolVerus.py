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
except KeyboardInterrupt:
    os.system("clear")
    print("\ntekan CTRL + C lagi untuk keluar\n")
    sys.exit(0)






