#coding=utf-8
from lxml import etree
import os


def parse_xml_to_dict(xml):
    """
    将xml文件解析成字典形式，参考tensorflow的recursive_parse_xml_to_dict
    Args:
        xml: xml tree obtained by parsing XML file contents using lxml.etree

    Returns:
        Python dictionary holding XML contents.
    """

    if len(xml) == 0:  # 遍历到底层，直接返回tag对应的信息
        return {xml.tag: xml.text}

    result = {}
    for child in xml:
        child_result = parse_xml_to_dict(child)  # 递归遍历标签信息
        if child.tag != 'object':
            result[child.tag] = child_result[child.tag]
        else:
            if child.tag not in result:  # 因为object可能有多个，所以需要放入列表里
                result[child.tag] = []
            result[child.tag].append(child_result[child.tag])
    return {xml.tag: result}


a = sorted([i for i in os.listdir(r'C:\Users\Administrator\Desktop\HCC_calssficy\ICC手术或穿刺组25诊\20210721刘红\ICC_liuhong\gt')])
for path in a:
    with open(r'C:\Users\Administrator\Desktop\HCC_calssficy\ICC手术或穿刺组25诊\20210721刘红\ICC_liuhong\gt' + '/' + str(path)) as fid:
        xml_str = fid.read()
    xml = etree.fromstring(xml_str)  #原文档根节点
    data = parse_xml_to_dict(xml)["annotation"]
    box = []
    # data_width = int(data["size"]["width"])
    # data_height = int(data["size"]["height"])
    for obj in data["object"]:
        xmin = int(obj["bndbox"]["xmin"])
        xmax = int(obj["bndbox"]["xmax"])
        ymin = int(obj["bndbox"]["ymin"])
        ymax = int(obj["bndbox"]["ymax"])
    data_width = xmax - xmin
    data_height = ymax - ymin
    box.append([xmin,ymin,data_width,data_height])

    write_line = "%d,%d,%d,%d\n" %(box[0][0],box[0][1],box[0][2], box[0][3])
    f = open("D:/Python learn/r.txt", "a+")
    f.write(write_line)
    f.close()
