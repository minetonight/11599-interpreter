#-*-coding:utf8;-*-
gender = self.readingType
buf = "" 
male = card[2] + card[4] + card[6] + card[8]

fem = card[1] + card[3] + card[5] + card[7] + card[9]

male_base = 5
fem_base = 7

buf += "Мъжка енергия %d от %d" % (male,  male_base)

buf += "\n Женска енергия %d от %d" % (fem,  fem_base)

 

