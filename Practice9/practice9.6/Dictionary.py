__author__ = 'student'
def make_dic(goose):
	I=open(goose)
	res={}
	for line in I:
		line=line[:-1].split(' - ')
		line[1]=line[1].split(', ')
		for i in line[1]:
			if i not in res.keys():
				res[i]=[line[0]]
			else:
				res[i].append(line[0])
	I.close()
	return res

def update(what, with_what):
	ru_en, en_ru= what, with_what
	for en in en_ru.keys():
		for ru in en_ru[en]:
			if ru not in ru_en.keys(): ru_en[ru]=[en]
			elif en not in ru_en[ru]: ru_en[ru].append(en)

def output(dic, fname):
	Oxygen=open(fname, 'w')
	for i in sorted(dic.keys()):
		Oxygen.write(i + ' - ' + ', '.join(sorted(dic[i]))+'\n')
	Oxygen.close()

ru_en=make_dic('ru-en.6')
en_ru=make_dic('en-ru.6')

update(ru_en, en_ru)
update(en_ru, ru_en)

output(ru_en, 'ru-en.6.1')
output(en_ru, 'en-ru.6.1')



