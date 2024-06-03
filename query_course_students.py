import pymysql
from tkinter import *
from tkinter import ttk

class QueryCourseStudents:
    def __init__(self, root):
        self.root = root
        self.ip = 'localhost'
        self.port = 3306
        self.id = 'root'
        self.pd = 'Xyn20040516!'
        self.db = 'school_db'

    def query_course_students(self):
        def fetch_course_students():
            course_no = entry_course_no.get()

            # 连接数据库
            self.connect = pymysql.connect(host=self.ip, port=self.port, user=self.id, passwd=self.pd, db=self.db)
            if self.connect:
                print('连接成功')

                # 查询语句
                search_sql = "SELECT * FROM course_student_view WHERE cno = %s"

                # 创建游标
                self.cursor2 = self.connect.cursor()
                self.cursor2.execute(search_sql, (course_no,))
                self.row = self.cursor2.fetchone()  # 读取查询结果

                # 清空 treeview
                for item in self.treeview.get_children():
                    self.treeview.delete(item)

                # 插入查询结果
                while self.row:
                    self.treeview.insert('', 0,
                                         values=(self.row[0], self.row[1], self.row[2], self.row[3], self.row[4]))
                    self.row = self.cursor2.fetchone()

                self.cursor2.close()
                self.connect.close()

        # 创建查询窗口
        query_window = Tk()
        query_window.geometry('600x400+100+100')
        query_window.title('课程学生查询')

        # 输入框和按钮
        label_course_no = Label(query_window, text='课程号:', font=('黑体', 12))
        label_course_no.grid(row=0, column=0, padx=10, pady=10)
        entry_course_no = Entry(query_window)
        entry_course_no.grid(row=0, column=1, padx=10, pady=10)
        button_fetch = Button(query_window, text='查询', command=fetch_course_students)
        button_fetch.grid(row=0, column=2, padx=10, pady=10)

        # 表格框
        columns = ("课程号", "课程名", "学生号", "学生名", "成绩")
        self.treeview = ttk.Treeview(query_window, height=18, show="headings", columns=columns)
        self.treeview.column("课程号", width=100, anchor='center')
        self.treeview.column("课程名", width=150, anchor='center')
        self.treeview.column("学生号", width=100, anchor='center')
        self.treeview.column("学生名", width=150, anchor='center')
        self.treeview.column("成绩", width=100, anchor='center')

        self.treeview.heading("课程号", text="课程号")
        self.treeview.heading("课程名", text="课程名")
        self.treeview.heading("学生号", text="学生号")
        self.treeview.heading("学生名", text="学生名")
        self.treeview.heading("成绩", text="成绩")
        self.treeview.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        query_window.mainloop()
