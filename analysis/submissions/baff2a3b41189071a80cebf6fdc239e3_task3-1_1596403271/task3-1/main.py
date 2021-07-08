import shutil, os

files = ['ccc.txt', 'data-02-01-1994.txt', 'mybook at 2020-04-01.txt']
new   = ['ccc.txt', 'data-02-01-1994.txt', 'mybook at 01-04-2020.txt']


if os.path.exists('./output/Photos_22-03-2019'):
    for t in os.listdir('./data/Photos_2019-03-22'):
        if os.path.isdir('./data/Photos_2019-03-22/'+t):
            for i in os.listdir('./data/Photos_2019-03-22/'+t):
                shutil.copy('./data/Photos_2019-03-22/'+t+'/'+i, './output/Photos_22-03-2019/'+t+'/'+i)
        else:
            shutil.copy('./data/Photos_2019-03-22/'+t, './output/Photos_22-03-2019/'+t)
else:
    shutil.copytree('./data/Photos_2019-03-22', './output/Photos_22-03-2019')

os.rename('./output/Photos_22-03-2019/2019-03-21 22.30.png', './output/Photos_22-03-2019/21-03-2019 22.30.png')

for i in range(3):
    shutil.copy('./data/'+files[i],'./output/'+new[i])