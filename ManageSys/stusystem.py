import os

filename = "student.txt"


def menu():
    print("============================学生信息管理系统===========================")
    print("------------------------------功能菜单--------------------------------")
    print("\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t5.排序")
    print("\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t7.显示所有学生信息")
    print("\t\t\t\t\t\t0.退出系统")
    print("----------------------------------------------------------------------")


def main():
    while True:
        menu()
        choice = int(input("请选择"))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("您确定要退出系统吗?y/n")
                if answer == 'y' or answer == 'Y':
                    print("谢谢您的使用！！！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def insert():
    student_list = []
    while True:
        id = input("请输入ID（如1001）： ")
        if not id:
            break
        name = input("请输入姓名: ")
        if not name:
            break

        try:
            english = int(input("请输入英语成绩： "))
            python = int(input("请输入python成绩： "))
            java = int(input("请输入java成绩: "))
        except:
            print("输入无效，不是整数类型，请重新输入\n")
            continue
        student = {'id': id, 'name': 'name', 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input("是否继续添加?y/n\n")
        if answer == 'y':
            continue
        else:
            break

    save(student_list)
    print("学生信息录入完毕！\n")


def search():
    pass


def delete():
    while True:
        student_id = input("请输入要删除学生的id")
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id 为 {student_id} 的学生已经被删除啦')
                    else:
                        print(f"没有找到id为 {student_id} 的学生")
            else:
                print("无学生信息")
                break
            show()
            answer = input("是否继续删除y/n?\n")
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            student_old = file.readlines()
    else:
        return

    student_id = input("请输入要修改学员的id")
    with open(filename, 'w') as file:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print("找到学生了，可以修改信息了")
                while True:
                    try:
                        d['name'] = input("请输入姓名")
                        d['english'] = input("请输入英语成绩")
                        d['python'] = input("请输入python成绩")
                        d['java'] = input("请输入java成绩")
                    except:
                        print("您的输入有误，请重新输入")
                    else:
                        break
                file.write(str(d) + '\n')
                print("修改成功")
            else:
                file.write(str(d) + '\n')
            answer = input("是否要继续修改其他学生的信息呢？y/n\n")
            if answer == 'y':
                continue
            else:
                break


def sort():
    pass


def total():
    pass


def show():
    pass


def save(lst):
    try:
        stu_txt = open(filename, 'a')
    except:
        stu_txt = open(filename, 'w')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


if __name__ == "__main__":
    main()
