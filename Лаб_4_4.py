def print_list(data_list, message="Список:"):

    if not data_list:
        print(f"{message} (порожній)")
    else:
        print(f"{message} {data_list}")

def get_every_third_element(original_list):
    new_list = original_list[2::3]
    return new_list


def main():
    print("Програма для формування списку з кожних третіх елементів")

    user_input = input("Введіть елементи списку через пробіл: ")
    source_list = user_input.split()

    print_list(source_list, "Початковий список:")

    if len(source_list) < 3:
        print("\nПомилка: у списку замало елементів для виконання операції.")
    else:
        result_list = get_every_third_element(source_list)

        print_list(result_list, "Новий список (кожен третій елемент):")


if __name__ == "__main__":
    main()