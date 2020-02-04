import random

class Group():
	def __init__(self, pref1, pref2, pref3, first_net, second_net = None,):
		self.first = first_net
		self.second = second_net
		self.pref1 = pref1
		self.pref2 = pref2
		self.pref3 = pref3
		self.hash = hash((self.first, self.second))
		if second_net:
			self.size = 2
		else:
			self.size = 1

	def remove_ranking(self, pref):
		if pref == self.pref1:
			self.pref1 = self.pref2
			self.pref2 = self.pref3
			self.pref3 = None
		elif pref == self.pref2:
			self.pref2 = self.pref3
			self.pref3 = None
		elif pref == self.pref3:
			self.pref3 = None



class PairGroup():
	def __init__(self, topic, first, second, third, fourth = None, fifth = None):
		self.topic = topic
		self.first = first
		self.second = second
		self.third = third
		self.fourth = fourth
		self.fifth = fifth


def process_class_data(fileName):
	if '.txt' not in fileName:
		raise ValueError
	f = open(fileName, "r")
	all_groups = []
	for line in f:
		input = line.replace(' ', '').replace('\n', '').split(',')
		names = []
		rankings = []
		if len(input) == 5:
			names = input[:2]
			rankings = input[2:]
			g = Group(input[2], input[3], input[4], input[0], input[1])
		elif len(input) == 4:
			names = input[:1]
			rankings = input[1:]
			g = Group(input[1], input[2], input[3], input[0])
		else:
			raise ValueError('There is some line not in the format xxx, #, #, #')
		all_groups.append(g)
	return all_groups


def process_names(fileName):
	if '.txt' not in fileName:
		raise ValueError
	f = open(fileName, "r")
	nets = []
	for line in f:
		nets.append(line.replace('\n', ''))
	return nets

def match_groups(groups, num_students):
	category_max = 2 * ((num_students / 2) // 8) 
	category_size = {}
	all_pairs = []
	while(len(groups) > 1):
		start = groups[0]
		first_pref = start.pref1
		if not first_pref:
			raise NotImplementedError('try raising the category max - group cannot be placed in preferable group')
		second = None
		for i in range(1, len(groups)):
			if groups[i].pref1 == first_pref:
				second = groups[i]
				break
		if not second:
			if not start.pref2:
				raise NotImplementedError('rerun - cannot give a certain group one their preferences')
			temp = start.pref1
			start.pref1 = start.pref2
			if start.pref3:
				start.pref2 = start.pref3
				start.pref3 = temp
			else:
				start.pref2 = temp
			continue
		pair = PairGroup(first_pref, start.first, start.second, second.first, second.second)
		if not start.second and not second.second:
			g = Group(first_pref, start.pref2, second.pref3, start.first, second.first)
			groups[i] = g
			groups = groups[1:]
		else:
			all_pairs.append(pair)
			if first_pref not in category_size:
				category_size[first_pref] = 0
			category_size[first_pref] +=1
			if category_size[first_pref] >= category_max:
				for g in groups:
					g.remove_ranking(first_pref)
			if i == len(groups)-1:
				groups = groups[1:i]
			else:
				groups = groups[1:i] + groups[i+1:]
	return all_pairs, groups


if __name__ == '__main__':
	class_data = process_class_data('class.txt') #returns a list of groups
	random.shuffle(class_data)
	nets = process_names('nets.txt') #returns a list of net ids
	pairs, groups = match_groups(class_data, len(nets))
	if (len(groups) == 1):
		print("Couldn't match one group - run again or match last group by yourself (results in output.txt")
		print("Net 1: ", groups[0].first)
		print("Net 2: ", groups[0].second)
		print("Pref 1: ", groups[0].pref1)
		print("Pref 2: ", groups[0].pref2)
	else:
		print("Done - results are in the output.txt document")
	file1 = open("output.txt","w") 
	for p in pairs:
		s = "" + str(p.topic) + ',' + str(p.first) + ',' + str(p.second) +','  + str(p.third) + ',' + str(p.fourth) + '\n'
		file1.write(s)
	file1.close() 
