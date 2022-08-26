# coding: gbk
#
import uiautomator2 as u2

d = u2.connect('bc5a8356')

im = d.xpath('//*[@resource-id="com.yiwuzhibo:id/av_room_grow_gift_list"]/android.widget.RelativeLayout[2]/android.widget.ImageView[2]').screenshot()
im.save(r'D:\workspace_new\uiauto2_ele\aseert_pic\big_meigui.jpg')
