
#упражнение  5:14 кинетическая энергия
# Ke = 1/2mv**2

def kinetic_energy(mass, speed):
    return (mass * speed**2) / 2

def main():
    mass = int(input('enter weight object- '))
    speed = int(input('enter speed object- '))
    kin_en = kinetic_energy(mass, speed)
    print()
    print(f'kinetic energy you object = {kin_en}')

main()