def check_fermat_theorem(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print("Упс! Великая теорема Ферма оказалась ложной!")
    else:
        print("Ура! Великая теорема Ферма верна для n=3.")

def main():
    # Вводим значения a, b, c, n
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    c = int(input("Введите значение c: "))
    n = int(input("Введите значение n (n должно быть больше 2): "))

    # Проверяем теорему Ферма
    check_fermat_theorem(a, b, c, n)

if __name__ == "__main__":
    main()
