from django.shortcuts import render
import os, shutil, subprocess, requests, datetime, json
from werkzeug.utils import secure_filename
from django.http import HttpResponseRedirect,FileResponse, HttpResponse, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from .forms import UploadDocumentForm
from django.core.files.storage import FileSystemStorage
from django import get_version
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
API_KEY = getattr(settings, 'API_KEY')

date = str(datetime.date.today().month) + '-' + str(datetime.date.today().day)
# Create your views here.

now = datetime.datetime.now()
nowTuple = now.timetuple()
# 매일 23시에 실행되도록, 근데 될려나.?
if nowTuple.tm_hour == 23:
    f = open("media/db/Visitor.txt", "a")
    txt = date + ' ' + str(g_number_of_visitor[date]) + '\n'
    f.write(txt)
    f.close()

    f = open("media/db/Filenum.txt", "a")
    txt = date + ' ' + str(g_number_of_visitor[date]) + '\n'
    f.write(txt)
    f.close()

g_number_of_visitor = dict()
g_number_of_file = dict()

fv = open("media/db/Visitor.txt", "r")
ff = open("media/db/Filenum.txt","r")
while True:
    vline = fv.readline()
    fline = ff.readline()
    if not vline: break
    if not fline: break
    for i in range(len(vline)):
        if vline[i] == ' ':
            date = vline[:i]
            num = int(vline[i+1:-1])
            g_number_of_visitor[date] = num

    for j in range(len(fline)):
        if fline[j] == ' ':
            date = fline[:j]
            num = int(fline[j+1:-1])
            g_number_of_file[date] = num
fv.close()
ff.close()

print(g_number_of_visitor)
print(g_number_of_file)
def index(request):
    global g_number_of_visitor, g_number_of_file,date
    if g_number_of_visitor.get(date): #해당 날짜의 기록이 존재하면
        g_number_of_visitor[date] += 1
    else:
        g_number_of_visitor[date] = 1

    if not g_number_of_file.get(date):
        tmp = list(g_number_of_file.values())
        g_number_of_file[date] = tmp[len(tmp)-1]

    folder = 'media/my_folder/'
    if request.method=='POST' and request.FILES['inputFile']:
        if g_number_of_file.get(date):  # 해당 날짜의 기록이 존재하면
            g_number_of_file[date] += 1
        else:
            if len(g_number_of_file) == 0:
                g_number_of_file[date] = 1
            else:
                temp = list(g_number_of_file.values())
                g_number_of_file[date] = temp[len(temp) - 1] + 1  # 누적

        myfile = request.FILES['inputFile']

        fn_rm = 'media/my_folder/safe-output-compressed.pdf'
        if os.path.isfile(fn_rm):
            os.remove(fn_rm)
            print('existed file is deleted')

#        fn_json = 'media/my_folder/virustotal-output.json'
#        if os.path.isfile(fn_json):
#            os.remove(fn_json)
#            print('json file is deleted')

        filelist = list()
        mydir = '/tmp/dangerzone-pixel'
        for f in os.listdir(mydir):
            if f.endswith(".height") or f.endswith(".rgb") or f.endswith(".width"):
                filelist.append(f)
        for f in filelist:
            os.remove(os.path.join(mydir, f))

        fs = FileSystemStorage(location=folder)
        fs.save(myfile.name, myfile)
        filename = myfile.name
        print("파일명", filename)
        os.rename('media/my_folder/' + filename, 'media/my_folder/inputFile.pdf')
        path = '/home/ubuntu/ubuntu-dev/media/my_folder/'
        #path = '/home/ubuntu/hanium-dangerzone-opensource/media/my_folder/'
        uploadpath = " " + path + "inputFile.pdf "
        virustotal_resource_id = virustotal_upload(uploadpath)
        subprocess.call(["/usr/bin/dangerzone-container" " documenttopixels --document-filename" + uploadpath + "--pixel-dir /tmp/dangerzone-pixel --container-name flmcode/dangerzone"],shell=True)
        subprocess.call(["/usr/bin/dangerzone-container" " pixelstopdf --pixel-dir /tmp/dangerzone-pixel --safe-dir /tmp/dangerzone-safe --container-name flmcode/dangerzone --ocr 0 --ocr-lang eng"],shell=True)
        #os.rename("/tmp/dangerzone-safe/safe-output-compressed.pdf",
                  # "/tmp/dangerzone-safe/" + filename + "_" + "safe-output.pdf")
        file_url = '/tmp/dangerzone-safe/safe-output-compressed.pdf'
        dest_url = path + 'safe-output-compressed.pdf'
        shutil.move(file_url, dest_url)
        rm_file = 'media/my_folder/inputFile.pdf'
        if os.path.isfile(rm_file):
            os.remove(rm_file)
            print(rm_file,"is deleted")
        # return render(request, 'fileupload.html', {'file_url': file_url})
        jn = path + 'virustotal-output.json'
        # jn = 'safe.json'
        virustotal_download(virustotal_resource_id,jn)
        jn = 'virustotal-output.json'
        return viruschart(request,jn)
    else:
        return render(request, 'index.html')

def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'my_folder/safe-output-compressed.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="safe.pdf"'
            return response
    else:
        return HttpResponseNotFound('Not Found!!!')

@csrf_exempt
def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    total_num_of_visitor_label = list(g_number_of_visitor.keys())
    total_num_of_file_label = list(g_number_of_file.keys())
    total_num_of_visitor = list(g_number_of_visitor.values())
    total_num_of_file = list(g_number_of_file.values())
    print(total_num_of_file,total_num_of_visitor)
    return render(request, 'dashboard.html',{'cnt':g_number_of_visitor[date],
                                             'file_cnt': g_number_of_file[date],
                                             'visitor_data':total_num_of_visitor,
                                             'file_data':total_num_of_file,
                                             'visitor_label': total_num_of_visitor_label,
                                             'file_label': total_num_of_file_label
                                             } )

def fileupload(request):
    return render(request,'fileupload.html')

def detection(request):
    return render(request, 'detection.html')

@csrf_exempt
def sendmail(request):
    return render(request,'sendmail.html')

def virustotal_upload(orgfile):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': API_KEY }
    files = {'file': "'" + orgfile + "'"}
    response = requests.post(url, files=files, params=params)
    return response.json()['resource']


def virustotal_download(resource_id, filename):
    fs = FileSystemStorage()
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': API_KEY, 'resource': resource_id}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)

    if not fs.exists(filename):
        with fs.open(filename, 'w') as json_file:
            json.dump(response.json(), json_file, indent=4, sort_keys=True)

def viruschart(request, jn):
    filename = 'media/my_folder/'+jn
    filename_default = 'media/my_folder/safe.json' 
    json_data = ''


    with open(filename_default,'r') as f:
        json_data = json.load(f)
        if 'scans' in json_data.keys():
            json_data = json_data['scans']
        else:
            return pdf_view(request)

        res = list()
        #json_data = json.dumps(json_data)

        for key, val in json_data.items():
            res.append([key, val['detected']])

    if json_data == '':
        HttpResponseNotFound('NOT FOUND')
    return render(request, 'detection.html', context = {'data':res})

