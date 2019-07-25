#coding=utf-8
import random
import string
import time
random_str=''.join(random.sample\
	(string.ascii_letters,15))#生成字符串

print random_str

random_int=random.randint(1,200)#生成整数

print random_int

random_float=random.random()#生成0-1之间的浮点数

print random_float

random_float2=random.uniform(10,30)#生成10到30之间的浮点数

print random_float2
primary_key=[]

for i in range(1500):
    dxbm =''.join(random.sample(string.ascii_letters,20))
    # qjbm = ''.join(random.sample(string.ascii_letters, 20))
    dxfl=random.randint(20,25)
    sex = ''.join(random.sample(string.ascii_letters, 20))
    color = ''.join(random.sample(string.ascii_letters, 20))
    age = random.randint(20, 25)
    # sblx = random.randint(20, 25)
    # jbxx = ''.join(random.sample(string.ascii_letters, 50))
    # sbdj = random.randint(20, 25)
    # bios = ''.join(random.sample(string.ascii_letters, 50))
    # disk = ''.join(random.sample(string.ascii_letters, 50))
    # cpu = ''.join(random.sample(string.ascii_letters, 50))
    # hfsj = random.randint(20, 25)
    # isby = random.randint(20, 25)
    # sbjs = random.randint(20, 25)
    # gjdq = random.randint(20, 25)
    # sscs = ''.join(random.sample(string.ascii_letters, 50))
    # zycd = random.randint(20, 25)
    # kszt = random.randint(20, 25)
    # qksj = random.randint(20, 25)
    # sksj = random.randint(20, 25)
    # skyy = ''.join(random.sample(string.ascii_letters, 50))
    # ksms = random.randint(20, 25)
    # zkfxx = ''.join(random.sample(string.ascii_letters, 50))
    # smmb = random.randint(20, 25)
    # jd = random.uniform(0, 100)
    # wd = random.uniform(0, 100)
    # gsd = random.uniform(0, 100)
    # zxqk = random.randint(20, 25)
    # sxsj = random.randint(20, 25)
    # xxsj = random.randint(20, 25)
    # sfggjd = random.randint(20, 25)
    # sfqjd = random.randint(20, 25)
    # sfmg = random.randint(20, 25)
    # tpfs = random.randint(20, 25)
    # zznl = random.randint(20, 25)
    # jzgz = random.randint(20, 25)
    # zzjz = random.randint(20, 25)
    # qbjz = random.randint(20, 25)
    # scck = ''.join(random.sample(string.ascii_letters, 50))
    # hqsd = random.randint(20, 25)
    # lydw = ''.join(random.sample(string.ascii_letters, 20))
    # zbr = ''.join(random.sample(string.ascii_letters, 20))
    # slsj = random.randint(20, 25)
    # gxsj = random.randint(20, 25)
    # scbz = random.randint(20, 25)
    # blzd = ''.join(random.sample(string.ascii_letters, 50))
    # bz = ''.join(random.sample(string.ascii_letters, 50))
    if dxbm in primary_key:
        continue
    else:
        primary_key.append(dxbm)
        insert_sql="insert into dms_kudu.zoo_bird_jbsx(dxbm,dxfl,sex,color,age) values('%s',%d,'%s','%s',%d)"%(dxbm,dxfl,sex,color,age)
        # insert_sql="insert into benchmark_kudu.nz_sb_jbsx values('%s','%s',%d,'%s',%d, %d, '%s', %d, '%s', '%s', '%s', %d, %d, %d, %d, '%s', %d, %d, %d, %d, '%s', %d, '%s', %d, %f, %f, %f, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, '%s', %d, '%s', '%s', %d, %d, %d, '%s', '%s')"\
        #            %(dxbm,qjbm,dxfl,sbmc,sblb,sblx,jbxx,sbdj,bios,disk,cpu,hfsj,isby,sbjs,gjdq,sscs,zycd,kszt,qksj,sksj,skyy,ksms,zkfxx,smmb,jd,wd,gsd,zxqk,sxsj,xxsj,sfggjd,sfqjd,sfmg,tpfs,zznl,jzgz,zzjz,qbjz,scck,hqsd,lydw,zbr,slsj,gxsj,scbz,blzd,bz)
        with open("F:\\insert.sql",'a') as f:
            f.write(insert_sql+';\n')
        print insert_sql