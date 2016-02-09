from urllib.request import urlopen
import bs4
import operator

def containsKey(d, key):
    contains = False
    for char in d:
        if char == key:
            return True
    return False

def populateDict(garbage, d):
    for char in garbage:
        if containsKey(d, char):
            d[char] += 1
        else:
            d[char] = 1

def keySort(d):
    return sorted(d.items(), key=lambda x:x[1],reverse=True)

def clean(d):
    out = dict(d)
    for key in d:
        if key in bad:
            del out[key]
        if len(key) > 1:
            del out[key]
    return out

def total(d):
    total = 0
    for key in d:
        total += d[key]
    return total

def combine_dicts(a, b):
    for key in a:
        if key in b:
            a[key] += b[key]
            del b[key]
    a.update(b)
    return a

// Declare characters we don't want to track, english alphabet and top 100 chinese character
bad = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 \n\r(),.?;:'"[]{}\-=+-
        !@！？ #$'/*-+\xa0，|&©∶。、（一><_?：▪ ）…~%”“的一是不了人我在有他这中大来上国个到说们为子和你地出
        道也时年得就那要下以生会自着去之过家学对可她里后小么心多天而能好都然没日于起发成事只作当想看文无开手十用主
        行方又如前所本见经头面公同三已老从动长	"""
        
// Declare URLs to pool data from
url = ["http://baike.baidu.com/subview/92404/5815703.htm",
       "http://baike.baidu.com/view/3314.htm",
       "http://baike.baidu.com/view/629336.htm",
       "http://baike.baidu.com/view/8332.htm",
       "http://baike.baidu.com/view/689084.htm",
       "http://baike.baidu.com/view/920697.htm",
       "http://baike.baidu.com/view/15076.htm",
       "http://baike.baidu.com/subview/37/6030295.htm",
       "http://baike.baidu.com/view/1438395.htm",
       "http://baike.baidu.com/subview/1659/7112047.htm"]

tot = {}
a={}
f = open('cs.txt', 'w')

// Collect data from websites
for i in range(0,2):
    web_page = urlopen(url[i])
    page_text = web_page.read()
    chinese = bs4.BeautifulSoup(page_text).text
    d = {}
    populateDict(chinese, d)
    a = combine_dicts(clean(d), a)
    totals = total(a)

// Sort data and store in file
for key, value in keySort(a)[:100]:
    out = key + " " + "{:3d}".format(a[key]) + "   %" + "{:.4f}".format((a[key]/totals)*100) + "\n"
    f.write(out)

f.close()
    

