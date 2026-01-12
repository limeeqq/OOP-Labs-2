from student import Student
from binary_tree import BinaryTree

def run_lab2():
    print("\nСписок студентів:")
    
    group_list = []
    
    s1 = Student("Максим", "Сидорець", 1, "KB123", 2005, "IP-14")
    s2 = Student("Марина", "Зайчук", 2, "KB124", 2004, "IP-12")
    s3 = Student("Миколай", "Танков", 1, "KB125", 2005, "IP-11")
    s4 = Student("Миколай", "Неколяй", 3, "KB126", 2003, "IP-13")

    group_list.append(s1)
    group_list.append(s2)
    group_list.append(s3)
    group_list.append(s4)
    print(f"У списку {len(group_list)} студентів.")

    print("шукаємо студента 'Танков'...")
    for s in group_list:
        if s.last_name == "Танков":
            print(f" -> Знайдено: {s.get_info()}")

    print("В=видаляємо студента 'Сидорець'...")
    group_list.remove(s1)
    

    print("залишились у списку:")
    for s in group_list:
        print(f" - {s}")


 
    print("\nбінарне дерево:")
    
    tree = BinaryTree()
    
    print("Заповнюємо дерево...")

    tree.add(s4)
    tree.add(s2)
    tree.add(s3)
    tree.add(s1)
  
    tree.show_tree()

if __name__ == "__main__":
    run_lab2()