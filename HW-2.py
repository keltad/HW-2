# Спершу створимо файл з даними для прикладу
with open('pets.txt', 'w', encoding='utf-8') as f:
    f.write("Муха 4 бульдог\n")
    f.write("Рекс 6 вівчарка\n")
    f.write("Барон 2 коргі\n")
    f.write("Мурка 7 сіамська\n")

# Основна логіка задачі
with open('pets.txt', 'r', encoding='utf-8') as infile, \
     open('young_pets.txt', 'w', encoding='utf-8') as outfile:
    
    for line in infile:
        parts = line.split()  # Розбиваємо рядок на [кличка, вік, порода]
        if parts:
            age = int(parts[1])
            if age < 5:
                outfile.write(line)

print("Фільтрація завершена. Результат у файлі 'young_pets.txt'.")