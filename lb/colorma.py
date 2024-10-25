def colored_output():
    output = [
        "\033[38;5;214m1.\033[0m Обновляю локальный репозиторий с помощью git pull",
        "![](\033[38;5;127mТютрюмова Анжелина Артёмовна\033[0m)",
        "\033[38;5;214m2.\033[0m В каталоге для отчёта текущей лабораторной работы использую команду make. Makefile находится в этом же каталоге report, поэтому файлы в docx и pdf форматах успешно сгенерировались. Проверяю наличие файлов в папке вручную.",
        "![](\033[38;5;127m/home/aatiutriumova/work/study/2024-2025/Архитектура компьютера/arch-pc/labs/lab03/report/image/2.png\033[0m){}",
        "![](\033[38;5;127m/home/aatiutriumova/work/study/2024-2025/Архитектура компьютера/arch-pc/labs/lab03/report/image/3.png\033[0m){}",
        "\033[38;5;214m3.\033[0m Командой make clean удаляю файлы и проверяю, что их больше нет в папке report.",
        "![](\033[38;5;127m/home/aatiutriumova/work/study/2024-2025/Архитектура компьютера/arch-pc/labs/lab03/report/image/4.png\033[0m){}",
        "![](\033[38;5;127m/home/aatiutriumova/work/study/2024-2025/Архитектура компьютера/arch-pc/labs/lab03/report/image/5.png\033[0m){}",
        "\033[38;5;214m4.\033[0m Открываю файл report.md с помощью редактора vim и начинаю заполнять отчёт по лабораторной работе согласно шаблону.",
        "![](\033[38;5;127m/home/aatiutriumova/work/study/2024-2025/Архитектура компьютера/arch-pc/labs/lab03/report/image/6.png\033[0m){}",
        "![](\033[38;5;127m/home/aatiutriumova/work/study/2024-2025/Архитектура компьютера/arch-pc/labs/lab03/report/image/7.png\033[0m){}",
        "",
        "\033[38;5;90m# Выводы\033[0m"  # Фиолетовый цвет для "Выводы" с кодом 90
    ]

    for line in output:
        print(line)

# Запуск функции
colored_output()
