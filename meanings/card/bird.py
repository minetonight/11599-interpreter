#-*-coding:utf8;-*-


buf = "" 
bird = card[2] + card[3] +\
  card[4] + card[7] +\
  card[1] + card[5] + card[9]

anchor = card[3] + card[6] +\
  card[7] + card[8] +\
  card[1] + card[5] + card[9]

buf += "птица е %d и котва е %d" % (bird, anchor) 

if bird > anchor:
    buf += "\n Люди-птицы  —  это  когда  количество  указанных  цифр преобла­  дает  значительно.  Их  всегда  привлекает  новое,  они  не  любят посто­  янство,  рутину,  однообразие.  Они  легко  принимают  все  новое,  и  сами  участвуют  в  поиске.  Их  несет,  несет  ветром,  просьбами,  увлечением и т.д.,  важно,  что  несет  всегда  и  во  всем.  Самое  неприятное  для  них  —  это  постоянство,  невозможность  перемен.  Птицы  в  клетках  не  поют,  а  медленно  превращаются  в камень." 
