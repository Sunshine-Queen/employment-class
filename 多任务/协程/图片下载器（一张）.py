import urllib.request

def main():
    req=urllib.request.urlopen("http://pic24.nipic.com/20120922/10614245_073225718000_2.jpg")
    img_content=req.read()

    with open("1.jpg","wb")as f:
        f.write(img_content)

if __name__ == '__main__':
    main()