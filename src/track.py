import re

disallowed_title_regex = r'[\/:*?"<>|]'


def parse_title(name, artist):
    title = name + ' - ' + artist
    return re.sub(disallowed_title_regex, '_', title)
