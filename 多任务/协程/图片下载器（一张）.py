import urllib.request

def main():
    req=urllib.request.urlopen("")
    img_content=req.read()

    with open("1.jpg","wb")as f:
        f.write(img_content)

if __name__ == '__main__':
    main()