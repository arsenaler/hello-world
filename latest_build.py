


import requests
import sys, os, time

#os.popen('touch build.txt')
#os.system("touch build_time.txt")
class test_get_latest_build(object):
    def __init__(self):
        self.url = "http://10.8.255.103/firmware/"
        self.t2 = "2017-"
        self.lst = []
        self.lst1 = []
        self.dict_build_info = {}
        self.dict_build_info1 = {}
    def test_get_all_build(self):
        content = requests.get(self.url).content
        try:
            file1= open("build.txt",'w')
            file1.write(content)
        except Exception as e:
            print('unexpect error happen')
        finally:
            file1.close()
        with open('build.txt') as f:
            for line in f:
                if self.t2 in line:
                    t1 = line.split('right">')[1].split("  ")[0]
                    build1 = line.split('<a')[1].split('"')[1]
                    self.lst.append(build1)
                    self.dict_build_info[build1] = t1
        print self.dict_build_info
        return self.dict_build_info
    def test_get_all_build1(self):
        self.lst1 = [i.rstrip('/').split('-')[-1] for i in self.lst]
        self.dict_build_info1 = {key.rstrip('/').split('-')[-1]:value for key, value in self.dict_build_info.iteritems()}
        return self.dict_build_info1
    def test_latest_build(self):

        return max(self.test_get_all_build(), key=self.test_get_all_build().get)

    def test_latest_build1(self):
        return max(self.test_get_all_build1(), key=self.test_get_all_build1().get)

    def test_download_latest_build(self):
        url_web = self.url + self.test_latest_build() + "webServer-" + self.test_latest_build1() + '.tar.gz'
        url_sonicos = self.url + self.test_latest_build() + "sonicos-" + self.test_latest_build1() + '.tar.gz'

        os.system('wget %s' %url_web)
        os.popen("wget %s" %url_sonicos)
        time.sleep(2)

    def test_tar_latest_build(self):
        web = "webServer-" + self.test_latest_build1() + '.tar.gz'
        sonicos = "sonicos-" + self.test_latest_build1() + '.tar.gz'
        os.system("tar zxvf %s" %sonicos)
        os.system("tar zxvf %s" %web)

    def test_backup_build(self):
        latest_build1 = self.test_latest_build1()
        date11 = self.dict_build_info1[latest_build1]
        date1 = date11.split(' ')[0]
        time.sleep(1)
        date2 = date1.replace('-', '')
        os.system("ls old_build | awk -F - '{print $2 $3 $4}'>build_time.txt")
        lst_time = lst1_time =[]
        with open('build_time.txt') as f:
            for line in f:
                lst_time.append(line)
        lst1_time = [i.strip('\n') for i in lst_time]

        if date2 in lst1_time:
            pass
        else:
            os.system("cp -ir sonicos old_build/sonicos-%s" %date1)
            os.system("cp -ir webServer old_build/webServer-%s" %date1)
    def test_add_gdb(self):
        os.system("sed -i 's/LD_LIBRARY_PATH=\".\/lib\" .\/packet-engine/LD_LIBRARY_PATH=\".\/lib\" gdb .\/packet-engine/g' sonicos/scripts/run.sh")
    def test_delete_old_build(self):
        os.system('./delete_old_build.sh')


