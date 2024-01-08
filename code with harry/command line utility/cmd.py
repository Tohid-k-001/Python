import argparse
import requests

def download_file(url,local_filename):
    local_filename=url.split("/")[-1]        #--> It will print the name of downloaded file which is at the last [-1]
    #note the stream true parameter below
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                    # if you have chunk encoded response uncomment if
                    # and set chunk_size parameter to none .
                    # if chunk:
                f.write(chunk)
    return local_filename
parser=argparse.ArgumentParser()

# add command line argument
parser.add_argument("url",help="url of the file to download")
parser.add_argument("output",help="by which name do you want save your file")

#parser the arguments
args= parser.parse_args()

#use the arguments in your code
print(args.url)
print(args.output)
download_file(args.url,args.output)
