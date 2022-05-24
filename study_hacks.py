# @author: semper curiosus

import requests
import os
from bs4 import BeautifulSoup
import re

# first, check there was a response from the web page to know that was a valid url
def response_check(url):

    page_number = 1
    url_base = url
    url_testing = ""
    r = 200
    status_code = 0
    page_content_raw = ""

    try:
        print(f"checking the url: {url}")

        while status_code == 0:
            print("setting url...")
            url_testing = url_base + str(page_number) + '/'

            print("making request...")
            r = requests.get(url_testing)

            status_code = r.status_code
        
            if status_code == 200:
                print(f"there was a response {status_code} from the url {url_testing}")
                
                # if there was a response from the page then setting the content.
                page_content_raw = r.content
                parse_soup(page_content_raw)

                # reset the status_code value & increment page
                status_code = 0
                page_number = page_number + 1

            else:
                print(f"the response {status_code} was given; killing script because 200 was not returned..")
                break

    except Exception as e:
        print(f"there was an exception while making the request to url {url}")
        print("excetption: " +  str(e))
    finally:
        print("checking url is complete.")

def parse_soup(page_content_raw):
    # print(str(page_content))
    print("parse for articles")
    article_urls = []

    page_soup = BeautifulSoup(page_content_raw, 'html.parser')

    try:
        data_from_page = page_soup.find(class_="main content blog")
        # print(str(data_from_page))
        articles = data_from_page.find_all('article')

        try:
            for article in articles:
            # from looking at study hack blog, the page has one or more "articles" (html tag name) that has a "blogtitle" and then content. 

                article_url = article.find('a').get('href')
                article_urls.append(article_url)

            # print(article_urls)

            for article in article_urls:
                get_article_details(article)

        except:
            print('there was an exception appending the article url to the list.')

    except Exception as e:
        print('there was an exception when getting the main content class data.')

def get_article_details(url):
    try: 
        #soup
        article_content_raw = requests.get(url).content
        article_soup = BeautifulSoup(article_content_raw, 'html.parser')
        article_content = article_soup.find(class_="main content blog").find('article')
        #date
        article_date = article_content.find('small').text
        article_date = article_date.split(' · ')[0]
        article_date_filename_format = str(format_date(article_date))
        #title
        article_title = article_content.find(class_='blogtitle').text
        #remove the un-needed sections (comments and such)
        article_content.div.decompose()
        article_content.small.decompose()
        article_content.h1.decompose()
        #format the things! 
        article_text = str(article_content.get_text())
        article_text = format_article_text(article_text)
        #urls on page
        article_refs = return_links_as_string(article_content.find_all('a'))
        #url
        article_source_url = url

        # print(f"blog \"{article_title}\" was published on {article_date} and the url is [{article_url}]")
        save_file(article_title, article_date_filename_format, article_date, article_text, article_source_url, article_refs)
    except Exception as e:
        print('there was an exception when trying to get the article details.')

def  return_links_as_string(links):
    link_hrefs = ""

    if len(links) > 0:
        for link in links:
            # print(link)
            link_hrefs += (f"\t * link from [{link.text}]: {link.get('href')}" + '\n')
    else:
        print('the list was empty.')
    
    return link_hrefs

def format_article_text(text):
    
    transformed_text = text

    if transformed_text is not None or transformed_text != '':
        transformed_text = replace_multiple_newline_chars(transformed_text)
        transformed_text = double_up_newline_chars(transformed_text)

        return transformed_text

def replace_multiple_newline_chars(transformed_text):
    count = 1
        # replace multiple new lines at beginning of text string.
    while (count > 0):           

        transformed_text =  transformed_text.replace('\n\n', '\n')
        count = transformed_text.count('\n\n')
        #pulling the count each time was not ideal, but it was giving me the most acurate representation of the inconsistancies in the multiple pairs of newlines.

    return transformed_text

def double_up_newline_chars(transformed_text):
    return transformed_text.replace('\n', '\n\n')
    

def format_date(date):
    # date = datetime.date(date)
    date = str(date).replace(',', '')

    if date is not None or date != '':  
        try:
            date_split = str(date).split(' ')

            month = return_month_integer(date_split[0])
            day = re.sub(r'[a-zA-Z]', '', date_split[1])
            year = date_split[2]
            # print(year +  '_' + month + '_' + day)
        except:
            print('there was an exception with formatting the date.')
        finally:
            return str(year) + '_' + str(month) + '_' + str(day)

def return_month_integer(month):
    # will just return the month name if nothing is found.
    month_name = month.lower()

    if month_name is not None or month_name != '' or month_name != 0:
        if month_name == 'jan' or month_name == 'january':
            month = 1
        elif month_name == 'feb' or month_name == 'february':
            month = 2
        elif month_name == 'mar' or month_name == 'march':
            month = 3
        elif month_name == 'apr' or month_name == 'april':
            month = 4
        elif month_name == 'may':
            month = 5
        elif month_name == 'jun' or month_name == 'june':
            month = 6
        elif month_name == 'jul' or month_name == 'july':
            month = 7
        elif month_name == 'aug' or month_name == 'august':
            month = 8
        elif month_name == 'sept' or month_name == 'september':
            month = 9
        elif month_name == 'oct' or month_name == 'october':
            month = 10
        elif month_name == 'nov' or month_name == 'november':
            month = 11
        elif month_name == 'dec' or month_name == 'december':
            month = 12
    return month

def make_file_name(date, file_name):

    if file_name is not None or file_name != '':
        try:
            file_name = file_name.replace(' ', '_')
            # the re sub is a new regular exression syntax that replaces all non-alphanumeric chars, save underscores. [a-z][A-Z][_]
            file_name = re.sub(r'\W', '', file_name)
            file_name = date + '_' + file_name + '.txt'
        except:
            print('the file name could not be concatenated.')
        finally:
            return file_name

# the saved items will use the "blogtitle" as the filename, with underscores _ instead of spaces, and in all lower case.
def save_file(article_title, article_date_filename_format, article_date_original, article_text, article_source_url, article_references):

    file_base = '/Users/erichulse/Projects/study_hacks_webscrape/articles'
    file_name = make_file_name(article_date_filename_format, article_title.lower())
    
    file_path_full = os.path.join(file_base,file_name)
    
    try:
        with open(file_path_full, 'a') as file:
            file.write(article_title + '\n\n')
            file.write(f"Original Date Published: {article_date_original} " + '\n')
            file.write(f"Source: {article_source_url}" + '\n')
            file.write('= = = = =')
            file.write(article_text + '\n')
            file.write('= = = = =' + '\n')
            file.write(article_references + '\n')

    except Exception as e:
        print('there was an exception while attempting to write the file.')
        print(str(e))

    finally:
        print(f"writing {file_name}")

# behavior assumptions
#   if there is no response, stop the program, I am not going to keep trying to get a response.
#   keep iterating until no response is given.
#   do not overwrite files
#
#   TRY the shelf or shelve module to store the highest page number for later. 
#   

def main():
    print('starting web scrape')
    url = "https://www.calnewport.com/blog/page/"
    response_check(url) 

    print("script is done running.")

# main call
main()