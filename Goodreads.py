#Import packages here
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

#Input ISBN here, try 9780140187014 as the input
isbn = input("Input the ISBN here: ");

#Key function here
def get_goodreads_info(isbn):

    #Basic URL here
    URL = "https://www.goodreads.com/book/isbn/";

    #Concatenate strings
    fullURL = URL + isbn;

    page = requests.get(fullURL);
   
    #Start collecting data
    soup = BeautifulSoup(page.content, 'html.parser');

    #Key data
    data = [];

    #Obtain key details
    #Title
    book_title = soup.find(itemprop="name");
    data.append(book_title.text.strip());
    #Series
    book_Series = soup.find(itemprop="bookSeries");
    try:
        data.append(book_Series.text.strip());
    except:
        data.append(None);
    #Author
    book_author = soup.find(class_="authorName");
    data.append(book_author.text.strip());
    #Rating
    rating_value = soup.find(itemprop="ratingValue");
    data.append(rating_value.text.strip());
    #Genre
    main_genre = soup.find(class_="actionLinkLite bookPageGenreLink");
    data.append(main_genre.text.strip());

    #Convert to a Pandas dataframe (via numpy)
    numpy_array = np.array(data);
    df = pd.DataFrame(numpy_array, columns = ["Data"], index = ["Book Title", "Book Series", "Author", "Rating", "Genre"]);
    return df


#Call function
key_book_data = get_goodreads_info(isbn)
print(key_book_data)
