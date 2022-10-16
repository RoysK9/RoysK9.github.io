from doctest import DocFileSuite
import os
import random
import copy
import decimal
import csv
import argparse
import glob

from pathlib import Path
 

def replace():

    dir_path = "./docs"
    
    for current_dir, sub_dirs, files_list in os.walk(dir_path): 
        for file_name in files_list: 
    
            p =os.path.join(current_dir,file_name)

            if os.path.splitext(p)[1] == ".html":  

                print(os.path.join(current_dir,file_name))
                read_path = Path(p)
                write_path = Path(p)
                
                # 読み込み
                with open(read_path, encoding="utf-8") as reader:
                    content = reader.read()
                
                # 置換
                content = content.replace(
                    '<link crossorigin="anonymous" href="https://roysk9.github.io/assets/css/stylesheet.c5ad9f205171fab820252a87a0292578dcaa85c950f40ab21addf6cb9611c26a.css" integrity="sha256-xa2fIFFx&#43;rggJSqHoCkleNyqhclQ9AqyGt32y5YRwmo=" rel="preload stylesheet" as="style">',
                    '<link href="https://roysk9.github.io/assets/css/stylesheet.c5ad9f205171fab820252a87a0292578dcaa85c950f40ab21addf6cb9611c26a.css" rel="stylesheet">'
                    )
                
                # 書き出し
                with open(write_path, encoding="utf-8", mode='w') as writer:
                    writer.write(content)


if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1'
    os.environ['CUBLAS_WORKSPACE_CONFIG'] = ":4096:8"   
    replace()
