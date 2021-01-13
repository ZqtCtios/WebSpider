import requests
from bs4 import BeautifulSoup
def getUrls():
    urls=[]
    url='https://www.pixiv.net/ranking_area.php?type=detail&no=6'
    html=requests.get(url).text
    soup=BeautifulSoup(html,"html.parser")
    for div in soup.find_all('div',attrs={'class':'work_wrapper'}):
        geturl='https://www.pixiv.net'+div.a['href']
        urls.append(geturl)
    print('共获取%s个页面'%(len(urls)))
    return urls
def getImg(urls):
    imgs=[]
    for url in urls:
        html=requests.get(url).text
        soup=BeautifulSoup(html,"html.parser")
        img=soup.find_all('img')
        print(img)

        imgs.append(img)
        
    print('共获取%s张图片地址'%(len(imgs)))
    return imgs;
    

if __name__ == '__main__':
    urls=getUrls()
    imgs=getImg(urls)
    #download(imgs)

    