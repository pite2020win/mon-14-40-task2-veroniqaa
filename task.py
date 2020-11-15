from abc import ABC, abstractmethod
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

class Event:

	@abstractmethod
	def modify(self, plane):
		pass

class Turbulence(Event):

	def __init__(self, mu, sigma):
		self.mu = mu
		self.sigma = sigma

	def modify(self, plane):
		plane.yaw += random.gauss(self.mu, self.sigma)
		plane.roll += random.gauss(self.mu, self.sigma)
		plane.pitch += random.gauss(self.mu, self.sigma)

class Correction(Event):

	def __init__(self, rtc, mu, sigma):
		self.rate_of_correction = rtc
		self.mu = mu
		self.sigma = sigma

	def modify(self, plane):	
		plane.roll -= random.gauss(self.mu, self.sigma*self.rate_of_correction)
		plane.pitch -= random.gauss(self.mu, self.sigma*self.rate_of_correction)
		plane.yaw -= random.gauss(self.mu, self.sigma*self.rate_of_correction)

class Plane:
	def __init__ (self, roll, pitch, yaw):
		self.roll = roll
		self.pitch = pitch
		self.yaw = yaw

	def simulate_correction(self):
		cor = Correction(2, 1, 2)
		cor.modify(self)

	def take_values(self):
		values=[self.roll, self.pitch, self.yaw]
		return values
	
class Environment:
	def __init__ (self):
		self.planes=[]

	def add_plane(self, plane):
		self.planes.append(plane)

	def simulate_turbulance(self):
		turb = Turbulence(1,4)
		for p in self.planes:
			turb.modify(p)

if __name__ == '__main__':

	plane1 = Plane(0,0,0)
	env = Environment()
	env.add_plane(plane1)

	i = 1

	while (i<30):
		env.simulate_turbulance()
		val = plane1.take_values()	
		logging.info("roll = {}, pitch = {}, yaw = {} \n".format(val[0], val[1], val[2]))	
		
		plane1.simulate_correction()

		i+=1
