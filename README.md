# Study Hacks Web Scrape
<!-- Title  -->

---

## Table of Contents

<!-- Table of Contents -->

- [About The Project](#about_project)
- [Getting Started](#getting_started)
- [Challenges](#challenges)
- [Author Credit](#author_credit)
- [Resources](#resources)
- [Final Note](#final_note)

---

## About The Project <a id="about_project"></a>

<!-- About the Project -->
I wanted to learn about web scraping. My goal for it was to gather data from a website. Mostly, I just read the documentation, linked below [Resources](#resources), and figured out what to do as I was going. My aim was to see how this process works at a high-level and play around with it. 

I am a big fan of the author Cal Newport, so I picked his [Study Hacks Blog](https://www.calnewport.com/blog) - definitely recommend checking it out. Conveniently for me, he increments his pages numerically, so I used that to my advantage and it was helpful to learn with too.


### Built With

<!-- Built With -->

Python!

### Features

<!-- Features -->

The application will go to the set url, in this case https://www.calnewport.com/blog and returns all articles starting with the first page all the way to whatever he is up to these days.

---

## Getting Started <a id="getting_started"></a>

<!-- Getting Started  -->

### Prerequisites & Dependencies

<!-- Prerequisites & Dependencies-->
- requests
- os
- BeautifulSoup
- re

### Installation

<!-- Installation -->

- Clone
- Use SSH
- Copy + Pasta (Paste) the Python file directly

### Usage

<!-- Usage -->

#### Behavior Assumptions
- If there is no response, stop the program, I am not going to keep trying to get a response.
- Keep iterating until no response is given, ie there are no more pages
- If the file is already downloaded do not overwrite

#### Configurables

<!-- Configurables -->
There are  not any configurable options in this app. 

### Running The App

<!-- Running -->
This is a command line application and can be run with a command like this: 

`python3 study_hacks.py` `study_hacks.py` is a suggested name, but this will be whatever you save the file as. 

---

## Challenges <a id="challenges"></a>

<!-- Challenges -->
I would have loved to add this section when I wrote the app, but it was a long time ago and I do not remember most of what was hard.

I do recall, looking over the code as I write this, my `get_article_details(url)` function being finicky drilling dowin into the tags finding the data I wanted.

As well as actually formatting the output just the way I wanted it to be -- *Chef's Kiss. 

---


## Author Credit <a id="author_credit"></a>

<!-- Author Credits -->
Eric, Semper Curiosus

---

## Resources <a id="resources"></a>

<!-- Resources -->

[Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)

---

## Final Note <a id="final_note"></a>

<!-- Final Note -->

This is a topic that I would like to come back to and learn more about. When other means are not an option and you need some data just go for it, but just make sure you are aware of the implications. (That soundes a lot more serious than I mean it to be, just do not be a ding-dong about scraping someone's website.)

Read this article on [Ethics of Web Scraping](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01)

Something I would like to add either here or to a future scrape 
- TRY the shelf or shelve module to store the highest page number for later. 
- Update this to include more data, such as who I am and add a robots.txt to respect it. 

---

