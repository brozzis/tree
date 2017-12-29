#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

class _db():

	connection = None
	c = None

	def __init__(self, host="localhost", user="ste", passwd="ste",db="tree", charset="utf8"):

		self.connection = MySQLdb.connect(host, user, passwd, db)
		self.connection.autocommit = True
		self.c = self.connection.cursor()


	def sqlExec(self, sql):
		print sql
		self.c.execute(sql)
		# connection.insert_id()
		lid = self.c.lastrowid
		self.commit()
		print lid
		return lid

	def sqlGet(self, sql):
		self.c.execute(sql)
		return self.c.fetchone()

	def sqlGetAll(self, sql):
		self.c.execute(sql)
		return self.c.fetchall()

	def commit(self):
		self.connection.commit()

	def close(self):
		self.c.close()


class _tree(_db):

	def __init__(self):
		# super(_tree, self).__init__() # python3
		_db.__init__(self)


	def insertRoot(self, label):
		sql = "insert into forest (pid, label) values (0, '{}')".format(label)
		return self.sqlExec(sql)

	def insert(self, pid, label):
		sql = "insert into forest (pid, label) values ({},'{}')".format(pid,label)
		return self.sqlExec(sql)

	def update(self, ):
		sql = "update"
		self.sqlExec(sql)

	def get(self, id):
		sql = "select * from forest where id={}".format(id)
		self.sqlExec(sql)


class tree(_tree):

	def addChild(self, pid, label):
		return self.insert(pid, label)

	def getParentByID(self, id):
		return self.get(id)


if __name__ == '__main__':

	t = tree()
	root = t.insertRoot("stefano")
	x = t.addChild(root, "python")
	t.addChild(x, "kivy")
	t.addChild(root, "openshift")
	t.addChild(root, "kubernetes")

