import pymysql
db=pymysql.connect(host='localhost',user='root',passwd='root',db='database1')

#prepare cursor object using cursor() method
cur1=db.cursor()
# sql='create table stud(id int,name varchar(10))'
# sql="insert into stud values(101,'anu')"
# sql="insert into stud values(102,'abi')"
# sql="update stud set name='sravan' where id=101"
# sql="select * from stud"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print("Id  Name")
# for i in rows:
#     print(i[0],i[1])
# sql="select * from stud"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print("Name")
# for i in rows:
#     print(i[1])
# db.commit()                                   #the python codes changes reflect on mysql
sql="select * from stud"
cur1.execute(sql)
rows=cur1.fetchone()
print("Id  Name")
if rows:
    print(rows[0],rows[1])



