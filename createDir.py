#coding=utf-8
import shutil
import os
import traceback
from glob import glob
import pandas as pd
from tqdm import tqdm

os.getcwd()
def copy_file(src_path, dst_path):
    # print('from : ',src_path[])
    # print('to : ',dst_path)
    try:
        # cmd = 'chmod -R +x ' + src_path
        # os.popen(cmd)
        shutil.copy(src_path, dst_path)
    except Exception as e:
        print('move_file ERROR: ',e)
        traceback.print_exc()


dir_path = 'D:/CLUST2015'
new_dir_path = 'D:/CLUST2015_copy'
List = ['Annotation','Data']
for i in tqdm(os.listdir(dir_path)):
    # chdir_path = dir_path + '/' + i + '/'+'Annotation'
    for a in List:
        if a == 'Annotation':
            List_dir = dir_path + '/' + i + '/'+ a + '/'+ i +'.txt'
            new_Annotation_path = new_dir_path + '/' + i + '/' + 'Annotation'
            print(new_Annotation_path)
            if not os.path.exists(new_Annotation_path):
                os.makedirs(new_Annotation_path)
            else:
                pass
            src_path1 = dir_path + '/' + i + '/'+ 'Annotation' + '/' + i +'.txt'
            dst_path1 = new_dir_path + '/' + i + '/' + 'Annotation' + '/' + i +'.txt'
            copy_file(src_path1, dst_path1)

            df_txt = pd.read_csv(List_dir, sep='\t|,| ', header=None)
            df_txt2 = df_txt.dropna(axis=1,how='any')
            # for w in [dir_path + '/' + i + '/'+ 'Data'+ '/'+ str(int(png_path)) + '.png' for png_path in df_txt2[0]]:
            for w in df_txt2[0]:
                # print(int(w))
                if not os.path.exists(new_dir_path+'/' + i + '/'+ 'Data'):
                    os.makedirs(new_dir_path+'/' + i + '/'+ 'Data')
                else:
                    pass
                if 'ETH' in i:
                    src_path1 = dir_path + '/' + i + '/'+ 'Data'+ '/'+ str(int(w)).zfill(5) + '.png'
                    # print(src_path)
                    dst_path1 = new_dir_path + '/' + i + '/'+ 'Data'+ '/'+ str(int(w)).zfill(5) + '.png'
                    copy_file(src_path1, dst_path1)
                else:
                    src_path  = dir_path + '/' + i + '/'+ 'Data'+ '/'+ str(int(w)).zfill(4) + '.png'
                    # print(src_path)
                    dst_path = new_dir_path + '/' + i + '/'+ 'Data'+ '/'+ str(int(w)).zfill(4) + '.png'
                    copy_file(src_path, dst_path)
