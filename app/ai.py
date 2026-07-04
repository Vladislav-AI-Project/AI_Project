def show_ai():
    print("=" * 40)
    print("📈 AI Agent")
    print("=" * 40)
    print("1. GPT")
    print("2. Claude")
    print("3. Gemini")
    ai_model = input("Выберите модель: ")
    if ai_model == "1":
        ai_model = "GPT"
    elif ai_model == "2":
        ai_model = "Claude"
    elif ai_model == "3":
        ai_model = "Gemini"
    print(f"Выбранная модель: {ai_model}")

    print("Пока находится в разработке.") 

    input("\nНажмите Enter для возврата в меню...")