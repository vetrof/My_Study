
# simple generator search link for imdb
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

import webbrowser

# get user parameter search
genres = '&genres=' + input('genres: ')
rating = '&user_rating=' + input('rating: ') + ','
votes_min = '&num_votes=' + input('votes min: ') + ','
keywords = '&keywords=' + input('keywords: ')

# ////////////////////////////
# temp test search area /
# genres_user = 'crime,mystery'
# rating_user = '7'
# votes_min_user = '5000'
# keyword_user = ''
# \temp test search area
# ///////////////////////////

# create value
base_link = 'https://www.imdb.com/search/title/?'
title = '&title='
title_type = '&title_type=' + 'feature'

view = '&view=simple'
count = '&count=250'


# create search link
search_link = base_link\
              + votes_min\
              + keywords\
              + rating\
              + genres\
              + view\
              + count

print(search_link)

webbrowser.open(search_link)



