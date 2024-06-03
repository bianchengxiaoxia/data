import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class StudentManagement:
    def __init__(self, root, ip, port, user, passwd, db, no):
        self.root = root
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.no = no
        self.temporary_sno = ''
        self.temporary_sname = ''
        self.temporary_sex = ''
        self.temporary_birth = ''
        self.temporary_tel = ''
        self.temporary_pwd = ''
        self.temporary_cno = ''
        self.temporary_cname = ''

    def select(self):
        # 链接数据库
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        if self.connect:
            print('连接成功')
            print(self.no)  # 用户名, 即学号
            # 查询语句
            search_sql1 = "SELECT * FROM course"
            search_sql2 = "SELECT c.cno, c.cname, c.credit " \
                          "FROM student_course sc " \
                          "INNER JOIN course c ON sc.tcid = c.cno " \
                          "WHERE sc.sno = %s"

            # 创建游标
            self.cursor1 = self.connect.cursor()

            # 初始框的声明
            root_select = Toplevel(self.root)
            root_select.geometry('700x500+100+100')
            root_select.title('选课系统')

            # 所有课程表格框
            columns = ("编号", "课程", "学分")
            self.treeview1 = ttk.Treeview(root_select, height=18, show="headings", columns=columns)
            self.treeview1.column("编号", width=50, anchor='center')  # 表示列,不显示
            self.treeview1.column("课程", width=75, anchor='center')
            self.treeview1.column("学分", width=50, anchor='center')
            self.treeview1.heading("编号", text="编号")  # 显示表头
            self.treeview1.heading("课程", text="课程")
            self.treeview1.heading("学分", text="学分")
            self.treeview1.grid(row=1, column=0, rowspan=3)
            # 插入查询结果
            self.cursor1.execute(search_sql1)
            self.row = self.cursor1.fetchone()  # 读取查询结果
            while self.row:
                self.treeview1.insert('', 0, values=(self.row[0], self.row[1], self.row[2]))
                self.row = self.cursor1.fetchone()

            # 已选课程表格框
            self.treeview2 = ttk.Treeview(root_select, height=18, show="headings", columns=columns)
            self.treeview2.column("编号", width=50, anchor='center')  # 表示列,不显示
            self.treeview2.column("课程", width=75, anchor='center')
            self.treeview2.column("学分", width=50, anchor='center')
            self.treeview2.heading("编号", text="编号")  # 显示表头
            self.treeview2.heading("课程", text="课程")
            self.treeview2.heading("学分", text="学分")
            self.treeview2.grid(row=1, column=1, rowspan=3)
            # 插入查询结果
            self.cursor1.execute(search_sql2, (self.no,))
            self.row = self.cursor1.fetchone()  # 读取查询结果
            while self.row:
                self.treeview2.insert('', 0, values=(self.row[0], self.row[1], self.row[2]))
                self.row = self.cursor1.fetchone()

            # 标签
            self.label_selectcourse1 = Label(root_select, text='学校开设课程表')
            self.label_selectcourse1.grid(row=0, column=0, padx=10, pady=10)
            self.label_selectcourse2 = Label(root_select, text='已选课程表')
            self.label_selectcourse2.grid(row=0, column=1, padx=10, pady=10)

            # 按钮框
            self.frame_selectbutton = LabelFrame(root_select, text='选课', font=('微软雅黑', 14))
            self.frame_selectbutton.grid(row=0, column=2, padx=10, pady=10, rowspan=4)
            # 输入框
            self.var4 = StringVar
            self.entry_insert = Entry(self.frame_selectbutton, textvariable=self.var4)
            self.entry_insert.grid(row=2, column=2, padx=10, pady=10)
            # 插入课程按钮
            self.button_insert = Button(self.frame_selectbutton, text='选择', width=10, height=2,
                                        command=self.select_insert)
            self.button_insert.grid(row=3, column=2, padx=10, pady=10)
            # Label
            self.label_selectcourse3 = Label(self.frame_selectbutton, text="输入要选择的课程编号: ")
            self.label_selectcourse3.grid(row=1, column=2, padx=10, pady=10)

            self.cursor1.close()
            self.connect.close()
            root_select.mainloop()

    def select_insert(self):
        # 连接数据库
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        self.cursor2 = self.connect.cursor()  # 创建游标
        # 查询输入课程是否存在
        sql_insert1 = "SELECT * FROM course WHERE cno = %s"
        course_number = self.entry_insert.get()
        # 插入/忽略课程
        sql_insert2 = "INSERT IGNORE INTO student_course (sno, tcid) VALUES (%s, %s);"

        try:
            self.cursor2.execute(sql_insert1, (course_number,))
            self.result = self.cursor2.fetchone()
            if self.result:
                self.cursor2.execute(sql_insert2, (self.no, course_number))
                self.connect.commit()
                messagebox.showinfo(title='提示', message='已添加/已存在!')
            else:
                messagebox.showinfo(title='提示', message='请输入正确的课程编号!')
        except pymysql.Error as e:
            messagebox.showinfo(title='数据库错误', message=str(e))
        finally:
            self.cursor2.close()
            self.connect.close()

    def smanage(self):
        # 链接数据库
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        if self.connect:
            print('连接成功')
            print(self.no)  # 用户名, 即学号
            # 查询语句
            search_sql1 = "SELECT sno, sname, sex, birthday, tel, pwd " \
                          "FROM student " \
                          "INNER JOIN student_pwd ON sno = user"

            # 创建游标
            self.cursor2 = self.connect.cursor()

            # 初始框的声明
            root_smanage = Toplevel(self.root)
            root_smanage.geometry("1150x550+100+100")
            root_smanage.title("学生管理系统")

            # 学生管理表格框
            columns = ("学号", "姓名", "性别", "生日", "电话", "密码")
            self.treeview3 = ttk.Treeview(root_smanage, height=18, show="headings", columns=columns)
            self.treeview3.column("学号", width=80, anchor='center')  # 表示列,不显示
            self.treeview3.column("姓名", width=70, anchor='center')
            self.treeview3.column("性别", width=50, anchor='center')
            self.treeview3.column("生日", width=100, anchor='center')
            self.treeview3.column("电话", width=80, anchor='center')
            self.treeview3.column("密码", width=70, anchor='center')
            self.treeview3.heading("学号", text="学号")  # 显示表头
            self.treeview3.heading("姓名", text="姓名")
            self.treeview3.heading("性别", text="性别")
            self.treeview3.heading("生日", text="生日")
            self.treeview3.heading("电话", text="电话")
            self.treeview3.heading("密码", text="密码")

            self.treeview3.grid(row=1, column=0, rowspan=8, padx=10)
            # 插入查询结果
            self.cursor2.execute(search_sql1)
            self.row = self.cursor2.fetchone()  # 读取查询结果
            while self.row:
                self.treeview3.insert('', 0, values=(
                    self.row[0], self.row[1], self.row[2], self.row[3], self.row[4], self.row[5]))
                self.row = self.cursor2.fetchone()

            # 该生成绩显示表格框
            columns = ("学号", "课程号", "课程", "成绩")
            self.treeview4 = ttk.Treeview(root_smanage, height=18, show="headings", columns=columns)
            self.treeview4.column("学号", width=80, anchor='center')  # 表示列,不显示
            self.treeview4.column("课程号", width=70, anchor='center')
            self.treeview4.column("课程", width=100, anchor='center')
            self.treeview4.column("成绩", width=50, anchor='center')
            self.treeview4.heading("学号", text="学号")  # 显示表头
            self.treeview4.heading("课程号", text="课程号")
            self.treeview4.heading("课程", text="课程")
            self.treeview4.heading("成绩", text="成绩")

            self.treeview4.grid(row=1, column=1, rowspan=8, columnspan=3)

            # 框框
            self.frame_update = LabelFrame(root_smanage, text='修改信息', font=('微软雅黑', 16))
            self.frame_update.grid(row=0, column=6, padx=10, pady=10, rowspan=5)

            # 标签
            self.label_smanage1 = Label(root_smanage, text='学生表')
            self.label_smanage1.grid(row=0, column=0, padx=10, pady=10)
            self.label_smanage2 = Label(root_smanage, text='该生成绩表')
            self.label_smanage2.grid(row=0, column=2, padx=10, pady=10)
            self.label_score = Label(root_smanage, text='该科成绩:')
            self.label_score.grid(row=9, column=1, padx=10, pady=10)
            self.label_smanage_no = Label(self.frame_update, text='学号')
            self.label_smanage_no.grid(row=0, column=0, padx=10, pady=10)
            self.label_smanage_name = Label(self.frame_update, text='姓名')
            self.label_smanage_name.grid(row=1, column=0, padx=10, pady=10)
            self.label_smanage_sex = Label(self.frame_update, text='性别')
            self.label_smanage_sex.grid(row=2, column=0, padx=10, pady=10)
            self.label_smanage_birth = Label(self.frame_update, text='生日')
            self.label_smanage_birth.grid(row=3, column=0, padx=10, pady=10)
            self.label_smanage_tel = Label(self.frame_update, text='电话')
            self.label_smanage_tel.grid(row=4, column=0, padx=10, pady=10)
            self.label_smanage_pwd = Label(self.frame_update, text='密码')
            self.label_smanage_pwd.grid(row=5, column=0, padx=10, pady=10)

            # 按钮
            self.button_delete = Button(root_smanage, text='删除该学生', width=20, height=2, command=self.smanage_delete)
            self.button_delete.grid(row=9, column=0, padx=20, pady=20)
            self.button_score = Button(root_smanage, text='成绩更新', width=10, height=1, command=self.smanage_score)
            self.button_score.grid(row=9, column=3, padx=10, pady=10)
            self.button_smanage_insert = Button(root_smanage, text='插入学生', width=20, height=2,
                                                command=self.smanage_insert)
            self.button_smanage_insert.grid(row=5, column=6, padx=20, pady=20, rowspan=5)
            self.button_smanage_update = Button(self.frame_update, text="确定修改", width=10, height=1,
                                                command=self.smanage_update)
            self.button_smanage_update.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

            # 输入框
            self.varscore = StringVar
            self.var_smanage_no = StringVar
            self.var_smanage_name = StringVar
            self.var_smanage_sex = StringVar
            self.var_smanage_birth = StringVar
            self.var_smanage_tel = StringVar
            self.var_smanage_pwd = StringVar
            self.entry_score = Entry(root_smanage, textvariable=self.varscore)
            self.entry_score.grid(row=9, column=2, padx=15, pady=10)
            self.entry_smanage_no = Entry(self.frame_update, textvariable=self.var_smanage_no)
            self.entry_smanage_no.grid(row=0, column=1, padx=15, pady=10)
            self.entry_smanage_name = Entry(self.frame_update, textvariable=self.var_smanage_name)
            self.entry_smanage_name.grid(row=1, column=1, padx=15, pady=10)
            self.entry_smanage_sex = Entry(self.frame_update, textvariable=self.var_smanage_sex)
            self.entry_smanage_sex.grid(row=2, column=1, padx=15, pady=10)
            self.entry_smanage_birth = Entry(self.frame_update, textvariable=self.var_smanage_birth)
            self.entry_smanage_birth.grid(row=3, column=1, padx=15, pady=10)
            self.entry_smanage_tel = Entry(self.frame_update, textvariable=self.var_smanage_tel)
            self.entry_smanage_tel.grid(row=4, column=1, padx=15, pady=10)
            self.entry_smanage_pwd = Entry(self.frame_update, textvariable=self.var_smanage_no)
            self.entry_smanage_pwd.grid(row=5, column=1, padx=15, pady=10)

            # 单击---显示该生详细信息
            def treeview_click1(event):
                print('单击')
                item_text = []
                if self.treeview3.selection():
                    # 获取学生表展示信息值
                    for item in self.treeview3.selection():
                        item_text = self.treeview3.item(item, "values")
                        print(item_text[0])
                    # 绑定
                    self.temporary_sno = item_text[0]
                    self.temporary_sname = item_text[1]
                    self.temporary_sex = item_text[2]
                    self.temporary_birth = item_text[3]
                    self.temporary_tel = item_text[4]
                    self.temporary_pwd = item_text[5]
                    # 查询成绩
                    search_sql2 = "SELECT sc.tcid, c.cname, sc.score " \
                                  "FROM student_course sc " \
                                  "INNER JOIN course c ON sc.tcid = c.cno " \
                                  "WHERE sc.sno = %s"
                    self.cursor2.execute(search_sql2, (self.temporary_sno,))
                    self.row = self.cursor2.fetchone()  # 读取查询结果
                    self.del_button(self.treeview4)
                    while self.row:
                        self.treeview4.insert('', 0,
                                              values=(self.temporary_sno, self.row[0], self.row[1], self.row[2]))
                        self.row = self.cursor2.fetchone()

                    # 修改信息栏里显示信息
                    self.entry_smanage_no.delete(0, "end")
                    self.entry_smanage_no.insert(0, self.temporary_sno)
                    self.entry_smanage_name.delete(0, "end")
                    self.entry_smanage_name.insert(0, self.temporary_sname)
                    self.entry_smanage_sex.delete(0, "end")
                    self.entry_smanage_sex.insert(0, item_text[2])
                    self.entry_smanage_birth.delete(0, "end")
                    self.entry_smanage_birth.insert(0, item_text[3])
                    self.entry_smanage_tel.delete(0, "end")
                    self.entry_smanage_tel.insert(0, item_text[4])
                    self.entry_smanage_pwd.delete(0, "end")
                    self.entry_smanage_pwd.insert(0, item_text[5])
                    # 清空该科成绩框
                    self.entry_score.delete(0, "end")

            self.treeview3.bind('<ButtonRelease-1>', treeview_click1)  # 绑定单击离开事件

            # 单击---显示该科成绩
            def treeview_click2(event):
                print('单击')
                item_text = []
                if self.treeview4.selection():
                    for item in self.treeview4.selection():
                        item_text = self.treeview4.item(item, "values")
                        print(item_text[0])
                    self.temporary_cname = item_text[2]
                    self.temporary_cno = item_text[1]
                    self.entry_score.delete(0, "end")
                    self.entry_score.insert(0, item_text[3])

            self.treeview4.bind('<ButtonRelease-1>', treeview_click2)  # 绑定单击离开事件

            root_smanage.mainloop()

    def del_button(self, tree):
        x = tree.get_children()
        for item in x:
            tree.delete(item)

    # 删除学生信息，并删除相关的课程记录
    def smanage_delete(self):
        if self.temporary_sno != '':
            # 链接数据库
            self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
            try:
                if self.connect:
                    print('连接成功')
                    print(self.no)  # 用户名, 即学号

                    # 开始事务
                    self.connect.begin()

                    # 查询语句
                    delete_student_course_sql = "DELETE FROM student_course WHERE sno=%s"
                    delete_student_sql = "DELETE FROM student WHERE sno=%s"
                    delete_student_pwd_sql = "DELETE FROM student_pwd WHERE user=%s"

                    # 创建游标
                    self.cursor2 = self.connect.cursor()

                    # 先删除学生课程记录
                    self.cursor2.execute(delete_student_course_sql, (self.temporary_sno,))

                    # 再删除学生密码记录
                    self.cursor2.execute(delete_student_pwd_sql, (self.temporary_sno,))

                    # 最后删除学生记录
                    self.cursor2.execute(delete_student_sql, (self.temporary_sno,))

                    # 提交事务
                    self.connect.commit()
                    messagebox.showinfo(title='提示', message='删除成功!')

                    # 重置treeview3
                    self.del_button(self.treeview3)
                    search_sql = """
                    SELECT sno, sname, sex, birthday, tel, pwd 
                    FROM student 
                    INNER JOIN student_pwd ON student.sno = student_pwd.user
                    """
                    self.cursor2.execute(search_sql)
                    self.row = self.cursor2.fetchone()  # 读取查询结果
                    while self.row:
                        self.treeview3.insert('', 0, values=(
                            self.row[0], self.row[1], self.row[2], self.row[3], self.row[4], self.row[5]))
                        self.row = self.cursor2.fetchone()

            except pymysql.Error as e:
                # 出现异常时回滚
                self.connect.rollback()
                messagebox.showinfo(title='数据库错误', message=str(e))
            finally:
                self.cursor2.close()
                self.connect.close()
        else:
            messagebox.showinfo(title='提示', message='未选中, 请选中学生')

    def smanage_score(self):
        if self.entry_score.get() != '':
            # 连接数据库
            self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
            self.cursor2 = self.connect.cursor()  # 创建游标

            if self.connect:
                print('连接成功')
                print(self.no)
                sql_student_score = "UPDATE student_course SET score=%s WHERE sno=%s AND tcid=%s"
                self.cursor2.execute(sql_student_score,
                                     (self.entry_score.get(), self.temporary_sno, self.temporary_cno))
                self.connect.commit()
                messagebox.showinfo(title='提示', message='成绩更新成功!')

                # 重置treeview4
                self.refresh_student_course()

        else:
            messagebox.showinfo(title='提示', message='请勿更新空成绩!')

    def smanage_update(self):
        if self.entry_smanage_no.get() == self.temporary_sno:
            self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
            self.cursor2 = self.connect.cursor()  # 创建游标
            sql_up = "UPDATE student SET sname=%s, sex=%s, birthday=%s, tel=%s WHERE sno=%s"
            if self.connect:
                print('连接成功')
                print(self.no)
                self.cursor2.execute(sql_up, (self.entry_smanage_name.get(),
                                              self.entry_smanage_sex.get(),
                                              self.entry_smanage_birth.get(),
                                              self.entry_smanage_tel.get(),
                                              self.temporary_sno))
                self.connect.commit()
                sql_up2 = "UPDATE student_pwd SET pwd=%s WHERE user=%s"
                self.cursor2.execute(sql_up2, (self.entry_smanage_pwd.get(), self.temporary_sno))
                self.connect.commit()
                messagebox.showinfo(title='提示', message='课程信息修改成功!')

                # 修改treeview3中值
                sql_up3 = "SELECT sno, sname, sex, birthday, tel, pwd " \
                          "FROM student " \
                          "INNER JOIN student_pwd ON sno = user"
                self.del_button(self.treeview3)
                self.cursor2.execute(sql_up3)
                self.row = self.cursor2.fetchone()
                while self.row:
                    self.treeview3.insert('', 0,
                                          values=(self.row[0],
                                                  self.row[1],
                                                  self.row[2],
                                                  self.row[3],
                                                  self.row[4],
                                                  self.row[5]))
                    self.row = self.cursor2.fetchone()
        else:
            messagebox.showinfo(title='提示', message='请勿修改学号!')

    def smanage_insert(self):
        root_window = Toplevel(self.root)  # 初始框的声明
        root_window.geometry('300x250+100+100')
        root_window.title('添加学生')
        # 框框
        self.frame_smanage_insert = LabelFrame(root_window)
        self.frame_smanage_insert.grid(padx=30, pady=30)
        # Label
        self.label_smanage_insert_sno = Label(self.frame_smanage_insert, text='学号：')
        self.label_smanage_insert_sno.grid(row=0, column=0, padx=10, pady=10)
        self.label_smanage_insert_sname = Label(self.frame_smanage_insert, text='姓名：')
        self.label_smanage_insert_sname.grid(row=1, column=0, padx=10, pady=10)
        self.label_smanage_insert_pwd = Label(self.frame_smanage_insert, text='初始密码为学号!')
        self.label_smanage_insert_pwd.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        # 输入框
        self.var_smanage_insert_sno = StringVar
        self.var_smanage_insert_sname = StringVar
        self.entry_smanage_insert_sno = Entry(self.frame_smanage_insert, textvariable=self.var_smanage_insert_sno)
        self.entry_smanage_insert_sno.grid(row=0, column=1, padx=10, pady=10)
        self.entry_smanage_insert_sname = Entry(self.frame_smanage_insert, textvariable=self.var_smanage_insert_sname)
        self.entry_smanage_insert_sname.grid(row=1, column=1, padx=10, pady=10)
        # 按钮
        self.button_ok = Button(self.frame_smanage_insert, text='确定', command=self.smanage_insert_ok)
        self.button_ok.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def smanage_insert_ok(self):
        # 连接数据库
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        self.cursor2 = self.connect.cursor()
        sno = self.entry_smanage_insert_sno.get()
        sname = self.entry_smanage_insert_sname.get()

        # 使用参数化查询安全插入学生信息
        sql_insert1 = "INSERT INTO student (sno, sname) VALUES (%s, %s)"
        try:
            self.cursor2.execute(sql_insert1, (sno, sname))
            self.connect.commit()

            # 插入学生密码信息，初始密码设置为学号
            sql_insert2 = "INSERT INTO student_pwd (user, pwd) VALUES (%s, %s)"
            self.cursor2.execute(sql_insert2, (sno, sno))
            self.connect.commit()

            messagebox.showinfo(title='提示', message='插入成功!')

            # 重新创建游标
            self.cursor2.close()
            self.cursor2 = self.connect.cursor()

            # 修改treeview3中信息
            sql_insert3 = "SELECT sno, sname, sex, birthday, tel, pwd " \
                          "FROM student " \
                          "INNER JOIN student_pwd " \
                          "WHERE sno=user"
            self.del_button(self.treeview3)
            self.cursor2.execute(sql_insert3)
            self.row = self.cursor2.fetchone()
            while self.row:
                self.treeview3.insert('', 0,
                                      values=(self.row[0],
                                              self.row[1],
                                              self.row[2],
                                              self.row[3],
                                              self.row[4],
                                              self.row[5]))
                self.row = self.cursor2.fetchone()

        except pymysql.Error as e:
            # 检查错误消息是否包含触发器的错误消息
            if '学号长度必须为7位' in str(e):
                messagebox.showinfo(title='长度错误', message='学号长度必须为7位，请重试!')
            else:
                messagebox.showinfo(title='数据库错误', message=str(e))
        finally:
            self.cursor2.close()
            self.connect.close()

    def refresh_student_course(self):
        self.del_button(self.treeview4)
        search_sql2 = "SELECT sc.tcid, c.cname, sc.score " \
                      "FROM student_course sc " \
                      "INNER JOIN course c ON sc.tcid = c.cno " \
                      "WHERE sc.sno = %s"
        self.cursor2.execute(search_sql2, (self.temporary_sno,))
        self.row = self.cursor2.fetchone()  # 读取查询结果
        while self.row:
            self.treeview4.insert('', 0,
                                  values=(self.temporary_sno, self.row[0], self.row[1], self.row[2]))
            self.row = self.cursor2.fetchone()

    def del_button(self, tree):
        x = tree.get_children()
        for item in x:
            tree.delete(item)

