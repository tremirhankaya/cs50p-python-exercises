velocity=300000000

def main():
    mass=int(input("Enter the mass of the object in kilograms: "))
    print(f"The energy of the object is: {calculate_energy(mass, velocity)} Joules")


def calculate_energy(mass, velocity):
    return  mass * velocity ** 2

main()