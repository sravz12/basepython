import pymysql
db=pymysql.connect(host='localhost',user='root',passwd='root',db='database1')
cur1=db.cursor()
# sql="create table New(Adno int,Name varchar(15),Average int,Sex char(5),Scode int)"
# sql="insert into New values(501,'R jain',98,'M',111)"
# # sql="insert into New values(545,'kavita',73,'F',333)"
# sql="insert into New values(705,'K.rashika',85,'F',111)"
# sql="insert into New values(754,'Rahul Geol',60,'M',444)"
# sql="insert into New values(892,'Sahil jain',78,'M',333)"
# sql="insert into New values(935,'Rohan saini',85,'M',222)"
# sql="insert into New values(955,'Anjali',64,'F',222)"

#1). display all information

# sql="select * from new"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print("Adno Name Average Sex Scode")
# for i in rows:
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

#2). display rohan saini's information
# sql="select * from new where Adno=935"
# cur1.execute(sql)
# rows=cur1.fetchall()
# for i in rows:
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

#3). display number of students in the table

# sql="select count(*) from new"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print("count")
# for i in rows:
#     print(i[0])
# db.commit()

#4). display number of students in each sex

# sql="select sex,count(*) from new group by sex"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print("count of students")
# for i in rows:
#     print(i[0],i[1])
# db.commit()

#5). display new information in ascending order by name

# sql="select * from new order by name asc"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print("Adno Name Avg Sex Scode")
# for i in rows:
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

#6) display information in descending order using avg marks

# sql="select * from new order by average desc"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print("Adno name avg sex scode")
# for i in rows:
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

#7). display name starting with 'k'

