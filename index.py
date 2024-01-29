#Mad Lips (Palabras Locas)

adj = input("Adejetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo Plural: ")
muerte = "pero es sujetada justo antes por su hermano" if  input("Final feliz?(Si/No): ").upper() == "SI" else "muriendo mientras su hermano escapa"

madlib = f"La princesa {adj}, siempre esta {verbo1} y busca problemas. Su hermano, el principe, siempre esta {verbo2} e intenta resolver sus {sustantivo_plural}. Corriendo por la montaña, los hermanos, tropiezan con las rocas. La princesa cae al precipicio {muerte}"

print(madlib)