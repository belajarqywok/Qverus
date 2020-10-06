#!/bin/env python3
import sys
import json
import requests
namaDompet=sys.argv[1]
data=requests.get("https://luckpool.net/verus/miner/"+str(namaDompet))
getData=json.loads(data.content)
if __name__ == "__main__":
    print(" -------------------------------------------------------- ")
    print("|__________ "+str(getData["address"])+" __________|")
    print("|________________________________________________________|")
    print("| > |"+" immature : "+str(getData["immature"]))
    print("| > |"+" balance : "+str(getData["balance"]))
    print("| > |"+" paid : "+str(getData["paid"]))
    print("|--------------------------------------------------------|")
    print("| > |"+" hashrate : "+str(getData["hashrateString"]))
    print("| > |"+" shares : "+str(getData["shares"]))
    print("| > |"+" efficiency : "+str(getData["efficiency"]))
    print("| > |"+" estimatedLuck : "+str(getData["estimatedLuck"]))



