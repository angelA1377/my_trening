def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка на корректность email
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    # Проверка на корректность получателя и отправителя
    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адрес {sender} на адрес {recipient}.")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Примеры вызова функции
send_email("Привет!", "student@example.com")  # Письмо успешно отправлено
send_email("Привет!", "student@example.com", "custom.sender@gmail.com")  # Нестандартный отправитель
send_email("Привет!", "student@example.com", "university.help@gmail.com")  # Письмо успешно отправлено
send_email("Привет!", "student@example.com", "invalid-email")  # Невозможно отправить письмо
send_email("Привет!", "university.help@gmail.com")  # Нельзя отправить письмо самому себе