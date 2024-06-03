import pymysql
from tkinter import *
from tkinter import messagebox  # 消息提示框
from tkinter import ttk
from query_course_students import QueryCourseStudents
from student_management import StudentManagement
from course_management import CourseManagement


class Register:

    def __init__(self, master):
        self.root = master  # 窗口传入
        # 数据库登录
        self.ip = 'localhost'
        self.port = 3306
        self.id = 'root'
        self.pd = 'Xyn20040516!'
        self.db = 'school_db'
        # 个人信息
        self.no = ''
        self.name = ''
        self.sex = ''
        self.birthday = ''
        self.tel = ''
        self.flag = 0
        # 临时变量(click单击后选择的变量 smanage中)
        self.temporary_sno = ''
        self.temporary_sname = ''
        self.temporary_sex = ''
        self.temporary_birth = ''
        self.temporary_tel = ''
        self.temporary_pwd = ''
        self.temporary_cno = ''
        self.temporary_cname = ''

    '''
    登录模块
    '''

    def register(self):
        # 账号密码输入框
        self.initface = LabelFrame(self.root, text='教务系统登录', font=('微软雅黑', 16))
        self.initface.grid(row=1, column=0, padx=170, pady=30, )

        self.people = Label(self.initface, text='账号 :', font=('黑体', 12))  # 账号
        self.people.grid(row=1, column=0, padx=20, pady=10, sticky=W)
        self.password = Label(self.initface, text='密码 :', font=('黑体', 12))  # 密码
        self.password.grid(row=2, column=0, padx=20, pady=10, sticky=W)
        self.var1 = StringVar
        self.var2 = StringVar
        self.entry_people = Entry(self.initface, textvariable=self.var1)  # 账号输入框
        self.entry_people.grid(row=1, column=1, padx=10, pady=10)
        self.entry_password = Entry(self.initface, textvariable=self.var2, show='*')  # 密码输入框
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        self.button_into = Button(self.initface, text='登录', command=self.conn)  # 登录按钮
        self.button_into.grid(row=3, column=0, padx=10, pady=20, sticky=E)
        self.button_into = Button(self.initface, text='退出', command=self.root.quit)  # 退出按钮
        self.button_into.grid(row=3, column=1, padx=20, pady=20, )

    # ======= register的登录
    def conn(self):
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.id, passwd=self.pd, db=self.db)
        self.cursor = self.connect.cursor()
        if self.connect:
            print('连接成功')
        user = self.entry_people.get()
        password = self.entry_password.get()

        # 学生登录验证
        self.ssql = "SELECT * FROM student_pwd WHERE user=%s AND pwd=%s"
        self.cursor.execute(self.ssql, (user, password))
        self.result = self.cursor.fetchone()
        if self.result:
            print('账号密码正确')
            self.flag = 1
            self.no = self.result[0]
            self.initface.destroy()  # 销毁initface
            self.check()
        else:
            # 教师登录验证
            self.tsql = "SELECT * FROM teacher_pwd WHERE user=%s AND pwd=%s"
            self.cursor.execute(self.tsql, (user, password))
            self.result = self.cursor.fetchone()
            if self.result:
                print('账号密码正确')
                self.flag = 2
                self.no = self.result[0]
                self.initface.destroy()  # 销毁initface
                self.check()

        # 若均未登录成功
        if self.flag == 0:
            # 账号或密码错误清空输入框
            self.entry_people.delete(0, END)
            self.entry_password.delete(0, END)
            messagebox.showinfo(title='提示', message='账号或密码输入错误\n请重新输入?')

        create_view_sql = """
            CREATE OR REPLACE VIEW student_scores_view AS
            SELECT 
                s.sno,
                s.sname,
                sc.tcid,
                sc.score
            FROM
                student s
            JOIN
                student_course sc ON s.sno = sc.sno;
            """
        self.cursor.execute(create_view_sql)
        self.connect.commit()

        self.cursor.close()
        self.connect.close()

    '''
    选择模块
    '''

    def check(self):
        # 查询并记录基本信息
        self.basic()  # self.no self.name self.sex self.sex self.birthday self.tel
        self.label_basic = Label(self.root, text='\n'
                                                 '学号/工号: %s\n\n'
                                                 '姓名: %s\n\n'
                                                 '性别: %s\n\n'
                                                 '出生日期: %s\n\n'
                                                 '联系方式: %s\n\n' %
                                                 (self.no, self.name, self.sex,
                                                  self.birthday, self.tel),
                                 font=('宋体', 10)
                                 )
        self.label_basic.grid(row=0, columnspan=4, padx=230)
        # 界面
        self.frame_checkbutton = LabelFrame(self.root, text='功能选择', font=('微软雅黑', 14))
        self.frame_checkbutton.grid(padx=60, pady=10)
        if self.flag == 1:
            # 查询成绩按钮
            self.button_success = Button(self.frame_checkbutton, text='查询成绩', width=10, height=2,
                                         command=self.success)
            self.button_success.grid(row=1, column=0, padx=20, pady=20)

            # 选择课程按钮
            self.button_select = Button(self.frame_checkbutton, text='选课', width=10, height=2, command=self.select)
            self.button_select.grid(row=1, column=1, padx=20, pady=20)
        elif self.flag == 2:
            # 学生管理按钮 以及成绩管理
            self.button_smanage = Button(self.frame_checkbutton, text='学生管理', width=10, height=2,
                                         command=self.smanage)
            self.button_smanage.grid(row=1, column=0, padx=20, pady=20)

            self.button_cmanage = Button(self.frame_checkbutton, text='课程管理', width=10, height=2,
                                         command=self.cmanage)
            self.button_cmanage.grid(row=1, column=1, padx=20, pady=20)

            # 添加课程学生查询按钮
            self.button_query_course_students = Button(self.frame_checkbutton, text='课程学生查询', width=15, height=2,
                                                       command=self.query_course_students)
            self.button_query_course_students.grid(row=2, column=0, padx=20, pady=20)

        # 修改密码按钮
        self.button_revise = Button(self.frame_checkbutton, text='修改密码', width=10, height=2, command=self.revise)
        self.button_revise.grid(row=1, column=2, padx=20, pady=20)
        # 修改信息按钮
        self.button_select = Button(self.frame_checkbutton, text='修改信息', width=10, height=2, command=self.update)
        self.button_select.grid(row=1, column=3, padx=20, pady=20)

    def basic(self):
        # 链接数据库
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.id, passwd=self.pd, db=self.db)
        if self.connect:
            print('连接成功')
            print(self.no)  # 用户名, 即学号/工号
            # 查询语句
            search_sql = ''
            if self.flag == 1:
                search_sql = "SELECT * FROM student WHERE sno=%s"
            elif self.flag == 2:
                search_sql = "SELECT * FROM teacher WHERE tno=%s"
            # 创建游标
            self.cursor1 = self.connect.cursor()
            self.cursor1.execute(search_sql, (self.no,))
            self.row = self.cursor1.fetchone()  # 读取查询结果

            self.name = self.row[1]
            self.sex = self.row[2]
            self.birthday = self.row[3]
            self.tel = self.row[4]
            self.row = ()  # 查询结果置空

    def query_course_students(self):
        qcs = QueryCourseStudents(self.root)
        qcs.query_course_students()

    def success(self):
        # 链接数据库
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.id, passwd=self.pd, db=self.db)
        if self.connect:
            print('连接成功')
            print(self.no)  # 用户名, 即学号
            # 查询语句
            search_sql = "SELECT c.cno, c.cname, sc.score " \
                         "FROM student_course sc " \
                         "INNER JOIN course c ON sc.tcid = c.cno " \
                         "WHERE sc.sno = %s"

            # 创建游标
            self.cursor1 = self.connect.cursor()
            self.cursor1.execute(search_sql, (self.no,))
            self.row = self.cursor1.fetchone()  # 读取查询结果

            # 表格框
            root = Tk()  # 初始框的声明
            root.geometry('500x400+100+100')
            root.title('成绩查询系统')
            columns = ("姓名", "学号", "课程", "成绩")
            self.treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)
            self.treeview.column("姓名", width=150, anchor='center')  # 表示列,不显示
            self.treeview.column("学号", width=100, anchor='center')
            self.treeview.column("课程", width=150, anchor='center')
            self.treeview.column("成绩", width=100, anchor='center')

            self.treeview.heading("姓名", text="姓名")  # 显示表头
            self.treeview.heading("学号", text="学号")
            self.treeview.heading("课程", text="课程")
            self.treeview.heading("成绩", text="成绩")
            self.treeview.pack(side=LEFT, fill=BOTH)

            # 插入查询结果
            while self.row:
                self.treeview.insert('', 0, values=(self.name, self.no, self.row[1], self.row[2]))
                self.row = self.cursor1.fetchone()

            self.cursor1.close()
            self.connect.close()
            root.mainloop()

    def revise(self):
        self.window = Tk()  # 初始框的声明
        self.window.geometry('400x200+100+100')
        self.window.title('密码修改管理')
        self.frame_revise = LabelFrame(self.window)
        self.frame_revise.grid(padx=60, pady=60)
        self.label_revise = Label(self.frame_revise, text='新密码：')
        self.label_revise.grid(row=0, column=0, padx=10, pady=10)
        self.var3 = StringVar
        self.entry_revise = Entry(self.frame_revise, textvariable=self.var3)
        self.entry_revise.grid(row=0, column=1, padx=10, pady=10)
        self.button_ok = Button(self.frame_revise, text='确定', command=self.revise_ok)
        self.button_ok.grid(row=1, column=0)
        self.button_resive = Button(self.frame_revise, text='取消', command=self.revise_resive)
        self.button_resive.grid(row=1, column=1)
        self.button_quit = Button(self.frame_revise, text='退出', command=self.window.destroy)
        self.button_quit.grid(row=1, column=2)

    def revise_ok(self):
        # 连接数据库
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.id, passwd=self.pd, db=self.db)
        self.cursor2 = self.connect.cursor()  # 创建游标
        sql_revise = ''
        new_password = self.entry_revise.get()
        if self.flag == 1:
            sql_revise = "UPDATE student_pwd SET pwd=%s WHERE user=%s"
        elif self.flag == 2:
            sql_revise = "UPDATE teacher_pwd SET pwd=%s WHERE user=%s"

        if self.connect:
            print('连接成功')
            print(self.no)
            self.cursor2.execute(sql_revise, (new_password, self.no))
            self.connect.commit()
            print(new_password)
            messagebox.showinfo(title='提示', message='密码修改成功!')
            self.cursor2.close()
            self.connect.close()

    def revise_resive(self):
        self.entry_revise.delete(0, END)

    def select(self):
        sm = StudentManagement(self.root, self.ip, self.port, self.id, self.pd, self.db, self.no)
        sm.select()

    def update(self):
        self.window = Tk()
        self.window.geometry('400x400')
        self.window.title('更新个人信息')

        self.varno = StringVar(self.window, value=self.no)
        self.varname = StringVar(self.window, value=self.name)
        self.varsex = StringVar(self.window, value=self.sex)
        self.varbirth = StringVar(self.window, value=self.birthday)
        self.vartel = StringVar(self.window, value=self.tel)
        # 输入框展示个人信息
        self.entry_no = Entry(self.window, textvariable=self.varno, state='disabled')  # 账号输入框
        self.entry_no.grid(row=1, column=1, padx=10, pady=10)
        self.entry_name = Entry(self.window, textvariable=self.varname)  # 名字输入框
        self.entry_name.grid(row=2, column=1, padx=10, pady=10)
        self.entry_sex = Entry(self.window, textvariable=self.varsex)  # 性别输入框
        self.entry_sex.grid(row=3, column=1, padx=10, pady=10)
        self.entry_birth = Entry(self.window, textvariable=self.varbirth)  # birth输入框
        self.entry_birth.grid(row=4, column=1, padx=10, pady=10)
        self.entry_tel = Entry(self.window, textvariable=self.vartel)
        self.entry_tel.grid(row=5, column=1, padx=10, pady=10)
        # Label输入框
        self.label_no = Label(self.window, text='学号/工号:', font=('黑体', 12))
        self.label_no.grid(row=1, column=0, padx=10, pady=10)
        self.label_name = Label(self.window, text='姓名:', font=('黑体', 12))
        self.label_name.grid(row=2, column=0, padx=10, pady=10)
        self.label_sex = Label(self.window, text='性别:', font=('黑体', 12))
        self.label_sex.grid(row=3, column=0, padx=10, pady=10)
        self.label_birth = Label(self.window, text='生日:', font=('黑体', 12))
        self.label_birth.grid(row=4, column=0, padx=10, pady=10)
        self.label_tel = Label(self.window, text='联系方式:', font=('黑体', 12))
        self.label_tel.grid(row=5, column=0, padx=10, pady=10)
        # Lable个人信息
        self.label_info = Label(self.window, text='\n'
                                                  '学号/工号: %s\n\n'
                                                  '姓名: %s\n\n'
                                                  '性别: %s\n\n'
                                                  '出生日期: %s\n\n'
                                                  '联系方式: %s\n\n' %
                                                  (self.no, self.name, self.sex,
                                                   self.birthday, self.tel),
                                font=('宋体', 10)
                                )
        self.label_info.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky=W)
        # 更新按钮
        self.button_update = Button(self.window, text='更新', width=10, height=2, command=self.update_up)
        self.button_update.grid(row=2, column=2, padx=10, pady=10, rowspan=3)

        self.window.mainloop()

    def update_up(self):
        # 连接数据库
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.id, passwd=self.pd, db=self.db)
        self.cursor2 = self.connect.cursor()  # 创建游标
        sql_up = ''
        if self.flag == 1:
            sql_up = "UPDATE student SET sname=%s, sex=%s, birthday=%s, tel=%s WHERE sno=%s"
        elif self.flag == 2:
            sql_up = "UPDATE teacher SET tname=%s, sex=%s, birthday=%s, tel=%s WHERE tno=%s"

        if self.connect:
            print('连接成功')
            print(self.no)
            self.cursor2.execute(sql_up, (
            self.entry_name.get(), self.entry_sex.get(), self.entry_birth.get(), self.entry_tel.get(), self.no))
            self.connect.commit()
            messagebox.showinfo(title='提示', message='信息修改成功!')
            self.cursor2.close()
            self.connect.close()

    def smanage(self):
        sm = StudentManagement(self.root, self.ip, self.port, self.id, self.pd, self.db, self.no)
        sm.smanage()

    def cmanage(self):
        cm = CourseManagement(self.root, self.ip, self.port, self.id, self.pd, self.db, self.no)
        cm.cmanage()
