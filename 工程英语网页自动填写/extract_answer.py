import re
import os
import sys,io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
# os.chdir(sys.path[0])

class extract_answer():
    def __init__(self, unit):
        self.unit = unit
        self.file = open('.\工程学科英语答案.txt', 'r',encoding='utf-8')
        self.content = self.search_unit(unit)

    def search_unit(self, unit):
        if unit > 10 or unit < 1:
            raise Exception('无效unit')
        while True:
            line = self.file.readline()
            if 'U'+str(unit) in line:
                break
        content = self.file.read()
        if unit == 10:
            total_content = re.search('Task2(.+)', content, re.S).group(0)
        else:
            total_content = re.search(
                'Task2(.+?)'+'U'+str(unit+1), content, re.S).group(0)
        return total_content

    def task2(self):
        content = re.search('Task2(.+?)Task3', self.content, re.S).group()
        answer = re.findall('\((\w)\)', content, re.S)
        if not answer:
            raise Exception('task2未找到答案')
        return answer

    def task3(self):
        content = re.search('Task3(.+?)Task4', self.content, re.S).group()
        answer = re.findall('\((\w)\)', content, re.S)
        if not answer:
            raise Exception('task3未找到答案')
        return answer

    def task4(self):
        content = re.search('Task4(.+?)Task5', self.content, re.S).group()
        answer = re.findall('\((.+?)\)', content, re.S)
        if not answer:
            raise Exception('task4未找到答案')
        return answer

    def task5(self):
        content = re.search('Task5(.+?)Task6', self.content, re.S).group()
        answer = re.findall('\((.+?)\)', content, re.S)
        if not answer:
            raise Exception('task5未找到答案')
        return answer

    def task6(self):
        content = re.search('Task6(.+?)Task7', self.content, re.S).group()
        answer = re.findall('\((.+?)\)', content, re.S)
        if not answer:
            raise Exception('task6未找到答案')
        return answer

    def task7(self):
        content = re.search('Task7(.+?)Task8', self.content, re.S).group()
        answer = re.findall('Reference answer： (.+)', content)
        if not answer:
            raise Exception('task7未找到答案')
        return answer

    def task8(self):
        content = re.search('Task8(.+?)Task9', self.content, re.S).group()
        answer = re.findall('Reference answer：\s*(.+?)\s\s', content, re.S)
        if not answer:
            raise Exception('task8未找到答案')
        return answer

    def task9(self):
        content = re.search('Task9(.+?)Task10',self.content, re.S).group()
        answer = re.findall('\((\w)\)', content, re.S)
        if not answer:
            raise Exception('task9未找到答案')
        return answer

    def task10(self):
        content = re.search('Task10(.+?)Task11', self.content, re.S).group()
        answer = re.findall('\((\w)\)', content, re.S)
        if not answer:
            raise Exception('task10未找到答案')
        return answer

    def task11(self):
        content = re.search('Task11(.+?)Task13',self.content, re.S).group()
        answer = re.findall('\((.+?)\)', content, re.S)
        if not answer:
            raise Exception('task11未找到答案')
        return answer

    def task13(self):
        content = re.search('Task13(.+?)Task14',self.content, re.S).group()
        answer = re.findall('\((.+?)\)', content, re.S)
        if not answer:
            raise Exception('task13未找到答案')
        return answer

    def task14(self):
        content = re.search('Task14(.+)', self.content, re.S).group()
        answer = re.findall('Reference answer[：|:]\s*\[(.+?)\]', content,re.S)
        if not answer:
            answer = re.findall('Reference answer[：|:]\s*(.+)', content)
        if not answer:
            answer = re.findall('\((.+?)\)', content,re.S)
        if not answer:
            raise Exception('task14未找到答案')
        return answer


if __name__ == '__main__':
    for i in range(1,11):
        a = extract_answer(i)
        try:
            b = a.task4()
            print('第%d单元：' % (i), b, len(b))
        except:
            continue
