#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

class _db():

	def __init__(self):
		self.connection = MySQLdb.connect(user='root')
		self.c = connection.cursor()


	def sqlExec(self, sql):
		self.c.execute(sql)
		# connection.insert_id()
		return self.c.lastrowid 

	def sqlGet(self, sql):
		self.c.execute(sql)
		return self.c.fetchone()

	def sqlGetAll(self, sql):
		self.c.execute(sql)
		return self.c.fetchall()


class _tree(_db):

	def __init__(self):
		pass

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
		self.insert(pid, label)

	def getParentByID(self, id):
		return self.get(id)


if __name__ == '__main__':

	t = tree()
	root = t.insertRoot("stefano")
	x = t.addChild(root, "python")
	t.addChild(x, "kivy")
	t.addChild(root, "openshift")
	t.addChild(root, "kubernetes")

