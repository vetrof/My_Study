
# simple generator search link for imdb
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

# get user parameter search
# genres_user = input('genres: ')
# rating_user = input('rating: ')
# votes_min_user = input('votes min: ')
# keyword_user = input('keywords: ')

# temp test search area /
# ////////////////////////////
genres_user = 'crime,mystery'
rating_user = '7'
votes_min_user = '1000'
keyword_user = ''
# ///////////////////////////
# \temp test search area

# create value
base_link = 'https://www.imdb.com/search/title/?'
title = '&title='
title_type = '&title_type=' + 'feature'
votes_min = '&num_votes=' + votes_min_user + ','
user_rating_min = '&user_rating=' + rating_user + ','
genres = '&genres=' + genres_user
keywords = '&keywords=' + keyword_user
view = '&view=simple'
count = '&count=250'


# create search link
search_link = base_link + votes_min + keywords + user_rating_min + genres + view + count

print(search_link)







