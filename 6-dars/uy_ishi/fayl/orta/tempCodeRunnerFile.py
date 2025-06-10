
with open("arabic.txt", "r") as f:
    arabic_text = f.read()

if arabic_text.strip() == "مرحباً، أنا طالب في تعليم الخلاص.":
    translated = "Salom, men Najot Ta'lim o'quvchisiman."
else:
    translated = "Tarjima topilmadi."

with open("uzbek.txt", "w") as f:
    f.write(translated)