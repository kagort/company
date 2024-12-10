"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

def dep_names_output (departments): # 1. Вывести названия всех отделов
    for item in departments:
        dep_name = item["title"]
        print(dep_name)

all_dep_names = dep_names_output(departments)
print()

def employers_names_output (departments): #2. Вывести имена всех сотрудников компании.
    for item in departments:
        for employer in item["employers"]:
            print(f"{employer['first_name']} {employer['last_name']}")
all_employers_names = employers_names_output(departments)
print()

def dep_employers_names(departements): # 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
    for item in departements:
        print(item["title"])
        for employer in item["employers"]:
            print(f"{employer['first_name']} {employer['last_name']}")
        print()
all_dep_emp_names = dep_employers_names(departments)

def emp_names_biggest_salary (departments): # 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
    emp_with_biggest_salary = []
    for item in departments:
        for employer in item["employers"]:
            if employer["salary_rub"]>= 100000:
                full_name = f"{employer['first_name']} {employer['last_name']}"
                emp_with_biggest_salary.append(full_name)
    return emp_with_biggest_salary
print("Сотрудники с самой высокой зарплатой:")
result = emp_names_biggest_salary(departments)
result_str = "\n".join(result)
print(result_str)
print()

def poor_position (departments): # 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
    bad_position = []
    for item in departments:
        for employer in item["employers"]:
            if employer["salary_rub"]<80000:
                position = f"{employer['position']}"
                bad_position.append(position)
    return bad_position
print("Позиции с самой низкой зарплатой:")
result = poor_position(departments)
unique_result = list(set(result))
result_str = "\n".join(unique_result)
print(result_str)
print()

def dep_costs_per_month (departments): # 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела.
    for item in departments:
        total_salary = 0
        for employer in item["employers"]:
            total_salary += employer["salary_rub"]
        print(f"В месяц уходит на {item['title']}: {total_salary} рублей")

dep_total_salary = dep_costs_per_month(departments)
print(dep_total_salary)
#(Как убрать None в выводе?)









