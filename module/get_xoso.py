import requests
from bs4 import BeautifulSoup
import sys
def get_number(url):
	ses = requests.sessions.session()
	path = ses.get(url)
	soup = BeautifulSoup(path.text,"html.parser")
	table = soup.find("table",id = "MB0")
	tag_tr = table.find_all("tr")[1:]
	result = ""
	for i in tag_tr:
		if i.find("em") != None:
			number = i.find("em").get_text(" ")
			result = " ".join((number,result))
		elif i.find("p") != None:
			number = i.find("p").get_text(" ")
			result = " ".join((number,result))
		else:
			pass
	results = result.strip().split(" ")
	return results

def check_winner(number,results):
	if number.isdigit():
		if str(number) in [result[-2:] for result in results]:
			return f"Bingo U are lucky with: {number}"
		else:
			return f"Gud luck next time with: {number}"
	else:
		return f"pls recheck your input: {number}"

def solve(numbers):
	results = get_number("https://xskt.com.vn/") 
	check_result = ""
	for number in numbers:
		check_result = "\n".join([check_winner(number,results),check_result])
	return check_result
	
def main():
	number = sys.argv[1:]
	print(solve(number))


if __name__ == '__main__':
	main()