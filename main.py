# Create a generic 'job' class.
# The init method will store the details for name, salary and hours worked
class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

#'job' will have another method that prints those details nicely.
  def job(self):
    print((f'''
    Job type: {self.name}
    Salary: {self.salary} €
    Hours Worked: {self.hoursWorked} per week''')) 

#The 'doctor' subclass should also include 'speciality' and 'years of experience'.
class doctor(job):
  def __init__(self, name, salary, hoursWorked, speciality, yearsOfExperience):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.speciality = speciality
    self.yearsOfExperience = yearsOfExperience

  #The print functions for each sub-class should print this extra data.
  def doctor(self):
    print((f'''
    Job type: {self.name}
    Salary: {self.salary} €
    Hours Worked: {self.hoursWorked} per week
    Speciality: {self.speciality}
    Years of Experience: {self.yearsOfExperience}
    '''))

#The 'teacher' subclass should also include 'subject' and 'position
class teacher(job):
  def __init__(self, name, salary, hoursWorked, subject, position):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.subject = subject
    self.position = position
  
    #The print functions for each sub-class should print this extra data.
  def teacher(self):
    print((f'''
    Job type: {self.name}
    Salary: {self.salary} €
    Hours Worked: {self.hoursWorked} per week
    Subject: {self.subject}
    Position: {self.position}
    '''))



banker = job("Banker",8000, "40")

banker.job()

DrAngeli = doctor("Doctor", 5000, "80", "Hausarzt", 20)
DrAngeli.doctor()

Willi = teacher("Teacher", 3000, "40", "Mathematik", "Vertretung")
Willi.teacher()
