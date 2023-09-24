# Scrapy-project
There are 2 versions of the spider
* The first version is called simply MangoSpider.py.  
  It uses API endpoint that returns all information about a given product in .json format.
  During my initial efforts to extract the information I have stumpled upon some requests in the network section of the inspect element.
  When I tried changing the color of the product, these requests would appear that would have very simillar urls, the only difference being the last 2 symbols which would change based on the selected color.
  I have used this link in the first solution since using the original link with only scrapy doesn't load the JS.
* The second version is called MangoSpiderWithSelenium.py
  It uses scrapy-selenium to load the JS on the page and css selectors to find the requred info about the product.
  I haven't added a chromedriver to the directory since the driver is different for every OS
* NB: I don't know if it was due to a mistake, but there were 2 different links for different products provided, so I have scraped the information for both.
