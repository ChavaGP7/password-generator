from generator.password_generator import generate_password


def main():
    print("Password Generator")
    print("------------------")

    length = int(input("Enter password length: "))

    password = generate_password(length)

    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
