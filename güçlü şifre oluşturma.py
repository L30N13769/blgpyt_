import random
import string

def generate_password(length):
    """Verilen uzunlukta rastgele bir şifre oluşturur"""
    # Şifre oluşturmak için kullanılacak karakterlerin listesi
    characters = string.ascii_letters + string.digits + string.punctuation

    # Şifre oluşturma
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Kullanıcıdan şifre uzunluğunu alınır
length = int(input("Lütfen şifre uzunluğunu girin: "))

# Şifre oluşturma
password = generate_password(length)

# Oluşturulan şifre yazdırılır
print("Oluşturulan şifre: ", password)


