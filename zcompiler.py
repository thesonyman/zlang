
import sys
#zscript
#code by thesonyman
#To use "zcompiler.py filename.txt"
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
varlist= {}
file_2_compile = sys.argv[1]
ifs = 0
with open(file_2_compile) as file:
	for line in file:

		if ("var|" in line):
			w = line.split("|")
			w = w[1]
			w = w.split("=")
			bee = w[0]
			bee2 = w[1]
			varlist[bee] = bee2
			#print varlist
		if ("if|" in line):
			ifs = ifs + 1
			z = line.split("|")
			try:
				if(eval(z[1]) == True):
					print "true"


				elif (eval(z[1]) == False):
					print "false"
			except NameError:
				for key, value in varlist.iteritems():
					#print key + " " + value
					key = key.replace(" ", "")
					z[0] = z[0].replace(" ", "")

					s = z[1].split("=")
					first = s[0]
					#print first
					if (str(key) == first):

						#print "HOLY CRIMMANY"
						p = value
						if(eval(z[1].replace(key,p)) == True):
							#print "true"
							for line in file:
								if "id=" in line:
									x = line.split("id=")
									if int(x[1]) == ifs:
										line.replace("id=%s" %ifs, "")
										print line

						elif (eval(z[1].replace(key,p)) == False):

							print "false"

		if ("tells" in line):
			line = line.replace("tells", "")
			if ("id=" in line):
				pass
			else:
				print line
