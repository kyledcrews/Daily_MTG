# -*- coding: utf-8 -*- 

import os

exec(open(os.getcwd() + "/config/config.py").read())

if len(sys.argv) < 2:
    print ('please input card_set')
    exit()
    
if sys.argv[1] not in card_set:
    print ('please input supportted card_set')
    print (card_set)
    exit()
    
set = sys.argv[1]

if os.path.exists("card_data") == False:
    os.mkdir("card_data")

if os.path.exists("card_data/%s"%(set)) == False:
    os.mkdir("card_data/%s"%(set))

for lan in language:    
    if os.path.exists("card_data/%s/%s"%(set, lan)) == False:    
        os.mkdir("card_data/%s/%s"%(set, lan))

    if os.path.exists("card_data/%s/%s_%s_all.html"%(set, set, lan)) == False:
    
        urllib.request.urlretrieve("http://magiccards.info/%s/%s.html"%(set, lan), "card_data/%s/%s_%s_all.html"%(set, set, lan))

        print ("%s/%s_%s_all.html"%(set, set, lan))
        
    for i in range(total_num[set]):
    
        index = i + 1
        print (index)
        
        # isd dka dgm
        if set in flip.keys():
            
            if index in flip[set]:

                if os.path.exists("card_data/%s/%s/%da.html"% (set, lan, index)) == False:
            
                    urllib.request.urlretrieve("http://magiccards.info/%s/%s/%da.html" % (set, lan, index), "card_data/%s/%s/%da.html"% (set, lan, index))
                    urllib.request.urlretrieve("http://magiccards.info/%s/%s/%db.html" % (set, lan, index), "card_data/%s/%s/%db.html"% (set, lan, index))
                
                    print ('save %s %da.html'%(set, index))
                    print ('save %s %db.html'%(set, index))
                    
            else:
            
                if os.path.exists("card_data/%s/%s/%d.html"% (set, lan, index)) == False:
                
                    urllib.request.urlretrieve("http://magiccards.info/%s/%s/%d.html" % (set, lan, index), "card_data/%s/%s/%d.html"% (set, lan, index))
                        
                    print ('save %s %d.html'%(set, index))
                    
            time.sleep(1)
                    
        else:
            if os.path.exists("card_data/%s/%s/%d.html"% (set, lan, index)) == False:
                
                urllib.request.urlretrieve("http://magiccards.info/%s/%s/%d.html" % (set, lan, index), "card_data/%s/%s/%d.html"% (set, lan, index))                    
                    
                print ('save %s %d.html'%(set, index))
                            
                time.sleep(1)
