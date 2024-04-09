from audioop import maxpp
import urllib.request as request
import json

org_dic = {}
priceList = []
end_dic = {}
maxPos = 0

# delete old data
with open("python/t.txt", 'w') as file:
    print("", file=file, end="")

# update url page
with open('python/t.txt', "a", encoding='utf-8') as file:
    for i in range(1, 10):
        URL = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone%2013%20pro&page="+str(i)+"&sort=sale/dc"
        with request.urlopen(URL) as rq:
            js = json.load(rq)
            # update org_dic and dic
            for j in range(len(js['prods'])):
                name = js['prods'][j]['name']
                price = js['prods'][j]['price']
                Id = (j+1)+(i-1)*len(js['prods'])
                org_dic.update( {Id : [name, price]} )
    length = len(org_dic) + 1
    for i in org_dic:
        Max = org_dic[i][1]
        for j in org_dic:
            if Max < org_dic[j][1]:
                Max = org_dic[j][1]
                maxPos = j
        else:
            end_dic.update({i:[org_dic[maxPos][0], org_dic[maxPos][1]]})
            org_dic[maxPos][1] = -1

    # print end_dic to t.txt
    for i in end_dic:
        print(f"{end_dic[i][0]}\n{end_dic[i][1]}", file=file)