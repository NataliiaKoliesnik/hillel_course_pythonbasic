# function for cleaning text from html tags

def delete_html_tags(html_file: str, result_file: str ='cleaned.txt') -> None:
    '''
    Remove HTML tags from a file and save cleaned text to a new file.
    :param html_file: Source HTML file.
    :param result_file: Output text file.
    :return: None
    '''
    import re
    with open(html_file, 'r', encoding ='utf-8') as file:
        html_text = file.read()
    # performs a search for an html tag and replaces it with an empty string
    html_text = re.sub(r'</?[^>]+>', '', html_text)
    with open(result_file, 'w', encoding ='utf-8') as file:
        for line in html_text.splitlines(): # splitting the resulting text into lines
            if line.strip():
                # removing extra spaces and tabs from the left; writing records line by line to a new file
                file.write(line.lstrip() +'\n')

delete_html_tags('draft.html')