{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter, BeautifulSoup, and Pandas\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "import pandas as pd\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 92.0.4515\n",
      "Get LATEST driver version for 92.0.4515\n",
      "Driver [/Users/amberngan/.wdm/drivers/chromedriver/mac64/92.0.4515.107/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "# Set the executable path and initialize Splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Visit the NASA Mars News Site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n",
    "\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the browser html to a soup object and then quit the browser\n",
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "\n",
    "slide_elem = news_soup.select_one('div.list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\">Mars 2020 Unwrapped and Ready for More Testing</div>"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Mars 2020 Unwrapped and Ready for More Testing'"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the first a tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"In time-lapse video, bunny-suited engineers remove the inner layer of protective foil on NASA's Mars 2020 rover after it was relocated for testing.\""
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### JPL Space Images Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<html class=\"fancybox-margin fancybox-lock\"><head>\n",
       "<meta charset=\"utf-8\"/>\n",
       "<meta content=\"width=device-width, initial-scale=1\" name=\"viewport\"/>\n",
       "<link href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" rel=\"stylesheet\"/>\n",
       "<!-- <link rel=\"stylesheet\" type=\"text/css\" href=\"css/font.css\"> -->\n",
       "<link href=\"css/app.css\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<link href=\"https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<title>Space Image</title>\n",
       "<style type=\"text/css\">.fancybox-margin{margin-right:0px;}</style></head>\n",
       "<body>\n",
       "<div class=\"header\">\n",
       "<nav class=\"navbar navbar-expand-lg\">\n",
       "<a class=\"navbar-brand\" href=\"#\"><img id=\"logo\" src=\"image/nasa.png\"/><span class=\"logo\">Jet Propulsion Laboratory</span>\n",
       "<span class=\"logo1\">California Institute of Technology</span></a>\n",
       "<button aria-controls=\"navbarNav\" aria-expanded=\"false\" aria-label=\"Toggle navigation\" class=\"navbar-toggler\" data-target=\"#navbarNav\" data-toggle=\"collapse\" type=\"button\">\n",
       "<span class=\"navbar-toggler-icon\"></span>\n",
       "</button>\n",
       "<div class=\"collapse navbar-collapse justify-content-end\" id=\"navbarNav\">\n",
       "<ul class=\"navbar-nav\">\n",
       "<li class=\"nav-item active\">\n",
       "<a class=\"nav-link\" href=\"#\"><i aria-hidden=\"true\" class=\"fa fa-bars\"></i>   MENU   <i aria-hidden=\"true\" class=\"fa fa-search\"></i></a>\n",
       "</li>\n",
       "</ul>\n",
       "</div>\n",
       "</nav>\n",
       "<div class=\"floating_text_area\">\n",
       "<h2 class=\"brand_title\">FEATURED IMAGE</h2>\n",
       "<h1 class=\"media_feature_title\">Dusty Space Cloud</h1>\n",
       "<br/>\n",
       "<a class=\"showimg fancybox-thumbs\" href=\"image/featured/mars2.jpg\" target=\"_blank\"> <button class=\"btn btn-outline-light\"> FULL IMAGE</button></a>\n",
       "</div>\n",
       "<img class=\"headerimage fade-in\" src=\"image/featured/mars2.jpg\"/></div>\n",
       "<div class=\"search sticky\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-6\">\n",
       "<input name=\"Search\" placeholder=\"Search\" type=\"text\"/>\n",
       "</div>\n",
       "<div class=\"col-md-6\">\n",
       "<select aria-label=\"Default select example\" class=\"form-select\" id=\"options\">\n",
       "<option onchange=\"0\" selected=\"\">Mars</option>\n",
       "<!-- <option data-filter=\"sun\" class=\"button\">Mars</option> -->\n",
       "<option class=\"button\" data-filter=\"Sun\">Sun</option>\n",
       "<option class=\"button\" data-filter=\"earth\">Earth</option>\n",
       "<option class=\"button\" data-filter=\"ida\">Ida</option>\n",
       "<option class=\"button\" data-filter=\"jupiter\">Jupiter</option>\n",
       "<option class=\"button\" data-filter=\"venus\">Venus</option>\n",
       "</select>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"container mt-5\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-6\">\n",
       "<h1>Images</h1>\n",
       "</div>\n",
       "<div class=\"col-md-6\" id=\"icon\">\n",
       "<div class=\"icon2\"></div>\n",
       "<div class=\"icon1\"></div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<!-- first div -->\n",
       "<div class=\"div1\" id=\"filter\">\n",
       "<div class=\"thmbgroup\"><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae7.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Icaria Fossae7</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes 7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes 7.jpg\"/><p class=\"thumbcontent\">December 31, 2020<br/>Proctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae7.jpg\"/><p class=\"thumbcontent\">December 31, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes 7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes 7.jpg\"/><p class=\"thumbcontent\">December 29, 2020<br/>Proctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes 7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes 7.jpg\"/><p class=\"thumbcontent\">December 28, 2020<br/>roctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae7.jpg\"/><p class=\"thumbcontent\">December 22, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae.jpg\"/><p class=\"thumbcontent\">December 21, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles4.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles4.jpg\"/><p class=\"thumbcontent\">December 18, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Niger Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Niger Vallis.jpg\"/><p class=\"thumbcontent\">December 17, 2020<br/>Niger Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes.jpg\"/><p class=\"thumbcontent\">December 16, 2020<br/>Proctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Niger Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Niger Vallis.jpg\"/><p class=\"thumbcontent\">December 15, 2020<br/>Niger Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">December 11, 2020<br/>Daedalia Planum</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Sirenum Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Sirenum Fossae.jpg\"/><p class=\"thumbcontent\">November,11, 2020<br/>Sirenum Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles4.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles4.jpg\"/><p class=\"thumbcontent\">November,13, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/South Polar Cap.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/South Polar Cap.jpg\"/><p class=\"thumbcontent\">November,14, 2020<br/>South Polar Cap</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">November,17, 2020<br/>Daedalia Planum</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles3.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles3.jpg\"/><p class=\"thumbcontent\">November,11, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Atlantis Chaos.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Atlantis Chaos.jpg\"/><p class=\"thumbcontent\">November,09, 2020<br/>Atlantis Chaos</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Daedalia Planum</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Niger Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Niger Vallis.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Niger Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Proctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Reull Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Reull Vallis.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Reull Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles3.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles3.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Sirenum Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Sirenum Fossae.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Sirenum Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/South Polar Cap.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/South Polar Cap.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>South Polar Cap</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Niger Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Niger Vallis.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Niger Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Daedalia Planum</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles4.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles4.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/South Polar Cap.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/South Polar Cap.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>South Polar Cap</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Daedalia Planum</p></div></a></div>\n",
       "</div>\n",
       "<!-- first div ends -->\n",
       "<!-- second div starts -->\n",
       "<div class=\"col-md-12 grid-margin\" id=\"column\">\n",
       "<ul class=\"post-list\">\n",
       "<li class=\"post-heading\"></li>\n",
       "</ul>\n",
       "</div>\n",
       "<!-- second div starts -->\n",
       "</div>\n",
       "<div class=\"first imgcontainer mt-3\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-3\">\n",
       "<img id=\"pic\" src=\"\"/>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<!-- end -->\n",
       "<div class=\"module_gallery container\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-6\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://www.jpl.nasa.gov/assets/images/content/tmp/images/jpl_photojournal(3x1).jpg\"/>\n",
       "<div class=\"card-body\">\n",
       "<h5 class=\"card-title\">JPL Photojournal</h5>\n",
       "<p class=\"card-text\">Access to the full library of publicly released images from various Solar System exploration programs</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"col-md-6\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://www.jpl.nasa.gov/assets/images/content/tmp/images/nasa_images(3x1).jpg\"/>\n",
       "<div class=\"card-body\">\n",
       "<h5 class=\"card-title\">Great images in NASA</h5>\n",
       "<p class=\"card-text\">A selection of the best-known images from a half-century of exploration and discovery</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"multi_teaser\">\n",
       "<div class=\"container\">\n",
       "<h1>You Might Also Like</h1>\n",
       "<div class=\"col-md-12 mt-5\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-4\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://imagecache.jpl.nasa.gov/images/640x350/C1-PIA24304---CatScanMars-16-640x350.gif\"/>\n",
       "<div class=\"card-body\">\n",
       "<p class=\"card-text\">Access to the full library of publicly released images from various Solar System exploration programs</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"col-md-4\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://imagecache.jpl.nasa.gov/images/640x350/PIA23491-16-640x350.jpg\"/>\n",
       "<div class=\"card-body\">\n",
       "<p class=\"card-text\">Access to the full library of publicly released images from various Solar System exploration programs</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"col-md-4\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://imagecache.jpl.nasa.gov/images/640x350/C1-PIA23180-16-640x350.gif\"/>\n",
       "<div class=\"card-body\">\n",
       "<p class=\"card-text\">Access to the full library of publicly released images from various Solar System exploration programs</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"footer\">\n",
       "<div class=\"container\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-3\">\n",
       "<h4>About JPL</h4>\n",
       "<ul>\n",
       "<li>About JPL</li>\n",
       "<li>JPL Vision</li>\n",
       "<li>Executive Council</li>\n",
       "<li>History</li>\n",
       "</ul>\n",
       "</div>\n",
       "<div class=\"col-md-3\">\n",
       "<h4>Education</h4>\n",
       "<ul>\n",
       "<li>Intern</li>\n",
       "<li>Learn</li>\n",
       "<li>Teach</li>\n",
       "<li>News</li>\n",
       "</ul>\n",
       "</div>\n",
       "<div class=\"col-md-3\">\n",
       "<h4>Our Sites</h4>\n",
       "<ul>\n",
       "<li>Asteroid Watch</li>\n",
       "<li>Basics of Spaceflight</li>\n",
       "<li>Cassini - Mission to Saturn</li>\n",
       "<li>Climate Kids</li>\n",
       "</ul>\n",
       "</div>\n",
       "<div class=\"col-md-3\">\n",
       "<h4>Galleries</h4>\n",
       "<ul>\n",
       "<li>JPL Space Images</li>\n",
       "<li>Videos</li>\n",
       "<li>Infographics</li>\n",
       "<li>Photojournal</li>\n",
       "</ul>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<!--<div class=\"showFullimage\">\n",
       "\t<button class=\"btn btn-outline-light hideimage\" onclick=hideimage()> Close</button>\n",
       "\t<img class=\"fullimage fade-in\" src=\"\">\n",
       "</div>-->\n",
       "<!-- <script src=\"js/jquery.easeScroll.js\"></script>  -->\n",
       "<script src=\"js/jquery-3.5.1.min.js\"></script>\n",
       "<!-- <script src=\"js/jquery-3.2.1.slim.min.js\"></script> -->\n",
       "<script src=\"js/demo.js\"></script>\n",
       "<!-- <script src=\"js/app.js\"></script> -->\n",
       "<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\"></script>\n",
       "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\"></script>\n",
       "<script src=\"js/fancyBox/jquery.fancybox.pack.js?v=2.1.5\" type=\"text/javascript\"></script>\n",
       "<link href=\"js/fancyBox/jquery.fancybox.css?v=2.1.5\" media=\"screen\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<link href=\"js/fancyBox/helpers/jquery.fancybox-thumbs.css?v=1.0.7\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<script src=\"js/fancyBox/helpers/jquery.fancybox-thumbs.js?v=1.0.7\" type=\"text/javascript\"></script>\n",
       "<div class=\"fancybox-overlay fancybox-overlay-fixed\" style=\"width: auto; height: auto; display: block;\"><div class=\"fancybox-wrap fancybox-desktop fancybox-type-image fancybox-opened\" style=\"width: 670px; height: auto; position: absolute; top: 209px; left: 309px; opacity: 1; overflow: visible;\" tabindex=\"-1\"><div class=\"fancybox-skin\" style=\"padding: 15px; width: auto; height: auto;\"><div class=\"fancybox-outer\"><div class=\"fancybox-inner\" style=\"overflow: visible; width: 640px; height: 350px;\"><img alt=\"\" class=\"fancybox-image\" src=\"image/featured/mars2.jpg\"/></div></div><a class=\"fancybox-item fancybox-close\" href=\"javascript:;\" title=\"Close\"></a></div></div></div></body></html>"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')\n",
    "img_soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base url to create an absolute url\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mars - Earth Comparison</td>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         0                1                2\n",
       "0  Mars - Earth Comparison             Mars            Earth\n",
       "1                Diameter:         6,779 km        12,742 km\n",
       "2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "3                   Moons:                2                1\n",
       "4       Distance from Sun:   227,943,824 km   149,598,262 km"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "Description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns=['Description', 'Mars', 'Earth']\n",
    "df.set_index('Description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>Description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<html lang=\"en\"><head>\n",
       "<link href=\"//ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<title>Astropedia Search Results | USGS Astrogeology Science Center</title>\n",
       "<meta content=\"USGS Astrogeology Science Center Astropedia search results.\" name=\"description\"/>\n",
       "<meta content=\"USGS,Astrogeology Science Center,Cartography,Geology,Space,Geological Survey,Mapping\" name=\"keywords\"/>\n",
       "<meta content=\"IE=edge\" http-equiv=\"X-UA-Compatible\"/>\n",
       "<meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\"/>\n",
       "<meta content=\"width=device-width, initial-scale=1, maximum-scale=1\" name=\"viewport\"/>\n",
       "<meta content=\"x61hXXVj7wtfBSNOPnTftajMsZ5yB2W-qRoyr7GtOKM\" name=\"google-site-verification\"/>\n",
       "<!--<link rel=\"stylesheet\" href=\"http://fonts.googleapis.com/css?family=Open+Sans:400italic,400,bold\"/>-->\n",
       "<link href=\"/css/main.css\" media=\"screen\" rel=\"stylesheet\"/>\n",
       "<link href=\"/css/print.css\" media=\"print\" rel=\"stylesheet\"/>\n",
       "<!--[if lt IE 9]>\n",
       "\t\t\t<script src=\"http://html5shiv.googlecode.com/svn/trunk/html5.js\"></script>\n",
       "\t\t\t<script src=\"/js/respond.min.js\"></script>\n",
       "\t\t\t<link rel=\"stylesheet\" type=\"text/css\" href=\"/css/ie.css\"/>\n",
       "                        <script>\n",
       "                          document.createElement('header');\n",
       "                          document.createElement('nav');\n",
       "                          document.createElement('section');\n",
       "                          document.createElement('article');\n",
       "                          document.createElement('aside');\n",
       "                          document.createElement('footer');\n",
       "                          document.createElement('hgroup');\n",
       "                        </script>\n",
       "                  <![endif]-->\n",
       "<link href=\"/favicon.ico\" rel=\"icon\" type=\"image/x-ico\"/>\n",
       "</head>\n",
       "<body id=\"results\">\n",
       "<header>\n",
       "<!--\n",
       "\t\t\t<h1>Astrogeology Science Center</h1>\n",
       "-->\n",
       "<a href=\"https://www.usgs.gov/centers/astrogeo-sc\" style=\"float:right;margin-top:10px;\" target=\"_blank\">\n",
       "<img alt=\"USGS: Science for a Changing World\" class=\"logo\" height=\"60\" src=\"/images/usgs_logo_main_2x.png\"/>\n",
       "</a>\n",
       "<a href=\"https://nasa.gov\" style=\"float:right;margin-top:5px;margin-right:20px;\" target=\"_blank\">\n",
       "<img alt=\"NASA\" class=\"logo\" height=\"65\" src=\"/images/logos/nasa-logo-web-med.png\"/>\n",
       "</a>\n",
       "<a href=\"https://www.usgs.gov/centers/astrogeology-science-center/science/pds-cartography-and-imaging-sciences-node-usgs\" style=\"float:right;margin-top:5px;margin-right: 10px;\" target=\"_blank\">\n",
       "<img alt=\"PDS Cartography and Imaging Science Node\" class=\"logo\" height=\"65\" src=\"/images/pds_logo-invisible-web.png\"/>\n",
       "</a>\n",
       "</header>\n",
       "<div class=\"wrapper\">\n",
       "<!--\n",
       "\t\t\t<nav>\n",
       "\t\t\t\t<a id=\"nav-toggle\" href=\"#\" title=\"Navigation Menu\">Menu</a>\n",
       "<ul class=\"dropdown dropdown-horizontal\" id=\"yw0\">\n",
       "<li><a href=\"/\">Home</a></li>\n",
       "<li><a href=\"/about\">About</a>\n",
       "<ul>\n",
       "<li><a href=\"/about/careers\">Careers</a></li>\n",
       "<li><a href=\"/contact\">Contact</a></li>\n",
       "<li><a href=\"/about/events\">Events</a></li>\n",
       "<li><a href=\"/site/glossary\">Glossary</a></li>\n",
       "<li><a href=\"/about/mission\">Mission</a></li>\n",
       "<li><a href=\"/news\">News</a></li>\n",
       "<li><a href=\"/people\">People</a></li>\n",
       "<li><a href=\"/about/using-our-images\">Using Our Images</a></li>\n",
       "<li><a href=\"/about/visitors\">Visitors</a></li>\n",
       "</ul>\n",
       "</li>\n",
       "<li><a href=\"/facilities\">Labs / Facilities</a>\n",
       "<ul>\n",
       "<li><a href=\"/facilities/flynn-creek-crater-sample-collection\">Flynn Creek Crater Sample Collection</a></li>\n",
       "<li><a href=\"http://www.moon-cal.org\">Lunar Calibration Project</a></li>\n",
       "<li><a href=\"/facilities/meteor-crater-sample-collection\">Meteor Crater Sample Collection</a></li>\n",
       "<li><a href=\"/facilities/mrctr\">MRCTR GIS Lab</a></li>\n",
       "<li><a href=\"/facilities/cartography-and-imaging-sciences-node-of-nasa-planetary-data-system\">PDS Cartography and Imaging Sciences Node</a></li>\n",
       "<li><a href=\"/pds/annex\">PDS IMG Annex</a></li>\n",
       "<li><a href=\"/facilities/photogrammetry-guest-facility\">Photogrammetry Guest Facility</a></li>\n",
       "<li><a href=\"/rpif\">Regional Planetary Information Facility (RPIF)</a></li>\n",
       "</ul>\n",
       "</li>\n",
       "<li><a href=\"/maps\">Maps / Products</a>\n",
       "<ul>\n",
       "<li><a href=\"/search\">Product Search</a></li>\n",
       "<li><a href=\"http://planetarynames.wr.usgs.gov\">Gazetteer of Planetary Nomenclature</a></li>\n",
       "<li><a href=\"http://planetarymapping.wr.usgs.gov\">Geologic Mapping Program</a></li>\n",
       "<li><a href=\"http://pilot.wr.usgs.gov\">Planetary Image Locator Tool (PILOT)</a></li>\n",
       "<li><a href=\"/search/planetary-index\">Planetary Map Index</a></li>\n",
       "</ul>\n",
       "</li>\n",
       "<li><a href=\"/geology\">Missions / Research</a>\n",
       "<ul>\n",
       "<li><a href=\"/geology/mars-dunes\">Mars Dunes</a></li>\n",
       "<li><a href=\"/geology/mars-ice\">Mars Ice</a></li>\n",
       "<li><a href=\"/missions\">Mission Support</a></li>\n",
       "<li><a href=\"/solar-system\">Solar System</a></li>\n",
       "<li><a href=\"/groups\">Working Groups</a></li>\n",
       "</ul>\n",
       "</li>\n",
       "<li><a href=\"/tools\">Tools</a>\n",
       "<ul>\n",
       "<li><a href=\"http://planetarynames.wr.usgs.gov\">Gazetteer of Planetary Nomenclature</a></li>\n",
       "<li><a href=\"http://isis.astrogeology.usgs.gov\">Integrated Software for Imagers and Spectrometers (ISIS)</a></li>\n",
       "<li><a href=\"http://astrogeology.usgs.gov/tools/map\">Map a Planet 2</a></li>\n",
       "<li><a href=\"http://pilot.wr.usgs.gov\">Planetary Image Locator Tool (PILOT)</a></li>\n",
       "<li><a href=\"http://astrocloud.wr.usgs.gov/\">Projection on the Web (POW)</a></li>\n",
       "</ul>\n",
       "</li>\n",
       "</ul>\t\t\t\t<form id=\"search\" class=\"search\" action=\"/search/results\" method=\"get\">\n",
       "\t\t\t\t\t<input type=\"submit\" value=\"\" title=\"Search Astropedia\"/>\n",
       "\t\t\t\t\t<input type=\"text\" placeholder=\"Search\" name=\"q\"/>\n",
       "\t\t\t\t</form>\n",
       "\t\t\t</nav>\n",
       "-->\n",
       "<div class=\"container\">\n",
       "<div class=\"widget block bar\">\n",
       "<a href=\"/search\" style=\"float:right;text-decoration:none;\">\n",
       "<img alt=\"Astropedia\" src=\"/images/astropedia/astropedia-logo-main.png\" style=\"width:200px;border:none;float:right;\"/>\n",
       "<div style=\"clear:both;font-size:.8em;float:right;color:#888;\">Lunar and Planetary Cartographic Catalog</div>\n",
       "</a>\n",
       "<div style=\"float:left;height:60px;\">\n",
       "</div>\n",
       "</div>\n",
       "<form action=\"/search/results\" class=\"bar widget block\" id=\"search-bar\">\n",
       "<input name=\"q\" type=\"hidden\" value=\"hemisphere-enhanced\"/>\n",
       "<input name=\"target\" type=\"hidden\" value=\"Mars\"/><input name=\"__ncforminfo\" type=\"hidden\" value=\"0ZUjA4RxaBd2fO2g_GlLySqkCIVm3Q9bqQOl6cYjPdTYvu3HR9Qi3ZWbt1DHSwCz7-DzTzee_lhJvvb8dLmpIeqjaE7M3mMj_xCdln4082XtVSWQOHjJ-g==\"/></form><div class=\"full-content\">\n",
       "<section class=\"block\" id=\"results-accordian\">\n",
       "<div class=\"result-list\" data-section=\"product\" id=\"product-section\">\n",
       "<div class=\"accordian\">\n",
       "<h2>Products</h2>\n",
       "<span class=\"count\">4 Results</span>\n",
       "<span class=\"collapse\">Collapse</span>\n",
       "</div>\n",
       "<div class=\"collapsible results\">\n",
       "<div class=\"item\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/cerberus_enhanced\"><img alt=\"Cerberus Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\"/></a><div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/cerberus_enhanced\"><h3>Cerberus Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 21 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Cerberus hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of 104 Viking Orbiter images acquired…</p></div> <!-- end description --></div><div class=\"item\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/schiaparelli_enhanced\"><img alt=\"Schiaparelli Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"/cache/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png\"/></a><div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/schiaparelli_enhanced\"><h3>Schiaparelli Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 35 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Schiaparelli hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The images were acquired in 1980 during early northern…</p></div> <!-- end description --></div><div class=\"item\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/syrtis_major_enhanced\"><img alt=\"Syrtis Major Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"/cache/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png\"/></a><div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/syrtis_major_enhanced\"><h3>Syrtis Major Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 25 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Syrtis Major hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of about 100 red and violet…</p></div> <!-- end description --></div><div class=\"item\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/valles_marineris_enhanced\"><img alt=\"Valles Marineris Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"/cache/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png\"/></a><div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/valles_marineris_enhanced\"><h3>Valles Marineris Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 27 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Valles Marineris hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The distance is 2500 kilometers from the surface of…</p></div> <!-- end description --></div><script>addBases=[];;if(typeof resetLayerSwitcher===\"function\"){resetLayerSwitcher(false)};var productTotal = 4;</script>\n",
       "</div> <!-- end this-section -->\n",
       "</div>\n",
       "</section>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"icons projects black scroll-wrapper\">\n",
       "<div class=\"scroll\">\n",
       "<a class=\"icon\" href=\"http://isis.astrogeology.usgs.gov\" title=\"Integrated Software for Imagers and Spectrometers\">\n",
       "<img alt=\"ISIS Logo\" height=\"112\" src=\"/images/logos/isis_2x.jpg\" width=\"112\"/>\n",
       "<span class=\"label\">ISIS</span>\n",
       "</a>\n",
       "<a class=\"icon\" href=\"http://planetarynames.wr.usgs.gov\" title=\"Gazetteer of Planetary Nomenclature\">\n",
       "<img alt=\"Nomenclature Logo\" height=\"112\" src=\"/images/logos/nomenclature_2x.jpg\" width=\"112\"/>\n",
       "<span class=\"label\">Planetary Nomenclature</span>\n",
       "</a>\n",
       "<a class=\"icon\" href=\"https://astrogeology.usgs.gov/tools/map-a-planet-2\" title=\"Map a Planet 2\">\n",
       "<img alt=\"Map-a-Planet Logo\" height=\"112\" src=\"/images/logos/map_a_planet_2x.jpg\" width=\"112\"/>\n",
       "<span class=\"label\">Map a Planet 2</span>\n",
       "</a>\n",
       "<a class=\"icon\" href=\"https://www.usgs.gov/centers/astrogeo-sc/science/cartography-and-imaging-sciences-node-nasa-planetary-data-system\" title=\"PDS Cartography and Imaging Science Node\">\n",
       "<img alt=\"PDS Logo\" height=\"112\" src=\"/images/pds_logo-black-web.png\"/>\n",
       "<span class=\"label\">PDS Cartography and Imaging Science Node</span>\n",
       "</a>\n",
       "<!--\n",
       "\t\t\t\t\t\t<a title=\"Astropedia Search\" href=\"/search\" class=\"icon\">\n",
       "\t\t\t\t\t\t\t<img alt=\"Astropedia Logo\" height=\"112\" width=\"112\" src=\"/images/logos/astropedia_2x.jpg\"/>\n",
       "\t\t\t\t\t\t\t<span class=\"label\">Astropedia</span>\n",
       "\t\t\t\t\t\t</a>\n",
       "-->\n",
       "<a class=\"icon\" href=\"https://www.usgs.gov/centers/astrogeo-sc/science/regional-planetary-image-facility-rpif\" title=\"Regional Planetary Image Facility\">\n",
       "<img alt=\"RPIF Logo\" height=\"112\" src=\"/images/logos/rpif_2x.jpg\" width=\"112\"/>\n",
       "<span class=\"label\">RPIF</span>\n",
       "</a>\n",
       "<a class=\"icon\" href=\"\" title=\"Photogrammetry Guest Facility\">\n",
       "<img alt=\"Photogrammetry Guest Faciltiy Logo\" height=\"112\" src=\"/images/logos/photogrammetry_2x.jpg\" width=\"112\"/>\n",
       "<span class=\"label\">Photogrammetry Guest Facility</span>\n",
       "</a>\n",
       "<a class=\"icon\" href=\"http://pilot.wr.usgs.gov\" title=\"Planetary Image Locator Tool\">\n",
       "<img alt=\"Pilot Logo\" height=\"112\" src=\"/images/logos/pilot_2x.jpg\" width=\"112\"/>\n",
       "<span class=\"label\">PILOT</span>\n",
       "</a>\n",
       "<a class=\"icon\" href=\"https://www.usgs.gov/centers/astrogeo-sc/science/mrctr-gis-lab\" title=\"Mapping, Remote-sensing, Cartography, Technology and Research GIS Lab\">\n",
       "<img alt=\"MRCTR GIS Lab Logo\" height=\"112\" src=\"/images/logos/mrctr_man_2x.png\" width=\"112\"/>\n",
       "<span class=\"label\">MRCTR GIS Lab</span>\n",
       "</a>\n",
       "</div>\n",
       "</div>\n",
       "<footer>\n",
       "<div class=\"left\">\n",
       "<a href=\"./search\">Search</a> |\n",
       "\t\t\t\t\t<a href=\"http://astrogeology.usgs.gov/maps/about\">About</a> |\n",
       "\t\t\t\t\t<a href=\"http://astrogeology.usgs.gov/maps/contact\">Contact</a>\n",
       "</div>\n",
       "<div class=\"right\">\n",
       "<a href=\"https://www.usgs.gov/centers/astrogeo-sc\">USGS Astrogeology Science Center</a>\n",
       "</div>\n",
       "</footer>\n",
       "</div>\n",
       "<!--\n",
       "\t\t<div class=\"credit\">\n",
       "\t\t\t<small>Background Credits: NASA/USGS</small>\n",
       "\t\t</div>\n",
       "-->\n",
       "<div class=\"page-background\" style=\"\n",
       "\t\t\tbackground:url('/images/backgrounds/mars.jpg');\n",
       "\t\t\tfilter:progid:DXImageTransform.Microsoft.AlphaImageLoader(\n",
       "\t\t\t\tsrc='/images/backgrounds/mars.jpg', sizingMethod='scale');\n",
       "\t\t\"></div>\n",
       "<script type=\"text/javascript\">\n",
       "var baseUrl = \"\";\n",
       "\n",
       "/*\n",
       "var _gaq = _gaq || [];_gaq.push(['_setAccount', 'UA-27613186-1']);_gaq.push(['_trackPageview']);(function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);})();\n",
       "*/\n",
       "\t\t</script>\n",
       "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js\" type=\"text/javascript\"></script>\n",
       "<script src=\"//ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js\" type=\"text/javascript\"></script>\n",
       "<script src=\"/js/general.js\" type=\"text/javascript\"></script>\n",
       "</body></html>"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "\n",
    "browser.visit(url)\n",
    "\n",
    "\n",
    "html = browser.html\n",
    "ssoup = soup(html, 'html.parser')\n",
    "ssoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n",
    "img_pages = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "for x in ssoup.find_all('a',class_='itemLink product-item'):\n",
    "    url_img = 'https://astrogeology.usgs.gov'+x.get(\"href\")\n",
    "    if url_img not in img_pages:\n",
    "        img_pages.append(url_img)\n",
    "for address in img_pages:\n",
    "    browser.visit(address)\n",
    "    a = browser.html\n",
    "    a = soup(a,'html.parser')\n",
    "    hemisphere_image_urls.append({'img_url':a.find('a',target='_blank',string=\"Sample\").get('href'),'title':a.find('h2',class_='title').string})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "nteract": {
   "version": "0.15.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
