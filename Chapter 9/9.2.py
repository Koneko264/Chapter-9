class Employee:
    def __init__(self, name, ID_num, department, job_title):
        self.name = name
        self.ID_num = ID_num
        self.department = department
        self.job_title = job_title
    def print_data(self):
        print('%20s %20s %20s %20s' % (self.name, self.ID_num, self.department, self.job_title))

Susan_Meyers = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
Mark_Jones = Employee('Mark Jones', '39119', 'IT', 'Programmer')
Joy_Rogers = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

print('%20s %20s %20s %20s\n' % ('Name', 'ID Number', 'Department', 'Job Title'))
Susan_Meyers.print_data()
Mark_Jones.print_data()
Joy_Rogers.print_data()
