import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class CourseManagement:
    def __init__(self, root, ip, port, user, passwd, db, no):
        self.root = root
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.no = no
        self.temporary_cno = ''

    def cmanage(self):
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        if self.connect:
            print('连接成功')
            print(self.no)  # 用户名, 即学号
            # 查询语句
            search_sql1 = "SELECT cno, cname, credit FROM course"
            # 创建游标
            self.cursor2 = self.connect.cursor()

            # 初始框的声明
            root_cmanage = Toplevel(self.root)
            root_cmanage.geometry("500x500+100+100")
            root_cmanage.title("课程管理系统")

            # 学生管理表格框
            columns = ("课程号", "名称", "学分")
            self.treeview5 = ttk.Treeview(root_cmanage, height=18, show="headings", columns=columns)
            self.treeview5.column("课程号", width=80, anchor='center')  # 表示列,不显示
            self.treeview5.column("名称", width=70, anchor='center')
            self.treeview5.column("学分", width=50, anchor='center')
            self.treeview5.heading("课程号", text="课程号")  # 显示表头
            self.treeview5.heading("名称", text="名称")
            self.treeview5.heading("学分", text="学分")

            self.treeview5.grid(row=1, column=0, rowspan=3, padx=10, pady=3)
            # 插入查询结果
            self.cursor2.execute(search_sql1)
            self.row = self.cursor2.fetchone()  # 读取查询结果
            while self.row:
                self.treeview5.insert('', 0, values=(self.row[0], self.row[1], self.row[2]))
                self.row = self.cursor2.fetchone()

            # 框框
            self.frame_cmanage = LabelFrame(root_cmanage, text='修改课程', font=('微软雅黑', 16))
            self.frame_cmanage.grid(row=1, column=1, padx=10, pady=10)

            # 标签
            self.label_cmanage1 = Label(root_cmanage, text='课程表')
            self.label_cmanage1.grid(row=0, column=0, padx=10, pady=10)
            self.label_cmanage_cno = Label(self.frame_cmanage, text='课程号:')
            self.label_cmanage_cno.grid(row=0, column=0, padx=10, pady=10)
            self.label_cmanage_cname = Label(self.frame_cmanage, text='课程名:')
            self.label_cmanage_cname.grid(row=1, column=0, padx=10, pady=10)
            self.label_cmanage_credit = Label(self.frame_cmanage, text='学分:')
            self.label_cmanage_credit.grid(row=2, column=0, padx=10, pady=10)

            # 按钮
            self.button_cmanage1 = Button(root_cmanage, text='选中课程删除', width=10, height=1, command=self.cmanage_delete)
            self.button_cmanage1.grid(row=4, column=0, padx=20, pady=20)
            self.button_cmanage_update = Button(self.frame_cmanage, text='确定修改', width=10, height=1,
                                                command=self.cmanage_update)
            self.button_cmanage_update.grid(row=4, column=0, padx=20, pady=20, columnspan=2)
            self.button_cmanage_insert = Button(root_cmanage, text='添加课程', width=20, height=2,
                                                command=self.cmanage_insert)
            self.button_cmanage_insert.grid(row=2, column=1, padx=10, pady=10)

            # 输入框
            self.var_cno = StringVar
            self.var_cname = StringVar
            self.var_credit = StringVar
            self.entry_cno = Entry(self.frame_cmanage, textvariable=self.var_cno)
            self.entry_cno.grid(row=0, column=1, padx=10, pady=10)
            self.entry_cname = Entry(self.frame_cmanage, textvariable=self.var_cname)
            self.entry_cname.grid(row=1, column=1, padx=10, pady=10)
            self.entry_credit = Entry(self.frame_cmanage, textvariable=self.var_credit)
            self.entry_credit.grid(row=2, column=1, padx=10, pady=10)

            def treeview_click1(event):
                print('单击')
                item_text = []
                if self.treeview5.selection():
                    # 获取课程表展示信息值
                    for item in self.treeview5.selection():
                        item_text = self.treeview5.item(item, "values")
                        print(item_text[0])
                    self.temporary_cno = item_text[0]
                    # 修改信息栏里显示信息
                    self.entry_cno.delete(0, "end")
                    self.entry_cno.insert(0, item_text[0])
                    self.entry_cname.delete(0, "end")
                    self.entry_cname.insert(0, item_text[1])
                    self.entry_credit.delete(0, "end")
                    self.entry_credit.insert(0, item_text[2])

            self.treeview5.bind('<ButtonRelease-1>', treeview_click1)  # 绑定单击离开事件

            root_cmanage.mainloop()

    def cmanage_delete(self):
        # 检查是否选中课程
        if self.temporary_cno != '':
            # 链接数据库
            self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
            try:
                if self.connect:
                    print('连接成功')
                    print(self.no)  # 用户名, 即工号

                    # 开始事务
                    self.connect.begin()

                    # 删除语句
                    delete_course_sql = "DELETE FROM course WHERE cno=%s"
                    delete_student_course_sql = "DELETE FROM student_course WHERE tcid=%s"

                    # 创建游标
                    self.cursor2 = self.connect.cursor()

                    # 输出调试信息，检查临时课程号是否正确
                    print(f"Deleting course with cno={self.temporary_cno}")

                    # 执行删除操作
                    self.cursor2.execute(delete_course_sql, (self.temporary_cno,))
                    self.cursor2.execute(delete_student_course_sql, (self.temporary_cno,))

                    # 提交事务
                    self.connect.commit()
                    messagebox.showinfo(title='提示', message='删除成功!')

                    # 重置课程列表视图
                    self.refresh_course_list()

            except pymysql.Error as e:
                # 出现异常时回滚
                self.connect.rollback()
                messagebox.showinfo(title='数据库错误', message=str(e))
            finally:
                self.cursor2.close()
                self.connect.close()
        else:
            messagebox.showinfo(title='提示', message='未选中课程，请选中课程')

    def refresh_course_list(self):
        # 重置treeview5
        self.del_button(self.treeview5)
        search_sql1 = "SELECT cno, cname, credit FROM course"
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        self.cursor2 = self.connect.cursor()
        self.cursor2.execute(search_sql1)
        self.row = self.cursor2.fetchone()  # 读取查询结果
        while self.row:
            self.treeview5.insert('', 0, values=(self.row[0], self.row[1], self.row[2]))
            self.row = self.cursor2.fetchone()
        self.cursor2.close()
        self.connect.close()

    def cmanage_update(self):
        if self.entry_cno.get() == self.temporary_cno:
            self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
            self.cursor2 = self.connect.cursor()  # 创建游标
            sql_call_proc = "CALL update_course_and_student_course(%s, %s)"

            try:
                if self.connect:
                    print('连接成功')
                    print(self.no)

                    # 开始事务
                    self.connect.begin()

                    # 调用存储过程更新课程信息和学生课程信息
                    self.cursor2.execute(sql_call_proc, (self.temporary_cno, self.entry_cname.get()))

                    # 提交事务
                    self.connect.commit()
                    messagebox.showinfo(title='提示', message='信息修改成功!')

                    # 修改treeview5中值
                    sql_up3 = "SELECT cno, cname, credit FROM course"
                    self.del_button(self.treeview5)
                    # 插入查询结果
                    self.cursor2.execute(sql_up3)
                    self.row = self.cursor2.fetchone()  # 读取查询结果
                    while self.row:
                        self.treeview5.insert('', 0, values=(self.row[0], self.row[1], self.row[2]))
                        self.row = self.cursor2.fetchone()

            except pymysql.Error as e:
                # 出现异常时回滚
                self.connect.rollback()
                messagebox.showinfo(title='数据库错误', message=str(e))
            finally:
                self.cursor2.close()
                self.connect.close()
        else:
            messagebox.showinfo(title='提示', message='请勿修改课程号!')

    def cmanage_insert(self):
        root_window = Toplevel(self.root)  # 初始框的声明
        root_window.geometry('300x250+100+100')
        root_window.title('添加课程')
        # 框框
        self.frame_cmanage_insert = LabelFrame(root_window)
        self.frame_cmanage_insert.grid(padx=30, pady=30)
        # Label
        self.label_cmanage_insert_cno = Label(self.frame_cmanage_insert, text='课程号：')
        self.label_cmanage_insert_cno.grid(row=0, column=0, padx=10, pady=10)
        self.label_cmanage_insert_cname = Label(self.frame_cmanage_insert, text='课程名：')
        self.label_cmanage_insert_cname.grid(row=1, column=0, padx=10, pady=10)
        self.label_cmanage_insert_credit = Label(self.frame_cmanage_insert, text='学分:')
        self.label_cmanage_insert_credit.grid(row=2, column=0, padx=10, pady=10)
        # 输入框
        self.var_cmanage_insert_cno = StringVar
        self.var_cmanage_insert_cname = StringVar
        self.var_cmanage_insert_credit = StringVar
        self.entry_cmanage_insert_cno = Entry(self.frame_cmanage_insert, textvariable=self.var_cmanage_insert_cno)
        self.entry_cmanage_insert_cno.grid(row=0, column=1, padx=10, pady=10)
        self.entry_cmanage_insert_cname = Entry(self.frame_cmanage_insert, textvariable=self.var_cmanage_insert_cname)
        self.entry_cmanage_insert_cname.grid(row=1, column=1, padx=10, pady=10)
        self.entry_cmanage_insert_credit = Entry(self.frame_cmanage_insert, textvariable=self.var_cmanage_insert_credit)
        self.entry_cmanage_insert_credit.grid(row=2, column=1, padx=10, pady=10)
        # 按钮
        self.button_ok = Button(self.frame_cmanage_insert, text='确定', command=self.cmanage_insert_ok)
        self.button_ok.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def cmanage_insert_ok(self):
        # 连接数据库
        self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        self.cursor2 = self.connect.cursor()  # 创建游标
        cno = self.entry_cmanage_insert_cno.get()
        cname = self.entry_cmanage_insert_cname.get()
        credit = self.entry_cmanage_insert_credit.get()
        sql_insert1 = "INSERT INTO course (cno, cname, credit) VALUES (%s, %s, %s)"
        try:
            self.cursor2.execute(sql_insert1, (cno, cname, credit))
            self.connect.commit()
            messagebox.showinfo(title='提示', message='插入成功!')
        except pymysql.Error as e:
            messagebox.showinfo(title='数据库错误', message=str(e))

            # 修改treeview5中值
            sql_up3 = "SELECT cno, cname, credit FROM course"
            self.del_button(self.treeview5)
            # 插入查询结果
            self.cursor2.execute(sql_up3)
            self.row = self.cursor2.fetchone()  # 读取查询结果
            while self.row:
                self.treeview5.insert('', 0, values=(self.row[0], self.row[1], self.row[2]))
                self.row = self.cursor2.fetchone()

    def del_button(self, tree):
        x = tree.get_children()
        for item in x:
            tree.delete(item)
