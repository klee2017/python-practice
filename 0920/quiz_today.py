class Monster():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        print("{}가 {}를 공격해 {}의 피해를 입혔다 !".format(self.name, target.name, self.damage))
        target.hp = target.hp - self.damage
        if target.hp <= 0:
            print('{}가 죽었다...'.format(target.name))
        else:
            print('{}의 남은 체력은 {}'.format(target.name, target.hp))

    def __str__(self):
        return '{}: 공격력 {}'.format(self.name, self.damage)

pikachu = Monster('피카츄', 300, 130)
ggobugi = Monster('꼬부기', 300, 100)

print(pikachu)
print(ggobugi)
pikachu.attack(ggobugi)
ggobugi.attack(pikachu)
pikachu.attack(ggobugi)
pikachu.attack(ggobugi)

