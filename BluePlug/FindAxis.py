import os
from PIL import Image
import numpy as np

def compare_matrix(m1, m2, operand):
    if operand == ">":
        return True if (m1>m2).all() else False
    elif operand == ">=":
        return True if (m1>=m2).all() else False
    elif operand == "<":
        return True if (m1<m2).all() else False
    elif operand == "<=":
        return True if (m1<=m2).all() else False
    elif operand == "==":
        return True if (m1==m2).all() else False

def image2array(image_path):
    # im_array:np.array = None
    # print (image_path)
    if image_path is not None and os.path.exists(image_path):
        im = Image.open(image_path).convert("L")
        im_array = np.array(im)
    else:
        raise FileExistsError
    return im_array

def find_sub_graph(main_page_path:str, sub_page_path:str, tolerance:np.int32=8):
    mainpage = image2array(main_page_path)
    match = image2array(sub_page_path)

    row_num = mainpage.shape[0]
    column_num = mainpage.shape[1]

    row_num_sub = match.shape[0]
    column_num_sub = match.shape[1]
    tolerance_matrix = np.ones((row_num_sub, column_num_sub), np.int32)*tolerance

    for i in range(0, row_num - row_num_sub, 10):
        for j in range(0, column_num - column_num_sub, 10):
            shot = mainpage[i:i+row_num_sub, j:j+column_num_sub]
            subres = abs(np.subtract(shot, match))
            if compare_matrix(subres, tolerance_matrix, "<="):
                print(i,j)
                return i,j


def find_sub_graphes(main_page_path:str, sub_page_paths:list, tolerance:np.int32=5, step=10):
    mainpage = image2array(main_page_path)
    matches = []
    matches = {}
    row_num_sub = step
    column_num_sub = step

    for m in sub_page_paths:
        # print (m)
        match = image2array(m)
        matches[m] = match
        # matches.append(match)

    row_num = mainpage.shape[0]
    column_num = mainpage.shape[1]

    tolerance_matrix = np.ones((row_num_sub, column_num_sub), np.int32) * tolerance
    # print("fff")
    for i in range(0, row_num - row_num_sub, step):
        for j in range(0, column_num - column_num_sub, step):
            shot = mainpage[i:i+row_num_sub, j:j+column_num_sub]
            for match in matches:
                subres = abs(np.subtract(shot, matches[match]))
                # print(match)
                #
                # if  i==70 and j==390 and "login_notice_close" in match:
                #     print(subres)
                #     print("**"*20)
                #     print(shot)
                #     print("&&&"*10)
                #     print(matches[match])
                #     print("&&&" * 10)
                subres =np.where(subres < 255-tolerance, subres, 0)
                if compare_matrix(subres, tolerance_matrix, "<="):
                    # print((match.split("\\")[-1]).split(".")[0],str(i)+" "+str(500-j))
                    return (match.split("\\")[-1]).split(".")[0],str(i)+" "+str(500-j)
                # subres = abs(np.subtract(matches[match],shot))
                # if i==770 and j==450 and "close_1." in match:
                #     print(subres)
                #     print("**"*20)
                #     print(shot)
                #     print("&&&"*10)
                #     print(matches[match])
                #     print("&&&" * 10)
                # if compare_matrix(subres, tolerance_matrix, "<="):
                #     print((match.split("\\")[-1]).split(".")[0],str(i)+" "+str(500-j))
                #     return (match.split("\\")[-1]).split(".")[0],str(i)+" "+str(500-j)
    return False,False

if __name__ == '__main__':
    a = ".\\3\\spe_talk_10.bmp"
    import re
    print ((a.split("\\")[-1]).split(".")[0])
    pass
