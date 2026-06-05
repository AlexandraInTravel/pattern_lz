#2вариант
#Фабричный метод
class Dish: #это главный базовый класс для всех блюд
    def fun(self):
        return ("Данного блюда нет")

#все следующие классы, которые будут описывать блюда, наследуем от Dish 
class Pasta(Dish):
    def fun(self):
        return ("Паста Карбонара")


class Soup(Dish):
    def fun(self):
        return ("Борщ")


class Burger(Dish):
    def fun(self):
        return ("Бургер")


class Salad(Dish):
    def fun(self):
        return ("Салат Цезарь")


class Sushi(Dish):
    def fun(self):
        return ("Суши с лососем")


class Pizza(Dish):
    def fun(self):
        return ("Пицца Маргарита")


class Steak(Dish):
    def fun(self):
        return ("Стейк")

class Error(Dish): #спец класс для неверного ввода
    def fun(self):
        return ("Пожалуйста, введите соответсвующее число: 1 - Пн, 2 - Вт, 3 - Ср, 4 - Чт, 5 - Пт, 6 - Сб, 7 - Вс")

class Restaurant: #класс ресторана, который работает как фабрика
    def day_dish(self, day): #используем фабричный метод, который принимает день недели и создает блюдо или не блюдо
        if day == ("1"):
            return Pasta()
        elif day == ("2"):
            return Soup()
        elif day == ("3"):
            return Burger()
        elif day == ("4"):
            return Salad()
        elif day == ("5"):
            return Sushi()
        elif day == ("6"):
            return Pizza()
        elif day == ("7"):
            return Steak()
        else:
            return Error()

    def d_d(self, day):
        dish = self.day_dish(day) #сохраняем в  dish вызванный фабричный метод
        #проверка на правильность ввода
        if dish.fun() == ("Пожалуйста, введите соответсвующее число: 1 - Пн, 2 - Вт, 3 - Ср, 4 - Чт, 5 - Пт, 6 - Сб, 7 - Вс"):
            print("Пожалуйста, введите соответсвующее число: 1 - Пн, 2 - Вт, 3 - Ср, 4 - Чт, 5 - Пт, 6 - Сб, 7 - Вс")
        else:
            print("Блюдо дня:", dish.fun())


def rest():
    d_restaurant = Restaurant() #закидываем в новую переменную 
    
    #выполнится только 8 раз
    for i in range(8):
        print ("!!!Программа запуститься только 8 раз!!!")
        your_day = input("Введите число, соответсвующее дню недели(1 - Пн, 2 - Вт, 3 - Ср, 4 - Чт, 5 - Пт, 6 - Сб, 7 - Вс): ")
        d_restaurant.d_d(your_day) #вызываем метод ресторана в зависимости от введенного числа



        
