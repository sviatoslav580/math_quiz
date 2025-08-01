import random

a = random.randint(0, 10)
b = random.randint(0, 10)


def generate_math_question():
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    problem = f"{a} {operation} {b}"
    return problem


def check_answer(primer, otvet):
    x = eval(primer)
    try:
        otvet = float(otvet)
        if otvet == x:
            return True
        else:
            return False

    except ValueError:
        return False


def math_quiz(number_of_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        sozdaniye_primerov = generate_math_question()
        print(sozdaniye_primerov)
        otvet_ot_cheloveka = input("Введите ответ: ")
        if check_answer(sozdaniye_primerov, otvet_ot_cheloveka):
            correct_answers += 1
            

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers >= number_of_questions * 0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers >= number_of_questions * 0.4:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


math_quiz()
