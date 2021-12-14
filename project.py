#rOkY
#FuCk

################################### KoPaL ####################################

import gtts
from playsound import playsound as pls
import os
from googletrans import Translator
from pprint import pprint

def ans(s):
    print("\nsome language code:-> below")

    print('af -for african   |  ar -for arabic     |  de -for german')
    print('bn -for bangla    |  el -for greek      |  en -for english')
    print('es -for spanish   |  fr -for french     |  id -for indonesian')
    print('gu -for gujarati  |  hi -for hindi      |  hr -for croatian')
    print('it -for italian   |  ja -for japanese   |  ko -for korean')
    print('kn -for kannada   |  la -for latin      |  ml -for malayalam')
    print('mr -for marathi   |  my -for myanmar    |  pt -for portuguese')
    print('ne -for nepali    |  ro -for romanian   |  ru -for russia')
    print('sr -for serbian   |  sv -for swedish    |  te -for telugu')
    print('ta -for tamil     |  th -for thai       |  tl -for filipino')
    print('tr -for turkish   |  ur -for urdu       |  hy -for armenian')
    print('vi -for vietnam   |  zh-tw -for Chinese |  sq -fro albanian')

    print("\nwrite language code for listen / use hints for above description:-> below")

    while(1):
        s1=str(input())
        if(s1=='stop' or s1=='STOP' or s1=='tham' or s1=='break' or s1=='bye'):
            print('again write new sentence:-> ')
            break
        translator = Translator()
        translation = translator.translate(s,dest=s1)
        txt=translation.text
        print(f"{translation.origin} ({translation.src})  ---->  {translation.text} ({translation.dest})")

        t_t_s=gtts.gTTS(txt,lang=s1)
        t_t_s.save("audio.mp3")
    
        pls("audio.mp3")

print("write text for convert voice:-> below")
while(1):
    s=str(input())
    if(s=='stop' or s=='STOP' or s=='tham' or s=='break' or s=='bye'):
        print('Thank You')
        break
    ans(s)
