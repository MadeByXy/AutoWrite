from lib import HttpHelper
import time

填报内容 = {
    # 经常调整的内容, \n或中文分号(；)换行
    "工作内容": "",
    "明日计划": "",
    "遗留问题": "",
    "备注": "",

    # 基本不会调整的内容
    "账号": "",
    "密码": "",

    "工作地点": {
        "省": "湖南省",
        "市": "长沙市"
    },
    "工作类型": "研发",
    "项目名称": "公司经营管理网上平台",
    "服务单位": "国网湖南省电力公司",
    "服务专业": "发展部",
    "服务用户": "余爱琴"
}


class AutoWrite:
    def __init__(self, content):
        self.http = HttpHelper.HttpHelper({"hidden_ui": False}, "chrome", "")
        self.content = content

    # 开始自动填写
    def run(self):
        http = self.http
        content = self.content
        http.get("http://58.87.106.79:8080/icms/login")

        # 登陆
        http.get_dom('//*[@id="loginName"]').send_keys(content["账号"])
        http.get_dom(
            '/html/body/div[1]/div[2]/form/ul/li[2]/div/input').send_keys(content["密码"])
        http.get_dom('/html/body/div[1]/div[2]/form/ul/li[3]/button').click()

        # 点击应用管理
        http.get_dom('//*[@id="menu"]/ul/li[2]').click()
        time.sleep(1)
        http.get_dom('//*[@id="menu"]/ul/li[2]/ul/a[2]').click()
        http.browser.switch_to.frame("homeifr")
        http.get_dom(
            '/html/body/div[1]/div[1]/div/div[1]/div[5]').click()

        # 填写内容
        http.get_dom('//*[@id="_easyui_textbox_input16"]').click()

        # 填写工作地点
        target = http.get_dom('//span[text()="' + content["工作地点"]
                              ["省"] + '"]/preceding-sibling::span[2]')
        target.click()
        http.browser.execute_script("arguments[0].scrollIntoView();", target)
        http.get_dom('//span[text()="' + content["工作地点"]
                     ["市"] + '"]/parent::div/parent::li').click()

        # 填写工作类型
        http.get_dom('//*[@id="_easyui_textbox_input15"]').click()
        type_change = {
            "研发": '//*[@id="_easyui_combobox_i2_0"]',
            "交流": '//*[@id="_easyui_combobox_i2_1"]',
            "工程": '//*[@id="_easyui_combobox_i2_2"]',
            "销售": '//*[@id="_easyui_combobox_i2_3"]',
            "运维": '//*[@id="_easyui_combobox_i2_4"]',
            "实施": '//*[@id="_easyui_combobox_i2_5"]'
        }
        http.get_dom(type_change[content['工作类型']]).click()

        # 填写其他内容
        http.get_dom(
            '//*[@id="_easyui_textbox_input3"]').send_keys(content["项目名称"])
        http.get_dom(
            '//*[@id="_easyui_textbox_input4"]').send_keys(content["服务单位"])
        http.get_dom(
            '//*[@id="_easyui_textbox_input5"]').send_keys(content["服务专业"])
        http.get_dom(
            '//*[@id="_easyui_textbox_input6"]').send_keys(content["服务用户"])
        http.get_dom(
            '//*[@id="_easyui_textbox_input7"]').send_keys(content["工作内容"].replace('；', '；\n'))
        http.get_dom(
            '//*[@id="_easyui_textbox_input8"]').send_keys(content["遗留问题"].replace('；', '；\n'))
        http.get_dom(
            '//*[@id="_easyui_textbox_input9"]').send_keys(content["明日计划"].replace('；', '；\n'))
        http.get_dom(
            '//*[@id="_easyui_textbox_input10"]').send_keys(content["备注"].replace('；', '；\n'))

        # 保存
        http.get_dom('//*[@id="dlg-buttons"]/a[1]').click()
        print("ok")

        time.sleep(2)
        http.quit()


AutoWrite(填报内容).run()
