from django.db import models

# Create your models here.
 
class Studs_banner_img(models.Model):
 bannerImage = models.ImageField(upload_to='static/admin/img/')
 
class Studs_cards(models.Model):
 image = models.ImageField(upload_to='static/admin/img')
 image_title = models.CharField(max_length=50)
 latest_price = models.IntegerField()
 old_price = models.IntegerField()
 
class Studs_artical(models.Model):
 articleHeading = models.CharField(max_length=100)
 articleDescription = models.CharField(max_length=1000)
 
 
class Hoops_Huggies(models.Model):
 Hoops_bannerImage = models.ImageField(upload_to='static/admin/img') 
 
class Hoops_Huggies_cards(models.Model):
 hoops_image = models.ImageField(upload_to='static/admin/img')
 hoops_image_title = models.CharField(max_length=50)
 hoops_latest_price = models.IntegerField()
 hoops_old_price = models.IntegerField()
 
class Hoops_Article_data(models.Model):
 hoops_articleHeading = models.CharField(max_length=100)
 hoops_articleDescription = models.CharField(max_length=1000)

class Hoops_Question_Ans(models.Model):
 Question = models.CharField(max_length=1000)
 
class Drops_Banner_img1(models.Model):
 drops_bannerImage = models.ImageField(upload_to='static/admin/img')
 
class Drops_Card_Info(models.Model):
 hoops_image = models.ImageField(upload_to='static/admin/img')
 hoops_image_title = models.CharField(max_length=50)
 hoops_latest_price = models.IntegerField()
 hoops_old_price = models.IntegerField()
 
class Drops_Article_data(models.Model):
 hoops_articleHeading = models.CharField(max_length=100)
 hoops_articleDescription = models.CharField(max_length=1000)
 
 
class Drops_Question_Ans(models.Model):
 Question = models.CharField(max_length=1000)
 
 
class Sui_Dhaga_cart(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Party_wear_cart(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Daily_wear_cart(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Necklacesmodel(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
 
 # Lariat_Necklaces start 
class Lariat_Necklaces(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Lari_Neck_Article(models.Model):
 articleHeading = models.CharField(max_length=200)
 articleDescription = models.CharField(max_length=1000)
 
class Lariant_Que(models.Model):
 Question = models.CharField(max_length=1000)
 
 
class HeartPendant(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Religious_Pend(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Flexible_Brac_Card(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Flexible_Bracelet_arti_mode(models.Model):
 articleHeading = models.CharField(max_length=200)
 articleDescription = models.CharField(max_length=1300)
 
class Cufflinks(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
 
class D_nosepin(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
 
class Gold_partywear(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
 
class Gold_OfficeWe(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Gold_Daily_w(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Gold_Kids(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class Gold_Drops_Danglers(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
 
 # kru
class Jewellery(models.Model):
	image_jewellery = models.ImageField(upload_to='static/admin/img/')
	price_jewellery=models.CharField(max_length=50)
	description_jewellery=models.CharField(max_length=100)

class Index_Slider(models.Model):
	image_index_Slider = models.ImageField(upload_to='static/admin/img/')

class Index_Bast_Slider(models.Model):
	bast_Slider_imgase = models.ImageField(upload_to='static/admin/img/')
	bast_Slider_Name=models.CharField(max_length=50)
	bast_Slider_Description=models.CharField(max_length=50)
	bast_Slider_Price=models.CharField(max_length=50)

class Bestseller_Category(models.Model):
	index_Bestseller_Category_img  = models.ImageField(upload_to='static/admin/img/')

class Shop_Category(models.Model):
	image_Shop_Category = models.ImageField(upload_to='static/admin/img/')
	Name_Shop_Category = models.CharField(max_length=50)
	description_Shop_Category = models.CharField(max_length=100)
class Png_Images(models.Model):
	index_Png = models.ImageField(upload_to='static/admin/img/')
	index_Png_Name = models.CharField(max_length=50)

class Save_Video(models.Model):
	bast_Slider_video=models.CharField(max_length=100)

class Png_JEWELLERS(models.Model):
	PNG_Jewellerss = models.ImageField(upload_to='static/admin/img/')
	PNG_Jewellers_text = models.CharField(max_length=50)
	index_Heiding=models.CharField(max_length=100)


class index_Store_Locator(models.Model):
	Store_Locator_img = models.ImageField(upload_to='static/admin/img/')
	Store_Locator_Heiding = models.CharField(max_length=50)
	Store_Locator_Description = models.CharField(max_length=100)

class index_Celebrity_Corner(models.Model):
	Celebrity_Corner_img = models.ImageField(upload_to='static/admin/img/')
	Celebrity_Corner_img1 = models.ImageField(upload_to='static/admin/img/')
	Celebrity_Corner_img2 = models.ImageField(upload_to='static/admin/img/')
	Celebrity_Corner_img3 = models.ImageField(upload_to='static/admin/img/')
	Celebrity_Corner_Heiding = models.CharField(max_length=50)
	Celebrity_Corner_Description = models.CharField(max_length=100)
 
# Krushna
class Arrival_Goldjewellery(models.Model):
	Arrival_goldjewellery_image= models.ImageField(upload_to='static/admin/img/')
	image_Description= models.CharField(max_length=1000)
	Arrival_goldjewellery_price = models.CharField(max_length=100)
	Arrival_goldjewellery_old_price = models.CharField(max_length=100)
 
class Mangalsutra_mahaotsave(models.Model):
	Mangalsutra_Mahaotsave_image= models.ImageField(upload_to='static/admin/img/')
	Mangalsutra_Mahaotsave_Description= models.CharField(max_length=1000)
	Mangalsutra_Mahaotsave_price = models.CharField(max_length=100)
	Mangalsutra_Mahaotsave_old_price = models.CharField(max_length=100)

class EIINA_Banner(models.Model):
	EIINA_bannerImage= models.ImageField(upload_to='static/admin/img/')
 

class EIINA_CARDs(models.Model):
	EIINA_image= models.ImageField(upload_to='static/admin/img/')
	EIINA_Description= models.CharField(max_length=1000)
	EIINA_Latest_price = models.CharField(max_length=100)
	EIINA_old_price = models.CharField(max_length=100)

class Necklace_mahotsav(models.Model):
	Necklace_Mahotsav_image= models.ImageField(upload_to='static/admin/img/')
	Necklace_Mahotsav_Description= models.CharField(max_length=1000)
	Necklace_Mahotsav_Latest_price = models.CharField(max_length=100)
	Necklace_Mahotsav_old_price = models.CharField(max_length=100)

class Diamond_Diwalisale(models.Model):
	diamond_diwalisale_image= models.ImageField(upload_to='static/admin/img/')
	diamond_diwalisale_Description= models.CharField(max_length=1000)
	diamond_diwalisale_Latest_price = models.CharField(max_length=100)
	diamond_diwalisale_old_price = models.CharField(max_length=100)

class Collecations_Swarajya(models.Model):
	collecations_swarajya_Image = models.ImageField(upload_to='static/admin/img/')

class Sllecations_swarajya(models.Model):
	ollecations_swarajya_image= models.ImageField(upload_to='static/admin/img/')
	ollecations_swarajya_Description= models.CharField(max_length=1000)
	ollecations_swarajya_Latest_price = models.CharField(max_length=100)
	ollecations_swarajya_old_price = models.CharField(max_length=100)


class Saptam_Collecation(models.Model):
	Saptam_Collecation_bannerImage = models.ImageField(upload_to='static/admin/img/')

class Saptam_Collection(models.Model):
	Saptam_Collection_image= models.ImageField(upload_to='static/admin/img/')
	Saptam_Collection_Description= models.CharField(max_length=1000)
	Saptam_Collection_Latest_price = models.CharField(max_length=100)
	Saptam_Collection_old_price = models.CharField(max_length=100)

class Aaryas(models.Model):
	Aarya_image= models.ImageField(upload_to='static/admin/img/')
	Aarya_Description= models.CharField(max_length=1000)
	Aarya_Latest_price = models.CharField(max_length=100)
	Aarya_old_price = models.CharField(max_length=100)

class Zodias(models.Model):
	zodias_image= models.ImageField(upload_to='static/admin/img/')
	zodias_Description= models.CharField(max_length=1000)
	zodias_Latest_price = models.CharField(max_length=100)
	zodias_old_price = models.CharField(max_length=100)

class Colour_Stones(models.Model):
	Colour_Stones_image= models.ImageField(upload_to='static/admin/img/')
	Colour_Stones_Description= models.CharField(max_length=1000)
	Colour_Stones_Latest_price = models.CharField(max_length=100)
	Colour_Stones_old_price = models.CharField(max_length=100)

class Police_Polki(models.Model):
	banner_Image_Police_Polki = models.ImageField(upload_to='static/admin/img/')

class Police_Polki_Cards(models.Model):
	Police_Polki_image= models.ImageField(upload_to='static/admin/img/')
	Police_Polki_Description= models.CharField(max_length=1000)
	Police_Polki_price = models.CharField(max_length=100)
	Police_Polki_old_price = models.CharField(max_length=100)
 
class Mangalsutra(models.Model):
 mangalsutra_image = models.ImageField(upload_to='static/admin/img')
 mangalsutra_title = models.CharField(max_length=200)
 mangalsutra_Latest_price = models.IntegerField()
 mangalsutra_price = models.IntegerField()
		
class Mangalsutras(models.Model):
 Mangalsutra_articleHeading = models.CharField(max_length=100)
 Mangalsutra_articleDescription = models.CharField(max_length=200)


class KurtaPage(models.Model):
 Kurta_image = models.ImageField(upload_to='static/admin/img')
 Kurta_title = models.CharField(max_length=200)
 Kurta_latest_price = models.IntegerField()
 Kurta_old_price = models.IntegerField()


class Gold_Jhumkass(models.Model):
 Gold_Jhumkas_image = models.ImageField(upload_to='static/admin/img')
 Gold_Jhumkas_image_title = models.CharField(max_length=200)
 Gold_Jhumkas_latest_price = models.IntegerField()
 Gold_Jhumkas_old_price = models.IntegerField()

class Gold_Menstuds(models.Model):
 Gold_Menstuds_image = models.ImageField(upload_to='static/admin/img')
 Gold_Menstuds_image_title = models.CharField(max_length=200)
 Gold_Menstuds_latest_price = models.IntegerField()
 Gold_Menstuds_old_price = models.IntegerField()

class Gold_GoldBraceletss(models.Model):
 Gold_GoldBracelets_image = models.ImageField(upload_to='static/admin/img')
 Gold_GoldBracelets_image_title = models.CharField(max_length=200)
 Gold_GoldBracelets_latest_price = models.IntegerField()
 Gold_GoldBracelets_old_price = models.IntegerField()

class Gold_vedhani(models.Model):
 Gold_vedhani_image = models.ImageField(upload_to='static/admin/img')
 Gold_vedhani_image_title = models.CharField(max_length=200)
 Gold_vedhani_latest_price = models.IntegerField()
 Gold_vedhani_old_price = models.IntegerField()
 
class GoldPlain(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 
class GoldPNG(models.Model):
 productImage = models.ImageField(upload_to='static/admin/img')
 productTitle = models.CharField(max_length=200)
 latestPrice = models.IntegerField()
 oldPrice = models.IntegerField()
 

class Gold_laxmi(models.Model):
 Gold_laxmi_image = models.ImageField(upload_to='static/admin/img')
 Gold_laxmi_Description = models.CharField(max_length=200)
 Gold_laxmi_Latest_price = models.IntegerField()
 
 # karan
class Diamondrings_bands(models.Model):
	dimaonderings_image = models.ImageField(upload_to='static/admin/img')
	diamondrings_pricce = models.CharField(max_length=50)
	diamondrings_text = models.CharField(max_length=200)
	

class Diamond_engagement_ring(models.Model):
	enagagement_image = models.ImageField(upload_to='static/admin/img')
	enagagement_price = models.CharField(max_length=50)
	enagagement_text = models.CharField(max_length=200)

class Diamond_fashion_ring(models.Model):
	image_fashion = models.ImageField(upload_to='static/admin/img')
	price_fashion = models.CharField(max_length=50)
	text_fashion = models.CharField(max_length=200)

class Casual_ring(models.Model):
	casualring_image = models.ImageField(upload_to='static/admin/img')
	casualring_price = models.CharField(max_length=50)
	casualring_text = models.CharField(max_length=200)
   
    
# 	Akshay Bodkhe
class Gold_Vedhani1(models.Model):
	gold_vedhani_image = models.ImageField(upload_to='static/admin/img')
	gold_vedhani_price = models.CharField(max_length=50)
	gold_vedhani_text = models.CharField(max_length=200)

class Gold_Plain(models.Model):
	gold_plain_image = models.ImageField(upload_to='static/admin/img')
	gold_plain_price = models.CharField(max_length=50)
	gold_plain_text = models.CharField(max_length=200)

class Gold_Laxmi_Shree(models.Model):
	gold_laxmi_shree_image = models.ImageField(upload_to='static/admin/img')
	gold_laxmi_shree_price = models.CharField(max_length=50)
	gold_laxmi_shree_text = models.CharField(max_length=200)

class Gold_PNG(models.Model):
	gold_png_image = models.ImageField(upload_to='static/admin/img')
	gold_png_price = models.CharField(max_length=50)
	gold_png_text = models.CharField(max_length=200)

class Silver_Ganesh(models.Model):
	silver_ganesh_image = models.ImageField(upload_to='static/admin/img')
	silver_ganesh_price = models.CharField(max_length=50)
	silver_ganesh_text = models.CharField(max_length=200)

class Silver_Chip(models.Model):
	silver_chip_image = models.ImageField(upload_to='static/admin/img')
	silver_chip_price = models.CharField(max_length=50)
	silver_chip_text = models.CharField(max_length=200)

class Silver_Laxmi(models.Model):
	silver_laxmi_image = models.ImageField(upload_to='static/admin/img')
	silver_laxmi_price = models.CharField(max_length=50)
	silver_laxmi_text = models.CharField(max_length=200)

class Investors(models.Model):
	investors_image = models.ImageField(upload_to='static/admin/img')

class Investors_Contact(models.Model):
	contact_name = models.CharField(max_length=200)
	contact_mobile = models.CharField(max_length=20)
	contact_email = models.CharField(max_length=200)
	contact_address = models.CharField(max_length=200)


class AnnualReport1(models.Model):
	annual_report = models.FileField(upload_to='static/admin/img')
	annual_report_details = models.CharField(max_length=100)

class Policies(models.Model):
	policies = models.FileField(upload_to='static/admin/img')
	policies_details = models.CharField(max_length=100)

class Corporate(models.Model):
	corporate = models.FileField(upload_to='static/admin/img')
	corporate_details = models.CharField(max_length=100)

class Group(models.Model):
	group_companies = models.FileField(upload_to='static/admin/img')
	group_companies_details = models.CharField(max_length=100)

class Fixed_Deposit(models.Model):
	fixed_deposit = models.FileField(upload_to='static/admin/img')
	fixed_deposit_details = models.CharField(max_length=100)

class Financial_Results(models.Model):
	financial_results = models.FileField(upload_to='static/admin/img')
	financial_results_details = models.CharField(max_length=100)

class Disclosure_Regulation(models.Model):
	disclosure = models.FileField(upload_to='static/admin/img')
	disclosure_details = models.CharField(max_length=100)

class Shareholding_Pattern(models.Model):
	shareholding_pattern = models.FileField(upload_to='static/admin/img')
	shareholding_pattern_details = models.CharField(max_length=100)

class Stock_Exchange(models.Model):
	stock_exchange = models.FileField(upload_to='static/admin/img')
	stock_exchange_details = models.CharField(max_length=100)

class Notice_Outcome(models.Model):
	notice_outcome = models.FileField(upload_to='static/admin/img')
	notice_outcome_details = models.CharField(max_length=100)

class Press_Release(models.Model):
	press_release = models.FileField(upload_to='static/admin/img')
	press_release_details = models.CharField(max_length=100)

class Corporate_Social(models.Model):
	corporate_social = models.FileField(upload_to='static/admin/img')
	corporate_social_details = models.CharField(max_length=100)

class Reports(models.Model):
	reports = models.FileField(upload_to='static/admin/img')
	reports_details = models.CharField(max_length=100)

class Risk_Policies(models.Model):
	policies1 = models.FileField(upload_to='static/admin/img')
	policies1_details = models.CharField(max_length=100)
	
class Post_Policies(models.Model):
	post_policies = models.FileField(upload_to='static/admin/img')
	post_policies_details = models.CharField(max_length=100)

class Material_Documents(models.Model):
	material_documents = models.FileField(upload_to='static/admin/img')
	material_documents_details = models.CharField(max_length=100)	

class Ipo_Documents(models.Model):
	ipo_documents = models.FileField(upload_to='static/admin/img')
	ipo_documents_details = models.CharField(max_length=100)
	