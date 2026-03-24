import re


with open('pets.txt', 'r', encoding='utf-8') as f:
    content = f.read()

words = content.split()
word_count = len(words)

sentences = [s for s in re.split(r'[.!?]+', content) if s.strip()]
sentence_count = len(sentences)

clean_words = [re.sub(r'[^\w\s]', '', w) for w in words]
longest_word = max(clean_words, key=len) if clean_words else ""

results = (
    f"Кількість слів у тексті: {word_count}\n"
    f"Кількість речень у тексті: {sentence_count}\n"
    f"Найдовше слово: {longest_word}"
)

with open('analysis_results.txt', 'w', encoding='utf-8') as f:
    f.write(results)

print(results)