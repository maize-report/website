import sys, re
import datetime

def write_article_html(article_output_filename, article_title, article_text, article_image_link):
    """
    Write the webpage html for an article. This doesn't edit the index.html webpage.

    Keyword args:
        article_output_filename - str -- filename of webpage html to output, don't add the '.html' file extension as this function adds it for you, EX: "thicc-alma"
        article_title - str -- title of the article, EX: "Beloved Illinois Sculpture ‘Alma Mater’ Gets Resculpted To Be “Stoopid Thícc”"
        article_text - str -- the body of the article
        article_image_link - str -- the relative link to the image for the article, EX: "images/thicc-alma.png"

    """
    wrapper = """
    <!DOCTYPE HTML>
<!--
    The Maize Report by Pixelarity
    pixelarity.com | hello@pixelarity.com
    License: pixelarity.com/license
-->
<html>
    <head>
        <title>{title}</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="assets/css/main.css" />
    </head>
    <body class="is-preload">

        <!-- Wrapper -->
            <div id="wrapper">

                <!-- Header -->
                        <header id="header">
                            <h1><a href="index.html"><img src="images/cornyboi.png" style="height:3em; vertical-align: middle;">The Maize Report</a></h1>
                            <nav class="links">
                                <ul>
                                    <li><a href="#">Blog</a></li>
                                    <li><a href="#">About Us</a></li>
                                    <!-- <li><a href="#">Tempus</a></li>
                                    <li><a href="#">Adipiscing</a></li> -->
                                </ul>
                            </nav>
                            <nav class="main">
                                <ul>
                                    <!-- <li class="search">
                                        <a class="fa-search" href="#search">Search</a>
                                        <form id="search" method="get" action="#">
                                            <input type="text" name="query" placeholder="Search" />
                                        </form>
                                    </li> -->
                                    <!-- <li class="menu">
                                        <a class="fa-bars" href="#menu">Menu</a>
                                    </li> -->
                                </ul>
                            </nav>
                        </header>

                <!-- Menu -->
                    

                <!-- Main -->
                    <div id="main">

                        <!-- Post -->
                            <article class="post">
                                <header>
                                    <div class="title">
                                        <h2><a href="#">{title}</a></h2>
                                        
                                    </div>
                                    <div class="meta">
                                        <time class="published" datetime="2015-11-01">{date}</time>
                                    </div>
                                </header>
                                <span class="image featured"><img src="{image_link}" alt="" /></span>
                                <br>
                                {text}
                                <footer>
                                    <ul class="stats">
                                        <li><a href="#">Blog</a></li>
                                    </ul>
                                </footer>
                            </article>

                            <section id="footer">
                                <ul class="icons">
                                    
                                    <li><a href="https://www.facebook.com/The-Maize-Report-461820147645627/" class="fa-facebook"><span class="label">Facebook</span></a></li>
                                    <li><a href="mailto:maizereport@gmail.com" class="fa-envelope"><span class="label">Email</span></a></li>
                                </ul>
                                <p class="copyright">&copy; The Maize Report 2018.</p>
                            </section>

                    </div>

                <!-- Footer -->
                    

            </div>

        <!-- Scripts -->
            <script src="assets/js/jquery.min.js"></script>
            <script src="assets/js/browser.min.js"></script>
            <script src="assets/js/breakpoints.min.js"></script>
            <script src="assets/js/util.js"></script>
            <script src="assets/js/main.js"></script>

    </body>
</html>
    """

    today_string = datetime.datetime.strftime(datetime.datetime.today(), '%b %d, %Y')

    text_with_html = re.sub(r'(.+?)(\n|$)+', r'<p>\1</p>\n\n', article_text)

    whole = wrapper.format(title=article_title, date=today_string, image_link=article_image_link, text=text_with_html)

    HTML_FILE_EXTENSION = '.html'

    with open(article_output_filename + HTML_FILE_EXTENSION, 'w') as output_file:
        output_file.write(whole)

if __name__ == "__main__":

    USAGE_PRINTOUT = "Usage: python write_article_html.py {ARTICLE_FILENAME}"
    if len(sys.argv) != 2:
        print(USAGE_PRINTOUT)
        exit()

    article_filename = sys.argv[1]

    with open(article_filename) as file:
        data = file.read()

        write_article_html(article_output_filename="thicc-alma", article_title="Thicc Alma", article_text=data, article_image_link="images/thicc-alma.png")
        


