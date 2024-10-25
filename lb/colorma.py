def colored_output():
    output = [
        "\033[38;5;45m---",
        "\033[38;5;45m## Front matter",
        "\033[38;5;45mtitle\033[0m:\033[38;5;127m 'Отчет по лабораторной работе'",
        "\033[38;5;45msubtitle\033[0m:\033[38;5;127m '№3'",
        "\033[38;5;45mauthor\033[0m:\033[38;5;127m 'Тютрюмова Анжелина Артёмовна'",
        "",
        "\033[38;5;45m## Generic otions",
        "\033[38;5;45mlang\033[0m: ru-RU",
        "\033[38;5;45mtoc-title\033[0m:\033[38;5;127m 'Содержание'",
        "",
        "\033[38;5;45m## Bibliography",
        "\033[38;5;45mbibliography\033[0m: bib/cite.bib",
        "\033[38;5;45mcsl\033[0m: pandoc/csl/gost-r-7-0-5-2008-numeric.csl",
        "",
        "\033[38;5;45m## Pdf output format",
        "\033[38;5;45mtoc\033[0m:\033[38;5;127m true\033[38;5;45m # Table of contents",
        "\033[38;5;45mtoc-depth\033[0m:\033[38;5;127m 2",
        "\033[38;5;45mlof\033[0m:\033[38;5;127m true\033[38;5;45m # List of figures",
        "\033[38;5;45mlot\033[0m:\033[38;5;127m true\033[38;5;45m # List of tables",
        "\033[38;5;45mfontsize\033[0m: 14pt",
        "\033[38;5;45mlinestretch\033[0m:\033[38;5;127m 1.5",
        "\033[38;5;45mpapersize\033[0m: a4",
        "\033[38;5;45mdocumentclass\033[0m: scrreprt",
        "-- РЕЖИМ ВСТАВКИ --                                     1,1           Начало"
    ]

    for line in output:
        print(line)

# Запуск функции
colored_output()
