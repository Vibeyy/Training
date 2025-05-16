#id,name,course,marks in dictionary
#add,view,update and delete functions
import json

class Student:
    __student_data = {}
    
    def add_student_info(self):
        student_id = int(input("Enter student id: "))
        if student_id not in self.__student_data:
            student_name = input("Enter student name: ")
            student_course = input("Enter student course: ")
            student_marks = int(input("Enter student marks: "))
            self.__student_data[student_id] = {"name": student_name, "course": student_course, "marks": student_marks}
            print("Student information added successfully.")
            self.add_to_json_file()
        else:
            print(f"Student data is already present for id: {student_id}")

    def view_student_info(self):
        student_id = int(input("Enter student id: "))
        if student_id in self.__student_data:
            print(f"Name: {self.__student_data[student_id]['name']}")
            print(f"Course: {self.__student_data[student_id]['course']}")
            print(f"Marks: {self.__student_data[student_id]['marks']}")
        else:
            print("Student information not found.")

    def update_student_info(self):
        student_id = int(input("Enter student id: "))
        if student_id in self.__student_data:
            student_name = input("Enter student name: ")
            student_course = input("Enter student course: ")
            student_marks = int(input("Enter student marks: "))
            self.__student_data[student_id] = {"name": student_name, "course": student_course, "marks": student_marks}
            print(f"Updated the information for Student {student_id} successfully")
            self.add_to_json_file()
        else:
            print("Student not found!")

    def delete_student_info(self):
        student_id = int(input("Enter the student ID: "))
        if student_id in self.__student_data:
            self.__student_data.pop(student_id)
            print(f"The record of the student {student_id} has been removed!")
            self.add_to_json_file()
        else:
            print("Student ID not found!")
    
    def __len__(self):
        return len(self.__student_data)
    
    def add_to_json_file(self):
        for key,value in self.__student_data.items():
            print(type(key))
        with open("student_data.json", "w") as f:
            json.dump(self.__student_data, f,indent=4)
    
    def retrieve_from_json(self):
        try:
            with open("student_data.json","r") as f:
                data = json.load(f)
                for key,value in data.items():
                    self.__student_data[int(key)] = value
                if len(self.__student_data)==0:
                    print("Fetching Data from the student data file.The file is empty, add student data")
                else:
                    print("Fetching data from the student data file. Fetched Successfully")
        except FileNotFoundError:
            print("File not found, creating a new file! Please Continue.")
    def view_all_student_info(self):
        self.retrieve_from_json()
        for key,value in self.__student_data.items():
            print(f"The record for student id {key} is:")
            print(f"Name: {self.__student_data[key]['name']}")
            print(f"Course: {self.__student_data[key]['course']}")
            print(f"Marks: {self.__student_data[key]['marks']}")
        
    
s = Student()
s.retrieve_from_json()
while True:
    choice = int(input("1.Add student data\n2.View all student data\n3.View student record with specific ID\n4.Update student data\n5.Delete Student data\n6.Exit\nEnter the choice : "))
    if choice == 1:
        s.add_student_info()
    elif choice == 2:
        s.view_all_student_info()
    elif choice == 3:
        s.view_student_info()
    elif choice == 4:
        s.update_student_info()
    elif choice == 5:
        s.delete_student_info()
    elif choice == 6:
        print("Number Of Student Records present before quiting is: ",len(s))
        break
    else:
        print("Please Enter a correct choice!")