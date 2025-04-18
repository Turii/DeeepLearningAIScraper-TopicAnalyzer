from playwright.sync_api import sync_playwright
import json

def scrape_courses():
    courses = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.deeplearning.ai/courses/")

        # Чекаємо заголовок
        page.wait_for_selector("h1.text-slate-900", timeout=10000)

        # Скролимо вниз для підвантаження всіх курсів
        for _ in range(10):
            page.mouse.wheel(0, 1000)
            page.wait_for_timeout(500)

        # Локатори: <a> з h3 (назва), p (опис)
        course_cards = page.locator("a:has(h3)").all()

        for card in course_cards:
            try:
                title = card.locator("h3").inner_text().strip()
                url = card.get_attribute("href")
                description = card.locator("p").inner_text().strip()
                if title and url:
                    full_url = f"https://www.deeplearning.ai{url}"
                    courses.append({
                        "title": title,
                        "url": full_url,
                        "description": description
                    })
            except:
                continue

        browser.close()

    # Зберігаємо JSON
    with open("courses.json", "w") as f:
        json.dump(courses, f, indent=2)

    print(f"{len(courses)} курсів збережено в courses.json")

if __name__ == "__main__":
    scrape_courses()