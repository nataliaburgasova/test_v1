# импортируем файл,откуда брать класс Question 
from Question import Question

#создаём список из 10 вопросов с различными вариантами ответов
question_promts = [
    "1.Создатель языка программирования Python\n(a) Гвидо Ван Россум\n(b) Дэвид Паттерсон\n(c) Эрвин Дональд Кнут\n(d) Джеймс Артур Гослинг\n\n",
    "2.Python является\n(a) компилируемым языком\n(b) интерпретируемым языком\n\n",
    "3.Команда print() используется для\n(a) вывода данных на экран\n(b)считывания данных с клавиатуры\n\n",
    "4.Значения для вывода, указываемые через запятую в команде print(), называются\n(a) аргументами\n(b) символами\n(c) строками\n\n",
    "5.Какие из имён допустимы для названия переменных в Python?\n(a) teacher_2\n(b) 2teacher\n(c) !2_teacher\n\n",
    "6.Вычислите результат целочисленного деления 23//7\n(a) 4\n(b) 3\n(c) 5\n\n",
    "7.Вычислите остаток от деления 23%7\n(a) 3\n(b) 2\n(c) 1\n\n",
    "8.Что будет выведено на экран в результате выполнения следующей программы?\nprint (82 // 3 ** 2 % 7)\n(a) 2\n(b) 41\n(c) 9\n\n",
    "9.Для чего нужен оператор break?\n(a) Для выхода из цикла\n(b) Для завершения программы\n(c) Для удаления программы\n\n",
    "10.Что делает функция len()\n(a) Возвращает случайное число\n(b) Возвращает длину строки\n(c) Возвращает номер символа\n(d) Возвращает модуль числа\n\n"
]

#создаём список, в котором указываем номер вопроса и верный ответ        
questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "b"),
    Question(question_promts[2], "a"),
    Question(question_promts[3], "a"),
    Question(question_promts[4], "a"),
    Question(question_promts[5], "b"),
    Question(question_promts[6], "b"),
    Question(question_promts[7], "a"),
    Question(question_promts[8], "a"),
    Question(question_promts[9], "b")
]

# создаём функцию define для запуска теста
def run_test(questions):
    score = 0 #счетчик ответов
    for question in questions: #создаем цикл перебора вопросов
        otvet = input (question.vopros) #ввод ответа пользователем
        if otvet == question.otvet:
            score +=1 #в случае верного ответа увеличитьколичество верных на +1
    print("У вас " + str(score)+ " ответов из 10 верных") #сколько верных ответов дано пользователем
    print ("Ваша оценка: ")
    if score == 10: #перевод баллов в отметку
            print ("5")
    if score > 7 and score <= 9:
            print ("4")
    if score <= 7 and score >= 6:
            print ("3")
    if score < 6: print ("2")
    
#запуск теста
run_test(questions)

    
