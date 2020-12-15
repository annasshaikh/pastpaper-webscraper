import requests
from bs4 import BeautifulSoup
import os

#Downloads The PDF fron its Url And Saves it 'filename' folder
def download_file(download_url, filename,index): 
    print(f"Downloading File #{index}: {filename} ")
    response = requests.get(download_url)
    file = open(filename, 'wb')
    file.write(response.content)
    file.close()

#Gets The Content and Finds All the PDF Link on that Page
#Call the download_file function to give it the PDF links
#Return the Total files found
def scarp_web(url,folder):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")
    str = []
    index = 1
    for str in soup.find_all('a'):
        check = str.get('href' ).split('.')
        if (check[-1]=='pdf'):
            current_url = str.get('href' ) 
            download_file(url + current_url, folder +'\\' +current_url,index)
            index += 1
    return index


def main():
    print("Website Supported: https://papers.gceguide.com/ \n")
    num_subject = int(input("Number Of Subjects: "))
    list_name , list_url = [], []
    totalfiles = 0
    #getting baseURl and Folder Name and Storing then in list
    for a in range(num_subject): 
        name = input("Enter the Name Of Subject: ")
        url = input("Enter The Url: ")
        list_name.append(name) 
        list_url.append(url)
        try:  
            os.mkdir(name)  
        except OSError as error:  
            print(error) 

    for i in range(num_subject):
        totalfiles += scarp_web(list_url[i],list_name[i])
        
    
    print(f'Total {totalfiles} Files Downloaded\a')


if __name__ == "__main__" :
    main()  