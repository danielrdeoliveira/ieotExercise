from file_open import File
from employee import Employee


if __name__ == '__main__':
    f = File()
    employee_dic = f.read_employees(filename="schedules.txt")
    print(employee_dic)
    employee_list = [Employee(k, v) for (k, v) in employee_dic.items()]

    for emp in employee_list:
        print(f"The amount to pay {emp.name} is: {emp.payment} USD")
