import subprocess
import numpy as np
import matplotlib.pyplot as plt
from pylab import * 
from matplotlib.patches import Circle

sp = subprocess.Popen(['ls', './'], stdout=subprocess.PIPE)
[output, _ ] = sp.communicate()
ls_output = output.decode("utf-8").split()
if 'plots' not in ls_output:
        subprocess.call('mkdir ./plots/', shell=True)

f = open('./data/g04_lab09data.csv','r')
g = open('./data/g04_lab09data_random.csv','r')
h = open('./data/g04_lab09data.csv','r')

iteration_no = 10
rerun_no = 10
random_no = 5
iteration_value = 6

steptime=list()
collisiontime=list()
velocitytime=list()
positiontime=list()
looptime=list()
steptime_error=list()

for i in range(iteration_no):
	count_steptime = 0
	count_collisiontime = 0
	count_velocitytime = 0
	count_positiontime = 0
	count_looptime = 0
	max_steptime = 0
	min_steptime = 100
	for j in range(rerun_no):
		var=f.readline()
		var1 = var[:-1].split(',')
		count_steptime += float(var1[2])
		count_collisiontime += float(var1[3])
		count_velocitytime += float(var1[4])
		count_positiontime += float(var1[5])
		count_looptime += float(var1[-1])
		step = float(var1[2])
		if (step > max_steptime):
			max_steptime = step
		if (step < min_steptime):
			min_steptime = step
		if (j == rerun_no-1):
			steptime.append(count_steptime/rerun_no)
			collisiontime.append(count_collisiontime/rerun_no)
			velocitytime.append(count_velocitytime/rerun_no)
			positiontime.append(count_positiontime/rerun_no)
			looptime.append(count_looptime/rerun_no)
			steptime_error.append(max_steptime-min_steptime)
############################

x = np.arange(1, iteration_no+1, 1)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(x, steptime, 0.5, align='center', color='r', label='Steptime')
ax2.plot(x, looptime, color='b', label='Looptime')
ax1.legend(loc=0)
ax2.legend(loc=0)
ax1.set_xlabel('Iterations')
ax2.set_ylabel('Loop time')
ax1.set_ylabel('Step time')
ax1.set_title('Step time and Loop time averaged over reruns (vs) Iteration numbers ')

max_value = max(looptime)
max_index = looptime.index(max_value)
min_value = min(looptime)
min_index = looptime.index(min_value)

max_iter = max_index
min_iter = min_index
caxis = plt.gca()
caxis.add_patch(Circle((max_iter+1, max_value), 0.2 , facecolor="grey", label="Max"))
caxis.add_patch(Circle((min_iter+1, min_value), 0.2 , facecolor="yellow", label="Min"))

caxis.legend(loc=0)
#extendfrac[None]
plt.savefig('./plots/g04_lab09_plot01.png')

#######################################

plt.clf()
temp_list = [x + y + z for x, y, z in zip(positiontime, collisiontime, velocitytime)]
fig, ax = plt.subplots()
ax.plot(x, steptime, label='Steptime')
ax.plot(x, collisiontime, label='Collision time')
ax.plot(x, velocitytime, label='Velocity updates time')
ax.plot(x, positiontime, label='Position updates time')
ax.plot(x, temp_list, label='sum of Velocity, collision and position times')
ax.set_title('plot-02')
ax.set_xlabel('Iterations')
ax.set_ylabel('Time')
ax.legend()
plt.savefig('./plots/g04_lab09_plot02.png')

#######################################

plt.clf()
fig, ax = plt.subplots()
rects1 = ax.plot(x, steptime, label='Steptime')
ax.errorbar(x, steptime, yerr = steptime_error, fmt='o', label='error bars')
ax.set_xlabel('Iterations')
ax.set_title('Steptime with error bars (vs) Iteration numbers')
ax.set_ylabel('Steptime')
ax.legend()
plt.savefig('./plots/g04_lab09_plot03.png')

########################################

plt.clf()
steptime_02 = list()
steptime_random = list()

for i in range(iteration_no):
	count_steptime = 0
	count_steptime_random = 0
	for j in range(rerun_no):
		var=h.readline()
		var1 = var[:-1].split(',')
		count_steptime += float(var1[2])
		step = float(var1[2])
		if (j == rerun_no-1):
			steptime_02.append(count_steptime/rerun_no)
	for j in range(random_no):
		var = g.readline()
		var1 = var[:-1].split(',')
		count_steptime_random += float(var1[2])
		if (j == random_no-1):
			steptime_random.append(count_steptime_random/random_no)

l1 = polyfit(x, steptime_02, 1)
l2 = polyfit(x, steptime_random, 1)

fn1 = poly1d(l1)
fn2 = poly1d(l2)

fig, ax = plt.subplots()
ax.plot(x, steptime_02, 'b.', label="Average step time")
ax.plot(x, fn1(x), 'b-', label='Best fit line')

ax.plot(x, steptime_random, 'r.', label="Average step time(random)")
ax.plot(x, fn2(x), 'r-', label='Best fit line for random data')

ax.set_title('plot-05')
ax.set_xlabel('Iteration number')
ax.set_ylabel('Step time')


ax.legend()

plt.savefig('./plots/g04_lab09_plot05.png')

###################################################
h.seek(0)
plt.clf()


steptime_roll = list()
start = (iteration_value-1) * rerun_no
for i in range(iteration_no):
	for j in range(rerun_no):
		if(i != iteration_value-1):
			h.readline()
		else:
			var = h.readline()
			var1 = var[:-1].split(',')
			steptime_roll.append(float(var1[2]))


fig, ax = plt.subplots()
var1 ,var2, var3 = ax.hist(steptime_roll,bins = 10, color='b', label="Frequency")
ax.hist(steptime_roll,bins = 10, histtype='step', color='r', label="cum frequency", cumulative=True)
ax.set_ylabel('count')
ax.set_xlabel('step time')
ax.set_title('plot-04')
ax.legend()
plt.yticks(np.arange(0, sum(var1)))
plt.savefig('./plots/g04_lab09_plot04.png')

f.close()
g.close()
h.close()
