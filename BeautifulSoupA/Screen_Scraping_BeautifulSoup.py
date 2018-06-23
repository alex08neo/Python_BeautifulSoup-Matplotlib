from bs4 import BeautifulSoup
import urllib.request
import sys,io,re
import pickle,json
import pprint

#I cann't use list, so I run each link one time.
#I made three pkl file and three Json file. Please older.
def genPickleFromUrlList(url, firstPkl):
    with urllib.request.urlopen(url) as fp:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, 'cp437', 'backslashreplace')
        soup = BeautifulSoup(fp, 'html.parser')
        [s.extract() for s in soup('script')]
        [s.extract() for s in soup('style')]
        box = soup.text
        words = [s for s in re.findall("\w+", box)]
        frequencyDic = {}
        for i in words:
            if i not in frequencyDic:
                frequencyDic[i] = 1
            else:
                frequencyDic[i] += 1
        with open('thirdPkl','wb') as f:
            pickle.dump(frequencyDic,f)
            f.close()
genPickleFromUrlList("http://www.smu.edu/cox", "thirdPkl")

def genJsonFromPickle(pickleFileName, JsonFileName):
         with open('thirdPkl','rb') as f:
             frequencyDic=pickle.load(f)

         with open('JsonFilecox','w') as fj:
             json.dump(frequencyDic,fj)

         with open('JsonFilecox','rb') as jf:
             bb = json.load(jf)



def genDictTopWords (pickleFileName,  nTopWords):
     with open('firstPkl', 'rb') as gw:
         frequencyDic = pickle.load(gw)
         top = sorted(frequencyDic.items(), key=lambda items: items[1], reverse=True)
         pp = pprint.PrettyPrinter(indent=nTopWords)
         pp.pprint(top)
genDictTopWords('thirdPkl', 3)