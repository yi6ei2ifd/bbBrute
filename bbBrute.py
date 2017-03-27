# coding:utf-8

import requests
from optparse import OptionParser


"""
1. https支持不足
2. 反爬虫机制引入
3. 队列 占用内存
4. 包装成一个类
5. 输出美化 颜色
6. 检查waf

"""

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Referer': 'https://www.google.com.hk'
}


def brute(base_url, file_list):

    url = ''
    for i in file_list:
        url = base_url + i
        req = requests.get(
            url=url, headers=header, allow_redirects=False, verify=False, timeout=60)
        try:
            req.raise_for_status()
        except requests.exceptions.HTTPError as e:
            continue
        if req.status_code == 200:
            print("[200]", url)
        if req.status_code == 403:
            print("[403]".url)


def main():
    parser = OptionParser(
        "Usage:    ./bbBrute.py [options]\nExample:  ./bbBrute.py -q -t 20 -u www.xxx.com")
    parser.add_option(
        "-t", "--thread", type="int", dest="thread", help="the number of thread")
    parser.add_option("-q", "--quiet", action="store_false",
                      dest="quiet", default=True, help="print simply")
    parser.add_option("-u", "--url", dest="url", help="target url")
    (options, args) = parser.parse_args()

    base_url = options.url
    if base_url == None:
        parser.print_help()
        return
    if not base_url.startswith('http://') and not base_url.startswith('https://'):
        base_url = 'http://' + base_url

    file_list = []
    with open('dic/PHP.txt', 'r') as fo:
        for line in fo.readlines():
            line = line.strip('\n').strip(' ')
            file_list.append(line)

    if not options.quiet:
        print('''
                ##############################
                #                            #
                #           bbBrute v1.0     #
                #                            #
                ##############################
            ''')

    # brute(base_url,file_list)


if __name__ == '__main__':
    main()
