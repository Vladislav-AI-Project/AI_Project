from app.menu import show_menu


def main():
    choice = ""
    while choice != "4":
        show_menu()
        choice = input("\nВыберите пункт: ")
        if choice == "1":
           print("📈 Запуск Crypto Agent...")
        elif choice == "2":
           print("🤖 Запуск AI Agent...")
        elif choice == "3":
           print("📰 Запуск News Agent...")
        elif choice == "4":
           print("👋 До свидания!")
        elif choice == "5":
            print("⚙️ Раздел настроек пока находится в разработке.")
        else:
            print("❌ Неверный выбор.")
if __name__ == "__main__":
    main()