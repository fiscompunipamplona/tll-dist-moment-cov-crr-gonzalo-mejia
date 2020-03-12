from numpy import*
from math import*

class Datas:

	def __init__(self,datos):
		self.data=datos
		self.media=0
		self.varianza=0
		self.destandar=0
		self.kurtosis=0

	def md(self):
		self.med=sum(self.data)/len(self.data)
		return(self.med)

	def vr(self):
		l=(self.data-self.med)
		m=l*l
		self.var=sum(m)/(len(self.data)-1)
		return(self.var)

	def ds(self):
		self.des=sqrt(self.var)
		return(self.des)

	def sk(self):
		self.a=(self.data - self.data)/self.des
		self.b=list(map(lambda x:x**3, self.a))
		self.skw=sum(self.b)/len(self.data)
		return(self.skw)

	def kr(self):
		self.c=list(map(lambda x:x**4, self.a))
		self.kur=(sum(self.c)/len(self.data))-3
		return(self.kur)
