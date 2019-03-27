#Based on what Kuba said about lab instructions, took me 35 minutes.
import matplotlib.pyplot as plt
import random
import math
import time

class driver:
	pos_x=0
	vertical_angle=0
	distance_to_obstacle=0

	def get_parameters(self):
		print("Turning angle: " + str(self.vertical_angle)+ " Car position: " + str(self.pos_x) )
		print("Next obstacle: " + str(self.distance_to_obstacle)+ "m")
	def steering_step(self):
		if self.distance_to_obstacle == 0:
			self.distance_to_obstacle=round(random.uniform(0,100) +1)
		if self.distance_to_obstacle > 40:
			self.vertical_angle=math.atan(self.pos_x/10)
		else:
			self.vertical_angle=math.atan((1+self.pos_x)/self.distance_to_obstacle)
		self.distance_to_obstacle = self.distance_to_obstacle-1
		self.pos_x=self.pos_x - math.sin(self.vertical_angle)

No1 = driver()
plt.figure()
while 1:
				
	No1.steering_step()
	No1.get_parameters()
	plt.plot([0.5,0.5],[0,100])
	plt.plot([-1.5,-1.5],[0,100])
	plt.plot([-0.5,-0.5],[0,100],'-.')
	plt.plot([-0.5,0.5],[No1.distance_to_obstacle,No1.distance_to_obstacle], color='black')
	plt.plot(No1.pos_x,10,'r*')
	plt.savefig('test.png')
	plt.clf()
time.sleep(0.2)
    
