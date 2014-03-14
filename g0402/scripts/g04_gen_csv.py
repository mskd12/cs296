import subprocess
import random
#print("Status:", sp.wait())

iterations, reruns, samples = 50, 30, 15
csvfile = open("../data/g04_lab09data.csv", 'w')
rand_csvfile = open("../data/g04_lab09data_random.csv", 'w')

for it in range(1, iterations + 1, 1):
	random_array = random.sample(range(1, reruns + 1, 1), samples)
	random_array.sort()
	curr_sample = 0
	for re in range(1, reruns + 1, 1):
		sp = subprocess.Popen(['../mybins/cs296_04_exe', str(it)], stdout=subprocess.PIPE)
		[output, _ ] = sp.communicate()
		output_words = output.decode("utf-8").split()
		steptime = output_words[10]
		coll_time = output_words[17]
		vel_time = output_words[25]
		pos_time = output_words[33]
		loop_time = output_words[39]
		csvfile.write(str(it) + "," + str(re) + "," + steptime + "," + coll_time + "," + vel_time + "," + pos_time + "," + loop_time + "\n")
		if (curr_sample < samples) and (re == random_array[curr_sample]):
			rand_csvfile.write(str(it) + "," + str(re) + "," + steptime + "," + coll_time + "," + vel_time + "," + pos_time + "," + loop_time + "\n")
			curr_sample = 1 + curr_sample

csvfile.close()
rand_csvfile.close()
