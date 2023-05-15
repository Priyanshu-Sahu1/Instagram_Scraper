Download pycharm and setup virtual enviroment in your pycharm inside the folder Instagram_Hastag_DataScraper using Command in terminal below. 

pip install virtualenv or can follow the below link to create virtual Environment

https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#env-requirements

After creating virtual environment in your project.
install scrapy package in pycharm ,
install instaloader package using pip install instaloader ,
install pandas into the terminal using pip install pandas command in the Terminal

To scrape data from hashtag you need a instagram login.
Need to add your credentials in parameter.py file.
Now Go to the scraperSkeleton(outer) directory using command in terminal mentined below
cd .\scraperSkeleton\

After reaching to the scraperSkeleton directory
Run following command in terminal.
scrapy crawl InstagramCrawler -o filename --nolog in the terminal. Where rentinnoida.csv(for reference) is the file name in which the output will be recorded
