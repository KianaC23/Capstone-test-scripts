import os
import datetime
import requests
import pandas as pd
from requests_html import HTML

now= datetime.datetime.now()
year = now.year


url = "https://www.blackclassicmovies.com/movies-database/action/"
# url_to_txt(url,headers=headers)

#open up webpage
def url_to_txt(url, filename="blkclassix.html", save ="False"):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    r = requests.get(url, headers=headers)
    #did we open successfully?
    print(f"Page status: {r.status_code}")
    # if successful save html to a new file locally
    if r.status_code ==200:
         html_text = r.text
         #can add year to file name
         with open(f"blkclassix-{year}.html",'w') as f:
           f.write(html_text)
         return html_text
    return""
url_to_txt(url)

def parse_and_extract(url, name = '2021'):

    html_text = url_to_txt(url)

    r_html = HTML(html=html_text)
    table_class = '.main-content'
    r_table = r_html.find(table_class)
    print(r_table)
    # table_data =[]
    # #check if there is text, if so pull this info
    # if len(r_table) == 1:
    #     # print(r_table[0].text)
    #     parsed_table = r_table[0]
    #     rows = parsed_table.find("tr") 
    #     header_row = rows[0]
    #     header_cols = header_row.find("th")
    #     header_names = [x.text for x in header_cols]
        
    #     # iterate through the rows and print
    #     for row in rows[1:]:
    #         # print(row.text)
    #         cols = row.find("td")
    #         row_data = []
    #         #iterate through coulmn info 
    #         for i, col in enumerate(cols):
    #             # print(i, col.text, '\n\n')
                
    #             header_name = header_names[i]
    #             row_data.append(col.text)
    #         table_data.append(row_data)
        
    #     #create data folder and save data to csv files    
    #     df = pd.DataFrame(table_data, columns = header_names)
    #     path = os.path.join(BASE_DIR, 'data1')
    #     os.makedirs(path, exist_ok = True)
    #     filepath = os.path.join('data1', f'{name}.csv')
    #     df.to_csv(filepath, index=False)
    #         # does the same thing as 
            # i=0
            # for x in row:
            #   i+=1
            #print(i,x)
# print(header_names)
# print(table_data)