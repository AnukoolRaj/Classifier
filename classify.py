import classifier

def myfun (str) :   
    t=twenty_train.target_names[text_clf_svm.predict([str])[0]]
    if((t=='comp.graphics')or
       (t=='comp.os.ms-windows.misc') or
       (t=='comp.sys.ibm.pc.hardware') or
       (t=='comp.sys.mac.hardware') or
       (t=='comp.windows.x') or (t=='sci.crypt')
       or (t=='sci.electronics') or
       (t=='sci.med') or
       (t=='sci.space')) : print('Science and Technology')

    if((t=='talk.politics.misc') or 
       (t=='talk.politics.guns') or
       (t=='talk.politics.mideast')) : print('News and History')
    
    if((t=='rec.sport.baseball') or
       (t=='rec.sport.hockey')): print('Sports and Entertainment')
    
    if((t=='talk.religion.misc') or
       (t=='alt.atheism') or
       (t=='soc.religion.christian') or
       (t=='rec.autos') or 
       (t=='rec.motorcycles')) : print('Life')
    
    if((t=='misc.forsale')) : print('Miscellaneous')



myfun('The way he played today was just so amazing especially after the break')
