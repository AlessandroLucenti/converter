import json

# Leggi il contenuto del file di testo
with open('PANIERE-ALGORITMI-E-STRUTTURE-DATI-2025.txt', 'r') as file:
    txt_content = file.read()

# Dividi il contenuto in capitoli
chapters = txt_content.split(" Capitolo ID ")

# Inizializza una lista per memorizzare i capitoli
chapter_list = []

# Itera su ogni capitolo
for chapter in chapters[1:]:
    lines = chapter.split("\n")
    chapter_title = lines[0].strip()
    questions = []

    # Itera su ogni riga del capitolo
    i = 1
    while i < len(lines):
        line = lines[i].strip()
        if line and line[0].isdigit():
            question_text = line.split(":")[1].strip()
            answers = {}
            correct_answer = ""
            section = ""

            # Raccogli le risposte e altri dettagli
            while i + 1 < len(lines) and not lines[i + 1][0].isdigit():
                i += 1
                answer_line = lines[i].strip()
                if answer_line.startswith("A."):
                    answers["A"] = answer_line[2:].strip()
                elif answer_line.startswith("B."):
                    answers["B"] = answer_line[2:].strip()
                elif answer_line.startswith("C."):
                    answers["C"] = answer_line[2:].strip()
                elif answer_line.startswith("D."):
                    answers["D"] = answer_line[2:].strip()
                elif answer_line.startswith("Risposta corretta:"):
                    correct_answer = answer_line.split(":")[1].strip()
                elif answer_line.startswith("Argomento:"):
                    section = answer_line.split(":")[1].strip()

            # Aggiungi la domanda alla lista
            questions.append({
                "question": question_text,
                "answers": answers,
                "correct_answer": correct_answer,
                "section": section
            })
        i += 1

    # Aggiungi il capitolo alla lista
    chapter_list.append({
        "chapter_title": chapter_title,
        "questions": questions
    })

# Crea la struttura JSON finale
final_json = json.dumps(chapter_list, indent=4, ensure_ascii=False)

# Salva il JSON in un file
with open('PANIERE-ALGORITMI-E-STRUTTURE-DATI-2025.json', 'w', encoding='utf-8') as json_file:
    json_file.write(final_json)

print("Conversione completata con successo.")