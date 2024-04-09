import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_indeed_jobs(job_title, location, num_pages):
    base_url = f"https://www.indeed.com/jobs?q={job_title.replace(' ', '+')}&l={location.replace(' ', '+')}&from=searchOnHP&vjk=d75d466f2feec441"
    jobs = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for page in range(num_pages):
        url = f"{base_url}&start={page * 10}"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise error for non-200 status codes

            soup = BeautifulSoup(response.text, 'html.parser')
            job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')

            for job in job_listings:
                title = job.find('a', class_='jobtitle').text.strip()
                company = job.find('span', class_='company').text.strip()
                location = job.find('span', class_='location').text.strip()
                summary = job.find('div', class_='summary').text.strip()
                salary = job.find('span', class_='salaryText')
                if salary:
                    salary = salary.text.strip()
                else:
                    salary = 'None'

                jobs.append({
                    'title': title,
                    'company': company,
                    'location': location,
                    'summary': summary,
                    'salary': salary
                })
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch page {page+1}: {e}")
        
        # Add a delay between requests to avoid being detected
        time.sleep(3)  # 3-second delay

    return jobs

def save_to_json(jobs, filename):
    with open(filename, 'w') as f:
        json.dump(jobs, f, indent=4)

if __name__ == "__main__":
    job_title = input("Enter job title: ")
    location = input("Enter location: ")
    num_pages = int(input("Enter number of pages: "))

    jobs = scrape_indeed_jobs(job_title, location, num_pages)
    save_to_json(jobs, 'jobs.json')
    print(f"Scraped {len(jobs)} job listings. Saved to jobs.json")


