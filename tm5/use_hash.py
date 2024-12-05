from passlib.context import CryptContext

# Настройка CryptContext с использованием bcrypt
pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated="auto",
    bcrypt__rounds=12)

# хеширование пароля
password = "my_secure_password"
hashed_password = pwd_context.hash(password)


# Проверка пароля
input_password = "my_secure_password"
if pwd_context.verify(input_password, hashed_password):
    print("Пароль верный!")
else:
    print("Неверный пароль!")