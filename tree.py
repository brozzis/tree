

class _tree():

	def update(self, ):
		print "update"
		pass

	def get(self, id):
		pass

class tree(_tree):

	def addChild(self):
		self.update()

	def getParentByID(self, id):
		return self.get(id)

if __name__ == '__main__':

	t = tree()
	t.addChild()