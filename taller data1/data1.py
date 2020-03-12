from numpy import*
from math import*

class Datas1:

	def __init__(self,datos):
		self.data=datos
		self.media=0	
		self.covarianza=0
		self.correlacion=0

	def md(self):
		self.med=sum(self.data)/len(self.data)
		return(self.med)

	def cv(self):
		self.x1=self.data[:,0]
		self.y1=self.data[:,1]
		self.x1y1=self.x1 * self.y1
		self.cov=(sum(self.x1y1)/len(self.x1y1)) - (sum(self.x1)/len(self.x1)) * (sum(self.y1)/len(self.y1))
		return(self.cov)

	def cr(self):
		self.x2=sum(self.x1)/len(self.x1)
		self.y2=sum(self.y1)/len(self.y1)
		self.xx=sum((self.x1 - self.x2)*(self.x1 - self.x2))/(len(self.x1) -1 )
		self.yy=sum((self.y1 - self.y2)*(self.y1 - self.y2))/(len(self.y1) -1 )
		self.cor=self.cov/(sqrt(self.xx)*sqrt(self.yy))
		return(self.cor)
