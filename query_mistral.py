import subprocess
import json
import os

# Створення папки для звіту
os.makedirs("mistral_reports", exist_ok=True)

# Завантаження даних
with open("courses.json", "r") as f:
    courses = json.load(f)

# Об'єднання описів
text_data = "\n\n".join([f"{c['title']}:\n{c['description']}" for c in courses])

# Промт
prompt = f"""You are a data analyst. Analyze the following course descriptions and generate a short summary.
Text:
{text_data}
"""

# Запуск моделі Mistral через ollama
result = subprocess.run(
    ["ollama", "run", "mistral"],
    input=prompt.encode("utf-8"),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

# Збереження результату
with open("mistral_reports/summary.txt", "w") as out:
    out.write(result.stdout.decode("utf-8"))

print("Summary saved to mistral_reports/summary.txt")