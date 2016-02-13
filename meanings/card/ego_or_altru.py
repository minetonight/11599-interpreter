#-*-coding:utf8;-*-

buf = "" 

if (card[1] > 1) and (card[4] > 0) and (card[7] > 0) and (card[5] > 0):
    buf += "ти си атруист" 
else:
    buf += "не си алтруист" 

buf += "\n" 

if (card[3] > 0) and (card[6] > 0) and (card[9] > 1) and (card[5] > 0):
    buf += "ти си егоист" 
else:
    buf += "не си егоист" 
    
buf += "\n" 

ego_power = card[3] + card[6] + card[9] + card[5]

atru_power = card[1] + card[4] + card[7] + card[5]

buf += "Баланс на атруизма %d/5 \n\
Баланс на егоизма %d/5" % (atru_power, ego_power) 





