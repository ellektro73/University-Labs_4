def main():
    try:
        n = int(input("Введіть кількість елементів масиву (N): "))

        if n <= 0:
            print("Довжина масиву повинна бути більшою за 0.")
            return

        array = []
        print(f"Введіть {n} дійсних елементів:")
        for i in range(n):
            element = float(input(f"Елемент {i + 1}: "))
            array.append(element)

        non_zero_elements = [x for x in array if x != 0]

        print("\nНенульові елементи у зворотному порядку:")

        if non_zero_elements:
            reversed_array = non_zero_elements[::-1]

            for item in reversed_array:
                print(item, end=" ")
            print()
        else:
            print("Ненульових елементів не знайдено.")

    except ValueError:
        print("Помилка: будь ласка, введіть число (ціле для N та дійсне для елементів).")


if __name__ == "__main__":
    main()