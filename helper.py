from faker import Faker

faker = Faker()


def generate_registration():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=10)
    return name, email, password
