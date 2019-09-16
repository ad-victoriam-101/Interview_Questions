# Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. 
# You should also allow for additional units to be added to the system
print "=-{Calebot Productions}-=-{2016}-="
print "Metric Converter"
print "Convert metric units to bigger or smaller metric units"

def metric():
  #What unit (grams, meters, liters, (more to be addded in future like watts))
  def unit():
    global u
    u = raw_input("What unit of metric (no prefix)? (grams, liters, meters): ").lower()
    if u == "grams" or u == "gram" or u == "g":
      u = "g"
      print "Grams selected!"
    elif u == "liters" or u == "liter" or u == "l":
      u = "l"
      print "Liters selected!"
    elif u == "meters" or u == "meter" or u == "m":
      u = "m"
      print "Meters selected!"
    else:
      print "Please use grams, liters, or meters.\n"
      unit()
  
  #Size to convert from
  def startsize():
    print "Sizes and abbreviations: "
    print "Kilo : k\nHecto : h\nDeca : da\nBasic unit : (leave blank)\nDeci : d\nCenti : c\nMilli : m"
    global ss
    ss = raw_input("What size to start at? (use abbreviation): ").lower()
    if ss == "k" or ss == "h" or ss == "da" or ss == "d" or ss == "c" or ss == "m":
      ss = ss
    elif ss == "" or ss == " " or ss == "none" or ss == "basic":
      ss = ""
    else:
      print "Please use provided abbreviations: "
      startsize()
  
  #Size to convert to
  def endsize():
	print "Sizes and abbreviations: "
	print "Kilo : k\nHecto : h\nDeca : da\nBasic unit : (leave blank)\nDeci : d\nCenti : c\nMilli : m"
	global es
	es = raw_input("What size to end at? (use abbreviation): ").lower()
	if es == "k" or es == "h" or es == "da" or es == "d" or es == "c" or es == "m":
		  es = es
	elif es == "" or es == " " or es == "none" or es == "basic":
		es = ""
	else:
		  print "Please use provided abbreviations: "
		  endsize()
	    
	#Numbers to convert
  f = {"k" : 1000, "h" : 100, "da" : 10, "" : 1, "d" : .1, "c" : .01, "m" : .001}
  t = {"k" : .001, "h" : .01, "da" : .1, "" : 1, "d" : 10, "c" : 100, "m" : 1000}
	
	#Converting
  def conv():
    global n
    global r
    n = float(raw_input("What number of " + ss + u + " do you want to convert: "))
    r = n * f[ss]
    r = r * t[es]
    r = str(r)
	
	#Redo?
  def again():
    re = raw_input("New? (y/n): ").lower()
    if re == "y":
      print "Going again!"
      metric()
    else:
      print "\"Y\" not selected. Ending program."
      print "Enjoy!"
	
	#Run
  unit()
  startsize()
  endsize()
  conv()
  print str(n) + ss + u + " = " + str(r) + es + u
  again()
  	
metric()
