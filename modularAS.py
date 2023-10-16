
from bs4 import BeautifulSoup
import csv
import re
import random

def read_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return html_content
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def extract_title(soup):
    title_element = soup.find('title')
    title = title_element.text.strip()
    title = re.sub(r'\[\d+\.\d+\]', '', title)
    return title

def remove_nested_spans(element):
    for span in element.find_all('span'):
        span.extract()
def extract_author_names(soup):
    author_names = "None"  # Initialize with a default value

    author_tag = soup.find('div', class_='ltx_authors')

    if author_tag:
        author_names_element = soup.find('span', class_='ltx_creator ltx_role_author')
    else:
        author_names = "None"

    if author_names == "None":
        author_name_elements = soup.find_all('span', class_='ltx_personname')

        author_names = []
        for element in author_name_elements:
            # Remove nested span tags and their content
            remove_nested_spans(element)

            name_text = element.get_text(strip=True)

            # Replace numbers and some characters
            name_text = re.sub(r'[^a-zA-Z, ]', '', name_text)

            # Remove a single character between two spaces
            name_text = ' '.join(word for word in name_text.split() if len(word) != 1 or word == ',' or word.isdigit())

            author_names.append(name_text)

        author_names = ', '.join(author_names)

    return author_names

def extract_author_email(soup):
    author_email_element = soup.find('span', class_='ltx_creator ltx_role_author')

    if author_email_element:
        author_email = author_email_element.find('span', class_='ltx_role_email')
        if author_email:
            author_email = author_email.get_text(strip=True)
        else:
            author_email = "None"
    else:
        email_elements = soup.find_all("span", class_=['ltx_role_email', 'ltx_author_notes', 'ltx_text ltx_notes'])
        author_email = [email.text.strip() for email in email_elements]
        author_email = ''.join(author_email)

    return author_email


def extract_author_address(soup):
    # Search for an address element within known HTML tags
    address_tags = ['p', 'div', 'span']
    address_classes = ['ltx_contact ltx_role_address', 'ltx_author_affiliation']

    for tag in address_tags:
        for class_name in address_classes:
            address_element = soup.find(tag, class_=class_name)
            if address_element:
                author_address = address_element.get_text(strip=True)
                # Truncate the address to a maximum of 200 characters
                return author_address[:200] if len(author_address) > 200 else author_address

    return "None"  # Return "None" if no address is found
def extract_abstract(soup):
    abstract_element = soup.find('div', class_='ltx_abstract')
    if abstract_element:
        abstract_p = abstract_element.find('p', class_='ltx_para')
        if not abstract_p:
            abstract_p = abstract_element.find('p', class_='ltx_p')
        if abstract_p:
            abstract = abstract_p.text.strip()
            words = abstract.split()
            abstract = ' '.join(words)
            return abstract
    return None

def extract_keywords(soup):
    keywords_element = soup.find('div', class_='ltx_section ltx_keywords')
    if keywords_element:
        keyword_elements = keywords_element.find_all('span', class_='ltx_text')
        keywords = [element.get_text() for element in keyword_elements]
        return ', '.join(keywords)
    else:
        return None


def process_html_file(file_path):
    html_content = read_html_file(file_path)
    if html_content is not None:
        soup = BeautifulSoup(html_content, 'html.parser')
        title = extract_title(soup)
        author_names = extract_author_names(soup)
        author_email = extract_author_email(soup)
        author_address = extract_author_address(soup)
        abstract = extract_abstract(soup)
        keywords = extract_keywords(soup)
        return title, author_names, author_email, author_address, abstract, keywords
    return None, None, None, None, None, None

def randomnumber(a,b):
    random_number = random.randint(a, b)
    formatted_random_number = f"{random_number:02}"
    return formatted_random_number
def save_paper_data(paper_data,data_files):
    # Save the paper data to multiple TSV files for redundancy
    for file_path in data_files:
        with open(file_path, 'a', newline='') as tsv_file:
            tsv_writer = csv.DictWriter(tsv_file, fieldnames=paper_data.keys(), delimiter='\t')
            if tsv_file.tell() == 0:
                tsv_writer.writeheader()
            tsv_writer.writerow(paper_data)


def main():
            # Create a dictionary to represent the paper data
            paper_data = {
                'Title': [],
                'Author Names': [],
                'Author Email': [],
                'Author Address': [],
                'Abstract': [],
                'Keywords': []
            }
            for i in range(2201, 2400):
                #r_number = random.randint(0,2427)
                formatted_number = f"{i:04}"
                file_path = "/Users/rey/documents/database/Assignments/01/2101.1"+formatted_number+".html"
                title, author_names, author_email, author_address, abstract, keywords = process_html_file(file_path)

                paper_data['Title']=title
                paper_data['Author Names']=author_names
                paper_data['Author Email']=author_email
                paper_data['Author Address']=author_address
                paper_data['Abstract']=abstract
                paper_data['Keywords']=keywords
                # Define a list of file paths for redundancy
                data_files = ["data_file1.tsv"]#, "data_file2.tsv", "data_file3.tsv", "data_file4.tsv"]
                save_paper_data(paper_data,data_files)

if __name__ == "__main__":
    main()