################                 BetterWay 22                 ################
# 딕셔너리와 튜플보다는 헬퍼 클래스로 관리하자
class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)

print(book.average_grade('Isaac Newton'))
print(book._grades)

class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
book.average_grade('Albert Einstein')
print(book._grades)

class WeightedGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            subject_avg /= total_weight
            score_sum += subject_avg
            score_count += 1
        return score_sum / score_count

book = WeightedGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 80, 0.5)
book.report_grade('Albert Einstein', 'Math', 90, 0.5)
book.report_grade('Albert Einstein', 'Gym', 90, 1.0)
book.report_grade('Albert Einstein', 'Gym', 80, 0.0)
book.average_grade('Albert Einstein')
print(book._grades)

import collections

Grade = collections.namedtuple('Grade', ('score', 'weight'))
#Grade(10, 20).score
#Grade(10, 0.1).weight

class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student(object):
    def __init__(self):
        self._subject = {}

    def subject(self, name):
        if name not in self._subject:
            self._subject[name] = Subject()
        return self._subject[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subject.values():
            total += subject.average_grade()
            count += 1
        return total / count

class GradeBook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

book = GradeBook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.10)
math.report_grade(70, 0.20)
gym = albert.subject('Gym')
gym.report_grade(90, 0.30)
gym.report_grade(80, 0.50)

print(albert.average_grade())
