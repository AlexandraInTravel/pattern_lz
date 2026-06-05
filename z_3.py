#Наблюдатель
class Cust: #класс для покупателя
    def __init__(self, name, w_prod): #инит для покупателей и обуви, которая им нужна
        self.name = name  #имя
        self.w_prod = w_prod  #обувь, которую он ждет

    def call(self, prod): #будто позвонили покупателю и он:
        print(self.name, "идет покупать")  


class Store: #класс для магазина
    def __init__(self):
        self.notebook = []  #пустой блокнот для покупателей

    
    def car(self, prod): #привоз товара
        print("В магазин привезли:", prod)  #и сам товар

        #цикл для проверки в блокноте на нужный товар
        for person in self.notebook:
            if person.w_prod == prod: #если товар совпадает с нужным
                person.call(prod)  #звонок

def pr():
    store = Store()  #закидываем весь класс в одну переменную

    p = Cust("Петя", "кроссовки")  #Петя, который ждет кроссовки
    g = Cust("Глаша", "туфли")  #Глаша, которая ждет туфли

    store.notebook.append(p)  #добавляем Петю
    store.notebook.append(g)  #и Глашу

    store.car("кроссовки")  #привезли кроссы - звоним Пете
    store.car("туфли")  #привезли туфли - звоним Глаше
