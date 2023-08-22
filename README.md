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

The application will go to the set url, in this case (https://www.calnewport.com/blog) and returns all articles starting with the first page all the way to whatever he is up to these days.

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

[Clone me HTTPS](https://github.com/sempercuriosus/study_hacks_scrape_public.git)
[Clone me SSH](git@github.com:sempercuriosus/study_hacks_scrape_public.git) 
Copy + Pasta (Paste) the Python file directly

### Usage

<!-- Usage -->

#### behavior assumptions
- If there is no response, stop the program, I am not going to keep trying to get a response.
- Keep iterating until no response is given, ie there are no more pages
- If the file is already downloaded do not overwrite


