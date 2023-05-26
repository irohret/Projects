import requests
import os
from bs4 import BeautifulSoup
import urllib.parse

# check if link in vaid anything other than 200 means unable to connect
# 403 Error mean server got the requrest, but doesn't allow data mining
url_name = input("Url: ")
r=requests.get(url_name)
print(r.status_code)


def download_images_from_url(url, save_directory):
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:

        # Create the directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <img> tags
        img_tags = soup.find_all('img')

        # Download each image
        for img_tag in img_tags:
            # Get the source URL of the image
            img_url = img_tag['src']

            # Remove query parameters from the image URL
            img_url = urllib.parse.urlparse(img_url).scheme + "://" + urllib.parse.urlparse(img_url).netloc + urllib.parse.urlparse(img_url).path

            # Send a GET request to download the image
            img_response = requests.get(img_url, stream=True)

            # Extract the file name from the URL
            file_name = os.path.basename(img_url)

            # Define the file path to save the image
            file_path = os.path.join(save_directory, file_name)

            # Save the image file
            with open(file_path, 'wb') as file:
                for chunk in img_response.iter_content(1024):
                    file.write(chunk)

            print(f"Image '{file_name}' downloaded successfully.")

        print("All images downloaded.")
    else:
        print("Failed to download images.")


if __name__ == '__main__':
    web_link = url_name
    save_directory = "./images"  # Desired save directory. This will create a folder where the script is running at

    # Check the operating system and set the appropriate path separator
    if os.name == 'nt':  # Windows
        save_directory = save_directory.replace('/', '\\')
    else:  # Mac and Linux
        save_directory = save_directory.replace('\\', '/')

    download_images_from_url(web_link, save_directory)