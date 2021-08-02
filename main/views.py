from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
from .models import history
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import Post
from django.http import HttpResponse
# import pyotp
# import shutil
# import qrcode
# import cv2
# import pyzbar.pyzbar as pyzbar
# import webbrowser
# from itertools import chain
import datetime
from django.contrib import messages
import requests     #카톡


# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)
        
        if user is not None:
            print("성공")
            login(request, user)
            
            response = render(request, 'main/login.html')
            response.set_cookie('username',username)
            response.set_cookie('password',password)

            return response

        else:
            print("실패")

    return render(request, "main/login.html")



def logout_view(request):
    # logout(request)
    # return redirect("login")
    #로그아웃할 때 otpdata 0으로 만들기

    response = render(request, 'main/logout.html')
    response.delete_cookie('username')
    response.delete_cookie('password')
    logout(request)
    return response


def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        korname = request.POST["korname"]
        username = request.POST["username"]
        password = request.POST["password"]
        phonenum = request.POST["phonenum"]
        auth = request.POST["auth"]
        email = request.POST["email"]

        user = User.objects.create_user(username,email,password)
        user.korname = korname
        user.phonenum = phonenum
        user.auth = auth
        user.save()
        return redirect("login")

    return render(request, "main/signup.html")

def first_intro(request):
    return render(request, 'main/first_intro.html')

def second_my(request):
    username = request.COOKIES.get('username')
    dbsee = User.objects.get(username=username)
    korname = dbsee.korname
    phonenum = dbsee.phonenum
    userpoint = dbsee.userpoint
    auth = dbsee.auth

    # 참여횟수 이벤트 위한 코드
    usenums = dbsee.usenums
    forevent = dbsee.forevent


    return render(request, 'main/second_my.html',{'username':username, 'korname':korname, 'usenums':usenums, 'phonenum':phonenum, 'userpoint': userpoint, 'forevent': forevent, 'auth': auth})

def third_pchange(request):
    username = request.COOKIES.get('username')
    dbsee = User.objects.get(username=username)
    userpoint = dbsee.userpoint

    def merge_list(*args, fill_value = None):
        max_length = max([len(lst) for lst in args])
        merged = []
        for i in range(max_length):
            merged.append([
            args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
            ])
        return merged

    snamelist = User.objects.filter(auth='store').values_list('korname', flat=True)
    spnumlist = User.objects.filter(auth='store').values_list('phonenum', flat=True)
    combined_list = merge_list(snamelist, spnumlist)


    if request.method == "POST":
        pointzero = User.objects.get(username=username)
        pointzero.userpoint = 0
        pointzero.save()

        #history에 포인트 사용내역 저장

        
        
        now = datetime.datetime.now()
        nowdate = now.strftime('%Y-%m-%d %H:%M:%S')

        history.objects.create(
            u_id = username,
            s_id = "지역화폐로 전환",
            nowpoint = 0,
            h_date = nowdate,
        )



        

        return render(request, 'main/intozero.html')

    return render(request, 'main/third_pchange.html',{'username':username, 'userpoint': userpoint, 'snamelist': snamelist, 'spnumlist': spnumlist, 'combined_list':combined_list})

def storelogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)
        if user is not None:
            print("성공")
            login(request, user)
        else:
            print("실패")

    return render(request, "main/storelogin.html")

def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'main/blog.html', {'postlist':postlist})


# def otpmake(request):
#     totp = pyotp.TOTP('GAYDAMBQGAYDAMBQGAYDAMBQGA======', 10)  # 180초 간격, 즉 3분마다 변경됨
#     # totp = pyotp.TOTP('base32secret3232', 10)
#     otpvalue = totp.now()
#     otpvalue = str(otpvalue)            #잘리는 것 같아서 str으로 변환함!!!!!!!!!!!!!!!
    
#     user = request.COOKIES.get('username')
#     update = User.objects.get(username=user)
#     update.otpdata = otpvalue
#     update.save()

#     return render(request,'main/otpmake.html',{'otpvalue':otpvalue})

# def otpcheck(request):
#     if request.method == "POST":
#         getotp = request.POST["getotp"]

#         userotp = User.objects.values_list('otpdata', flat=True)



#         for a in userotp:
#             b=str(a)

#             if b == getotp:
#                 pointplus = User.objects.get(otpdata=a)
#                 pointplus.userpoint += 3000
#                 pointplus.usenums +=1
#                 pointplus.save()

#                 return HttpResponse("포인트적립 성공")
#             else:
#                 return HttpResponse("실패")
        
#     return render(request, 'main/otpcheck.html')

# def otpreader(request):
#     #cap = cv2.imread(0)

#     cap = cv2.VideoCapture(0)

#     num = 0

#     while True:
#         success, frame = cap.read()

#         if success:
#             for code in pyzbar.decode(frame):
#                 my_code = code.data.decode('utf-8')
#                 print("인식 성공: ", my_code)
                
#                 #webbrowser.open(my_code)
#                 my_code = str(my_code)
#                 if my_code == "http://127.0.0.1:8000/otpcheck/":
#                     num += 1
#                     return render(request, 'main/otpcheck.html')
#                 else:
#                     continue
                

                                     

#             cv2.imshow('cam', frame)
            

#             key = cv2.waitKey(1)

#             if (num > 0):
#                 break

#             if (key == 27):
#                 break          

#     cap.release()
#     #frame = str(frame)
#     cv2.destroyAllWindows()

#     return render(request, 'main/otpreader.html')

def userpage(request):
    username = request.COOKIES.get('username')
    dbsee2 = User.objects.get(username=username)
    auth = dbsee2.auth



    if (auth == 'store'):
        return render(request, 'main/alert.html')
    
    korname = dbsee2.korname
    usenums = dbsee2.usenums
    phonenum = dbsee2.phonenum
    userpoint = dbsee2.userpoint

    historyall = history.objects.filter(u_id = username)

    return render(request, 'main/userpage.html',{'auth':auth, 'username':username, 'korname':korname, 'usenums':usenums, 'userpoint':userpoint, 'phonenum': phonenum, 'historyall':historyall})

def storepass(request):
    username = request.COOKIES.get('username')
    dbsee3 = User.objects.get(username=username)
    auth = dbsee3.auth
    test = 0

    if (auth == 'user'):
        return render(request, 'main/alert.html')

    if request.method == "POST":
        inputnum = request.POST["inputnum"]

        phonenumlist = User.objects.values_list('phonenum', flat=True)



        for a in phonenumlist:

            if a==inputnum:
                test += 1

                pointplus = User.objects.get(phonenum=a)
                temp_name = pointplus.korname
                pointplus.userpoint += 3000
                temp_point = pointplus.userpoint
                pointplus.usenums +=1
                pointplus.save()
                now = datetime.datetime.now()
                nowdate = now.strftime('%Y-%m-%d %H:%M:%S')

                history.objects.create(
                    u_id = temp_name,
                    s_id = request.COOKIES.get('username'),
                    nowpoint = temp_point,
                    h_date = nowdate,
                 )


                return render(request, 'main/sucplus.html')
    
        if test == 0:
            return render(request, 'main/failplus.html')

    

    return render(request, 'main/storepass.html')


def gift(request):
    if request.method == "POST":
        username = request.COOKIES.get('username')
        dbuser = User.objects.get(username=username)
        dbuser.forevent += 1
        dbuser.save()

        
        import json

        with open("kakao_code.json","r") as fp:
            tokens = json.load(fp)

        friend_url = "https://kapi.kakao.com/v1/api/talk/friends"


        headers={"Authorization" : "Bearer " + tokens["access_token"]}

        result = json.loads(requests.get(friend_url, headers=headers).text)

        friends_list = result.get("elements")

        friend_id = friends_list[0].get("uuid")


        send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

        data={
            'receiver_uuids': '["{}"]'.format(friend_id),
            "template_object": json.dumps({
                "object_type":"text",
                "text":"용기모아에서 구매하신 기프티콘입니다.",
                "link":{
                    "web_url":"www.naver.com"
                },
                "button_title": "확인하러가기"
            })
        }

        response = requests.post(send_url, headers=headers, data=data)
        response.status_code



        return render(request, 'main/sendgift.html')

    return render(request, 'main/gift.html')

def sendgift(request):

    #카톡
    
    #-------------------------------------------------------------------------

    return render(request, 'main/sendgift.html')

def nopoint(request):
    return render(request, 'main/nopoint.html')

def buygifticon(request):
    username = request.COOKIES.get('username')
    userdata = User.objects.get(username=username)
    
    if userdata.userpoint<5000:
        return render(request, 'main/nopoint.html')

    else:
        if request.method == "POST":
            userdata.userpoint -= 5000
            temp_point = userdata.userpoint
            userdata.save()

            now = datetime.datetime.now()
            nowdate = now.strftime('%Y-%m-%d %H:%M:%S')

            history.objects.create(
                u_id = username,
                s_id = "기프트콘 전환",
                nowpoint = temp_point,
                h_date = nowdate,
            )

            #-카톡 전송-----------------------------------------------------
            import requests
            import json

            with open("kakao_code.json","r") as fp:
                tokens = json.load(fp)

            friend_url = "https://kapi.kakao.com/v1/api/talk/friends"


            headers={"Authorization" : "Bearer " + tokens["access_token"]}

            result = json.loads(requests.get(friend_url, headers=headers).text)

            friends_list = result.get("elements")

            friend_id = friends_list[0].get("uuid")


            send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

            data={
                'receiver_uuids': '["{}"]'.format(friend_id),
                "template_object": json.dumps({
                    "object_type":"text",
                    "text":"용기모아에서 구매하신 기프티콘입니다.",
                    "link":{
                        "web_url":"www.naver.com"
                    },
                    "button_title": "확인하러가기"
                })
            }

            response = requests.post(send_url, headers=headers, data=data)
            response.status_code
            #------------------------------------------------------


            return render(request, 'main/sendgift.html')

            
               

    # if request.method == "POST":
    #     username = request.COOKIES.get('username')
    #     userdata = User.objects.get(username=username)

    #     if userdata.userpoint >= 5000:
    #         userdata.userpoint -= 5000
    #         userdata.save()
    #         return render(request, 'main/sendgift.html')

    #     else:
    #         return render(request, 'main/nopoint.html')

    return render(request, 'main/buygifticon.html')

def honeytip(request):
    return render(request, 'main/honeytip.html')