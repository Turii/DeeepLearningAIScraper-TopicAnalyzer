import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# === Створити папку для звітів ===
report_dir = "reports"
os.makedirs(report_dir, exist_ok=True)

# === Завантаження курсів ===
with open("courses.json", "r") as f:
    courses = json.load(f)

# === Об’єднання title + description ===
text_data = " ".join([f"{course['title']} {course['description']}" for course in courses]).lower()

# === Ключові слова для аналізу ===
keywords = ["AI", "Python", "LLM", "Prompt", "LangChain", "Vision", "ChatGPT", "Transformer", "Agent", "ML", "MLOps"]
counts = {kw: text_data.count(kw.lower()) for kw in keywords}

# === DataFrame ===
df_keywords = pd.DataFrame(counts.items(), columns=["Keyword", "Count"])
df_keywords = df_keywords[df_keywords["Count"] > 0].sort_values(by="Count", ascending=False)

# === Збереження CSV ===
csv_path = os.path.join(report_dir, "keyword_frequency.csv")
df_keywords.to_csv(csv_path, index=False)

# === Побудова та збереження bar chart ===
plt.figure(figsize=(10, 6))
plt.bar(df_keywords["Keyword"], df_keywords["Count"], color="skyblue")
plt.title("Keyword Frequency in DeepLearning.AI Courses")
plt.xlabel("Keyword")
plt.ylabel("Mentions")
plt.xticks(rotation=45)
plt.tight_layout()
bar_chart_path = os.path.join(report_dir, "keyword_frequency_chart.png")
plt.savefig(bar_chart_path)
plt.close()

# === Побудова та збереження Word Cloud ===
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_data)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Course Titles and Descriptions")
plt.tight_layout()
wordcloud_path = os.path.join(report_dir, "wordcloud.png")
plt.savefig(wordcloud_path)
plt.close()

# === Готово ===
print("Аналіз завершено! Звіти збережено в папку 'reports':")
print(f"- {csv_path}")
print(f"- {bar_chart_path}")
print(f"- {wordcloud_path}")