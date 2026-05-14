def print_list(data_list, message="Поточний список:"):
    print(f"{message} {data_list}")


def remove_by_value(data_list, value):
    if value in data_list:
        data_list.remove(value)
        print(f"Елемент '{value}' успішно видалено.")
        return True
    else:
        print(f"Помилка: Елемента '{value}' немає у списку.")
        return False


def main():
    user_input = input("Введіть елементи списку через пробіл: ")
    my_list = user_input.split()

    if not my_list:
        print("Список порожній.")
        return

    print_list(my_list, "Початковий список:")
    val_to_delete = input("Введіть значення для видалення: ")
    remove_by_value(my_list, val_to_delete)
    print_list(my_list, "Оновлений список:")

if __name__ == "__main__":
    main()