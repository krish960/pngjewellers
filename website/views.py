from django.shortcuts import render,redirect
from django.http import HttpResponse
from adminpanel import models
from website import models as dadas




def nav(req):
 return render(req,'nav.html')

def footer(req):
 return render(req,'footer.html')


def Diamond(req):
 return render(req,"Diamond.html")


def investors(req):
    investors = models.Investors.objects.all()
    investors_contact = models.Investors_Contact.objects.all()
    annual = models.AnnualReport1.objects.all()
    policies = models.Policies.objects.all()
    policies1 = models.Risk_Policies.objects.all()
    post_policies = models.Post_Policies.objects.all()
    corporate = models.Corporate.objects.all()
    material_documents = models.Material_Documents.objects.all()
    ipo_documents = models.Ipo_Documents.objects.all()
    group = models.Group.objects.all()
    deposit = models.Fixed_Deposit.objects.all()
    results = models.Financial_Results.objects.all()
    regulation = models.Disclosure_Regulation.objects.all()
    pattern = models.Shareholding_Pattern.objects.all()
    stock = models.Stock_Exchange.objects.all()
    notice = models.Notice_Outcome.objects.all()
    press = models.Press_Release.objects.all()
    social = models.Corporate_Social.objects.all()
    reports = models.Reports.objects.all()




    obj = {"investors":investors,"investors_contact":investors_contact,"annual":annual,"policies":policies,
           "policies1":policies1,"post_policies":post_policies,"corporate":corporate,"material_documents":material_documents,
           "ipo_documents":ipo_documents,"group":group,"deposit":deposit,"results":results,"regulation":regulation,
           "pattern":pattern,"stock":stock,"notice":notice,"press":press,"social":social,"reports":reports,
            }
    return render(req,"investors.html",obj)

def bullions(req):
 return render(req,"bullions.html")


def sui_daga(req):
 data = models.Sui_Dhaga_cart.objects.all()
 obj = {'data':data}
 return render(req,"sui_daga.html",obj)
 
def studs(req):
    banner_img = models.Studs_banner_img.objects.all()
    card_data = models.Studs_cards.objects.all()
    artical_Data = models.Studs_artical.objects.all()
    obj = {'banner_img':banner_img,'card_data':card_data,'artical_Data':artical_Data}
    return render(req,'studs.html',obj)
       
       
def Trimurtisilver_coins(req):
 return render(req,"Trimurtisilver_coins.html")



def sliver_ganesha_coin(req):
  silver_ganesh = models.Silver_Ganesh.objects.all()
  obj = {"silver_ganesh":silver_ganesh}
  return render(req,"sliver_ganesha_coin.html",obj)
 
def pure_sliver_chip(req):
  silver_chip = models.Silver_Chip.objects.all()
  obj = {"silver_chip":silver_chip}
  return render(req,"pure_sliver_chip.html",obj)

def png(req):
    data = models.GoldPNG.objects.all()
    png = models.Gold_PNG.objects.all()
    obj = {'data':data,"png":png}
    return render(req,"png.html",obj)

def office_wear(req):
 data = models.Gold_OfficeWe.objects.all()
 obj = {'data':data}
 return render(req,"office_wear.html",obj)




def laxmi_sliver_coin(req):
  silver_laxmi = models.Silver_Laxmi.objects.all()
  obj = {"silver_laxmi":silver_laxmi}
  return render(req,"laxmi_sliver_coin.html",obj)


def HoopsandHuggies(req):
 img1 = models.Hoops_Huggies.objects.all()
 card = models.Hoops_Huggies_cards.objects.all()
 arti = models.Hoops_Article_data.objects.all()
 Que = models.Hoops_Question_Ans.objects.all()
 obj = {'img1':img1,'card':card,'arti':arti,'Que':Que}   
 return render(req,"HoopsandHuggies.html",obj)

def GoldParty_wear(req):
 data = models.Gold_partywear.objects.all()
 obj = {'data':data}
 return render(req,"Goldparty_wear.html",obj)


def Goldrops_and_danglers(req):
 data = models.Gold_Drops_Danglers.objects.all()
 obj = {'data':data}
 return render(req,"Goldrops_and_danglers.html",obj)


def Gold_plain(req):
 data = models.GoldPlain.objects.all()
 plain = models.Gold_Plain.objects.all()
 obj = {'data':data,"plain":plain}
 return render(req,"Gold_plain.html",obj)

def Gold_laxmi_shree(req):
 return render(req,"Gold_laxmi_shree.html")

def Gold_kids_earrings(req):
 data = models.Gold_Kids.objects.all()
 obj = {'data':data}
 return render(req,"Gold_kids_earrings.html",obj)

def Gold_daily_wear(req):
 data = models.Gold_Daily_w.objects.all()
 obj = {'data':data}
 return render(req,"Gold_daily_wear.html",obj)

def DropsandDangless(req):
 banner = models.Drops_Banner_img1.objects.all()
 card = models.Drops_Card_Info.objects.all()
 arti = models.Drops_Article_data.objects.all()
 que = models.Drops_Question_Ans.objects.all()
 obj = {'banner':banner,'card':card,'arti':arti,'que':que}
 return render(req,"DropsandDangless.html",obj)

def DimondNecklasLarient(req):
 cart = models.Lariat_Necklaces.objects.all()
 arti = models.Lari_Neck_Article.objects.all()
 que = models.Lariant_Que.objects.all()
 obj = {'cart':cart,'arti':arti,'que':que}
 return render(req,"DimondNecklasLarient.html",obj)

def Diamondrings_dailywear(req):
 return render(req,"Diamondrings_dailywear.html")



def Diamond_short_necklaces(req):
 data = models.Necklacesmodel.objects.all()
 obj = {'data':data}
 return render(req,"Diamond_short_necklaces.html",obj)

def Diamond_religious_pendant(req):
 data = models.Religious_Pend.objects.all()
 obj = {'data':data}
 return render(req,"Diamond_religious_pendant.html",obj)

def Diamond_nosepin(req):
 card = models.D_nosepin.objects.all()
 obj = {'card':card}
 return render(req,"Diamond_nosepin.html",obj)


def Diamond_hearte_pendant(req):
 data = models.HeartPendant.objects.all()
 obj = {'data':data}   
 return render(req,"Diamond_hearte_pendant.html",obj)



def Diamond_cufflink(req):
 data = models.Cufflinks.objects.all()
 obj = {'data':data}
 return render(req,"Diamond_cufflink.html",obj)



def Diamond_partyWear(req):
 data  = models.Party_wear_cart.objects.all()
 obj = {'data':data}   
 return render(req,"Diamond_partyWear.html",obj)

def Daily_wear(req):
 data = models.Daily_wear_cart.objects.all()
 obj = {'data':data}
 return render(req,"Daily_wear.html",obj)

# def Dai_Fashion_Ring(req):
#  return render(req,"Dai_Fashion_Ring.html")

def collection(req):
 return render(req,"collection.html")

def Bangles_Flexible_Bracel(req):
 data = models.Flexible_Brac_Card.objects.all()
 arti = models.Flexible_Bracelet_arti_mode.objects.all()
 obj = {'data':data,'arti':arti}
 return render(req,"Bangles_Flexible_Bracel.html",obj)


# krush
def index(req):
    index_Slider = models.Index_Slider.objects.all()
    bast_slider=models.Index_Bast_Slider.objects.all()
    Bestseller_Category_img=models.Bestseller_Category.objects.all()
    shop_Category = models.Shop_Category.objects.all()
    save_index_png=models.Png_Images.objects.all()
    save_video=models.Save_Video.objects.all()
    Png_Jewellers=models.Png_JEWELLERS.objects.all()
    store_Locator=models.index_Store_Locator.objects.all()
    celebrity_Corner=models.index_Celebrity_Corner.objects.all()
    obj = {"index_Slider": index_Slider,"bast_slider": bast_slider,"Bestseller_Category_img":Bestseller_Category_img,"shop_Category":shop_Category,"save_index_png":save_index_png,"save_video":save_video,"Png_Jewellers":Png_Jewellers,"store_Locator":store_Locator,"celebrity_Corner":celebrity_Corner}
    
    return render(req, "index.html", obj)


def all_jewellery(req):
    jewellery = models.Jewellery.objects.all()
    obj = {"jewellery": jewellery}
    return render(req, "all_jewellery.html", obj)



def Arrival_goldjewellery(req):
    save_Arrival=models.Arrival_Goldjewellery.objects.all()
    obj ={"save_Arrival": save_Arrival}
    return render(req,"Arrival_goldjewellery.html",obj)

def Mangalsutra_Mahaotsave(req):
    save_Mangalsutra=models.Mangalsutra_mahaotsave.objects.all()
    obj ={"save_Mangalsutra": save_Mangalsutra}
    return render(req,"Mangalsutra_Mahaotsave.html", obj)

def EIINA(req):
    EIINA_banner=models.EIINA_Banner.objects.all()
    save_EIINA=models.EIINA_CARDs.objects.all()
    obj ={"EIINA_banner": EIINA_banner,"save_EIINA":save_EIINA}
    return render(req,"EIINA.html", obj)

def Necklace_Mahotsav(req):
    save_Mahotsav=models.Necklace_mahotsav.objects.all()
    obj ={"save_Mahotsav": save_Mahotsav}
    return render(req,"Necklace_Mahotsav.html", obj)

def diamond_diwalisale(req):
    save_diamond_diwalisale=models.Diamond_Diwalisale.objects.all()
    obj ={"save_diamond_diwalisale": save_diamond_diwalisale}
    return render(req,"diamond_diwalisale.html", obj)

def swarajya_collecations(req):
    banner = models.Collecations_Swarajya.objects.all()
    ollecations_swarajya=models.Sllecations_swarajya.objects.all()
    obj ={"banner": banner,"ollecations_swarajya": ollecations_swarajya}
    return render(req,"swarajya_collecations.html", obj)

def saptam_collecation(req):
    banner=models.Saptam_Collecation.objects.all()
    Store = models.Saptam_Collection.objects.all()
    obj={"banner": banner,"Store": Store}
    return render(req,"saptam_collecation.html", obj)

def Aarya(req):
    arys = models.Aaryas.objects.all()
    obj ={"arys": arys}
    return render(req,"Aarya.html", obj)
 
def zodias(req):
    zodiass = models.Zodias.objects.all()
    obj ={"zodiass": zodiass}
    return render(req,"zodias.html", obj)

def color_stone(req):
    Stones = models.Colour_Stones.objects.all()
    obj ={"Stones": Stones}
    return render(req,"color_stone.html", obj)

def police_polki(req):
    banner=models.Police_Polki.objects.all()
    PolicCard=models.Police_Polki_Cards.objects.all()
    obj ={"banner": banner,"PolicCard": PolicCard}
    return render(req,"police_polki.html", obj)

# kru
def Trendy_mo_d_mangalsutra(req):
    mangalsutra = models.Mangalsutra.objects.all()
    mangalsutras = models.Mangalsutras.objects.all()
    obj ={"mangalsutra": mangalsutra,"mangalsutras":mangalsutras}
    return render(req,"Trendy_mo_d_mangalsutra.html", obj)


def mean_studs(req):
    Gold = models.Gold_Menstuds.objects.all()
    obj ={"Gold": Gold}
    return render(req,"mean_studs.html", obj)

def kids_bracelets(req):
    Gold = models.Gold_GoldBraceletss.objects.all()
    obj ={"Gold": Gold}
    return render(req,"kids_bracelets.html", obj)


def Goldjhumka(req):
    Gold = models.Gold_Jhumkass.objects.all()
    obj ={"Gold": Gold}
    return render(req,"Goldjhumka.html", obj)

def Gold_vedhani(req):
    vedhani = models.Gold_Vedhani1.objects.all()
    Gold = models.Gold_vedhani.objects.all()
    obj ={"Gold": Gold,"vedhani":vedhani}
    return render(req,"Gold_vedhani.html",obj)

def Diamond_kurta_buttons(req):
    Kurta = models.KurtaPage.objects.all()
    obj ={"Kurta": Kurta}
    return render(req,"Diamond_kurta_buttons.html", obj)

def Gold_laxmi_shree(req):
    save_Gold_laxmi = models.Gold_laxmi.objects.all()
    obj ={"save_Gold_laxmi": save_Gold_laxmi}
    return render(req,"Gold_laxmi_shree.html", obj)

# karan
def Diamondrings_bands(req):
 Diamondrings_bands = models.Diamondrings_bands.objects.all()
 obj={"Diamondrings_bands":Diamondrings_bands}
 return render(req,"Diamondrings_bands.html",obj)


def Diamond_engagement_rings(req):
  Diamond_engagement_rings = models.Diamond_engagement_ring.objects.all()
  obj = {"Diamond_engagement_rings":Diamond_engagement_rings}
  return render(req,"Diamond_engagement_rings.html",obj)



def Diamond_casual_rings(req):
  casual_ring= models.Casual_ring.objects.all()
  obj = {"casual_ring":casual_ring}
  return render(req,"Diamond_casual_rings.html",obj)


def Dai_Fashion_Ring(req):
  fashion_ring = models.Diamond_fashion_ring.objects.all()
  obj = {"fashion_ring":fashion_ring}
  return render(req,"Dai_Fashion_Ring.html",obj)


def Pj_Franchise(req):
    return render(req,"Pj_Franchise.html")

def save_Pj_Franchise(req):
    data = dadas.Franchise(
        firstName =req.POST['firstName'],
        email_address =req.POST['email_address'],
        phone_no =req.POST['phone_no'],
        occupation =req.POST['occupation'],
        City_name =req.POST['City_name'],
        pincodes =req.POST['pincodes'],
        investment =req.POST['investment'],
    )
    data.save()
    return redirect("/Pj_Franchise")


def Store_Locator(req):
    return render(req,"Store_Locator.html")

def login(req):
    return render(req,"login.html")

def signup(req):
    return render(req,"signup.html")



def Contact(req):
    return render(req,"Contact.html")

def contest_programs(req):
    return render(req,"contest_programs.html")