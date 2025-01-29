from django.shortcuts import render, redirect
from django.http import HttpResponse
from adminpanel import models
from website import models as dadas 




import json
import os

FIXED_USERNAME = "admin"
PASSWORD_FILE = "password_store.json"

def load_password():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {"password": "password123"}  

def save_password(password_store):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(password_store, file)

password_store = load_password()

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username == FIXED_USERNAME and password == password_store["password"]:
            messages.success(request, "Login successful!")
            return redirect("/admin/dashbord")
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "admin/login.html")

def forgot_password_view(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        
        if old_password == password_store["password"]:
            if new_password == confirm_password:
                password_store["password"] = new_password
                save_password(password_store)
                messages.success(request, "Password updated successfully!")
                return redirect("/admin/forgot_password")
            else:
                messages.error(request, "New passwords do not match.")
        else:
            messages.error(request, "Old password is incorrect.")
    
    return render(request, "admin/forgot_password.html")



# def admin_index(req):
#     return render(req, 'admin/admin_index.html')


def Navbar(req):
    return render(req, 'admin/Navbar.html')


def Footer(req):
    return render(req, 'admin/Footer.html')

def dashbord(req):
    return render(req,"admin/dashbord.html")


def Add_banner_img(req):
    banner = models.Studs_banner_img.objects.all()
    obj = {'banner':banner}
    return render(req,'admin/Add_banner_img.html',obj)

def upload_banner_img(req):
    stu_banner = models.Studs_banner_img(
        bannerImage = req.FILES['bannerImage'],
    )
    stu_banner.save()
    return redirect('/admin/Add_banner_img')


def delete_banner(req):
    id = req.GET['id']
    models.Studs_banner_img.objects.get(id = id).delete()
    return redirect('/admin/Add_banner_img')

def delete_card_studs(req):
    id = req.GET['id']
    models.Studs_cards.objects.get(id = id).delete()
    return redirect("/admin/studs_card")

def edit_banner_img(req):
    ban = models.Studs_banner_img.objects.get(id = req.POST['id'])
    ban.bannerImage = req.FILES['bannerImage_edit"']
    ban.save()
    return redirect('/admin/Add_banner_img')


def studs_card(req):
    data = models.Studs_cards.objects.all()
    obj = {'data':data}
    return render(req,'admin/studs_card.html',obj)

def studs_card_Data(req):
    card_Data = models.Studs_cards(
        image = req.FILES['image'],
        image_title = req.POST['image_title'],
        latest_price = req.POST['latest_price'],
        old_price = req.POST['old_price'],   
    )
    card_Data.save()
    return redirect('/admin/studs_card')

def edit_card_studs(req):
    old_Data =models.Studs_cards.objects.get(id = req.GET['id'])
    obj = {"old_Data":old_Data}
    return render(req,'admin/edit_card_studs.html',obj)


def edit_studs_card(req):
    edit_s_card = models.Studs_cards.objects.get(id = req.POST['id'])
    edit_s_card.image = req.FILES['cardImage_edit']
    edit_s_card.image_title = req.POST['imgTitle_edit']
    edit_s_card.latest_price = req.POST['latestPrice_edit']
    edit_s_card.old_price = req.POST['oldPrice_edit']
    edit_s_card.save()
    return redirect("/admin/studs_card")

def studs_artical(req):
    data = models.Studs_artical.objects.all()
    obj = {'data':data}
    return render(req,'admin/studs_artical.html',obj)

def studs_artica_data(req):
    studs_artical = models.Studs_artical(
        articleHeading = req.POST['articleHeading'],
        articleDescription = req.POST['articleDescription'],
    )
    studs_artical.save()
    return redirect("/admin/studs_artical")

def delete_artical_studs(req):
    id = req.GET['id']
    models.Studs_artical.objects.get(id = id).delete()
    return redirect("/admin/studs_artical")

 
def edit_artical_studs(req):
    old_Data = models.Studs_artical.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_artical_studs.html',obj)

def edit_artical_data(req):
    edit_artical =models.Studs_artical.objects.get(id=req.POST['id']) 
    edit_artical.articleHeading = req.POST['articleHeading_edit']
    edit_artical.articleDescription = req.POST['articleDescription_edit']
    edit_artical.save()
    return redirect("/admin/studs_artical")

def Hoops_and_Huggies(req):
    return render(req,'admin/Hoops_and_Huggies.html')

def HoopsBannerImg(req):
    data = models.Hoops_Huggies.objects.all()
    obj = {'data':data}
    return render(req,'admin/HoopsBannerImg.html',obj)

def Hoops_huggies_banner_img(req):
    hoops = models.Hoops_Huggies(
        Hoops_bannerImage = req.FILES['Hoops_bannerImage'],
    )
    hoops.save()
    return redirect("/admin/Hoops_and_Huggies")

def delete_hoops_banner(req):
    id = req.GET['id']
    models.Hoops_Huggies.objects.get(id = id).delete()
    return redirect("/admin/HoopsBannerImg")

def Hoopscard_info(req):
    data = models.Hoops_Huggies_cards.objects.all()
    obj = {'data':data}
    return render(req,'admin/Hoopscard_info.html',obj)

def Hoops_card_Data(req):
 hoops = models.Hoops_Huggies_cards(
 hoops_image = req.FILES['hoops_image'], 
 hoops_image_title = req.POST['hoops_image_title'],
 hoops_latest_price = req.POST['hoops_latest_price'],
 hoops_old_price = req.POST['hoops_old_price'], 
 )  
 hoops.save()
 return redirect('/admin/Hoopscard_info')

def delete_card_hoops(req):
    id = req.GET['id']
    models.Hoops_Huggies_cards.objects.get(id = id).delete()
    return redirect("/admin/Hoopscard_info")


def edit_card__hoops(req):
    old_Data = models.Hoops_Huggies_cards.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/edit_card__hoops.html',obj)


def edit_hoops_card(req):
    card_edit = models.Hoops_Huggies_cards.objects.get(id = req.POST['id'])
    card_edit.hoops_image = req.FILES['hoops_cardImage_edit']
    card_edit.hoops_image_title = req.POST['hoops_imgTitle_edit']
    card_edit.hoops_latest_price = req.POST['hoops_latestPrice_edit']
    card_edit.hoops_old_price = req.POST['hoops_oldPrice_edit']
    card_edit.save()
    return redirect("/admin/Hoopscard_info")

def hoops_articleanddescription(req):
    data = models.Hoops_Article_data.objects.all()
    obj = {'data':data}
    return render(req,'admin/hoops_articleanddescription.html',obj)


def hoops_artica_data(req):
    article = models.Hoops_Article_data(
        hoops_articleHeading = req.POST['hoops_articleHeading'],
        hoops_articleDescription = req.POST['hoops_articleDescription'],
    )
    article.save()
    return redirect("/admin/hoops_articleanddescription")

def delete_artical_hoops(req):
    id = req.GET['id']
    models.Hoops_Article_data.objects.get(id = id).delete()
    return redirect("/admin/hoops_articleanddescription")


def edit_artical_hoops(req):
    old_Data = models.Hoops_Article_data.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/edit_artical_hoops.html',obj)


def hoops_edit_artical_data(req):
     artical_edit = models.Hoops_Article_data.objects.get(id = req.POST['id'])
     artical_edit.hoops_articleHeading = req.POST['hoops_articleHeading_edit']
     artical_edit.hoops_articleDescription=req.POST['hoops_articleDescription_edit']
     artical_edit.save()
     return redirect("/admin/hoops_articleanddescription")
 
def Queandans_Hoops(req):
    data = models.Hoops_Question_Ans.objects.all()
    obj = {'data':data}
    return render(req,'admin/Queandans_Hoops.html',obj)

def hoops_question_ans(req):
    que = models.Hoops_Question_Ans(
    Question = req.POST['Question'],
    )
    que.save()
    return redirect("/admin/Queandans_Hoops")

def delete_question_hoops(req):
    id = req.GET['id']
    models.Hoops_Question_Ans.objects.get(id = id).delete()
    return redirect("/admin/Queandans_Hoops")



def edit_qusetion_ans_hoops(req):
    old_data = models.Hoops_Question_Ans.objects.get(id = req.GET['id'])
    obj = {'old_data':old_data}
    return render(req,'admin/edit_qusetion_ans_hoops.html',obj)



def edit_hoops_question_ans(req):
    edit_que = models.Hoops_Question_Ans.objects.get(id=req.POST['id'])
    edit_que.Question = req.POST['Question_edit']
    edit_que.save()
    return redirect("/admin/Queandans_Hoops")

def drops_banglers(req):
    return render(req,'admin/drops_banglers.html')


def DropsBannerImg(req):
    data = models.Drops_Banner_img1.objects.all()
    obj = {'data':data}
    return render(req,'admin/DropsBannerImg.html',obj)

def Drops_banner_img(req):
    drop_img = models.Drops_Banner_img1(
        drops_bannerImage = req.FILES['drops_bannerImage'],
    ) 
    drop_img.save()
    return redirect("/admin/DropsBannerImg")

def delete_drops_banner(req):
    id = req.GET['id']
    models.Drops_Banner_img1.objects.get(id = id).delete()
    return redirect("/admin/DropsBannerImg")

def Dropscard_info(req):
    data = models.Drops_Card_Info.objects.all()
    obj = {'data':data}
    return render(req,'admin/Dropscard_info.html',obj)


def Drops_card_Data(req):
 hoops = models.Drops_Card_Info(
 hoops_image = req.FILES['hoops_image'], 
 hoops_image_title = req.POST['hoops_image_title'],
 hoops_latest_price = req.POST['hoops_latest_price'],
 hoops_old_price = req.POST['hoops_old_price'], 
 )  
 hoops.save()
 return redirect('/admin/Dropscard_info')

def delete_card_drops(req):
    id = req.GET['id']
    models.Drops_Card_Info.objects.get(id = id).delete()
    return redirect("/admin/Dropscard_info")

def edit_card__drops(req):
    old_Data = models.Drops_Card_Info.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/edit_card__drops.html',obj)

def edit_drops_card(req):
    card_edit = models.Drops_Card_Info.objects.get(id = req.POST['id'])
    card_edit.hoops_image = req.FILES['hoops_cardImage_edit']
    card_edit.hoops_image_title = req.POST['hoops_imgTitle_edit']
    card_edit.hoops_latest_price = req.POST['hoops_latestPrice_edit']
    card_edit.hoops_old_price = req.POST['hoops_oldPrice_edit']
    card_edit.save()
    return redirect("/admin/Dropscard_info")

def Drops_articleanddescription(req):
    data = models.Drops_Article_data.objects.all()
    obj = {'data':data}
    return render(req,'admin/Drops_articleanddescription.html',obj)


def Drops_artica_data(req):
    article = models.Drops_Article_data(
    hoops_articleHeading = req.POST['hoops_articleHeading'],
    hoops_articleDescription = req.POST['hoops_articleDescription'],
    )
    article.save()
    return redirect("/admin/Drops_articleanddescription")

def delete_artical_drops(req):
    id = req.GET['id']
    models.Drops_Article_data.objects.get(id = id).delete()
    return redirect("/admin/Drops_articleanddescription")


def edit_artical_drops(req):
    old_Data = models.Drops_Article_data.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/edit_artical_drops.html',obj)



def drops_edit_artical_data(req):
     artical_edit = models.Drops_Article_data.objects.get(id = req.POST['id'])
     artical_edit.hoops_articleHeading = req.POST['hoops_articleHeading_edit']
     artical_edit.hoops_articleDescription=req.POST['hoops_articleDescription_edit']
     artical_edit.save()
     return redirect("/admin/Drops_articleanddescription")
 
def Queandans_Drops(req):
    data = models.Drops_Question_Ans.objects.all()
    obj = {'data':data}
    return render(req,'admin/Queandans_Drops.html',obj)

def Drops_question_ans(req):
    que = models.Drops_Question_Ans(
        Question = req.POST['Question'],
    )
    que.save()
    return redirect("/admin/Queandans_Drops")

def delete_question_drops(req):
    id = req.GET['id']
    models.Drops_Question_Ans.objects.get(id=id).delete()
    return redirect("/admin/Queandans_Drops")

def edit_qusetion_ans_drops(req):
    old_data = models.Drops_Question_Ans.objects.get(id = req.GET['id'])
    obj = {'old_data':old_data}
    return render(req,'admin/edit_qusetion_ans_drops.html',obj)


def edit_drops_question_ans(req):
    edit_que = models.Drops_Question_Ans.objects.get(id=req.POST['id'])
    edit_que.Question = req.POST['Question_edit']
    edit_que.save()
    return redirect("/admin/Queandans_Drops")

def Sui_Dhaga(req):
    data = models.Sui_Dhaga_cart.objects.all()
    obj = {'data':data}
    return render(req,'admin/Sui_Dhaga.html',obj)

def sui_dhaga_card_data(req):
    sui = models.Sui_Dhaga_cart(
        productImage = req.FILES['productImage'],
        productTitle = req.POST['productTitle'],
        latestPrice = req.POST['latestPrice'],
        oldPrice = req.POST['oldPrice'],
    )
    sui.save()
    return redirect("/admin/Sui_Dhaga")

def delete_card_sui(req):
    id = req.GET['id']
    models.Sui_Dhaga_cart.objects.get(id = id).delete()
    return redirect("/admin/Sui_Dhaga")

def Edit_sui_dhaga(req):
    old_Data = models.Sui_Dhaga_cart.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_sui_dhaga.html',obj)


def edit_sui_dhaga_card(req):
    edit_card = models.Sui_Dhaga_cart.objects.get(id = req.POST['id'])
    edit_card.productImage = req.FILES['cardImage_edit']
    edit_card.productTitle = req.POST['imgTitle_edit']
    edit_card.latestPrice = req.POST['latestPrice_edit']
    edit_card.oldPrice = req.POST['oldPrice_edit']
    edit_card.save()
    return redirect("/admin/Sui_Dhaga")

def Party_Wear(req):
    data = models.Party_wear_cart.objects.all()
    obj = {'data':data}
    return render(req,'admin/Party_Wear.html',obj)

def delete_slider(req):
    id = req.GET['id']
    models.Index_Slider.objects.get(id = id).delete()
    return redirect("/admin/Slider")

def edit_Slider(req):
    old_Data = models.Index_Slider.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/edit_Slider.html',obj)
    
    
def update_Slider(req):
    old_Data = models.Index_Slider.objects.get(id = req.POST['id'])
    old_Data.image_index_Slider = req.FILES['image_index_Slider']
    old_Data.save()
    return redirect("/admin/Slider")


    # 

def party_wear_card_data(req):
    party = models.Party_wear_cart(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],
    )
    party.save()
    return redirect("/admin/Party_Wear")


def delete_card_party_wear(req):
    id = req.GET['id']
    models.Party_wear_cart.objects.get(id = id).delete()
    return redirect("/admin/Party_Wear")     


def Edit_party_wear(req):
    old_Data = models.Party_wear_cart.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_party_wear.html',obj)
    
    
def party_wear_card(req):
    edit_card = models.Party_wear_cart.objects.get(id = req.POST['id'])
    edit_card.productImage = req.FILES['cardImage_edit']
    edit_card.productTitle = req.POST['imgTitle_edit']
    edit_card.latestPrice = req.POST['latestPrice_edit']
    edit_card.oldPrice = req.POST['oldPrice_edit']
    edit_card.save()
    return redirect("/admin/Party_Wear")



def Erings_Daily_Wear(req):
    data = models.Daily_wear_cart.objects.all()
    obj = {'data':data}
    return render(req,'admin/Erings_Daily_Wear.html',obj)


def Daily_Wear_card_data(req):
    party = models.Daily_wear_cart(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],
    )
    party.save()
    return redirect("/admin/Erings_Daily_Wear")


def delete_card_daily_wear(req):
    id = req.GET['id']
    models.Daily_wear_cart.objects.get(id = id).delete()
    return redirect("/admin/Erings_Daily_Wear")



def Edit_daily_wear(req):     
    old_Data = models.Daily_wear_cart.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_daily_wear.html',obj)

def Edit_daily_wear_card(req):
    edit_card = models.Daily_wear_cart.objects.get(id = req.POST['id'])
    edit_card.productImage = req.FILES['cardImage_edit']
    edit_card.productTitle = req.POST['imgTitle_edit']
    edit_card.latestPrice = req.POST['latestPrice_edit']
    edit_card.oldPrice = req.POST['oldPrice_edit']
    edit_card.save()
    return redirect("/admin/Erings_Daily_Wear")

def Diamond_Short_Necklace(req):
    data = models.Necklacesmodel.objects.all()
    obj = {'data':data}
    return render(req,'admin/Diamond_Short_Necklace.html',obj)

def DiamondShortNecklaces_data(req):
    Necklaces = models.Necklacesmodel(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],
    )
    Necklaces.save()
    return redirect("/admin/Diamond_Short_Necklace")

def delete_DiamondShortNecklaces(req):
    id = req.GET['id']
    models.Necklacesmodel.objects.get(id = id).delete()
    return redirect("/admin/Diamond_Short_Necklace")


def Edit_Diamond_Short_Necklace(req):
    old_Data = models.Necklacesmodel.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_Diamond_Short_Necklace.html',obj)


def Edit_Diamond_necklace_data(req):
    edit_card = models.Necklacesmodel.objects.get(id = req.POST['id'])
    edit_card.productImage = req.FILES['cardImage_edit']
    edit_card.productTitle = req.POST['imgTitle_edit']
    edit_card.latestPrice = req.POST['latestPrice_edit']
    edit_card.oldPrice = req.POST['oldPrice_edit']
    edit_card.save()
    return redirect("/admin/Diamond_Short_Necklace")


def Lariat_Necklace_card(req):
    data = models.Lariat_Necklaces.objects.all()
    obj = {'data':data}
    return render(req,'admin/Lariat_Necklace_card.html',obj)


def Lariat_Necklaces_data(req):
    Lariat = models.Lariat_Necklaces(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],
    )
    Lariat.save()
    return redirect("/admin/Lariat_Necklace_card")



def delete_Lariat_Necklaces(req):
    id = req.GET['id']
    models.Lariat_Necklaces.objects.get(id = id).delete()
    return redirect("/admin/Lariat_Necklace_card")

def Edit_Lariat_Necklaces(req):
    old_Data = models.Lariat_Necklaces.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_Lariat_Necklaces.html',obj)



def edit_Lariat_Necklaces_card(req):
    edit_card = models.Lariat_Necklaces.objects.get(id = req.POST['id'])
    edit_card.productImage = req.FILES['cardImage_edit']
    edit_card.productTitle = req.POST['imgTitle_edit']
    edit_card.latestPrice = req.POST['latestPrice_edit']
    edit_card.oldPrice = req.POST['oldPrice_edit']
    edit_card.save()
    return redirect("/admin/Lariat_Necklace_card")

def Lariat_Necklace_Home(req):
    return render(req,'admin/Lariat_Necklace_Home.html')

def Lariat_Necklace_article_des(req):
    data = models.Lari_Neck_Article.objects.all()
    obj = {'data':data}
    return render(req,'admin/Lariat_Necklace_article_des.html',obj)

def Lariat_artical_data(req):
    arti_Data = models.Lari_Neck_Article(
        articleHeading = req.POST['articleHeading'],
        articleDescription = req.POST['articleDescription'],
    )
    arti_Data.save()
    return redirect("/admin/Lariat_Necklace_article_des")

def delete_artical_lariat(req):
    id = req.GET['id']
    models.Lari_Neck_Article.objects.get(id = id).delete()
    return redirect("/admin/Lariat_Necklace_article_des")

def edit_artical_lariat(req):
    old_Data = models.Lari_Neck_Article.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/edit_artical_lariat.html',obj)

def lariat_edit_artical_data(req):
    lariat_edit = models.Lari_Neck_Article.objects.get(id = req.POST['id'])
    lariat_edit.articleHeading = req.POST['articleHeading_edit']
    lariat_edit.articleDescription = req.POST['articleDescription_edit']
    lariat_edit.save()
    return redirect("/admin/Lariat_Necklace_article_des")

def Lariat_Necklace_Ques(req):
    data = models.Lariant_Que.objects.all()
    obj = {'data':data}
    return render(req,'admin/Lariat_Necklace_Ques.html',obj)


def lariat_question(req):
    que = models.Lariant_Que(
        Question = req.POST['Question'],
    )
    que.save()
    return redirect("/admin/Lariat_Necklace_Ques")

def delete_question_lariat_neck(req):
    id = req.GET['id']
    models.Lariant_Que.objects.get(id = id).delete()
    return redirect("/admin/Lariat_Necklace_Ques")


def edit_qusetion_lariat_neck(req):
    old_Data = models.Lariant_Que.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/edit_qusetion_lariat_neck.html',obj)


def edit_lariat_data(req):
    lariat_edit = models.Lariant_Que.objects.get(id = req.POST['id'])
    lariat_edit.Question = req.POST['Question_edit']
    lariat_edit.save()
    return redirect("/admin/Lariat_Necklace_Ques")


def Heart_Pendant(req):
    data = models.HeartPendant.objects.all()
    obj = {'data':data}
    return render(req,'admin/Heart_Pendant.html',obj)


def HeartPendant_card_save(req):
    HeartP = models.HeartPendant(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],
    )
    HeartP.save()
    return redirect("/admin/Heart_Pendant")

def delete_HeartPendant(req):
    id = req.GET['id']
    models.HeartPendant.objects.get(id = id).delete()
    return redirect("/admin/Heart_Pendant")

def Edit_Diamond_Heart_Pendant(req):
    old_Data = models.HeartPendant.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_Diamond_Heart_Pendant.html',obj)


def edit_Diamond_Heart_card(req):
    edit_Heart = models.HeartPendant.objects.get(id = req.POST['id'])
    edit_Heart.productImage = req.FILES['cardImage_edit']
    edit_Heart.productTitle = req.POST['imgTitle_edit']
    edit_Heart.latestPrice = req.POST['latestPrice_edit']
    edit_Heart.oldPrice = req.POST['oldPrice_edit']
    edit_Heart.save()
    return redirect("/admin/Heart_Pendant")

def diamond_religious_pendant(req):
    data = models.Religious_Pend.objects.all()
    obj = {'data':data}
    return render(req,'admin/diamond_religious_pendant.html',obj)


def religious_pendant_card_save(req):
    religious = models.Religious_Pend(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],
    )
    religious.save()
    return redirect("/admin/diamond_religious_pendant")


def delete_religious_pendant(req):
    id = req.GET['id']
    models.Religious_Pend.objects.get(id = id).delete()
    return redirect("/admin/diamond_religious_pendant")


def Edit_diamond_religious_pendant(req):
    old_Data = models.Religious_Pend.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,"admin/Edit_diamond_religious_pendant.html",obj)

def edit_diamond_religious_pendant_card(req):
    edit_Heart = models.Religious_Pend.objects.get(id = req.POST['id'])
    edit_Heart.productImage = req.FILES['cardImage_edit']
    edit_Heart.productTitle = req.POST['imgTitle_edit']
    edit_Heart.latestPrice = req.POST['latestPrice_edit']
    edit_Heart.oldPrice = req.POST['oldPrice_edit']
    edit_Heart.save()
    return redirect("/admin/diamond_religious_pendant")


def Flexible_Bracelet(req):
    return render(req,'admin/Flexible_Bracelet.html')

def Flexible_Bracelet_Card(req):
    data = models.Flexible_Brac_Card.objects.all()
    obj = {'data':data}
    return render(req,'admin/Flexible_Bracelet_Card.html',obj)


def Flexible_Bracelet_save(req):
    religious = models.Flexible_Brac_Card(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],
    )
    religious.save()
    return redirect("/admin/Flexible_Bracelet_Card")

def delete_Flexible_Bracelet(req):
    id = req.GET['id']
    models.Flexible_Brac_Card.objects.get(id = id).delete()
    return redirect("/admin/Flexible_Bracelet_Card")


def Edit_Flexible_Bracelet(req):
    old_Data = models.Flexible_Brac_Card.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_Flexible_Bracelet.html',obj)

def edit_Flexible_Braceletcard(req):
    edit_Flex_card = models.Flexible_Brac_Card.objects.get(id = req.POST['id'])
    edit_Flex_card.productImage = req.FILES['cardImage_edit']
    edit_Flex_card.productTitle = req.POST['imgTitle_edit']
    edit_Flex_card.latestPrice = req.POST['latestPrice_edit']
    edit_Flex_card.oldPrice = req.POST['oldPrice_edit']
    edit_Flex_card.save()
    return redirect("/admin/Flexible_Bracelet_Card")


def Flexible_Bracelet_article_Des(req):
    data = models.Flexible_Bracelet_arti_mode.objects.all()
    obj = {'data':data}
    return render(req,'admin/Flexible_Bracelet_article_Des.html',obj)


def Flexible_Bracelet_artical_data(req):
    arti_Data = models.Flexible_Bracelet_arti_mode(
    articleHeading = req.POST['articleHeading'],
    articleDescription = req.POST['articleDescription'],
    )
    arti_Data.save()
    return redirect("/admin/Flexible_Bracelet_article_Des")

def delete_Flexible_Bracelet_artical(req):
    id = req.GET['id']
    models.Flexible_Bracelet_arti_mode.objects.get(id = id).delete()
    return redirect("/admin/Flexible_Bracelet_article_Des")


def edit_Flexible_Bracelet_artical(req):
    old_Data = models.Flexible_Bracelet_arti_mode.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/edit_Flexible_Bracelet_artical.html',obj)


def edit_Flexible_Bracelet_artical_data(req):
    Flexible_edit = models.Flexible_Bracelet_arti_mode.objects.get(id = req.POST['id'])
    Flexible_edit.articleHeading = req.POST['articleHeading_edit']
    Flexible_edit.articleDescription = req.POST['articleDescription_edit']
    Flexible_edit.save()
    return redirect("/admin/Lariat_Necklace_article_des")


def Diamond_Cufflinks(req):
    data = models.Cufflinks.objects.all()
    obj = {'data':data}
    return render(req,'admin/Diamond_Cufflinks.html',obj)

def Cufflinks_card_save(req):
    Cufflinks = models.Cufflinks(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],
    )
    Cufflinks.save()
    return redirect("/admin/Diamond_Cufflinks")

def delete_Cufflinks_card(req):
    id = req.GET['id']
    models.Cufflinks.objects.get(id= id).delete()
    return redirect("/admin/Diamond_Cufflinks")


def Edit_Cufflinks_card(req):
    old_Data = models.Cufflinks.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_Cufflinks_card.html',obj)


def edit_Cufflinks_card_da(req):
    edit_Cufflinks = models.Cufflinks.objects.get(id = req.POST['id'])
    edit_Cufflinks.productImage = req.FILES['cardImage_edit']
    edit_Cufflinks.productTitle = req.POST['imgTitle_edit']
    edit_Cufflinks.latestPrice = req.POST['latestPrice_edit']
    edit_Cufflinks.oldPrice = req.POST['oldPrice_edit']
    edit_Cufflinks.save()
    return redirect("/admin/Diamond_Cufflinks")

def diamond_nosepin(req):
    data = models.D_nosepin.objects.all()
    obj = {'data':data}
    return render(req,'admin/diamond_nosepin.html',obj)


def nosepin_card_save(req):
    nosepin = models.D_nosepin(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],    
    )
    nosepin.save()
    return redirect("/admin/diamond_nosepin")

def delete_nosepin_card(req):
    id = req.GET['id']
    models.D_nosepin.objects.get(id = id).delete()
    return redirect("/admin/diamond_nosepin")


def Edit_nosepin_card(req):
    old_Data = models.D_nosepin.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_nosepin_card.html',obj)


def edit_nosepin_card_da(req):
    edit_nosepin = models.D_nosepin.objects.get(id = req.POST['id'])
    edit_nosepin.productImage = req.FILES['cardImage_edit']
    edit_nosepin.productTitle = req.POST['imgTitle_edit']
    edit_nosepin.latestPrice = req.POST['latestPrice_edit']
    edit_nosepin.oldPrice = req.POST['oldPrice_edit']
    edit_nosepin.save()
    return redirect("/admin/diamond_nosepin")

def Gold_PartyWear(req):
    data = models.Gold_partywear.objects.all()
    obj = {'data':data}
    return render(req,'admin/Gold_PartyWear.html',obj)


def Gold_party_wear_save(req):
    Gold_party = models.Gold_partywear(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],    
    )
    Gold_party.save()
    return redirect("/admin/Gold_PartyWear")


def delete_Gold_party_wear(req):
    id = req.GET['id']
    models.Gold_partywear.objects.get(id = id).delete()
    return redirect("/admin/Gold_PartyWear")

def Edit_Gold_party_wear(req):
    old_Data = models.Gold_partywear.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/Edit_Gold_party_wear.html',obj)


def edit_Gold_party_card_da(req):
    edit_gold_party = models.Gold_partywear.objects.get(id = req.POST['id'])
    edit_gold_party.productImage = req.FILES['cardImage_edit']
    edit_gold_party.productTitle = req.POST['imgTitle_edit']
    edit_gold_party.latestPrice = req.POST['latestPrice_edit']
    edit_gold_party.oldPrice = req.POST['oldPrice_edit']
    edit_gold_party.save()
    return redirect("/admin/Gold_PartyWear")

def Gold_OfficeWear(req):
    data = models.Gold_OfficeWe.objects.all()
    obj = {'data':data}
    return render(req,'admin/Gold_OfficeWear.html',obj)


def Gold_Office_wear_save(req):
    Gold_Office = models.Gold_OfficeWe(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],    
    )
    Gold_Office.save()
    return redirect("/admin/Gold_OfficeWear")


def delete_Gold_office_wear(req):
    id = req.GET['id']
    models.Gold_OfficeWe.objects.get(id = id).delete()
    return redirect("/admin/Gold_OfficeWear")

def Edit_Gold_office_wear(req):
    old_Data = models.Gold_OfficeWe.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_Gold_office_wear.html',obj)

def edit_office_party_card_da(req):
    edit_gold_office = models.Gold_OfficeWe.objects.get(id = req.POST['id'])
    edit_gold_office.productImage = req.FILES['cardImage_edit']
    edit_gold_office.productTitle = req.POST['imgTitle_edit']
    edit_gold_office.latestPrice = req.POST['latestPrice_edit']
    edit_gold_office.oldPrice = req.POST['oldPrice_edit']
    edit_gold_office.save()
    return redirect("/admin/Gold_OfficeWear")


def Gold_dailywear(req):
    data = models.Gold_Daily_w.objects.all()
    obj = {'data':data}
    return render(req,'admin/Gold_dailywear.html',obj)

def Gold_daily_wear_save(req):
    Gold_daily = models.Gold_Daily_w(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],    
    )
    Gold_daily.save()
    return redirect("/admin/Gold_dailywear")


def delete_Gold_daily_wear(req):
    id = req.GET['id']
    models.Gold_Daily_w.objects.get(id=id).delete()
    return redirect("/admin/Gold_dailywear")



def Edit_Gold_daily_wear(req):
    old_Data = models.Gold_Daily_w.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_Gold_daily_wear.html',obj)

def edit_daily_party_card_da(req):
    edit_gold_daily = models.Gold_Daily_w.objects.get(id = req.POST['id'])
    edit_gold_daily.productImage = req.FILES['cardImage_edit']
    edit_gold_daily.productTitle = req.POST['imgTitle_edit']
    edit_gold_daily.latestPrice = req.POST['latestPrice_edit']
    edit_gold_daily.oldPrice = req.POST['oldPrice_edit']
    edit_gold_daily.save()
    return redirect("/admin/Gold_dailywear")

def Gold_Kids(req):
    data = models.Gold_Kids.objects.all()
    obj = {'data':data}
    return render(req,'admin/Gold_Kids.html',obj)


def Gold_kids_wear_save(req):
    Gold_kids = models.Gold_Kids(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],    
    )
    Gold_kids.save()
    return redirect("/admin/Gold_Kids")


def delete_Gold_kids_wear(req):
    id = req.GET['id']
    models.Gold_Kids.objects.get(id = id).delete()
    return redirect("/admin/Gold_Kids")

def Edit_Gold_kids_wear(req):
    old_Data = models.Gold_Kids.objects.get(id=req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_Gold_kids_wear.html',obj)

def edit_kids_card_da(req):
    edit_gold_kids = models.Gold_Kids.objects.get(id = req.POST['id'])
    edit_gold_kids.productImage = req.FILES['cardImage_edit']
    edit_gold_kids.productTitle = req.POST['imgTitle_edit']
    edit_gold_kids.latestPrice = req.POST['latestPrice_edit']
    edit_gold_kids.oldPrice = req.POST['oldPrice_edit']
    edit_gold_kids.save()
    return redirect("/admin/Gold_Kids")

def Gold_Drops_Danglers(req):
    data = models.Gold_Drops_Danglers.objects.all()
    obj = {'data':data}
    return render(req,'admin/Gold_Drops_Danglers.html',obj)

    
def Gold_DropsDanglers_wear_save(req):
    Gold_DropsDanglers = models.Gold_Drops_Danglers(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],    
    )
    Gold_DropsDanglers.save()
    return redirect("/admin/Gold_Drops_Danglers")

def delete_Gold_Drops_dang_wear(req):
    id = req.GET['id']
    models.Gold_Drops_Danglers.objects.get(id = id).delete()
    return redirect("/admin/Gold_Drops_Danglers")

def Edit_Gold_Drops_dang_wear(req):
    old_Data = models.Gold_Drops_Danglers.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/Edit_Gold_Drops_dang_wear.html',obj) 

def edit_drops_dang_wear_card_data(req):
    edit_gold_drops = models.Gold_Drops_Danglers.objects.get(id = req.POST['id'])
    edit_gold_drops.productImage = req.FILES['cardImage_edit']
    edit_gold_drops.productTitle = req.POST['imgTitle_edit']
    edit_gold_drops.latestPrice = req.POST['latestPrice_edit']
    edit_gold_drops.oldPrice = req.POST['oldPrice_edit']
    edit_gold_drops.save()
    return redirect("/admin/Gold_Drops_Danglers")


# kru
def Jewellery(req):
    jewellery = models.Jewellery.objects.all()
    obj = {"key":jewellery} 
    return render(req, "admin/Jewellery.html", obj)



def save_jewellery(req):
    jewellery = models.Jewellery(
        image_jewellery=req.FILES['image_jewellery'],
        price_jewellery=req.POST['price_jewellery'],
        description_jewellery=req.POST['description_jewellery'],
    )
    jewellery.save()
    return redirect("/admin/Jewellery")

def delete_jewellery(req):
    order_id=req.GET['id']
    models.Jewellery.objects.get(id = order_id).delete()
    return redirect("/admin/Jewellery")

def edit_jewellery(req):
    old_Data = models.Jewellery.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_jewellery.html',obj)

def Update_edit_jewellery(req):
    edit_artical =models.Jewellery.objects.get(id=req.POST['id']) 
    edit_artical.image_jewellery = req.FILES['image_jewellery']
    edit_artical.price_jewellery = req.POST['price_jewellery']
    edit_artical.description_jewellery = req.POST['description_jewellery']
    edit_artical.save()
    return redirect("/admin/Jewellery")

def Index_main_page(req):
    return render(req,"admin/Index_main_page.html")

def Slider(req):
    index_Slider = models.Index_Slider.objects.all()
    obj = {"index_Slider": index_Slider}
    return render(req, "admin/Slider.html", obj)

def save_index_Slider(req):
    index_Slider = models.Index_Slider(
        image_index_Slider=req.FILES['image_index_Slider'],
    )
    index_Slider.save()
    return redirect("/admin/Slider")

def delete_slider(req):
    order_id=req.GET['id']
    models.Index_Slider.objects.get(id = order_id).delete()
    return redirect("/admin/Slider")


def Best_Slider(req):
    bast_slider=models.Index_Bast_Slider.objects.all()
    obj = {"bast_slider": bast_slider}
    return render(req,"admin/Best_Slider.html", obj)

def index_bast_slider(req):
    bast_slider=models.Index_Bast_Slider(
        bast_Slider_imgase=req.FILES['bast_Slider_imgase'],
        bast_Slider_Name=req.POST['bast_Slider_Name'],
        bast_Slider_Description=req.POST['bast_Slider_Description'],
        bast_Slider_Price=req.POST['bast_Slider_Price']
    )
    bast_slider.save()
    return redirect("/admin/Best_Slider")

def delete_custmore(req):
    order_id=req.GET['id']
    models.Index_Bast_Slider.objects.get(id = order_id).delete()
    return redirect("/admin/Best_Slider")

def index_Bestseller_Category(req):
    Bestseller_Category_img=models.Bestseller_Category.objects.all()
    obj = {"Bestseller_Category_img": Bestseller_Category_img}
    return render(req,"admin/index_Bestseller_Category.html", obj)

def save_index_Bestseller_Category(req):
    Bestseller_Category=models.Bestseller_Category(
        index_Bestseller_Category_img=req.FILES['index_Bestseller_Category_img'],
    )
    Bestseller_Category.save()
    return redirect("/admin/index_Bestseller_Category")

def delete_index_Bestseller(req):
    order_id=req.GET['id']
    models.Bestseller_Category.objects.get(id = order_id).delete()
    return redirect("/admin/index_Bestseller_Category")

def index_Shop_Category(req):
    shop_Category = models.Shop_Category.objects.all()
    obj = {"shop_Category": shop_Category}
    return render(req,"admin/index_Shop_Category.html", obj)

def save_index_Shop_Category(req):
    shop_Category = models.Shop_Category(
        image_Shop_Category=req.FILES['image_Shop_Category'],
        Name_Shop_Category=req.POST['Name_Shop_Category'],
        description_Shop_Category=req.POST['description_Shop_Category'],
    )
    shop_Category.save()
    return redirect("/admin/index_Shop_Category")

def delete_shop_Category(req):
    order_id=req.GET['id']
    models.Shop_Category.objects.get(id = order_id).delete()
    return redirect("/admin/index_Shop_Category")

def index_PNG_Promises(req):
    save_index_png=models.Png_Images.objects.all()
    obj ={"save_index_png": save_index_png}
    return render(req,"admin/index_PNG_Promises.html", obj)

def save_index_bast_slider(req):
    save_index_png=models.Png_Images(
        index_Png=req.FILES['index_Png'],
        index_Png_Name=req.POST['index_Png_Name'],
    )
    save_index_png.save()
    return redirect("/admin/index_PNG_Promises")

def delete_index_Png_Name(req):
    order_id=req.GET['id']
    models.Png_Images.objects.get(id = order_id).delete()
    return redirect("/admin/index_PNG_Promises")

def edit_index_Png_Name(req):
    old_Data = models.Png_Images.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_index_Png_Name.html',obj)

def Update_edit_index_Png_Name(req):
    edit_artical =models.Png_Images.objects.get(id=req.POST['id']) 
    edit_artical.index_Png = req.FILES['index_Png']
    edit_artical.index_Png_Name = req.POST['index_Png_Name']
    edit_artical.save()
    return redirect("/admin/index_PNG_Promises")





def index_video(req):
    save_video=models.Save_Video.objects.all()
    obj = {"save_video": save_video}
    return render(req,"admin/index_video.html", obj)

def save_index_video(req):
    save_video=models.Save_Video(
        bast_Slider_video=req.FILES['bast_Slider_video']
    )
    save_video.save()
    return redirect("/admin/index_video")

def delete_video(req):
    order_id=req.GET['id']
    models.Save_Video.objects.get(id = order_id).delete()
    return redirect("/admin/index_video")


def PNG_Jewellers(req):
    Png_Jewellers=models.Png_JEWELLERS.objects.all()
    obj ={"Png_Jewellers": Png_Jewellers}
    return render(req,"admin/PNG_Jewellers.html", obj)

def index_PNG_Jewellers(req):
    Png_Jewellers=models.Png_JEWELLERS(
        PNG_Jewellerss=req.FILES['PNG_Jewellerss'],
        PNG_Jewellers_text=req.POST['PNG_Jewellers_text'],
        index_Heiding=req.POST['index_Heiding'],

    )
    Png_Jewellers.save()
    return redirect("/admin/PNG_Jewellers")

def delete_Png_Jewellerss(req):
    order_id=req.GET['id']
    models.Png_JEWELLERS.objects.get(id = order_id).delete()
    return redirect("/admin/PNG_Jewellers")

def edit_Info(req):
    edit_info = models.Png_JEWELLERS.objects.get(id=req.GET['id'])
    obj={"edit_info":edit_info}
    return render(req,"admin/edit_Info.html", obj)


def update_info(req):
    update=models.Png_JEWELLERS.objects.get(id=req.POST['id'])
    update.PNG_Jewellerss=req.FILES['PNG_Jewellerss']
    update.PNG_Jewellers_text=req.POST['PNG_Jewellers_text']
    update.index_Heiding=req.POST['index_Heiding']
    update.save()
    return redirect("/admin/PNG_Jewellers")

def Store_Locator(req):
    store_Locator=models.index_Store_Locator.objects.all()
    obj ={"store_Locator": store_Locator}
    return render(req,"admin/Store_Locator.html", obj)

def index_Store_Locator(req):
    store_Locator=models.index_Store_Locator(
        Store_Locator_img=req.FILES['Store_Locator_img'],
        Store_Locator_Heiding=req.POST['Store_Locator_Heiding'],
        Store_Locator_Description=req.POST['Store_Locator_Description']
    )
    store_Locator.save()
    return redirect("/admin/Store_Locator")

def delete_Store_Locator(req):
    order_id=req.GET['id']
    models.index_Store_Locator.objects.get(id = order_id).delete()
    return redirect("/admin/Store_Locator")

def edit_Store_Locator(req):
    edit_info = models.index_Store_Locator.objects.get(id=req.GET['id'])
    obj={"edit_info":edit_info}
    return render(req,"admin/edit_Store_Locator.html", obj)


def update_edit_Store_Locator(req):
    update=models.index_Store_Locator.objects.get(id=req.POST['id'])
    update.Store_Locator_img=req.FILES['Store_Locator_img']
    update.Store_Locator_Heiding=req.POST['Store_Locator_Heiding']
    update.Store_Locator_Description=req.POST['Store_Locator_Description']
    update.save()
    return redirect("/admin/index_Store_Locator")

def Celebrity_Corner(req):
    celebrity_Corner=models.index_Celebrity_Corner.objects.all()
    obj ={"celebrity_Corner": celebrity_Corner}
    return render(req,"admin/Celebrity_Corner.html", obj)

def index_Celebrity_Corner(req):
    celebrity_Corner=models.index_Celebrity_Corner(
        Celebrity_Corner_img=req.FILES['Celebrity_Corner_img'],
        Celebrity_Corner_img1=req.FILES['Celebrity_Corner_img1'],
        Celebrity_Corner_img2=req.FILES['Celebrity_Corner_img2'],
        Celebrity_Corner_img3=req.FILES['Celebrity_Corner_img3'],
        Celebrity_Corner_Heiding=req.POST['Celebrity_Corner_Heiding'],
        Celebrity_Corner_Description=req.POST['Celebrity_Corner_Description']
    )
    celebrity_Corner.save()
    return redirect("/admin/Celebrity_Corner")

def delete_Celebrity_Corner(req):
    order_id=req.GET['id']
    models.index_Celebrity_Corner.objects.get(id = order_id).delete()
    return redirect("/admin/Celebrity_Corner")


def edit_Celebrity_Corner(req):
    old_Data = models.index_Celebrity_Corner.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_Celebrity_Corner.html',obj)

def update_edit_Celebrity_Corner(req):
    edit_artical =models.index_Celebrity_Corner.objects.get(id=req.POST['id']) 
    edit_artical.Celebrity_Corner_img = req.FILES['Celebrity_Corner_img']
    edit_artical.Celebrity_Corner_img1 = req.FILES['Celebrity_Corner_img1']
    edit_artical.Celebrity_Corner_img2 = req.FILES['Celebrity_Corner_img2']
    edit_artical.Celebrity_Corner_img3 = req.FILES['Celebrity_Corner_img3']
    edit_artical.Celebrity_Corner_Heiding = req.POST['Celebrity_Corner_Heiding']
    edit_artical.Celebrity_Corner_Description = req.POST['Celebrity_Corner_Description']


    edit_artical.save()
    return redirect("/admin/Celebrity_Corner")








def save_jewellery(req):
    jewellery = models.Jewellery(
        image_jewellery=req.FILES['image_jewellery'],
        price_jewellery=req.POST['price_jewellery'],
        description_jewellery=req.POST['description_jewellery'],
    )
    jewellery.save()
    return redirect("/admin/Jewellery")
    
def Slider(req):
    index_Slider = models.Index_Slider.objects.all()
    obj = {"index_Slider": index_Slider}
    return render(req, "admin/Slider.html", obj)

def save_index_Slider(req):
    index_Slider = models.Index_Slider(
        image_index_Slider=req.FILES['image_index_Slider'],
    )
    index_Slider.save()
    return redirect("/admin/Slider")

def Best_Slider(req):
    bast_slider=models.Index_Bast_Slider.objects.all()
    obj = {"bast_slider": bast_slider}
    return render(req,"admin/Best_Slider.html", obj)

def index_bast_slider(req):
    bast_slider=models.Index_Bast_Slider(
        bast_Slider_imgase=req.FILES['bast_Slider_imgase'],
        bast_Slider_Name=req.POST['bast_Slider_Name'],
        bast_Slider_Description=req.POST['bast_Slider_Description'],
        bast_Slider_Price=req.POST['bast_Slider_Price']
    )
    bast_slider.save()
    return redirect("/admin/Best_Slider")


def Collections_Main(req):
    return render(req,"admin/Collections_Main.html")


def Arrival_goldjewellery(req):
    save_Arrival=models.Arrival_Goldjewellery.objects.all()
    obj ={"save_Arrival": save_Arrival}
    return render(req,"admin/Arrival_goldjewellery.html",obj)

def save_Arrival_goldjewellery(req):
    save_Arrival=models.Arrival_Goldjewellery(
        Arrival_goldjewellery_image=req.FILES['Arrival_goldjewellery_image'],
        image_Description=req.POST['image_Description'],
        Arrival_goldjewellery_price=req.POST['Arrival_goldjewellery_price'],
        Arrival_goldjewellery_old_price=req.POST['Arrival_goldjewellery_old_price'],

    )
    save_Arrival.save()
    return redirect("/admin/Arrival_goldjewellery")

def delete_card_Arrival(req):
    id = req.GET['id']
    models.Arrival_Goldjewellery.objects.get(id = id).delete()
    return redirect("/admin/Arrival_goldjewellery")

def edit_card_Arrival(req):
    old_Data = models.Arrival_Goldjewellery.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_card_Arrival.html',obj)

def edit_Arrival_data(req):
    edit_artical =models.Arrival_Goldjewellery.objects.get(id=req.POST['id']) 
    edit_artical.Arrival_goldjewellery_image = req.FILES['Arrival_goldjewellery_image']
    edit_artical.image_Description = req.POST['image_Description']
    edit_artical.Arrival_goldjewellery_price = req.POST['Arrival_goldjewellery_price']
    edit_artical.Arrival_goldjewellery_old_price = req.POST['Arrival_goldjewellery_old_price']
    edit_artical.save()
    return redirect("/admin/Arrival_goldjewellery")


def Mangalsutra_Mahaotsave(req):
    save_Mangalsutra=models.Mangalsutra_mahaotsave.objects.all()
    obj ={"save_Mangalsutra": save_Mangalsutra}
    return render(req,"admin/Mangalsutra_Mahaotsave.html",obj)

def save_Mangalsutra_Mahaotsave(req):
    save_Mangalsutra=models.Mangalsutra_mahaotsave(
        Mangalsutra_Mahaotsave_image=req.FILES['Mangalsutra_Mahaotsave_image'],
        Mangalsutra_Mahaotsave_Description=req.POST['Mangalsutra_Mahaotsave_Description'],
        Mangalsutra_Mahaotsave_price=req.POST['Mangalsutra_Mahaotsave_price'],
        Mangalsutra_Mahaotsave_old_price=req.POST['Mangalsutra_Mahaotsave_old_price'],

    )
    save_Mangalsutra.save()
    return redirect("/admin/Mangalsutra_Mahaotsave")

def delete_card_Mangalsutra(req):
    id = req.GET['id']
    models.Mangalsutra_mahaotsave.objects.get(id = id).delete()
    return redirect("/admin/Mangalsutra_Mahaotsave")

def edit_card_Mangalsutra(req):
    old_Data = models.Mangalsutra_mahaotsave.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_card_Mangalsutra.html',obj)

def save_edit_Mangalsutra(req):
    edit_artical =models.Mangalsutra_mahaotsave.objects.get(id=req.POST['id']) 
    edit_artical.Mangalsutra_Mahaotsave_image = req.FILES['Mangalsutra_Mahaotsave_image']
    edit_artical.Mangalsutra_Mahaotsave_Description = req.POST['Mangalsutra_Mahaotsave_Description']
    edit_artical.Mangalsutra_Mahaotsave_price = req.POST['Mangalsutra_Mahaotsave_price']
    edit_artical.Mangalsutra_Mahaotsave_old_price = req.POST['Mangalsutra_Mahaotsave_old_price']
    edit_artical.save()
    return redirect("/admin/Mangalsutra_Mahaotsave")

def EIINA(req):
    return render(req,"admin/EIINA.html")

def EIINA_Slider(req):
    EIINA_banner=models.EIINA_Banner.objects.all()
    obj ={"EIINA_banner": EIINA_banner}
    return render(req,"admin/EIINA_Slider.html", obj)

def upload_EIINA_banner_img(req):
    EIINA_banner=models.EIINA_Banner(
        EIINA_bannerImage=req.FILES['EIINA_bannerImage'],
    )
    EIINA_banner.save()
    return redirect("/admin/EIINA_Slider")

def delete_EIINA_banner(req):
    id = req.GET['id']
    models.EIINA_Banner.objects.get(id = id).delete()
    return redirect("/admin/EIINA_Slider")

def EIINA_Cards(req):
    save_EIINA=models.EIINA_CARDs.objects.all()
    obj ={"save_EIINA": save_EIINA}
    return render(req,"admin/EIINA_Cards.html", obj)

def save_EIINA_card(req):
    save_EIINA=models.EIINA_CARDs(
        EIINA_image=req.FILES['EIINA_image'],
        EIINA_Description=req.POST['EIINA_Description'],
        EIINA_Latest_price=req.POST['EIINA_Latest_price'],
        EIINA_old_price=req.POST['EIINA_old_price'],
    )
    save_EIINA.save()
    return redirect("/admin/EIINA_Cards")

def delete_card_EIINA(req):
    id = req.GET['id']
    models.EIINA_CARDs.objects.get(id = id).delete()
    return redirect("/admin/EIINA_Cards")

def edit_EIINA(req):
    old_Data = models.EIINA_CARDs.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_EIINA.html',obj)

def save_edit_EIINA(req):
    edit_artical =models.EIINA_CARDs.objects.get(id=req.POST['id']) 
    edit_artical.EIINA_image = req.FILES['EIINA_image']
    edit_artical.EIINA_Description = req.POST['EIINA_Description']
    edit_artical.EIINA_Latest_price = req.POST['EIINA_Latest_price']
    edit_artical.EIINA_old_price = req.POST['EIINA_old_price']
    edit_artical.save()
    return redirect("/admin/EIINA_Cards")

def Necklace_Mahotsav(req):
    save_Mahotsav=models.Necklace_mahotsav.objects.all()
    obj ={"save_Mahotsav": save_Mahotsav}
    return render(req,"admin/Necklace_Mahotsav.html", obj)

def save_Necklace_Mahotsav(req):
    save_Mahotsav=models.Necklace_mahotsav(
        Necklace_Mahotsav_image=req.FILES['Necklace_Mahotsav_image'],
        Necklace_Mahotsav_Description=req.POST['Necklace_Mahotsav_Description'],
        Necklace_Mahotsav_Latest_price=req.POST['Necklace_Mahotsav_Latest_price'],
        Necklace_Mahotsav_old_price=req.POST['Necklace_Mahotsav_old_price'],
    )
    save_Mahotsav.save()
    return redirect("/admin/Necklace_Mahotsav")

def delete_card_Necklace_Mahotsav(req):
    id = req.GET['id']
    models.Necklace_mahotsav.objects.get(id = id).delete()
    return redirect("/admin/Necklace_Mahotsav")

def edit_Necklace_Mahotsav(req):
    old_Data = models.Necklace_mahotsav.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_Necklace_Mahotsav.html',obj)

def save_Necklace_Mahotsavs(req):
    edit_artical =models.Necklace_mahotsav.objects.get(id=req.POST['id']) 
    edit_artical.Necklace_Mahotsav_image = req.FILES['Necklace_Mahotsav_image']
    edit_artical.Necklace_Mahotsav_Description = req.POST['Necklace_Mahotsav_Description']
    edit_artical.Necklace_Mahotsav_Latest_price = req.POST['Necklace_Mahotsav_Latest_price']
    edit_artical.Necklace_Mahotsav_old_price = req.POST['Necklace_Mahotsav_old_price']
    edit_artical.save()
    return redirect("/admin/Necklace_Mahotsav")

def diamond_diwalisale(req):
    save_diamond_diwalisale=models.Diamond_Diwalisale.objects.all()
    obj ={"save_diamond_diwalisale": save_diamond_diwalisale}
    return render(req,"admin/diamond_diwalisale.html", obj)

def save_diamond_diwalisale_card(req):
    save_diamond_diwalisale=models.Diamond_Diwalisale(
        diamond_diwalisale_image=req.FILES['diamond_diwalisale_image'],
        diamond_diwalisale_Description=req.POST['diamond_diwalisale_Description'],
        diamond_diwalisale_Latest_price=req.POST['diamond_diwalisale_Latest_price'],
        diamond_diwalisale_old_price=req.POST['diamond_diwalisale_old_price'],
    )
    save_diamond_diwalisale.save()
    return redirect("/admin/diamond_diwalisale")

def delete_card_diamond_diwalisale(req):
    id = req.GET['id']
    models.Diamond_Diwalisale.objects.get(id = id).delete()
    return redirect("/admin/diamond_diwalisale")


def edit_diamond_diwalisale(req):
    old_Data = models.Diamond_Diwalisale.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_diamond_diwalisale.html',obj)

def update_diamond_diwalisale(req):
    edit_artical =models.Diamond_Diwalisale.objects.get(id=req.POST['id']) 
    edit_artical.diamond_diwalisale_image = req.FILES['diamond_diwalisale_image']
    edit_artical.diamond_diwalisale_Description = req.POST['diamond_diwalisale_Description']
    edit_artical.diamond_diwalisale_Latest_price = req.POST['diamond_diwalisale_Latest_price']
    edit_artical.diamond_diwalisale_old_price = req.POST['diamond_diwalisale_old_price']
    edit_artical.save()
    return redirect("/admin/diamond_diwalisale")

def swarajya_collecations(req):
    return render(req,"admin/swarajya_collecations.html")

def collecations_swarajya_Slider(req):
    banner = models.Collecations_Swarajya.objects.all()
    obj ={"banner": banner}
    return render(req,"admin/collecations_swarajya_Slider.html", obj)

def save_collecations_swarajya_banner(req):
    banner = models.Collecations_Swarajya(
        collecations_swarajya_Image=req.FILES['collecations_swarajya_Image'],
    )
    banner.save()
    return redirect("/admin/collecations_swarajya_Slider")

def delete_banner_collecations_swarajya_Image(req):
    id = req.GET['id']
    models.Collecations_Swarajya.objects.get(id = id).delete()
    return redirect("/admin/collecations_swarajya_Slider")

def collecations_swarajya_Cards(req):
    ollecations_swarajya=models.Sllecations_swarajya.objects.all()
    obj = {"ollecations_swarajya": ollecations_swarajya}
    return render(req,"admin/collecations_swarajya_Cards.html", obj)

def save_ollecations_swarajya_card(req):
    ollecations_swarajya=models.Sllecations_swarajya(
        ollecations_swarajya_image=req.FILES['ollecations_swarajya_image'],
        ollecations_swarajya_Description=req.POST['ollecations_swarajya_Description'],
        ollecations_swarajya_Latest_price=req.POST['ollecations_swarajya_Latest_price'],
        ollecations_swarajya_old_price=req.POST['ollecations_swarajya_old_price'],
    )
    ollecations_swarajya.save()
    return redirect("/admin/collecations_swarajya_Cards")

def delete_card_ollecations_swarajya(req):
    id =req.GET['id']
    models.Sllecations_swarajya.objects.get(id = id).delete()
    return redirect("/admin/collecations_swarajya_Cards")


def edit_ollecations_swarajya(req):
    old_Data = models.Sllecations_swarajya.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_ollecations_swarajya.html',obj)

def Update_Sllecations_swarajya(req):
    edit_artical =models.Sllecations_swarajya.objects.get(id=req.POST['id']) 
    edit_artical.ollecations_swarajya_image = req.FILES['ollecations_swarajya_image']
    edit_artical.ollecations_swarajya_Description = req.POST['ollecations_swarajya_Description']
    edit_artical.ollecations_swarajya_Latest_price = req.POST['ollecations_swarajya_Latest_price']
    edit_artical.ollecations_swarajya_old_price = req.POST['ollecations_swarajya_old_price']
    edit_artical.save()
    return redirect("/admin/collecations_swarajya_Cards")


def saptam_collecation(req):
    return render(req,"admin/saptam_collecation.html")

def Saptam_Collecation_Slider(req):
    banner=models.Saptam_Collecation.objects.all()
    obj ={"banner": banner}
    return render(req,"admin/Saptam_Collecation_Slider.html", obj)

def upload_banner_Saptam_Collecation_img(req):
    banner=models.Saptam_Collecation(
        Saptam_Collecation_bannerImage=req.FILES['Saptam_Collecation_bannerImage'],
    )
    banner.save()
    return redirect("/admin/Saptam_Collecation_Slider")

def Saptam_Collecation_Cards(req):
    Store = models.Saptam_Collection.objects.all()
    obj ={"Store": Store}
    return render(req,"admin/Saptam_Collecation_Cards.html", obj)

def save_Saptam_Collection(req):
    Store = models.Saptam_Collection(
        Saptam_Collection_image=req.FILES['Saptam_Collection_image'],
        Saptam_Collection_Description=req.POST['Saptam_Collection_Description'],
        Saptam_Collection_Latest_price=req.POST['Saptam_Collection_Latest_price'],
        Saptam_Collection_old_price=req.POST['Saptam_Collection_old_price'],
    )
    Store.save()
    return redirect("/admin/Saptam_Collecation_Cards")

def delete_card_Saptam_Collection(req):
    id =req.GET['id']
    models.Saptam_Collection.objects.get(id = id).delete()
    return redirect("/admin/Saptam_Collecation_Cards")

def edit_Saptam_Collection(req):
    old_Data = models.Saptam_Collection.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_Saptam_Collection.html',obj)

def Update_Saptam_Collection(req):
    edit_artical =models.Saptam_Collection.objects.get(id=req.POST['id']) 
    edit_artical.Saptam_Collection_image = req.FILES['Saptam_Collection_image']
    edit_artical.Saptam_Collection_Description = req.POST['Saptam_Collection_Description']
    edit_artical.Saptam_Collection_Latest_price = req.POST['Saptam_Collection_Latest_price']
    edit_artical.Saptam_Collection_old_price = req.POST['Saptam_Collection_old_price']
    edit_artical.save()
    return redirect("/admin/Saptam_Collecation_Cards")

def Aarya(req):
    arys = models.Aaryas.objects.all()
    obj ={"arys": arys}
    return render(req,"admin/Aarya.html", obj)

def save_Aarya_card(req):
    arys = models.Aaryas(
        Aarya_image=req.FILES['Aarya_image'],
        Aarya_Description=req.POST['Aarya_Description'],
        Aarya_Latest_price=req.POST['Aarya_Latest_price'],
        Aarya_old_price=req.POST['Aarya_old_price'],
    )
    arys.save()
    return redirect("/admin/Aarya")

def delete_card_Aarya(req):
    id =req.GET['id']
    models.Aaryas.objects.get(id = id).delete()
    return redirect("/admin/Aarya")

def edit_Aarya(req):
    old_Data = models.Aaryas.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_Aarya.html',obj)

def Update_Aarya(req):
    edit_artical =models.Aaryas.objects.get(id=req.POST['id']) 
    edit_artical.Aarya_image = req.FILES['Aarya_image']
    edit_artical.Aarya_Description = req.POST['Aarya_Description']
    edit_artical.Aarya_Latest_price = req.POST['Aarya_Latest_price']
    edit_artical.Aarya_old_price = req.POST['Aarya_old_price']
    edit_artical.save()
    return redirect("/admin/Aarya")

def zodias(req):
    zodiass = models.Zodias.objects.all()
    obj ={"zodiass": zodiass}
    return render(req,"admin/zodias.html", obj)

def save_zodias_card(req):
    zodiass = models.Zodias(
        zodias_image=req.FILES['zodias_image'],
        zodias_Description=req.POST['zodias_Description'],
        zodias_Latest_price=req.POST['zodias_Latest_price'],
        zodias_old_price=req.POST['zodias_old_price'],
    )
    zodiass.save()
    return redirect("/admin/zodias")

def delete_card_zodias(req):
    id=req.GET['id']
    models.Zodias.objects.get(id =id).delete()
    return redirect("/admin/zodias")

def edit_zodias(req):
    old_Data = models.Zodias.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_zodias.html',obj)

def Update_Zodias(req):
    edit_artical =models.Zodias.objects.get(id=req.POST['id']) 
    edit_artical.zodias_image = req.FILES['zodias_image']
    edit_artical.zodias_Description = req.POST['zodias_Description']
    edit_artical.zodias_Latest_price = req.POST['zodias_Latest_price']
    edit_artical.zodias_old_price = req.POST['zodias_old_price']
    edit_artical.save()
    return redirect("/admin/zodias")


def color_stone(req):
    Stones = models.Colour_Stones.objects.all()
    obj ={"Stones": Stones}
    return render(req,"admin/color_stone.html", obj)

def save_Colour_Stones_card(req):
    Stones = models.Colour_Stones(
        Colour_Stones_image=req.FILES['Colour_Stones_image'],
        Colour_Stones_Description=req.POST['Colour_Stones_Description'],
        Colour_Stones_Latest_price=req.POST['Colour_Stones_Latest_price'],
        Colour_Stones_old_price=req.POST['Colour_Stones_old_price'],
    )
    Stones.save()
    return redirect("/admin/color_stone")
def delete_card_Colour_Stones(req):
    id = req.GET['id']
    models.Colour_Stones.objects.get(id = id).delete()
    return redirect("/admin/color_stone")

def edit_Colour_Stones(req):
    old_Data = models.Colour_Stones.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,'admin/edit_Colour_Stones.html',obj)

def Update_Colour_Stones(req):
    edit_artical =models.Colour_Stones.objects.get(id=req.POST['id']) 
    edit_artical.Colour_Stones_image = req.FILES['Colour_Stones_image']
    edit_artical.Colour_Stones_Description = req.POST['Colour_Stones_Description']
    edit_artical.Colour_Stones_Latest_price = req.POST['Colour_Stones_Latest_price']
    edit_artical.Colour_Stones_old_price = req.POST['Colour_Stones_old_price']
    edit_artical.save()
    return redirect("/admin/color_stone")

def police_polki(req):
    return render(req,"admin/police_polki.html")

def Police_Polki_Slider(req):
    banner=models.Police_Polki.objects.all()
    obj ={"banner": banner}
    return render(req,"admin/Police_Polki_Slider.html", obj)

def upload_banner_Police_Polki(req):
    banner=models.Police_Polki(
        banner_Image_Police_Polki=req.FILES['banner_Image_Police_Polki'],
    )
    banner.save()
    return redirect("/admin/Police_Polki_Slider")

def delete_banner_Police_Polki(req):
    id = req.GET['id']
    models.Police_Polki.objects.get(id = id).delete()
    return redirect("/admin/Police_Polki_Slider")

def Police_Polki_Cards(req):
    PolicCard=models.Police_Polki_Cards.objects.all()
    obj ={"PolicCard": PolicCard}
    return render(req,"admin/Police_Polki_Cards.html", obj)

def save_Police_Polki_Cards(req):
    PolicCard=models.Police_Polki_Cards(
        Police_Polki_image=req.FILES['Police_Polki_image'],
        Police_Polki_Description=req.POST['Police_Polki_Description'],
        Police_Polki_price=req.POST['Police_Polki_price'],
        Police_Polki_old_price=req.POST['Police_Polki_old_price'],
    )
    PolicCard.save()
    return redirect("/admin/Police_Polki_Cards")

def delete_card_PolicCard(req):
    id = req.GET['id']
    models.Police_Polki_Cards.objects.get(id = id).delete()
    return redirect("/admin/Police_Polki_Cards")

def edit_card_PolicCard(req):
    old_Data = models.Police_Polki_Cards.objects.get(id = req.GET['id'])
    obj ={'old_Data':old_Data}
    return render(req,"admin/edit_card_PolicCard.html", obj)

def edit_PolicCard_card(req):
    edit_artical =models.Police_Polki_Cards.objects.get(id=req.POST['id']) 
    edit_artical.Police_Polki_image = req.FILES['Police_Polki_image']
    edit_artical.Police_Polki_Description = req.POST['Police_Polki_Description']
    edit_artical.Police_Polki_price = req.POST['Police_Polki_price']
    edit_artical.Police_Polki_old_price = req.POST['Police_Polki_old_price']
    edit_artical.save()
    return redirect("/admin/Police_Polki_Cards")

def Trendy_mo_d_mangalsutra(req):
    return render(req,"admin/Trendy_mo_d_mangalsutra.html")

def Drops_mangalsutraCard(req):
    mangalsutra = models.Mangalsutra.objects.all()
    obj ={"mangalsutra": mangalsutra}
    return render(req,"admin/Drops_mangalsutraCard.html", obj)

def save_card_mangalsutra(req):
    mangalsutra = models.Mangalsutra(
        mangalsutra_image = req.FILES['mangalsutra_image'],
        mangalsutra_title = req.POST['mangalsutra_title'],
        mangalsutra_Latest_price = req.POST['mangalsutra_Latest_price'],
        mangalsutra_price = req.POST['mangalsutra_price'],
    )
    mangalsutra.save()
    return redirect("/admin/Drops_mangalsutraCard")

def delete_card_mangalsutra(req):
    id = req.GET['id']
    models.Mangalsutra.objects.get(id = id).delete()
    return redirect("/admin/Drops_mangalsutraCard")

def edit_card_mangalsutra(req):
    old_Data = models.Mangalsutra.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,'admin/edit_card_mangalsutra.html',obj)


def edit_Diamond_Drops_mangalsutraCard(req):
    edit_Heart = models.Mangalsutra.objects.get(id = req.POST['id'])
    edit_Heart.mangalsutra_image = req.FILES['mangalsutra_image']
    edit_Heart.mangalsutra_title = req.POST['mangalsutra_title']
    edit_Heart.mangalsutra_Latest_price = req.POST['mangalsutra_Latest_price']
    edit_Heart.mangalsutra_price = req.POST['mangalsutra_price']
    edit_Heart.save()
    return redirect("/admin/Drops_mangalsutraCard")

def Drop_mangalsutra_text(req):
    mangalsutra = models.Mangalsutras.objects.all()
    obj ={"mangalsutra": mangalsutra}
    return render(req,"admin/Drop_mangalsutra_text.html", obj)

def save_card_mangalsutras(req):
    mangalsutra = models.Mangalsutras(
        Mangalsutra_articleHeading = req.POST['Mangalsutra_articleHeading'],
        Mangalsutra_articleDescription = req.POST['Mangalsutra_articleDescription'],
    )
    mangalsutra.save()
    return redirect("/admin/Drop_mangalsutra_text")

def delete_mangalsutra(req):
    id = req.GET['id']
    models.Mangalsutras.objects.get(id = id).delete()
    return redirect("/admin/Drop_mangalsutra_text")

def edit_mangalsutra(req):
    old_Data = models.Mangalsutras.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,"admin/edit_mangalsutra.html", obj)


def edit_Diamond_mangalsutra(req):
    edit_Heart = models.Mangalsutras.objects.get(id = req.POST['id'])
    edit_Heart.Mangalsutra_articleHeading = req.POST['Mangalsutra_articleHeading']
    edit_Heart.Mangalsutra_articleDescription = req.POST['Mangalsutra_articleDescription']
    edit_Heart.save()
    return redirect("/admin/Drop_mangalsutra_text")

def Kurta_Button(req):
    Kurta = models.KurtaPage.objects.all()
    obj ={"Kurta": Kurta}
    return render(req,"admin/Kurta_Button.html", obj)

def Kurta_page_card_Data(req):
    Kurta = models.KurtaPage(
        Kurta_image = req.FILES['Kurta_image'],
        Kurta_title = req.POST['Kurta_title'],
        Kurta_latest_price = req.POST['Kurta_latest_price'],
        Kurta_old_price = req.POST['Kurta_old_price'],
    )
    Kurta.save()
    return redirect("/admin/Kurta_Button")

def delete_card_Kurta(req):
    id = req.GET['id']
    models.KurtaPage.objects.get(id = id).delete()
    return redirect("/admin/Kurta_Button")

def edit_card_Kurta(req):
    old_Data = models.KurtaPage.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,"admin/edit_card_Kurta.html", obj)


def edit_Diamond_KurtaPage(req):
    edit_Heart = models.KurtaPage.objects.get(id = req.POST['id'])
    edit_Heart.Kurta_image = req.FILES['Kurta_image']
    edit_Heart.Kurta_title = req.POST['Kurta_title']
    edit_Heart.Kurta_latest_price = req.POST['Kurta_latest_price']
    edit_Heart.Kurta_old_price = req.POST['Kurta_old_price']
    edit_Heart.save()
    return redirect("/admin/Kurta_Button")

def Gold_Jhumkas(req):
    Gold = models.Gold_Jhumkass.objects.all()
    obj ={"Gold": Gold}
    return render(req,"admin/Gold_Jhumkas.html", obj)

def Gold_Jhumkas_card_Data(req):
    Gold = models.Gold_Jhumkass(
        Gold_Jhumkas_image = req.FILES['Gold_Jhumkas_image'],
        Gold_Jhumkas_image_title = req.POST['Gold_Jhumkas_image_title'],
        Gold_Jhumkas_latest_price = req.POST['Gold_Jhumkas_latest_price'],
        Gold_Jhumkas_old_price = req.POST['Gold_Jhumkas_old_price'],
    )
    Gold.save()
    return redirect("/admin/Gold_Jhumkas")

def delete_card_Gold_Jhumkas(req):
    id= req.GET['id']
    models.Gold_Jhumkass.objects.get(id = id).delete()

    return redirect("/admin/Gold_Jhumkas")

def edit_card_Gold_Jhumkas(req):
    old_Data = models.Gold_Jhumkass.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,"admin/edit_card_Gold_Jhumkas.html", obj)


def edit_Diamond_Gold_Jhumkas(req):
    edit_Heart = models.Gold_Jhumkass.objects.get(id = req.POST['id'])
    edit_Heart.Gold_Jhumkas_image = req.FILES['Gold_Jhumkas_image']
    edit_Heart.Gold_Jhumkas_image_title = req.POST['Gold_Jhumkas_image_title']
    edit_Heart.Gold_Jhumkas_latest_price = req.POST['Gold_Jhumkas_latest_price']
    edit_Heart.Gold_Jhumkas_old_price = req.POST['Gold_Jhumkas_old_price']
    edit_Heart.save()
    return redirect("/admin/Gold_Jhumkas")

def Gold_Menstuds(req):
    Gold = models.Gold_Menstuds.objects.all()
    obj ={"Gold": Gold}
    return render(req,"admin/Gold_Menstuds.html", obj)

def Gold_Menstuds_card_Data(req):
    Gold = models.Gold_Menstuds(
        Gold_Menstuds_image = req.FILES['Gold_Menstuds_image'],
        Gold_Menstuds_image_title = req.POST['Gold_Menstuds_image_title'],
        Gold_Menstuds_latest_price = req.POST['Gold_Menstuds_latest_price'],
        Gold_Menstuds_old_price = req.POST['Gold_Menstuds_old_price'],
    )
    Gold.save()
    return redirect("/admin/Gold_Menstuds")

def delete_card_Gold_Menstuds(req):
    id = req.GET['id']
    models.Gold_Menstuds.objects.get(id = id ).delete()
    return redirect("/admin/Gold_Menstuds")

def edit_card_Gold_Menstuds(req):
    old_Data = models.Gold_Menstuds.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,"admin/edit_card_Gold_Menstuds.html", obj)


def edit_Diamond_Gold_Menstuds(req):
    edit_Heart = models.Gold_Menstuds.objects.get(id = req.POST['id'])
    edit_Heart.Gold_Menstuds_image = req.FILES['Gold_Menstuds_image']
    edit_Heart.Gold_Menstuds_image_title = req.POST['Gold_Menstuds_image_title']
    edit_Heart.Gold_Menstuds_latest_price = req.POST['Gold_Menstuds_latest_price']
    edit_Heart.Gold_Menstuds_old_price = req.POST['Gold_Menstuds_old_price']
    edit_Heart.save()
    return redirect("/admin/Gold_Menstuds")

def Gold_GoldBracelets(req):
    Gold = models.Gold_GoldBraceletss.objects.all()
    obj ={"Gold": Gold}
    return render(req,"admin/Gold_GoldBracelets.html", obj)

def Gold_GoldBracelets_card_Data(req):
    Gold = models.Gold_GoldBraceletss(
        Gold_GoldBracelets_image = req.FILES['Gold_GoldBracelets_image'],
        Gold_GoldBracelets_image_title = req.POST['Gold_GoldBracelets_image_title'],
        Gold_GoldBracelets_latest_price = req.POST['Gold_GoldBracelets_latest_price'],
        Gold_GoldBracelets_old_price = req.POST['Gold_GoldBracelets_old_price'],
    )
    Gold.save()
    return redirect("/admin/Gold_GoldBracelets")

def delete_card_Gold_GoldBracelets(req):
    id = req.GET['id']
    models.Gold_GoldBraceletss.objects.get(id = id).delete()
    return redirect("/admin/Gold_GoldBracelets")

def edit_card_Gold_GoldBracelets(req):
    old_Data = models.Gold_GoldBraceletss.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,"admin/edit_card__Gold_GoldBracelets.html", obj)


def edit_Diamond_GoldBracelets(req):
    edit_Heart = models.Gold_GoldBraceletss.objects.get(id = req.POST['id'])
    edit_Heart.Gold_GoldBracelets_image = req.FILES['Gold_GoldBracelets_image']
    edit_Heart.Gold_GoldBracelets_image_title = req.POST['Gold_GoldBracelets_image_title']
    edit_Heart.Gold_GoldBracelets_latest_price = req.POST['Gold_GoldBracelets_latest_price']
    edit_Heart.Gold_GoldBracelets_old_price = req.POST['Gold_GoldBracelets_old_price']
    edit_Heart.save()
    return redirect("/admin/Gold_GoldBracelets")

def Gold_vedhani(req):
    Gold = models.Gold_vedhani.objects.all()
    obj ={"Gold": Gold}
    return render(req,"admin/Gold_vedhani.html", obj)


def Gold_vedhani_card_Data(req):
    Gold = models.Gold_vedhani(
        Gold_vedhani_image = req.FILES['Gold_vedhani_image'],
        Gold_vedhani_image_title = req.POST['Gold_vedhani_image_title'],
        Gold_vedhani_latest_price = req.POST['Gold_vedhani_latest_price'],
        Gold_vedhani_old_price = req.POST['Gold_vedhani_old_price'],
    )
    Gold.save()
    return redirect("/admin/Gold_vedhani")

def delete_card_Gold_vedhani(req):
    id = req.GET['id']
    models.Gold_vedhani.objects.get(id = id).delete()
    return redirect("/admin/Gold_vedhani")

def edit_card_Gold_vedhani(req):
    old_Data = models.Gold_vedhani.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,"admin/edit_card__Gold_vedhani.html", obj)


def edit_Diamond_Gold_vedhani(req):
    edit_Heart = models.Gold_vedhani.objects.get(id = req.POST['id'])
    edit_Heart.Gold_vedhani_image = req.FILES['Gold_vedhani_image']
    edit_Heart.Gold_vedhani_image_title = req.POST['Gold_vedhani_image_title']
    edit_Heart.Gold_vedhani_latest_price = req.POST['Gold_vedhani_latest_price']
    edit_Heart.Gold_vedhani_old_price = req.POST['Gold_vedhani_old_price']
    edit_Heart.save()
    return redirect("/admin/Gold_vedhani")

def Gold_plain(req):
 data = models.GoldPlain.objects.all()
 obj = {'data':data}
 return render(req,'admin/Gold_plain.html',obj)

# Rohit

def Gold_plain_wear_save(req):
 plain = models.GoldPlain(
 productImage = req.FILES['productImage'],
 productTitle = req.POST['productTitle'],
 latestPrice = req.POST['latestPrice'],
 oldPrice = req.POST['oldPrice'],
 )
 plain.save()
 return redirect("/admin/Gold_plain")


def delete_Gold_plain_wear(req):
    id = req.GET['id']
    models.GoldPlain.objects.get(id=id).delete()
    return redirect("/admin/Gold_plain")

def Edit_Gold_plain_wear(req):
 old_Data = models.GoldPlain.objects.get(id = req.GET['id'])
 obj = {'old_Data':old_Data}
 return render(req,'admin/Edit_Gold_plain_wear.html',obj)



def edit_Gold_plain_card_da(req):
    edit_gold_plain = models.GoldPlain.objects.get(id = req.POST['id'])
    edit_gold_plain.productImage = req.FILES['cardImage_edit']
    edit_gold_plain.productTitle = req.POST['imgTitle_edit']
    edit_gold_plain.latestPrice = req.POST['latestPrice_edit']
    edit_gold_plain.oldPrice = req.POST['oldPrice_edit']
    edit_gold_plain.save()
    return redirect("/admin/Gold_plain")

def PNG(req):
 data = models.GoldPNG.objects.all()
 obj = {'data':data}
 return render(req,'admin/PNG.html',obj)


def Gold_PNG_wear_save(req):
    png = models.GoldPNG(
    productImage = req.FILES['productImage'],
    productTitle = req.POST['productTitle'],
    latestPrice = req.POST['latestPrice'],
    oldPrice = req.POST['oldPrice'],
   )
    png.save()
    return redirect("/admin/PNG")

def delete_Gold_png_wear(req):
 id = req.GET['id']
 models.GoldPNG.objects.get(id = id).delete()
 return redirect("/admin/PNG")

def Edit_Gold_png_wear(req):
 old_Data = models.GoldPNG.objects.get(id = req.GET['id'])
 obj = {'old_Data':old_Data}
 return render(req,'admin/Edit_Gold_png_wear.html',obj)

def edit_Gold_png_card_da(req):
    edit_gold_png = models.GoldPNG.objects.get(id = req.POST['id'])
    edit_gold_png.productImage = req.FILES['cardImage_edit']
    edit_gold_png.productTitle = req.POST['imgTitle_edit']
    edit_gold_png.latestPrice = req.POST['latestPrice_edit']
    edit_gold_png.oldPrice = req.POST['oldPrice_edit']
    edit_gold_png.save()
    return redirect("/admin/PNG")


# ----
def delete_bast_slider(req):
    order_id=req.GET['id']
    models.Index_Bast_Slider.objects.get(id = order_id).delete()
    return redirect("/admin/Best_Slider")

def edit_bast_slider(req):
    edit_info = models.Index_Bast_Slider.objects.get(id=req.GET['id'])
    obj={"edit_info":edit_info}
    return render(req,"admin/edit_bast_slider.html", obj)


def update_info_bast_slider(req):
    update=models.Index_Bast_Slider.objects.get(id=req.POST['id'])
    update.bast_Slider_imgase=req.FILES['bast_Slider_imgase']
    update.bast_Slider_Name=req.POST['bast_Slider_Name']
    update.bast_Slider_Description=req.POST['bast_Slider_Description']
    update.bast_Slider_Price=req.POST['bast_Slider_Price']
    
    update.save()
    return redirect("/admin/Best_Slider")


def Gold_laxmi_shree(req):
    save_Gold_laxmi = models.Gold_laxmi.objects.all()
    obj ={"save_Gold_laxmi": save_Gold_laxmi}
    return render(req,"admin/Gold_laxmi_shree.html", obj)

def Save_Gold_laxmi_shree(req):
    data = models.Gold_laxmi(
        Gold_laxmi_image = req.FILES['Gold_laxmi_image'],
        Gold_laxmi_Description = req.POST['Gold_laxmi_Description'],
        Gold_laxmi_Latest_price = req.POST['Gold_laxmi_Latest_price'],
    )
    data.save()
    return redirect("/admin/Gold_laxmi_shree")

def delete_card_Gold_laxmi(req):
    id = req.GET['id']
    models.Gold_laxmi.objects.get(id = id).delete()
    return redirect("/admin/Gold_laxmi_shree")

def edit_Gold_laxmi(req):
    old_Data = models.Gold_laxmi.objects.get(id = req.GET['id'])
    obj = {'old_Data':old_Data}
    return render(req,"admin/edit_Gold_laxmi.html", obj)


def update_Gold_laxmi(req):
    edit_Heart = models.Gold_laxmi.objects.get(id = req.POST['id'])
    edit_Heart.Gold_laxmi_image = req.FILES['Gold_laxmi_image']
    edit_Heart.Gold_laxmi_Description = req.POST['Gold_laxmi_Description']
    edit_Heart.Gold_laxmi_Latest_price = req.POST['Gold_laxmi_Latest_price']
    edit_Heart.save()
    return redirect("/admin/Gold_laxmi_shree")

def Studs_Erings(req):
    return render(req,'admin/Studs_Erings.html')

# karan
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Casual_ring
from django.core.files.storage import FileSystemStorage


# crud #
def Diamondrings_bands(req):
    diamondrings_bands = models.Diamondrings_bands.objects.all()
    obj= {"diamondrings_bands":diamondrings_bands}
    return render(req, "admin/Diamondrings_bands.html",obj)


def save_Diamondrings(req):
    rings = models.Diamondrings_bands(
        dimaonderings_image=req.FILES['rings_image'],
        diamondrings_pricce=req.POST['rings_price'],
        diamondrings_text=req.POST['rings_text']
    )
    rings.save()
    return redirect("/admin/Diamondrings_bands")

# delete  bands
def delete_bands_ring(req):
    if req.method == 'POST':
        ban_id = req.POST.get('id')
        if not ban_id:
            return HttpResponseBadRequest("ID not provided")
        bands_ring = get_object_or_404(models.Diamondrings_bands, id=ban_id)
        bands_ring.delete()
        
        return redirect("/admin/Diamondrings_bands")

    return HttpResponseBadRequest("Invalid request method")


# edit bands

def edit_bands_ring(req):
    old_bands = models.Diamondrings_bands.objects.get(id = req.GET['id'])
    obj = {"old_bands":old_bands}
    return render(req,"admin/edit_bands_ring.html",obj)
    # return HttpResponse ("edit")

def update_Diamondrings(req):
    old_bands = models.Diamondrings_bands.objects.get(id = req.POST['id'])
    old_bands.dimaonderings_image = req.FILES['dimaonderings_image']
    old_bands.diamondrings_pricce = req.POST['diamondrings_pricce']
    old_bands.diamondrings_text = req.POST['diamondrings_text']
    old_bands.save()
    return redirect('/admin/Diamondrings_bands')




# eng crud #
def Diamond_engagement_ring(req):
    diamondring_engagement_ring = models.Diamond_engagement_ring.objects.all()
    obj = {"diamondring_engagement_ring":diamondring_engagement_ring}
    return render(req,"admin/Diamond_engagement_ring.html",obj)

def save_engagement_ring(req):
    enagagement_rings = models.Diamond_engagement_ring(
      enagagement_image =req.FILES['enagagement_image'],
	  enagagement_price = req.POST['enagagement_price'],
	  enagagement_text = req.POST['enagagement_description']
    )
    enagagement_rings.save()
    return redirect("/admin/Diamond_engagement_ring")

#eng delte#

def delete_engagement_ring(req):
    if req.method == 'POST':
        eng_id = req.POST.get('id')
        if not eng_id:
            return HttpResponseBadRequest("ID not provided")
        engagement_ring = get_object_or_404(models.Diamond_engagement_ring, id=eng_id)
        engagement_ring.delete()
        
        return redirect("/admin/Diamond_engagement_ring")

    return HttpResponseBadRequest("Invalid request method")

# eng edit

def edit_engagement_ring(req):
    old_engagement = models.Diamond_engagement_ring.objects.get(id = req.GET['id'])
    obj = {"old_engagement":old_engagement}
    return render(req,"admin/edit_engagement_ring.html",obj)

def update_engagement(req):
    old_engagement = models.Diamond_engagement_ring.objects.get(id = req.POST['id'])
    old_engagement.enagagement_image = req.FILES['enagagement_image']
    old_engagement.enagagement_price = req.POST['enagagement_price']
    old_engagement.enagagement_text = req.POST['enagagement_text']
    old_engagement.save()
    return redirect('/admin/Diamond_engagement_ring')

# fashion crud #

def Diamond_fashion_ring(req):
    fashion_ring = models.Diamond_fashion_ring.objects.all()
    obj= {"fashion_ring":fashion_ring}
    return render(req,"admin/Diamond_fashion_ring.html",obj)

def save_fashion_ring(req):
    diamond_ring_fashion = models.Diamond_fashion_ring(
        image_fashion = req.FILES['image_fashion'],
        price_fashion = req.POST['price_fashion'],
        text_fashion = req.POST['text_fashion']
    )
    diamond_ring_fashion.save()
    return redirect("/admin/Diamond_fashion_ring")
# fashion delete#

def delete_fashion_ring(req):
    if req.method == 'POST':
        fas_id = req.POST.get('id')
        if not fas_id:
            return HttpResponseBadRequest("ID not provided")
        fashion_ring = get_object_or_404(models.Diamond_fashion_ring, id=fas_id)
        fashion_ring.delete()
        
        return redirect("/admin/Diamond_fashion_ring")

    return HttpResponseBadRequest("Invalid request method")



# edit fashion# 

def edit_fashion_ring(req):
    old_fashion = models.Diamond_fashion_ring.objects.get(id = req.GET['id'])
    obj = {"old_fashion":old_fashion}
    return render(req,"admin/edit_fashion_ring.html",obj)
    # return HttpResponse ("edit")

def update_fashion(req):
    old_fashion = models.Diamond_fashion_ring.objects.get(id = req.POST['id'])
    old_fashion.image_fashion = req.FILES['image_fashion']
    old_fashion.price_fashion = req.POST['price_fashion']
    old_fashion.text_fashion = req.POST['text_fashion']
    old_fashion.save()
    return redirect('/admin/Diamond_fashion_ring')


# casual ring crud
def Diamond_casual_ring(req):
    ring_casual = models.Casual_ring.objects.all()
    obj = {"ring_casual":ring_casual}
    return render(req,"admin/Diamond_casual_ring.html",obj)


def save_casual_ring(req):
    casual = models.Casual_ring(
    casualring_image = req.FILES['casualring_image'],
	casualring_price = req.POST['casualring_price'],
	casualring_text = req.POST['casualring_text']
    )
    casual.save()
    return redirect("/admin/Diamond_casual_ring")


# delete casual

def delete_casual_ring(req):
    if req.method == 'POST':
        ring_id = req.POST.get('id')
        if not ring_id:
            return HttpResponseBadRequest("ID not provided")
        casual_ring = get_object_or_404(models.Casual_ring, id=ring_id)
        casual_ring.delete()
        
        return redirect("/admin/Diamond_casual_ring")

    return HttpResponseBadRequest("Invalid request method")

# edit casual #
def edit_casual_ring(req, ring_id):
    ring = get_object_or_404(Casual_ring, id=ring_id)

    if req.method == "POST":
        casualring_image = req.FILES.get('casualring_image', None)
        casualring_price = req.POST.get('casualring_price')
        casualring_text = req.POST.get('casualring_text')

        if casualring_image:
            ring.casualring_image = casualring_image
        
        ring.casualring_price = casualring_price
        ring.casualring_text = casualring_text
        ring.save()

        return redirect('/admin/Diamond_casual_ring')

    return render(req, 'admin/edit_casual_ring.html', {'ring': ring})


#       Akshay Bodkhe

#  Gold Vedhani Start
def gold_vedhani(req):
    vedhani = models.Gold_Vedhani1.objects.all()
    obj = {"vedhani":vedhani}
    return render(req,"admin/gold_vedhani.html",obj)

def save_gold_vedhani(req):
    vedhani = models.Gold_Vedhani1(
        gold_vedhani_image = req.FILES['gold_vedhani_image'],
        gold_vedhani_price = req.POST['gold_vedhani_price'],
        gold_vedhani_text = req.POST['gold_vedhani_text']
    )
    vedhani.save()
    # return HttpResponse("Saved")
    return redirect("/admin/gold_vedhani")

def edit_gold_vedhani(req):
    old_vedhani = models.Gold_Vedhani1.objects.get(id = req.GET['id'])
    obj = {"old_vedhani":old_vedhani}
    return render(req,"admin/edit_gold_vedhani.html",obj)

def update_gold_vedhani(req):
    old_vedhani = models.Gold_Vedhani1.objects.get(id = req.POST['id'])
    old_vedhani.gold_vedhani_image = req.FILES['gold_vedhani_image']
    old_vedhani.gold_vedhani_price = req.POST['gold_vedhani_price']
    old_vedhani.gold_vedhani_text = req.POST['gold_vedhani_text']
    old_vedhani.save()
    # return HttpResponse("Update")
    return redirect("/admin/gold_vedhani")

def delete_gold_vedhani(req):
    old_vedhani = models.Gold_Vedhani1.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/gold_vedhani")

#  Gold Vedhani End

#  Gold Plain Start
def gold_plain(req):
    plain = models.Gold_Plain.objects.all()
    obj = {"plain":plain}
    return render(req,"admin/gold_plain.html",obj)

def save_gold_plain(req):
    vedhani = models.Gold_Plain(
        gold_plain_image = req.FILES['gold_plain_image'],
        gold_plain_price = req.POST['gold_plain_price'],
        gold_plain_text = req.POST['gold_plain_text']
    )
    vedhani.save()
    # return HttpResponse("Saved")
    return redirect("/admin/gold_plain")

def edit_gold_plain(req):
    old_plain = models.Gold_Plain.objects.get(id = req.GET['id'])
    obj = {"old_plain":old_plain}
    return render(req,"admin/edit_gold_plain.html",obj)

def update_gold_plain(req):
    old_plain = models.Gold_Plain.objects.get(id = req.POST['id'])
    old_plain.gold_plain_image = req.FILES['gold_plain_image']
    old_plain.gold_plain_price = req.POST['gold_plain_price']
    old_plain.gold_plain_text = req.POST['gold_plain_text']
    old_plain.save()
    # return HttpResponse("Update")
    return redirect("/admin/gold_plain")

def delete_gold_plain(req):
    old_vedhani = models.Gold_Plain.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/gold_plain")

#  Gold Plain End


#  Gold laxmi_shree Start
def gold_laxmi_shree(req):
    laxmi_shree = models.Gold_Laxmi_Shree.objects.all()
    obj = {"laxmi_shree":laxmi_shree}
    return render(req,"admin/gold_laxmi_shree.html",obj)

def save_laxmi_shree(req):
    laxmi_shree = models.Gold_Laxmi_Shree(
        gold_laxmi_shree_image = req.FILES['gold_laxmi_shree_image'],
        gold_laxmi_shree_price = req.POST['gold_laxmi_shree_price'],
        gold_laxmi_shree_text = req.POST['gold_laxmi_shree_text']
    )
    laxmi_shree.save()
    # return HttpResponse("Saved")
    return redirect("/admin/gold_laxmi_shree")

def edit_gold_laxmi_shree(req):
    old_laxmi_shree = models.Gold_Laxmi_Shree.objects.get(id = req.GET['id'])
    obj = {"old_laxmi_shree":old_laxmi_shree}
    return render(req,"admin/edit_gold_laxmi_shree.html",obj)

def update_laxmi_shree(req):
    old_laxmi_shree = models.Gold_Laxmi_Shree.objects.get(id = req.POST['id'])
    old_laxmi_shree.gold_laxmi_shree_image = req.FILES['gold_laxmi_shree_image']
    old_laxmi_shree.gold_laxmi_shree_price = req.POST['gold_laxmi_shree_price']
    old_laxmi_shree.gold_laxmi_shree_text = req.POST['gold_laxmi_shree_text']
    old_laxmi_shree.save()
    # return HttpResponse("Update")
    return redirect("/admin/gold_laxmi_shree")

def delete_gold_laxmi_shree(req):
    old_laxmi_shree = models.Gold_Laxmi_Shree.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/gold_laxmi_shree")

#  Gold laxmi_shree End

#  Gold PNG Start
def png(req):
    png = models.Gold_PNG.objects.all()
    obj = {"png":png}
    return render(req,"admin/png.html",obj)

def save_gold_png(req):
    png = models.Gold_PNG(
       gold_png_image = req.FILES['gold_png_image'],
       gold_png_price = req.POST['gold_png_price'],
       gold_png_text = req.POST['gold_png_text']
    )
    png.save()
    # return HttpResponse("Saved")
    return redirect("/admin/png")

def edit_gold_png(req):
    old_png = models.Gold_PNG.objects.get(id = req.GET['id'])
    obj = {"old_png":old_png}
    return render(req,"admin/edit_gold_png.html",obj)

def update_gold_png(req):
    old_png = models.Gold_PNG.objects.get(id = req.POST['id'])
    old_png.gold_png_image = req.FILES['gold_png_image']
    old_png.gold_png_price = req.POST['gold_png_price']
    old_png.gold_png_text = req.POST['gold_png_text']
    old_png.save()
    # return HttpResponse("Update")
    return redirect("/admin/png")

def delete_gold_png(req):
    old_laxmi_shree = models.Gold_PNG.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/png")

#  Gold PNG End

#  Gold silver_ganesh_coin Start
def silver_ganesh_coin(req):
    silver_ganesh = models.Silver_Ganesh.objects.all()
    obj = {"silver_ganesh":silver_ganesh}
    return render(req,"admin/silver_ganesh_coin.html",obj)

def save_silver_ganesh(req):
    silver_ganesh = models.Silver_Ganesh(
       silver_ganesh_image = req.FILES['silver_ganesh_image'],
       silver_ganesh_price = req.POST['silver_ganesh_price'],
       silver_ganesh_text = req.POST['silver_ganesh_text']
    )
    silver_ganesh.save()
    # return HttpResponse("Saved")
    return redirect("/admin/silver_ganesh_coin")

def edit_silver_ganesh(req):
    old_silver_ganesh = models.Silver_Ganesh.objects.get(id = req.GET['id'])
    obj = {"old_silver_ganesh":old_silver_ganesh}
    return render(req,"admin/edit_silver_ganesh.html",obj)

def update_silver_ganesh(req):
    old_silver_ganesh = models.Silver_Ganesh.objects.get(id = req.POST['id'])
    old_silver_ganesh.silver_ganesh_image = req.FILES['silver_ganesh_image']
    old_silver_ganesh.silver_ganesh_price = req.POST['silver_ganesh_price']
    old_silver_ganesh.silver_ganesh_text = req.POST['silver_ganesh_text']
    old_silver_ganesh.save()
    # return HttpResponse("Update")
    return redirect("/admin/silver_ganesh_coin")

def delete_silver_ganesh(req):
    old_silver_ganesh = models.Silver_Ganesh.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/silver_ganesh_coin")

#   silver_ganesh_coin End

def Silver_Coin(req):
    return render(req,"admin/Silver_Coin.html")

#   pure_silver_chip Start

def pure_silver_chip(req):
    silver_chip = models.Silver_Chip.objects.all()
    obj = {"silver_chip":silver_chip}
    return render(req,"admin/pure_silver_chip.html",obj)

def save_silver_chip(req):
    silver_chip = models.Silver_Chip(
       silver_chip_image = req.FILES['silver_chip_image'],
       silver_chip_price = req.POST['silver_chip_price'],
       silver_chip_text = req.POST['silver_chip_text']
    )
    silver_chip.save()
    # return HttpResponse("Saved")
    return redirect("/admin/pure_silver_chip")

def edit_silver_chip(req):
    old_silver_chip = models.Silver_Chip.objects.get(id = req.GET['id'])
    obj = {"old_silver_chip":old_silver_chip}
    return render(req,"admin/edit_silver_chip.html",obj)

def update_silver_chip(req):
    old_silver_chip = models.Silver_Chip.objects.get(id = req.POST['id'])
    old_silver_chip.silver_chip_image = req.FILES['silver_chip_image']
    old_silver_chip.silver_chip_price = req.POST['silver_chip_price']
    old_silver_chip.silver_chip_text = req.POST['silver_chip_text']
    old_silver_chip.save()
    # return HttpResponse("Update")
    return redirect("/admin/pure_silver_chip")

def delete_silver_chip(req):
    old_silver_ganesh = models.Silver_Chip.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/pure_silver_chip")

#   pure_silver_chip End

#   silver_laxmi Start

def silver_laxmi(req):
    silver_laxmi = models.Silver_Laxmi.objects.all()
    obj = {"silver_laxmi":silver_laxmi}
    return render(req,"admin/silver_laxmi.html",obj)

def save_silver_laxmi(req):
    silver_laxmi = models.Silver_Laxmi(
       silver_laxmi_image = req.FILES['silver_laxmi_image'],
       silver_laxmi_price = req.POST['silver_laxmi_price'],
       silver_laxmi_text = req.POST['silver_laxmi_text']
    )
    silver_laxmi.save()
    # return HttpResponse("Saved")
    return redirect("/admin/silver_laxmi")

def edit_silver_laxmi(req):
    old_silver_laxmi = models.Silver_Laxmi.objects.get(id = req.GET['id'])
    obj = {"old_silver_laxmi":old_silver_laxmi}
    return render(req,"admin/edit_silver_laxmi.html",obj)

def update_silver_laxmi(req):
    old_silver_laxmi = models.Silver_Laxmi.objects.get(id = req.POST['id'])
    old_silver_laxmi.silver_laxmi_image = req.FILES['silver_laxmi_image']
    old_silver_laxmi.silver_laxmi_price = req.POST['silver_laxmi_price']
    old_silver_laxmi.silver_laxmi_text = req.POST['silver_laxmi_text']
    old_silver_laxmi.save()
    # return HttpResponse("Update")
    return redirect("/admin/silver_laxmi")

def delete_silver_laxmi(req):
    old_silver_laxmi = models.Silver_Laxmi.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/silver_laxmi")

#   silver_laxmi End


#   investors_image Start

def investors_image(req):
    investors = models.Investors.objects.all()
    obj = {"investors":investors}
    return render(req,"admin/investors_image.html",obj)

def save_investors(req):
    investors = models.Investors(
       investors_image = req.FILES['investors_image'],
    )
    investors.save()
    # return HttpResponse("Saved")
    return redirect("/admin/investors_image")

def edit_investors_image(req):
    old_investors = models.Investors.objects.get(id = req.GET['id'])
    obj = {"old_investors":old_investors}
    return render(req,"admin/edit_investors_image.html",obj)

def update_investors(req):
    old_investors = models.Investors.objects.get(id = req.POST['id'])
    old_investors.investors_image = req.FILES['investors_image']
    old_investors.save()
    # return HttpResponse("Update")
    return redirect("/admin/investors_image")

def delete_investors_image(req):
    old_investors = models.Investors.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/investors_image")

#   investors_image End

#   investors_contacts Start

def investors_contacts(req):
    investors = models.Investors_Contact.objects.all()
    obj = {"investors":investors}
    return render(req,"admin/investors_contacts.html",obj)

def save_investor_contacts(req):
    investors = models.Investors_Contact(
       contact_name= req.POST['contact_name'],
       contact_mobile= req.POST['contact_mobile'],
       contact_email= req.POST['contact_email'],
       contact_address= req.POST['contact_address'],
    )
    investors.save()
    # return HttpResponse("Saved")
    return redirect("/admin/investors_contacts")

def edit_investor_contacts(req):
    investor_contacts = models.Investors_Contact.objects.get(id = req.GET['id'])
    obj = {"investor_contacts":investor_contacts}
    return render(req,"admin/edit_investor_contacts.html",obj)

def update_investor_contacts(req):
    investor_contacts = models.Investors_Contact.objects.get(id = req.POST['id'])
    investor_contacts.contact_name = req.POST['contact_name']
    investor_contacts.contact_mobile = req.POST['contact_mobile']
    investor_contacts.contact_email = req.POST['contact_email']
    investor_contacts.contact_address = req.POST['contact_address']
    investor_contacts.save()
    # return HttpResponse("Update")
    return redirect("/admin/investors_contacts")

def delete_investor_contacts(req):
    investor_contacts = models.Investors_Contact.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/investors_contacts")

#   investors_contacts End

#   annual_reports Start

def annual_reports(req):
    annual = models.AnnualReport1.objects.all()
    obj = {"annual":annual}
    return render(req,"admin/annual_reports.html",obj)

def save_annual_report(req):
    Annual = models.AnnualReport1(
       annual_report = req.FILES['annual_report'],
       annual_report_details= req.POST['annual_report_details'],
    )
    Annual.save()
    # return HttpResponse("Saved")
    return redirect("/admin/annual_reports")


def delete_annual_report(req):
    Annual = models.AnnualReport1.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/annual_reports")

#   annual_reports End

#   policies Start
def corporate_policies(req):
    policies = models.Policies.objects.all()
    obj = {"policies":policies}
    return render(req,"admin/corporate_policies.html",obj)

def save_policies(req):
    policies = models.Policies(
       policies = req.FILES['policies'],
       policies_details= req.POST['policies_details'],
    )
    policies.save()
    # return HttpResponse("Saved")
    return redirect("/admin/policies")

def delete_policies(req):
    policies = models.Policies.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/policies")

#   policies End

#   Risk policies1 Start

def policies1(req):
    policies1 = models.Risk_Policies.objects.all()
    obj = {"policies1":policies1}
    return render(req,"admin/policies1.html",obj)

def save_policies1(req):
    policies1 = models.Risk_Policies(
       policies1 = req.FILES['policies1'],
       policies1_details= req.POST['policies1_details'],
    )
    policies1.save()
    # return HttpResponse("Saved")
    return redirect("/admin/corporate_social")

def delete_policies1(req):
    reports = models.Risk_Policies.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/corporate_social")

#   Risk policies1 End

#   Post policies Start

def post_policies(req):
    post_policies = models.Post_Policies.objects.all()
    obj = {"post_policies":post_policies}
    return render(req,"admin/post_policies.html",obj)

def save_post_policies(req):
    post_policies = models.Post_Policies(
       post_policies = req.FILES['post_policies'],
       post_policies_details= req.POST['post_policies_details'],
    )
    post_policies.save()
    # return HttpResponse("Saved")
    return redirect("/admin/post_policies")

def delete_post_policies(req):
    reports = models.Post_Policies.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/post_policies")

#   Post policies End

#   corporate_governance Start
def corporate_governance(req):
    corporate = models.Corporate.objects.all()
    obj = {"corporate":corporate}
    return render(req,"admin/corporate_governance.html",obj)

def save_corporate(req):
    corporate = models.Corporate(
       corporate = req.FILES['corporate'],
       corporate_details= req.POST['corporate_details'],
    )
    corporate.save()
    # return HttpResponse("Saved")
    return redirect("/admin/corporate_governance")

def delete_corporate(req):
    policies = models.Corporate.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/corporate_governance")

#   corporate_governance End

#    material_documents Start

def material_documents(req):
    material_documents = models.Material_Documents.objects.all()
    obj = {"material_documents":material_documents}
    return render(req,"admin/material_documents.html",obj)

def save_material_documents(req):
    material_documents = models.Material_Documents(
       material_documents = req.FILES['material_documents'],
       material_documents_details= req.POST['material_documents_details'],
    )
    material_documents.save()
    # return HttpResponse("Saved")
    return redirect("/admin/material_documents")

def delete_material_documents(req):
    material_documents = models.Material_Documents.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/material_documents")

#   material_documents  End

#    ipo_documents Start

def ipo_documents(req):
    ipo_documents = models.Ipo_Documents.objects.all()
    obj = {"ipo_documents":ipo_documents}
    return render(req,"admin/ipo_documents.html",obj)

def save_ipo_documents(req):
    ipo_documents = models.Ipo_Documents(
       ipo_documents = req.FILES['ipo_documents'],
       ipo_documents_details= req.POST['ipo_documents_details'],
    )
    ipo_documents.save()
    # return HttpResponse("Saved")
    return redirect("/admin/ipo_documents")

def delete_ipo_documents(req):
    ipo_documents = models.Ipo_Documents.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/ipo_documents")
#   ipo_documents  End


#   group_gompanies Start
def group_gompanies(req):
    group = models.Group.objects.all()
    obj = {"group":group}
    return render(req,"admin/group_gompanies.html",obj)

def save_group(req):
    group = models.Group(
       group_companies = req.FILES['group_companies'],
       group_companies_details= req.POST['group_companies_details'],
    )
    group.save()
    # return HttpResponse("Saved")
    return redirect("/admin/group_gompanies")

def delete_group_companies(req):
    policies = models.Group.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/group_gompanies")

#   group_gompanies End


#   fixed_deposit Start
def fixed_deposit(req):
    deposit = models.Fixed_Deposit.objects.all()
    obj = {"deposit":deposit}
    return render(req,"admin/fixed_deposit.html",obj)

def save_fixed_deposit(req):
    fixed_deposit = models.Fixed_Deposit(
       fixed_deposit = req.FILES['fixed_deposit'],
       fixed_deposit_details= req.POST['fixed_deposit_details'],
    )
    fixed_deposit.save()
    # return HttpResponse("Saved")
    return redirect("/admin/fixed_deposit")

def delete_fixed_deposit(req):
    fixed_deposit = models.Fixed_Deposit.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/fixed_deposit")

#   fixed_deposit End

#   financial_results Start
def financial_results(req):
    results = models.Financial_Results.objects.all()
    obj = {"results":results}
    return render(req,"admin/financial_results.html",obj)

def save_financial_results(req):
    financial_results = models.Financial_Results(
       financial_results = req.FILES['financial_results'],
       financial_results_details= req.POST['financial_results_details'],
    )
    financial_results.save()
    # return HttpResponse("Saved")
    return redirect("/admin/financial_results")

def delete_financial_results(req):
    financial_results = models.Financial_Results.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/financial_results")

#   financial_results End


#   disclosure_under_regulation Start
def disclosure_under_regulation(req):
    regulation = models.Disclosure_Regulation.objects.all()
    obj = {"regulation":regulation}
    return render(req,"admin/disclosure_under_regulation.html",obj)

def save_disclosure(req):
    disclosure = models.Disclosure_Regulation(
       disclosure = req.FILES['disclosure'],
       disclosure_details= req.POST['disclosure_details'],
    )
    disclosure.save()
    # return HttpResponse("Saved")
    return redirect("/admin/disclosure_under_regulation")

def delete_disclosure(req):
    financial_results = models.Disclosure_Regulation.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/disclosure_under_regulation")

#   financial_results End

#   shareholding_pattern Start
def shareholding_pattern(req):
    pattern = models.Shareholding_Pattern.objects.all()
    obj = {"pattern":pattern}
    return render(req,"admin/shareholding_pattern.html",obj)

def save_shareholding_pattern(req):
    pattern = models.Shareholding_Pattern(
       shareholding_pattern = req.FILES['shareholding_pattern'],
       shareholding_pattern_details= req.POST['shareholding_pattern_details'],
    )
    pattern.save()
    # return HttpResponse("Saved")
    return redirect("/admin/shareholding_pattern")

def delete_shareholding_pattern(req):
    shareholding_pattern = models.Shareholding_Pattern.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/shareholding_pattern")

#   shareholding_pattern End

#   shareholding_pattern Start
def stock_exchange(req):
    stock = models.Stock_Exchange.objects.all()
    obj = {"stock":stock}
    return render(req,"admin/stock_exchange.html",obj)

def save_stock_exchange(req):
    stock = models.Stock_Exchange(
       stock_exchange = req.FILES['stock_exchange'],
       stock_exchange_details= req.POST['stock_exchange_details'],
    )
    stock.save()
    # return HttpResponse("Saved")
    return redirect("/admin/stock_exchange")

def delete_stock_exchange(req):
    stock_exchange = models.Stock_Exchange.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/stock_exchange")

#   shareholding_pattern End

#   shareholding_pattern Start
def notice_outcome(req):
    notice = models.Notice_Outcome.objects.all()
    obj = {"notice":notice}
    return render(req,"admin/notice_outcome.html",obj)

def save_notice_outcome(req):
    notice = models.Notice_Outcome(
       notice_outcome = req.FILES['notice_outcome'],
       notice_outcome_details= req.POST['notice_outcome_details'],
    )
    notice.save()
    # return HttpResponse("Saved")
    return redirect("/admin/stock_exchange")

def delete_notice_outcome(req):
    notice = models.Notice_Outcome.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/stock_exchange")

#   shareholding_pattern End

#   press_release Start
def press_release(req):
    press = models.Press_Release.objects.all()
    obj = {"press":press}
    return render(req,"admin/press_release.html",obj)

def save_press_release(req):
    press = models.Press_Release(
       press_release = req.FILES['press_release'],
       press_release_details= req.POST['press_release_details'],
    )
    press.save()
    # return HttpResponse("Saved")
    return redirect("/admin/press_release")

def delete_press_release(req):
    notice = models.Press_Release.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/press_release")

#   press_release End

#   corporate_social Start
def corporate_social(req):
    social = models.Corporate_Social.objects.all()
    obj = {"social":social}
    return render(req,"admin/corporate_social.html",obj)

def save_corporate_social(req):
    social = models.Corporate_Social(
       corporate_social = req.FILES['corporate_social'],
       corporate_social_details= req.POST['corporate_social_details'],
    )
    social.save()
    # return HttpResponse("Saved")
    return redirect("/admin/corporate_social")

def delete_corporate_social(req):
    social = models.Corporate_Social.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/corporate_social")

#   press_release End


#   reports Start
def reports(req):
    reports = models.Reports.objects.all()
    obj = {"reports":reports}
    return render(req,"admin/reports.html",obj)

def save_reports(req):
    reports = models.Reports(
       reports = req.FILES['reports'],
       reports_details= req.POST['reports_details'],
    )
    reports.save()
    # return HttpResponse("Saved")
    return redirect("/admin/corporate_social")

def delete_reports(req):
    reports = models.Reports.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/corporate_social")

#   reports End

#   Risk policies1 Start

def policies1(req):
    policies1 = models.Risk_Policies.objects.all()
    obj = {"policies1":policies1}
    return render(req,"admin/policies1.html",obj)

def save_policies1(req):
    policies1 = models.Risk_Policies(
       policies1 = req.FILES['policies1'],
       policies1_details= req.POST['policies1_details'],
    )
    policies1.save()
    # return HttpResponse("Saved")
    return redirect("/admin/corporate_social")

def delete_policies1(req):
    reports = models.Risk_Policies.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/corporate_social")

#   Risk policies1 End

#   Post policies Start

def post_policies(req):
    post_policies = models.Post_Policies.objects.all()
    obj = {"post_policies":post_policies}
    return render(req,"admin/post_policies.html",obj)

def save_post_policies(req):
    post_policies = models.Post_Policies(
       post_policies = req.FILES['post_policies'],
       post_policies_details= req.POST['post_policies_details'],
    )
    post_policies.save()
    # return HttpResponse("Saved")
    return redirect("/admin/post_policies")

def delete_post_policies(req):
    reports = models.Post_Policies.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/post_policies")

#   Post policies End

#    material_documents Start

def material_documents(req):
    material_documents = models.Material_Documents.objects.all()
    obj = {"material_documents":material_documents}
    return render(req,"admin/material_documents.html",obj)

def save_material_documents(req):
    material_documents = models.Material_Documents(
       material_documents = req.FILES['material_documents'],
       material_documents_details= req.POST['material_documents_details'],
    )
    material_documents.save()
    # return HttpResponse("Saved")
    return redirect("/admin/material_documents")

def delete_material_documents(req):
    material_documents = models.Material_Documents.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/material_documents")

#   material_documents  End

#    ipo_documents Start

def ipo_documents(req):
    ipo_documents = models.Ipo_Documents.objects.all()
    obj = {"ipo_documents":ipo_documents}
    return render(req,"admin/ipo_documents.html",obj)

def save_ipo_documents(req):
    ipo_documents = models.Ipo_Documents(
       ipo_documents = req.FILES['ipo_documents'],
       ipo_documents_details= req.POST['ipo_documents_details'],
    )
    ipo_documents.save()
    # return HttpResponse("Saved")
    return redirect("/admin/ipo_documents")

def delete_ipo_documents(req):
    ipo_documents = models.Ipo_Documents.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Delete Data")
    return redirect("/admin/ipo_documents")
#   ipo_documents  End


def Profile(req):
    return render(req,"admin/Profile.html")

def Pj_Franchisess(req):
    data = dadas.Franchise.objects.all()
    obj ={"data": data}
    return render(req,"admin/Pj_Franchisess.html", obj)


# def Edit_Pj_Franchisess(req):
#     return render(req,"admin/Edit_Pj_Franchisess.html")

def Edit_Pj_Franchisess(req):
    old_data = dadas.Franchise.objects.get(id = req.GET['id'])
    obj = {"old_data":old_data}
    return render(req,"admin/Edit_Pj_Franchisess.html",obj)

def update_pg_franchiess(req):
    old_data = dadas.Franchise.objects.get(id = req.POST['id'])
    old_data.firstName = req.POST['firstName']
    old_data.phone_no = req.POST['phone_no']
    old_data.email_address = req.POST['email_address']
    old_data.occupation = req.POST['occupation']
    old_data.City_name = req.POST['City_name']
    old_data.pincodes = req.POST['pincodes']
    old_data.investment = req.POST['investment']


    old_data.save()
    return redirect('/admin/Pj_Franchisess')
