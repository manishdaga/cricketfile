import availaible_matches 
import fullcmntry
import score
import highlights
import re
import time
print('=====WELCOME TO LIVE CRICKET UPDATES======')
print('TODAYS MATCHES ARE -')
t=0
matches=availaible_matches.get_ids()
for i in list(matches.keys()):
    q=re.sub('-','s ',i)
    print('['+str(t)+']',q.upper())
    t=t+1
rspnce=int(input('Enter the appropriate number \n'))
if (rspnce>len(matches.keys())):
    print(' Number out of range')
    raise ValueError('Number out of range')
else:
    mtchid=list(matches.values())[rspnce]
print(mtchid)
print('The following types of updates are possible')
print('[0] full commentary')
print('[1] highlights')
print('[2] score')
subrsp=int(input('Enter the suitable choice \n'))
if (subrsp>2):
    raise ValueError('Number out of range')
    print(' Number out of range \n')
if subrsp==0:
    while True:
        fullcmntry.fllcmntry(mtchid)
        time.sleep(5)
if subrsp==1:
    highlights.highlights(mtchid)
if subrsp==2:
    while True:
        score.score1(mtchid)
        time.sleep(5)

