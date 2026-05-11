import requests

# Send message methodi
token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
chat_id = "6830300399"

method_send = "sendMessage"
response_send = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method_send}",
    data={
        'chat_id': chat_id,
        'text': 'Salom. Bu mening telegram botim!'
    }
)

send_data = response_send.json()

msg_id = send_data['result']['message_id']

# Delete methodi
method_delete = "deleteMessage"
response_delete = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method_delete}",
    data={
        'chat_id': chat_id,
        'message_id': msg_id
    }
)

print(response_delete.json())

# Bot ismini olish
token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
method = "getMyName"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
)

print(response.json())

# Botni standart huquqlarini olish
token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
method = "getMyDefaultAdministratorRights"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
)

print(response.json())

# sendDice methodi
token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
method = "sendDice"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
    data={
        'chat_id': '6830300399',
        'emoji': '🏀'
    }
)
print(response.json())

# Bot haqida ma'lumot olish
token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
method = "getMe"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
)
print(response.json())

# Updates qilish methodi
token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
method = "getUpdates"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
)
print(response.json())

# Foydalanuvchini telegramdagi rasmlarini qaytaruvchi methodi
token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
method = "getUserProfilePhotos"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
    data={
        'user_id': 6830300399
    }
)
print(response.json())

# Telegramda bot ustida yozmoqda degan chiqaradigan method
token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
method = "sendChatAction"

response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
    data={
        'chat_id': 6830300399,
        'action': 'typing'
    }
)
print(response.json())

token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
method = "sendLocation"

response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
    data={
        'chat_id': 6830300399,
        'latitude': 41.311081,
        'longitude': 69.240562
    }
)
print(response.json())