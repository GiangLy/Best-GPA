# gpa.py
#    Program to find student with highest GPA

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():
    # open the input file for reading
    filename = input("Enter name the grade file: ")
    infile = open(filename, 'r')

    # set best to the record for the first student in the file
    best = makeStudent(infile.readline())
    studentlist = []
    # process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        s = makeStudent(line)
        # if this student is best so far, remember it.
        if s.gpa() > best.gpa():
            best = s
        elif s.gpa() == best.gpa():
            studentlist.append(s)
    
    studentlist.append(best)

    infile.close()
    
    print("There are {0} best students.".format(len(studentlist)))
    for i in range(len(studentlist)):
        # print information about the best student
        print("The best student is:", studentlist[i].getName())
        print("hours:", studentlist[i].getHours())
        print("GPA:", studentlist[i].gpa())

if __name__ == '__main__':
    main()
