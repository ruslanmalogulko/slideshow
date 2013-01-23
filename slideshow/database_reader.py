#!/usr/bin/python
import MySQLdb, time, random


host = "localhost"
user = "root"
passwd = "1"
database = "url"
db = MySQLdb.connect(host='localhost', passwd='1', user='root', db='url')
rnd = 1
k = []

urlset = []
def read_from_database(sql, db, rnd):
 # creating cursor
	cursor = db.cursor()
	cursor.execute(sql)
	results = cursor.fetchall()
	for i in results:
		b = i[0]
		print b
	return b;

def write_to_file(filename, urlset):
	f = open(filename, 'w')
	for i in urlset:
		print >> f, i
	f.close()

while (rnd<10):
	sql = "SELECT URL FROM urls where id = " + str(rnd)
	if (len(urlset)<=1):
		i = 1
	else:
		i = random.randint(1, len(urlset))
	k = read_from_database(sql, db, rnd)
	if (len(urlset)< 10):
		urlset.append(k)
	else: 
		urlset[i-1] = k 
	write_to_file('/home/russel/tmp/sourse_file.txt', urlset)
	rnd += 1
	time.sleep (5)

