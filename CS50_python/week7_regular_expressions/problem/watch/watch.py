
# Watch on YouTube
# parse url and modify, shorter him
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'youtube.com/embed/(.+?)"', s):
        url = 'https://youtu.be/' + match.group(1)
        return url
    return None


if __name__ == "__main__":
    main()
