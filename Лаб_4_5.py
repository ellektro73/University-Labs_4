def analyze_text(input_text):
    vowels_set = {'а', 'e', 'є', 'и', 'і', 'ї','о', 'у', 'ю', 'я'}
    consonants_set = {
        'б', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п',
        'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'в','й'
    }

    text_list = list(input_text.lower())

    vowels_count = 0
    consonants_count = 0

    for char in text_list:
        if char in vowels_set:
            vowels_count += 1
        elif char in consonants_set:
            consonants_count += 1

    print(f"Кількість голосних: {vowels_count}")
    print(f"Кількість приголосних: {consonants_count}")

    if vowels_count > consonants_count:
        result_msg = "Голосних літер більше."
        result_set = vowels_set
    elif consonants_count > vowels_count:
        result_msg = "Приголосних літер більше."
        result_set = consonants_set
    else:
        result_msg = "Кількість однаковий або літер немає."
        temp_list = list(vowels_set.union(consonants_set))
        result_set = set(temp_list)

    return result_msg, result_set


def print_result_set(data_set):
    print("Множина відповідних літер:")
    print(data_set)


def main():
    user_text = input("Введіть текст (цифри та латинські літери): ")

    message, final_set = analyze_text(user_text)

    print(f"\nРезультат: {message}")
    print_result_set(final_set)


if __name__ == "__main__":
    main()