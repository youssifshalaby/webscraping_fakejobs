import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get("https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(page.content, "lxml")
jobs = soup.find_all("div",class_="card-content")
titles = []
companys = []
locations = []
times = []
links = []
for i in range(len(jobs)):
  titles.append(jobs[i].find("h2").text.strip())
  companys.append(jobs[i].find("h3").text.strip())
  locations.append(jobs[i].find("p",class_="location").text.strip())
  times.append(jobs[i].find("time").text.strip())
  links.append(jobs[i].find_all("a")[0]["href"])

df = pd.DataFrame({"title":titles,"company":companys,"location":locations,"time":times,"link":links})
df.to_csv("fake_jobs.csv",index=False)