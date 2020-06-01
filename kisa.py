import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os

class MangakisaCrawler():
    """docstring for ClassName"""

    

    def __init__(self):
        super(MangakisaCrawler, self).__init__()
        self.arg = "arg"

    base_url = "https://mangakisa.com"

    #this returns a dictionary of search results based on your search term
    def getSearchResults(self, search_term):

        try:
            kisa_search = self.base_url + "/search?q=" + search_term.replace(" ", "+")
            response = requests.get(kisa_search, timeout=60)
            content = BeautifulSoup(response.content, "html.parser")

            search_info = content.find(
                "div", {'class': 'iepbox nobackground'}).findAll('a', {'class': 'an'})

            titles = []
            urls = []
            status = []
            categories = []
            imgs = []

            for result in search_info:
                titles.append(result.find("div", {'class': 'similardd'}).text.strip())

            for result in search_info:
                urls.append(self.base_url + result.attrs['href'])

            for result in search_info:
                status.append(result.find("div", {'class': 'similardd-status'}).text.strip())

            for result in search_info:
                categories.append(result.find("div", {'class': 'similardd-categories'}).text.strip())

            for result in search_info:
                imgs.append(self.base_url + result.find("img", {'class': 'coveri'}).attrs['src'])

            search_results = {}

            for i in range(len(search_info)):
                temp = []
                temp.append(urls[i])
                temp.append(imgs[i])
                temp.append(status[i])
                temp.append(categories[i])

                search_results[titles[i]] = temp

        except requests.exceptions.Timeout:
            print("Timeout occurred")
        except:
            # print("SOMETHING HAPPENED")
            not_found_text = """
We are 99% sure we have the anime you are looking for. Here are a few tips to make it easier to find it.
Let's say you are searching for "Seven Deadly Sins":

1) Try the alternative japanese title "Nanatsu no Taizai" (Check MyAnimeList's page).

2) Try using just one word like "Seven", "Deadly", "Nanatsu" or "Taizai".

3) Make sure you are not searching "7 deadly sins", instead of "seven deadly sins".
"""
            search_results = { 'Search Not Found': ['',
                        '',
                        not_found_text,
                        '']}

        return search_results

    #this returns a dictionary full of information on your specific manga
    def getMangaInfo(self, manga_url):
        try:
            response = requests.get(manga_url, timeout=None)
            content = BeautifulSoup(response.content, "html.parser")

            # there will be one dictionary that will be returned at the end of this
            # each and every one of these strings will play a part in being a key and value pair
            title = ""
            image = ""
            description = """ """
            categories = []
            author = ""
            status = ""
            total_chapters = ""
            # chapter_titles = []
            chapter_urls = []

            # over here, we populate each variable 

            title = content.find("h1", {'class': 'infodes'}).text.strip()
            image = self.base_url + "/" + content.find("img", {'class': 'posteri'}).attrs['src']
            description = content.find("div", {'class': 'infodes2'}).text.strip()

            infodes2 = content.findAll("div", {'class': 'infodes2'})[1].findAll("div", {'class': 'textc'})

            author = infodes2[1].text.strip()
            status = infodes2[2].text.strip()
            total_chapters = infodes2[3].text.strip()

            for atag in infodes2[0].findAll("a", {'class': 'infoan'}):
                categories.append(atag.text.strip())

            chapterbox = content.find("div", {'class': 'infoepboxmain'}).find("div", {'class': 'infoepbox'}).findAll("a", {'class': 'infovan'})

            for chapter in chapterbox:
                chapter_urls.append(self.base_url + "/" + chapter.attrs['href'])

            chapter_urls.reverse()

            manga_info = {}
            manga_info["Title"] = title
            manga_info["Poster"] = image
            manga_info["Description"] = description
            manga_info["Categories"] = categories
            manga_info["Author"] = author
            manga_info["Status"] = status
            manga_info["Total Chapters"] = total_chapters
            manga_info["Chapter Links"] = chapter_urls




        except requests.exceptions.Timeout:
            print("Timeout occurred")

        return manga_info

    #this function returns a list of all the image urls of any webpage
    def getAllChapterImgLinks(self, link_to_images):

        links = []

        try:
            response = requests.get(link_to_images, timeout=60)
            content = BeautifulSoup(response.content, 'html.parser')
            img_tag = content.findAll('img')
            links = ["https:" + img['src'] for img in img_tag]
        except Exception as e:
            print(e)
        return links

    # this function downloads all the images from a webpage into a specified directory
    def downloadImgsToDir(self, image_list, fullpath):
        filetype = ""
        total = len(image_list)
        for i in range(0, total):

            if image_list[i][-4:] == ".jpg":
                filetype = ".jpg"
            else:
                filetype = ".png"

            pic = requests.get(image_list[i],
                               stream=True, headers={'User-agent': 'Mozilla/5.0'})

            if pic.status_code == 200:
                with open(fullpath + "/pg" + str(i) + filetype, 'wb') as f:
                    f.write(pic.content)

    def downloadChaptersAndOrganize(self, manga_title, chapter_links, download_range_lower, download_range_upper):
        # first enter Manga folder
        # check then check if the folder called "manga_title exists"

        # if it exists, enter the folder and make a list of chapter numbers that already exist
        # check the range and start a for loop between [download_range_lower, download_range_upper]
        # within each loop, make a chapter subfolder in the following format: chapter_[index value in the loop]
        # first make a image list for the chapter using the chapter url and then feed it into download img to dir function
        # then reiterate the loop until the end of the domain is reached

        # if it doesn't exist, make a new folder and then do all the steps above

        current_directory = os.getcwd()
        library_directory = os.path.join(current_directory, r'Manga')
        manga_folder = os.path.join(library_directory, manga_title)
        # print(manga_folder)

        #Make a folder for the manga that is being downloaded if it doesn't already exist
        if not os.path.exists(manga_folder):
           os.makedirs(manga_folder)

        for i in range(len(chapter_links)):
            chapter_folder = os.path.join(manga_folder, "chapter_" + str(i))

            if i >= download_range_lower and i <= download_range_upper and not os.path.exists(chapter_folder):
                   os.makedirs(chapter_folder)
                   image_list = self.getAllChapterImgLinks(chapter_links[i])
                   self.downloadImgsToDir(image_list, chapter_folder)
        

    # def updateMangaChapters



# def main():
#     crawler = MangakisaCrawler()
#     manga_previews = crawler.getSearchResults("tokyo     ")
#     pprint(manga_previews)
#     # manga_info = crawler.getMangaInfo(manga_previews.get("Tokyo Ghoul")[0])#inputting selected manga url from preview
    
#     # pprint(manga_info)
#     # print(len(manga_info.get("Chapter Links")))

#     # crawler.downloadChaptersAndOrganize(manga_info.get("Title"), manga_info.get("Chapter Links"), 0, 10)



# if __name__ == "__main__":
#     main()
