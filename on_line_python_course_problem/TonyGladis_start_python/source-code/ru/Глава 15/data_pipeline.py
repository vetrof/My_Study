class Factory:
    def process(self, input):
        raise NotImplementedError

class Extract(Factory):
    def process(self, input):
        print("Идет извлечение...")
        output = {}
        return output

class Parse(Factory):
    def process(self, input):
        print("Идет разбор...")
        output = {}
        return output

class Load(Factory):
    def process(self, input):
        print("Идет загрузка...")
        output = {}
        return output

pipe = {
    "Извлечь"   : Extract(),
    "Разобрать" : Parse(),
    "Загрузить" : Load(),
}
inputs = {}
# Конвейерная обработка
for name, instance in pipe.items():
    inputs = instance.process(inputs)