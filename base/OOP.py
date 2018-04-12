class Student(object):
    def __init__(self, name, gender, score=None):
        self.name = name
        self.score = score
        self.__gender = gender

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# bart = Student('Bart Simpson', 59)
# bart.print_score()
# print()

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')