{"filter":false,"title":"student.py","tooltip":"/dbms/dbms_submissions/dbms_assignment_013/student.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":114,"column":11},"action":"insert","lines":["class DoesNotExist(Exception):","\tpass","","class MultipleObjectsReturned(Exception):","\tpass","","class InvalidField(Exception):","\tpass","","class Student:","\tdef __init__(self, name, age, score):","\t\tself.name = name","\t\tself.student_id = None","\t\tself.age = age","\t\tself.score = score","\t\t","\tdef __repr__(self):","\t\treturn \"Student(student_id={0}, name={1}, age={2}, score={3})\".format(self.student_id,self.name,self.age,self.score)","\t","\t@classmethod","\tdef get(cls,**kwargs): ","\t\t","\t\tfor key,value in kwargs.items():","\t\t\tcls.column = key","\t\t\tcls.value = value","\t","\t\tif cls.column not in ('student_id','name','age','score'):","\t\t\traise InvalidField('InvalidField')","\t\t\t","\t\tif cls.column == 'name':","\t\t\trecord = read_data(f\"select * from Student where {cls.column} = \\'{cls.value}\\'\")","\t\telse:","\t\t\trecord = read_data(f\"select * from Student where {cls.column} = {cls.value}\")","\t\t","\t\tif len(record)==0:","\t\t\traise DoesNotExist('DoesNotExist')","\t\telif len(record)>1:","\t\t\traise MultipleObjectsReturned('MultipleObjectsReturned')","\t","\t\toutput = Student(record[0][1],record[0][2],record[0][3])","\t\toutput.student_id = record[0][0]","\t\treturn output","\t","\t@staticmethod","\tdef filter(**args):","\t\tfinal_outcome = []","\t\tfor k,v in args.items():","\t\t\tinvalid_field=k.split('__')","\t\t\tif invalid_field[0] not in ('student_id','name','age','score'):","\t\t\t\traise InvalidField","\t\t\tif k in ('student_id','name','age','score'):","\t\t\t\trecords = read_data(f\"select * from Student where {k} = '{v}'\")","\t\t\telse:","\t\t\t\tvar = k.split('__')","\t\t\t\tif var[1] == 'lt':","\t\t\t\t\trecords = read_data(f\"select * from Student where {var[0]} < {v}\")","\t\t\t\telif var[1] == 'lte':","\t\t\t\t\trecords = read_data(f\"select * from Student where {var[0]} <= {v}\")","\t\t\t\telif var[1] == 'gt':","\t\t\t\t\trecords = read_data(f\"select * from Student where {var[0]} > {v}\")","\t\t\t\telif var[1] == 'gte':","\t\t\t\t\trecords = read_data(f\"select * from Student where {var[0]} >= {v}\")","\t\t\t\telif var[1] == 'neq':","\t\t\t\t\trecords = read_data(f\"select * from Student where {var[0]} <> '{v}'\")","\t\t\t\telif var[1] == 'in':","\t\t\t\t\tin_condition = tuple(v)","\t\t\t\t\trecords = read_data(f\"select * from Student where {var[0]} in {in_condition}\")","\t\t\t\telif var[1] == 'contains':","\t\t\t\t\trecords = read_data(f\"select * from Student where {var[0]} LIKE '%{v}%'\")","\t\t\t","\t\t\tfor i in range(len(records)):","\t\t\t\toutput = Student(records[i][1],records[i][2],records[i][3])","\t\t\t\toutput.student_id = records[i][0]","\t\t\t\tfinal_outcome.append(output)","","\t\treturn final_outcome","\t\t\t","\tdef save(self):","\t\timport sqlite3","\t\tconnection = sqlite3.connect(\"selected_students.sqlite3\")","\t\tcrsr = connection.cursor() ","\t\tcrsr.execute(\"PRAGMA foreign_keys=on;\") ","\t\tif self.student_id == None:","\t\t\tcrsr.execute(f\"insert into Student (name,age,score) values (\\'{self.name}\\',{self.age},{self.score})\")        ","\t\t\tself.student_id = crsr.lastrowid","\t\telse:","\t\t\tdata = read_data(f\"select * from  Student Where student_id={self.student_id}\")","\t\t\tif len(data) != 0:","\t\t\t\tcrsr.execute(f\"update Student SET name=\\'{self.name}\\',age={self.age},score={self.score}\")","\t\t\telse:","\t\t\t\tcrsr.execute(f\"insert into Student (student_id,name,age,score) values ({self.student_id},\\'{self.name}\\',{self.age},{self.score})\")","\t\tconnection.commit() ","\t\tconnection.close()","","\tdef delete(self):","\t\twrite_data(f\"delete from student where student_id={self.student_id}\")","\t\t","\t","def write_data(sql_query):","\timport sqlite3","\tconnection = sqlite3.connect(\"selected_students.sqlite3\")","\tcrsr = connection.cursor() ","\tcrsr.execute(\"PRAGMA foreign_keys=on;\") ","\tcrsr.execute(sql_query) ","\tconnection.commit() ","\tconnection.close()","","def read_data(sql_query):","\timport sqlite3","\tconnection = sqlite3.connect(\"selected_students.sqlite3\")","\tcrsr = connection.cursor()","\tcrsr.execute(sql_query) ","\tans= crsr.fetchall()  ","\tconnection.close() ","\treturn ans"],"id":1,"ignore":true}]]},"ace":{"folds":[],"scrolltop":1739.5,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":95,"state":"start","mode":"ace/mode/python"}},"timestamp":1590403811574,"hash":"ece8255ebef231f11256d25d49a142d027e7f059"}