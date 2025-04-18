import subprocess
import os

# === Створення папки для звітів від моделі ===
report_dir = "mistral_reports"
os.makedirs(report_dir, exist_ok=True)

# === Шлях до summary.txt ===
summary_path = os.path.join(report_dir, "summary.txt")
with open(summary_path, "r") as f:
    course_descriptions = f.read()

# === Промт для моделі ===
PROMPT = """You are an expert in data analysis and AI trends.

Based on the following course descriptions, provide:
1. A summary of the most common themes in these AI courses.
2. Which topics are most frequently covered?
3. What type of user (beginner, intermediate, advanced) do these courses seem to target overall?
4. Suggest 3 new course ideas that would complement this list.

Course Descriptions:
"""

full_prompt = PROMPT + course_descriptions

# === Запуск Mistral через Ollama CLI ===
result = subprocess.run(
    ["ollama", "run", "mistral"],
    input=full_prompt.encode("utf-8"),
    capture_output=True
)

# === Збереження відповіді в ту ж папку ===
response_path = os.path.join(report_dir, "mistral_response.txt")
with open(response_path, "w") as f:
    f.write(result.stdout.decode("utf-8"))

print(f"🧠 Done! Response saved to: {response_path}")