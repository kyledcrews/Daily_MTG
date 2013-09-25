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

if os.path.exists("card_data/%s"%set) == False:
    os.mkdir("card_data/%s"%set)

if os.path.exists("card_data/%s/images"%set) == False:
    os.mkdir("card_data/%s/images"%set)
    
if os.path.exists("card_data/%s/images/English"%set) == False:
    os.mkdir("card_data/%s/images/English"%set)

if os.path.exists("card_data/%s/images/Taiwan"%set) == False:
    os.mkdir("card_data/%s/images/Taiwan"%set)

for i in range(total_num[set]):    
    index = i + 1
    
    # isd dka dgm
    if set in flip.keys():
            
        if index in flip[set]:

            # Taiwan    
            if os.path.exists("card_data/%s/images/Taiwan/%da.jpg"%(set, index)) == False:
                
                urllib.request.urlretrieve('http://magiccards.info/scans/tw/%s/%da.jpg'%(set, index), "card_data/%s/images/Taiwan/%da.jpg"%(set, index))
                urllib.request.urlretrieve('http://magiccards.info/scans/tw/%s/%db.jpg'%(set, index), "card_data/%s/images/Taiwan/%db.jpg"%(set, index))
                print ("Save %s %da tw"%(set, index))
                print ("Save %s %db tw"%(set, index))
                
            time.sleep(1)
        
            # English
            if os.path.exists("card_data/%s/images/English/%da.jpg"%(set, index)) == False:
                
                urllib.request.urlretrieve('http://magiccards.info/scans/en/%s/%da.jpg'%(set, index), "card_data/%s/images/English/%da.jpg"%(set, index))
                urllib.request.urlretrieve('http://magiccards.info/scans/en/%s/%db.jpg'%(set, index), "card_data/%s/images/English/%db.jpg"%(set, index))
                print ("Save %s %da en"%(set, index))
                print ("Save %s %db en"%(set, index))
                
            time.sleep(1)
                    
        else:
        
            # Taiwan    
            if os.path.exists("card_data/%s/images/Taiwan/%d.jpg"%(set, index)) == False:
                
                urllib.request.urlretrieve('http://magiccards.info/scans/tw/%s/%d.jpg'%(set, index), "card_data/%s/images/Taiwan/%d.jpg"%(set, index))
                print ("Save %s %d tw"%(set, index))
                
            time.sleep(1)
        
            # English
            if os.path.exists("card_data/%s/images/English/%d.jpg"%(set, index)) == False:
                
                urllib.request.urlretrieve('http://magiccards.info/scans/en/%s/%d.jpg'%(set, index), "card_data/%s/images/English/%d.jpg"%(set, index))
                print ("Save %s %d en"%(set, index))
                
            time.sleep(1)
        
   
    else:
    
         # Taiwan    
        if os.path.exists("card_data/%s/images/Taiwan/%d.jpg"%(set, index)) == False:
            
            urllib.request.urlretrieve('http://magiccards.info/scans/tw/%s/%d.jpg'%(set, index), "card_data/%s/images/Taiwan/%d.jpg"%(set, index))
            print ("Save %s %d tw"%(set, index))
            
        time.sleep(1)
        
        # English
        if os.path.exists("card_data/%s/images/English/%d.jpg"%(set, index)) == False:
            
            urllib.request.urlretrieve('http://magiccards.info/scans/en/%s/%d.jpg'%(set, index), "card_data/%s/images/English/%d.jpg"%(set, index))
            print ("Save %s %d en"%(set, index))
            
        time.sleep(1)
        
    