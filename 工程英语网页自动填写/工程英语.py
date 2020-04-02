from selenium import webdriver
from extract_answer import *
import re
from retrying import retry
import time
import math


__author__ = '龚天'


class shitingshuo():
    def __init__(self, account, password):
        # self.answer=extract_answer(unit)
        self.driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
        self.account = account
        self.password = password
        # self.unit=unit

    def preparation(self):
        self.driver.get('http://47.100.203.126:8081/Common/index.aspx')
        try:# 尝试登陆
            self.driver.find_element_by_name('ctl00$ContentPlaceHolder1$UcLogin1$txt_UserName')\
                .send_keys(self.account)
            self.driver.find_element_by_name('ctl00$ContentPlaceHolder1$UcLogin1$txt_PassWord')\
                .send_keys(self.password)
            self.driver.find_element_by_name('ctl00$ContentPlaceHolder1$UcLogin1$ibtn_ok')\
                .click()
        except:# 已经处于登陆状态，直接前往主页
            self.driver.get(
                'http://47.100.203.126:8081/CourseLearning/ClassroomOnline.aspx')
        self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_div_ok"]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/a')\
            .click()
        self.select_unit()  # 选择单元
        self.driver.find_element_by_link_text('Task 1').click()# 选择Task1

    def select_unit(self):
        temp_unit_xpath = '//*[@id="aspnetForm"]/table/tbody/tr/td[2]/table[1]/tbody/tr[3]/td/div/span/table/tbody/tr[{}]/td[{}]/a'
        if(self.unit%2):# 奇数
            unit_xpath = temp_unit_xpath.format(math.ceil(self.unit/2),2)
        else:# 偶数
            unit_xpath = temp_unit_xpath.format(math.ceil(self.unit/2),4)
        self.driver.find_element_by_xpath(unit_xpath).click()

    @retry(stop_max_attempt_number=7)# 重复尝试
    def do_task2(self):
        ans = self.answer.task2()
        try:
            for n,a in enumerate(ans):
                xpath = r'//input[@type="radio"][@value="{}"]'.format(a)
                self.driver.find_elements_by_xpath(xpath)[n].click()
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:# 跳过非做题页
            self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=7)# 重复尝试
    def do_task3(self):
        ans = self.answer.task3()
        try:# 跳过非做题页
            xpath = r'//input[@type="text"]'
            for n,a in enumerate(ans):
                self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('Task3因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=5)# 重复尝试
    def do_task4(self):
        ans = self.answer.task4()
        try:# 跳过非做题页
            for n,a in enumerate(ans):
                xpath = r'//input[@type="text"]'
                self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task4因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=5)# 重复尝试
    def do_task5(self):
        ans = self.answer.task5()
        try:
            for n,a in enumerate(ans):
                xpath = r'//input[@type="text"]'
                self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task5因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            # self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=7)# 重复尝试
    def do_task6(self):
        ans = self.answer.task6()
        try:
            for n,a in enumerate(ans):
                xpath = r'//input[@type="text"]'
                self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task6因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
            
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            #self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=3)# 重复尝试
    def do_task7(self):
        ans = self.answer.task7()
        try:
            for n,a in enumerate(ans):
                xpath = r'//textarea'
                self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task7因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
            
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            #self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=3)# 重复尝试
    def do_task8(self):
        ans = self.answer.task8()
        try:
            for n,a in enumerate(ans):
                xpath = r'//textarea'
                self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task8因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
            
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            #self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=3)# 重复尝试
    def do_task9(self):
        ans = self.answer.task9()
        try:
            for n,a in enumerate(ans):
                xpath = r'//input[@type="text"]'
                self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task9因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            #self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=3)# 重复尝试
    def do_task10(self):
        ans = self.answer.task10()
        try:
            for n,a in enumerate(ans):
                xpath = r'//input[@type="radio"][@value="{}"]'.format(a)
                self.driver.find_elements_by_xpath(xpath)[n].click()
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task10因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=3)# 重复尝试
    def do_task11(self):
        ans = self.answer.task11()
        try:
            for n,a in enumerate(ans):
                xpath = r'//input[@type="text"]'
                self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task11因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做的Task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=3)# 重复尝试
    def do_task13(self):
        ans = self.answer.task13()
        try:
            for n,a in enumerate(ans):
                xpath = r'//input[@type="text"]'
                self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task13因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:# 跳过已做task
                pass
            finally:# next
                self.driver.find_element_by_link_text('Next').click()
        except:
            self.driver.find_element_by_link_text('Next').click()
            raise Exception()

    @retry(stop_max_attempt_number=3)# 重复尝试
    def do_task14(self):
        ans = self.answer.task14()
        try:
            try:# 第14题有两种题型
                for n,a in enumerate(ans):
                    xpath = r'//input[@type="text"]'
                    self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            except:
                for n,a in enumerate(ans):
                    xpath = r'//textarea'
                    self.driver.find_elements_by_xpath(xpath)[n].send_keys(a)
            time.sleep(3)   # 暂停3秒，防止服务器监测
            try:# submit
                if len(ans)!=len(self.driver.find_elements_by_xpath(xpath)):# 答案与填空不匹配
                    print('task14因程序错误跳过，请自行填写')
                    raise ValueError()
                self.driver.find_element_by_name(
                    'ctl00$ContentPlaceHolder1$submit').click()
                a1 = self.driver.switch_to.alert
                a1.accept()
            except:
                pass
        except:
            self.driver.find_element_by_link_text('Next').click()
            raise Exception()


    def run(self, unit):
        self.answer = extract_answer(unit)
        self.unit = unit
        self.preparation()
        self.do_task2()
        self.do_task3()
        self.do_task4()
        self.do_task5()
        self.do_task6()
        self.do_task7()
        self.do_task8()
        self.do_task9()
        self.do_task10()
        self.do_task11()
        self.do_task13()
        self.do_task14()


if __name__ == '__main__':
    account = input('输入账号：')
    password = input('输入密码：')
    units = input('输入单元(用逗号隔开，如：1,2,3)：')
    units = [int(i) for i in units.split(',')]
    sts = shitingshuo(account, password)
    for i in units:
        sts.run(i)
