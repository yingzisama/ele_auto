# coding: gbk
#
import uiautomator2 as u2

d = u2.connect('A3KUUT2113000390')

im = d(descriptionContains="�Զ�������").screenshot()
im.save(r'D:\workspace_new\uiauto2_ele\aseert_pic\mind_shield_manager.jpg')
