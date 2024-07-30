

def is_vaild_email(email):
    if '@' not in email:
        return False
    elif email.endswith('.com') or email.endswith('.ru') or email.endswith('.net'):
        return False
    else:
        return True
    
def send_email(message, sender, recipient='university.help@gmail.com'):
    if not is_vaild_email(recipient) == False or not is_vaild_email(sender) == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')  
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru','urban.teacher@mail.ru')