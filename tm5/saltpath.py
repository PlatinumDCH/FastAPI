import bcrypt
password = b'saksaganskogo22' # пароль должен быть в байтах
salt = bcrypt.gensalt(rounds=6) # число итераций ( по умолчанию 12 )
hashed_psw = bcrypt.hashpw(password, salt)
print(f'Кешированный пароль, {hashed_psw.decode()}')

def wrong_password():
    input_pass = password + b'haha'
    if bcrypt.checkpw(input_pass, hashed_psw):
        print('Correct')
    else:
        print('Incorrect')
def true_password():
    input_pass = password
    if bcrypt.checkpw(input_pass, hashed_psw):
        print('Correct')
    else:
        print('Incorrect')

if __name__ == '__main__':

    wrong_password(), true_password()