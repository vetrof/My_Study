import json


string = '{"matrix":[{"available":true,"selected":true,"productCode":"107227073","characteristic":{"type":"Clothes_Colour","title":"Цвет","id":"мультиколор","values":[{"value":"мультиколор"}],"primaryImage":{"small":"https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h90/h40/64574798987294/batik-120-23z-children-107227073-1jpg.jpg","medium":"https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h9f/h53/64574799183902/batik-120-23z-children-107227073-1jpg.jpg","large":"https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h2d/hd2/64574798626846/batik-120-23z-children-107227073-1jpg.jpg"}},"matrix":[{"available":true,"selected":true,"productCode":"106625286","characteristic":{"type":"batik--children-clothes-size-ru","title":"Размер","id":"110","values":[{"dimension":"RUS","value":"110"}]}},{"available":true,"selected":false,"productCode":"106625318","characteristic":{"type":"batik--children-clothes-size-ru","title":"Размер","id":"116","values":[{"dimension":"RUS","value":"116"}]}},{"available":false,"selected":false,"productCode":"106625320","characteristic":{"type":"batik--children-clothes-size-ru","title":"Размер","id":"122","values":[{"dimension":"RUS","value":"122"}]}}]}]}'

script = json.loads(string)['matrix']

for s in script:
    print('Цвет, доступ: ', s['characteristic']['id'], end=' / ')
    print(s['available'])
    for m in s['matrix']:
        print('Размер, доступ: ', m['characteristic']['id'], end=' / ')
        print(m['available'])




# print('color:',script['matrix'][0]['characteristic']['id'])
# for i in script['matrix'][0]['matrix']:
#     print(i['available'])
#     print(i['characteristic']['id'])
#


# /matrix/0/matrix/0/characteristic/id
# /matrix/0/characteristic/id