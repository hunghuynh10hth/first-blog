import json
import requests
import datetime
from bs4 import BeautifulSoup

class get_data:
	def __init__(self):
		self.list = []

	def get_request(self,url):
		ses = requests.sessions.session()
		resp = ses.get(url)
		return resp

	def get_data_jobs(self, url):
		path = self.get_request(url)
		data = path.json()
		for i in data:
			self.list.append((i["title"],i["html_url"]))
		return self.list

	def get_url_posts(self,url,label):
		soup = BeautifulSoup(self.get_request(url).text, "html.parser")
		tag_h3 = soup.find_all("h3", attrs ={"itemprop":"name"})
		for i in tag_h3:
			self.list.append(str(i.a))

			if len(self.list) == 10 and label == "Lastest":
				return self.list

		try:
			url = soup.find(attrs = {"id":"Blog1_blog-pager-older-link"}).get("href")
			self.get_url_posts(url,label)
		except:
			return self.list
		
		return self.list

def get_label_posts(label):
	if label == "Lastest":
		url = "https://www.familug.org"
	else:
		url = "https://www.familug.org/search/label/{}".format(label)
	return get_data().get_url_posts(url,label)
	
def solve():
	posts = {}
	labels = ["Python","Command","sysadmin","Lastest"]
	for label in labels:
		posts[label] = get_label_posts(label)
	API = "https://api.github.com/repos/awesome-jobs/vietnam/issues"
	jobs = get_data().get_data_jobs(API)
	return {"jobs":jobs , "posts": posts}

def main():
	data = solve()
	data["time"] = datetime.datetime.now().strftime("%a,%b %d at %H:%M:%S")
	with open("data.json","wt") as f:
		json.dump(data, f, indent= 4)

if __name__ == '__main__':
	main()