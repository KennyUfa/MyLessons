import random
name1= input('Введи имя первого игрока:')
dam1 = input("введи свой урон(1-50):")
name2 = input('Введи имя второго игрока:')
dam2 = input('Введи его урон(1-50):')

class Hero():
    def __init__(self, name, dd):
        self.heals = 100
        self.name = name
        self.dd = dd
    def hit(self, obj):
        if obj.heals != 0:
            damage = random.randint(0, self.dd)

            obj.heals -= damage
            print(self.name + " наносит урон:" + str(damage))
            print(obj.name + ' осталось ' + str(obj.heals) + " здоровья")
            if obj.heals <= 0:
                print('Убит', obj.name)
            return obj.heals

        else:
            print('Он уже мертв')

    def show(self):
        print(self.name + ' ' + str(self.heals))


war_1 = Hero(name1, int(dam1))
war_2 = Hero(name2, int(dam2))
while war_2.heals > 0 and war_1.heals > 0:
    count = random.random()
    if count > 0.5:
        war_2.name, war_1.hit(war_2)
    else:
        war_1.name, war_2.hit(war_1)