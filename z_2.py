#2вариант
#Фасад
class light_main:
    def light_off(self):
        print("Все лампы выключены")

    def econom(self):
        print("Включено энергосберегающее освещение")


class security:
    def lock_doors(self):
        print("Двери заблокированы")

    def unlock_doors(self):
        print("Двери разблокированы")


class music:
    def music_off(self):
        print("Музыка выключена")

    def relax_music(self):
        print("Запущена relax-музыка")


class smart_home_class:
    def __init__(self):
        #собираем все вместе внутри фасада:
        self._l = light_main()
        self._s = security()
        self._media = music()

    def away(self):
        print('Включение режима "Я УШЕЛ"')
        self._l.light_off() #свет выключен
        self._s.lock_doors() #двери заблокированы
        self._media.music_off() #музыка выключена
        

    def here(self):
        print('Включение режима "Я ДОМА"')
        self._l.econom() #свет на экорежиме
        self._s.unlock_doors() #двери разблокированы
        self._media.relax_music() #релаксирующая музыка

def home():
    smart_home = smart_home_class() #закидываем в переменную наш смарт_хоум класс

#выполнится только 3 раза
    for i in range(3):
        print ("!!!Программа запуститься только 3 раза!!!")
        user_input = input("Вы сейчас дома? (1 - да, 0 - ушел): ")
        if user_input == "1":
            smart_home.here() #дома
        elif user_input == "0":
            smart_home.away() #не дома
        else:
            print("!Введите 0 или 1!")
