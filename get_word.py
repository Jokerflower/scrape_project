with open("html_text.txt", 'r') as file:
	text = file.read()


text.find('lang="en" word=', beginning) != -1:


word_start_point = text.find('"', beginning + 15)
word_end_point = text.find('"', word_start_point + 1)


word = text[word_start_point + 1 :  word_end_point]