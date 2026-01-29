# ===========================
# Pamata komentāru piemēri
# ===========================

# Vienas rindas komentārs – paskaidro konkrētu koda rindu

"""
Vairāku rindu komentārs (docstring)
Šādi var ierakstīt garākus paskaidrojumus vai instrukcijas.
Docstring parasti izmanto funkcijām, klasēm vai faila sākumā.
"""

# ===========================
# VS Code noderīgi īsceļi
# ===========================

"""
Dažas VS Code komandas saīsnes:
- Ctrl + /           – komentāru pievienošana/noņemšana rindai
- Alt + ↑/↓          – rindu pārvietošana augšup/lejup
- Alt + Z            – teksta aplocīšana (wrap)
- Shift + Alt + ↑/↓  – rindu kopēšana augšup/lejup
- Ctrl + D           – nākamā tāda paša vārda iezīmēšana
"""

# ===========================
# Print funkcijas piemēri
# ===========================

print("hello world")  # Izvada tekstu "hello world" uz ekrāna

print("Šis ir otrais print")  # Izvada tekstu "Šis ir otrais print" uz ekrāna

print("A", 17, "C")  # Izvada "A", skaitli 17 un "C" ar atstarpi starp tiem

print("A", 17, "C", sep="-")  # Izvada "A-17-C" (izmanto def. separatoru "-")

print("Šī izvade turpinās tajā pašā rindā ", end="!!!")  # Beigās pievieno "!!!", nevis jaunu rindu
print(" un šis teksts ir tajā pašā rindā")  # Turpina tajā pašā rindā

# \n – jauna rinda
print("Pirmā rinda\nOtrā rinda\nTrešā rinda")  # Izvada trīs rindas

print("😂")  # Izvada emocijzīmi

# ===========================
# Kļūdas piemērs
# ===========================

# print("5" + 7)  # Mēģina saskaitīt tekstu "5" un skaitli 7, izraisot kļūdu

# Traceback (most recent call last):
# File "c:\\Users\\eriks\\OneDrive\\Documents\\01_Skola\\RTU\\28.01.2026\\test.py", line 25, in <module>
# print("5" + 7)  # TypeError: can only concatenate str (not "int") to str

# ===========================
# Datu tipu noteikšana
# ===========================

print(type(5))        # int – vesels skaitlis
print(type(5.0))      # float – decimālskaitlis
print(type("teksts")) # str – teksts
print(type(True))     # bool – loģiskais tips

# ===========================
vesels_skaitlis = 10 # pieņemst lietot snake_case stilu mainīgo nosaukumos 
peldosais_skaitlis = 3.14159 # decimālskaitlis, ciparus nevar izmantot mainīgo nosaukumos un priekšā nevar būt cipars
teksts = "Sveiki, pasaule!" # teksts
loģiskais_tips = boolean = False # loģiskais tips (True vai False) = boolean
# ===========================
"""
# Bīstams pārrakstīšanas piemērs
# print = 6 # Pārraksta iebūvēto 'print' funkciju ar skaitli 6
# print("Šis izraisīs kļūdu, jo 'print' ir pārrakstīts ar skaitli 6.")

"""
# ==========================

# matemātiskās darbības
a = 10
b = 3
print(a + b)  # Saskaitīšana: izvada 13
print(a - b)  # Atņemšana: izvada 7
print(a * b)  # Reizināšana: izvada 30
print(a / b)  # Dalīšana: izvada 3.3333...
print(a // b) # Veselā daļa no dalīšanas: izvada 3
print(a % b)  # Atlikums no dalīšanas: izvada 1
print(a ** b) # Pakāpe: izvada 1000 (10^3)
# ==========================

# ievade no lietotāja
# lietotāja_ievade = input("Ievadi kaut ko: ") # Pieprasa lietotājam ievadīt tekstu
# print("Tu ievadīji:", lietotāja_ievade) # Izvada lietotāja ievadi
vards = input("Ievadi savu vārdu: ")
print("Sveiks, " + vards + "!")

# lai pārveidotu ievadi no viena tipa uz citu
# skaitlis = int(input("Ievadi skaitli: ")) # Pārveido ievadi par veselu skaitli
