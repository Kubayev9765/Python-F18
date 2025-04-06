1.
Yil= 2025
Ism=input("Ismingni kirit: " )
TugYil=int(input("Qaysi yilda tug'ilgansan: "))
Yosh= Yil- TugYil
Natija=f"{Ism} sen {Yosh} dasan" 
print(Natija)

2.
Malibu = 'LMaasleitbtui'
print(Malibu[1:12:2])
Lassetti = 'LMaasleitbtui'
print(Lassetti[0:13:2])

3.
Matiz = 'MsaatmiazD'
print(Matiz[0:9:2])

4.
txt = "I'am John. I am from London"
print(txt[20:27:1])

5.
suz=input("Xoxlagan so'zingni yoz:  ")
print (suz[::-1])

6.
text_kiriting=(input("Text kiriting: mercedes: "))
unlilar = "aeiouAEIOU"
Unlilar_soni = 0
for harf in text_kiriting:
        if harf in unlilar:
            Unlilar_soni += 1
print (Unlilar_soni)

7.
Sonlarni_kiriting = input("Sonlarni shoshmasdan kiriting: ")
raqamlar = list(map(float, Sonlarni_kiriting.split()))
eng_kattasi = max(raqamlar)
print("Eng katta raqam: ", eng_kattasi)

8.
matn=input("Xoxlagan bitta matnni kiriting: ")
teskari= matn[::-1]
if matn==teskari:
    print("Kiritgan so'zingiz palindrom ekan!")
else:
    print("Kiritgan so'zingiz polindrom emas.")

9.
email = input(" Pochtangizni kiriting: ")
if "@" in email:
    domain = email.split("@")[1]
    print(f"Pochtangizni domini: {domain}")
else:
    print("Siz elektron pochta kiritmadingiz. Iltimos elektron pochpangizni kiriting.")

10.
def generate_password(length=12):    
    letters = string.ascii_letters     
    password = ''.join(random.choice(letters) for _ in range(length))    
    return password
password = generate_password(12)
print("Generated Password:", password)


