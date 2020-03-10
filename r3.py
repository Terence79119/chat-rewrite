def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):

	allen_word_count = 0
	viki_word_count = 0
	allen_pic_count = 0
	viki_pic_count = 0
	allen_stick_count = 0
	viki_stick_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				allen_pic_count += allen_pic_count + 1
			elif s[2] == '貼圖':
				allen_stick_count += allen_stick_count + 1
			for m in s[2:]:
				allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '圖片':
				viki_pic_count += viki_pic_count + 1
			elif s[2] == '貼圖':
				viki_stick_count += viki_stick_count + 1
			for m in s[2:]:
				viki_word_count += len(m)
	print('Allen 傳了', allen_word_count, '個字')
	print('Allen 傳了', allen_pic_count, '張圖')
	print('Allen 傳了', allen_stick_count, '張貼圖')
	print('Viki 傳了', viki_word_count, '個字')
	print('Viki 傳了', viki_pic_count, '張圖')
	print('Viki 傳了', viki_stick_count, '張貼圖')

			

		#if name == 'Viki':
			#viki_word_count =+ len(s[2:])

		
	


def write_file(filename, lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line +'\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)
	


main()
