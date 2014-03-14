import re
import subprocess

tex_file = open("./doc/g04_prof_report.tex", "r")

subsections = 0
include = False
plot_analysis = ""
for line in tex_file:
	if include:
		print(line)	
		if re.search(r'\\', line) and "indent" not in line and "subsection" not in line :
			continue
		elif "indent" in line:
			plot_analysis = plot_analysis + line[7:]
			print(1)
		else:
			plot_analysis = plot_analysis + line
			print(1)
	
	if re.match(r'^\\subsection', line.lower()):
		print(1)
		subsections = subsections + 1
		if "analysis of the data" in line.lower():
			plot_analysis = plot_analysis + line
			include = True
		elif include and subsections > 2:
			break

tex_file.close()
plot_analysis = plot_analysis.split("\n")
print(plot_analysis)
p = re.compile(r'\\cite{[a-zA-Z0-9]*}')
for i in range(len(plot_analysis)):
	plot_analysis[i] = p.sub("", plot_analysis[i])

headers = "<!DOCTYPE html>\n<html style=\"height:100%\">\n\t<head>\n\t\t<link rel=\"stylesheet\" type=\"text/css\" href=\"./index.css\">\n\t\t<title>\n\t\t\tAnalysis of Box2D Simulation Data\n\t\t</title>\n\t</head>\n\n\t<body class=\"body\" style=\"background-image:url('./images/grey_wash_wall.png')\">\n\n\t\t<center>\n\t\t\t<div>\n\t\t\t\t<h1>\n\t\t\t\t\tAnalysis of Box2D Simulation Data\n\t\t\t\t</h1>\n\t\t\t\t<h3 style=\"margin-left:20%;margin-top:-1.5%\">\n\t\t\t\t\tPratik Fegade (120050004)\n\t\t\t\t\t<br>\n\t\t\t\t\tM. S. Krishna Deepak (120050057)\n\t\t\t\t\t<br>\n\t\t\t\t\tP. Bharath Kumar (120050058)\n\t\t\t\t\t<br>\n\t\t\t\t</h3>\n\t\t\t</div>\n\t\t</center>\n\t\t<hr>\n"

html_file = open("./doc/g04_lab09_report.html", 'w')
html_file.write(headers)
body = "\t\t<div name=\"homeContent\" style=\"margin-left:1%\">\n"
html_file.write(body)

file_text = ""
for line in plot_analysis[:len(plot_analysis) - 2]:
		if not line.isspace():
			if re.match(r'\\subsection', line):
				title = line[line.find("{") + 1:line.find("}")]
				file_text += "\t\t\t<h2 style=\"margin-left:-1%\">\n\t\t\t\t" + title + "\n" + "\t\t\t</h2>\n"
			else:
				file_text += "\t\t\t<p style=\"font-size:14pt\">\n" + "\t\t\t\t" + line + "\n\t\t\t</p>\n"

file_text += "\t\t\t<br>\n" + "\t\t\t<h2 style=\"margin-left:-1%\">Plots of the Collected Data</h2>\n" + "\t\t\t<center>\n\t\t\t\t<div>\n\t\t\t\t\t<br>\n"
sp = subprocess.Popen(['ls', './plots/'], stdout=subprocess.PIPE)
[output, _ ] = sp.communicate()
img_list = output.decode("utf-8").split()

plot_names = ["Avg. Steptimes and Looptimes v/s Iterations", "Avg. Steptimes, Velocity, Collision and Position Update times v/s Iterations", "Steptimes v/s Iterations with Error Bars", "Histogram of Steptimes for 58 Iterations", "Avg. Steptimes for Random Samples and Entire Data v/s Iterations", "", "", "", ""]

for img_index in range(len(img_list)):
	file_text += "\t\t\t\t\t<img src=\"../plots/" + img_list[img_index] + "/\" height = \"400\">\n\t\t\t\t\t<br>\n"
	file_text += "\t\t\t\t\t<figcaption>Fig." + str(img_index + 1) + ":  " + plot_names[img_index] + "</figcaption>\n\t\t\t\t\t<br>\n"

file_text += "\t\t\t\t</div>\n\t\t\t</center>\n" + "\t\t</div>\n\t</body>\n</html>"
html_file.write(file_text)
