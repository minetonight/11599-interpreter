#-*-coding:utf8;-*-

buf = "" 

if card[3] > 0 and card[6] > 0 and card[9] > 1:
    buf = "редът за Мъдрост е запълнен" 
    power = card[3] + card[6] + card[9]
    buf += "\nСилата му е %d при норма от %d"%(power, 4) 
    