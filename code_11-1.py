import csv

# Імена вхідного та вихідного файлів
input_file = "inflation_data.csv"
output_file = "inflation_summary.csv"

try:
    # Відкриваємо вхідний файл для читання
    with open(input_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Ініціалізуємо словник для збереження даних за роками
        yearly_data = {}

        # Зчитуємо дані з файлу
        for row in reader:
            year = row["Time"]
            country = row["Country Name"]
            value = row["Value"]
            
            # Перевіряємо, чи значення числове та не є порожнім
            if value and value.replace('.', '', 1).replace('-', '', 1).isdigit():
                value = float(value)
                if year not in yearly_data:
                    yearly_data[year] = {"min": (country, value), "max": (country, value)}
                else:
                    if value < yearly_data[year]["min"][1]:
                        yearly_data[year]["min"] = (country, value)
                    if value > yearly_data[year]["max"][1]:
                        yearly_data[year]["max"] = (country, value)

    # Записуємо результати у новий файл
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Year", "Country with Min Inflation", "Min Value", "Country with Max Inflation", "Max Value"])

        for year in sorted(yearly_data.keys()):
            min_country, min_value = yearly_data[year]["min"]
            max_country, max_value = yearly_data[year]["max"]
            writer.writerow([year, min_country, min_value, max_country, max_value])
    
    print(f"Результати записані у файл '{output_file}'")

except FileNotFoundError:
    print(f"Файл '{input_file}' не знайдено!")
except Exception as e:
    print("Сталася помилка:", str(e))
