from faker import Faker

fake = Faker()

def random_name() -> str:
    name = fake.name()
    return name

print(random_name())