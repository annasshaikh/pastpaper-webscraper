# Python Web Scraper

12th Dec 2020

This Is a Web Scraper to download all pastpaper from a [website](https://papers.gceguide.com/A%20Levels/) for Cambridge A-Level pastpapers 
## Usage

Note: Have Stable Internet Connection 

You would need the full Url of the component. The Following is a Example for Chemistry (9701) 
```bash
https://papers.gceguide.com/A%20Levels/Chemistry%20(9701)/
```
## Example


Output:

UI:

<a href="https://ibb.co/T1V37fX"><img src="https://i.ibb.co/tz7rvGf/Output.png" alt="Output" border="0"></a>


Here Are Example Of All Physics (9702) Past Paper :

<a href="https://ibb.co/FgzV2KZ"><img src="https://i.ibb.co/9sWt6NK/Out-Put-Folder.png" alt="Out-Put-Folder" border="0"></a>

## Code

```python
import requests
from bs4 import BeautifulSoup
import os

#Downloads The PDF from its Url And Saves it 'filename' folder
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
