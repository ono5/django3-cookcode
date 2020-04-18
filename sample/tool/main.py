# -*- coding: utf-8 -*-
import os
import re

from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader


@dataclass
class SeleniumTemplate(object):
    '''
    Seleniumテンプレートファイル作成クラス
    '''
    display_name: str # 画面名
    locators_file: str # ロケーターファイルのパス
    pagemodels_file: str # ページモデルファイルのパス
    javascript_file: str # JavaScriptファイルパス
    locators_tpl: str # ロケーターのテンプレートファイル
    pagemodes_tpl: str # ページモデルのテンプレートファイル
    is_override: bool # 上書き許可

    def __is_file(self):
        '''
        ファイル存在チェック
        :return:
        '''

        if os.path.isfile(self.locators_file):
            print(f'#### WRARING #### 既に${self.locators_file}は、存在します。')
            raise FileExistsError

        if os.path.isfile(self.pagemodels_file):
            print(f'#### WRARING #### 既に${self.locators_file}は、存在します。')
            raise FileExistsError

    def __get_target_str(self, target):
        '''
        引数に渡した文字列から必要な情報を取得する

        :param target: 対象文字列
        :return: マッチした文字列(key, value
        '''
        regular_express = r"(?P<key>[\w]+):'(?P<value>[\w]+)',"
        m = re.match(regular_express, target)
        return m['key'], m['value']

    def __writing_to_template(self, locator_elems, pagemodel_elems):
        '''
        テンプレートファイルを作成する。
        :param locator_elems: ロケーターの要素
        :param pagemodel_elems: ページモデルの要素
        :return:
        '''
        # テンプレートファイルを指定
        env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
        locators_tpl = env.get_template(self.locators_tpl)
        pagemodels_tpl = env.get_template(self.locators_tpl)

        # テンプレートへの挿入
        locators_py = locators_tpl.render({'display_name': self.display_name, 'elems': locator_elems})
        pagemodels_py = pagemodels_tpl.render({'display_name': self.display_name, 'elems': pagemodel_elems})

        # ファイルへの書き込み
        with open(self.locators_file, 'w') as f:
            f.write(locators_py)

        with open(self.pagemodels_file, 'w') as f:
            f.write(pagemodels_py)

        return

    def __parse_javascript_file(self):
        '''
        JavaScriptファイルをパースして、ディクショナリを作成する。
        :return:
        '''
        locator_elems = []
        pagemodel_elems = []
        with open(self.javascript_file, 'r') as f:
            for line in f:
                if ":" in line:
                    line = line.replace(' ', '').rstrip(('\n'))
                    key, value = self.__get_target_str(line)
                    locator_elems.append({'key': key, 'value': value})
                    pagemodel_elems.append({'key': key.lower(), 'value': key})

        return locator_elems, pagemodel_elems

    def main(self):
        '''
        locators.pyを作成する
        :return:
        '''

        # ファイルの上書きチェック
        if not self.is_override:
            # ファイルの存在チェック
            self.__is_file()

        # JavaScriptをパース
        locator_elems, pagemodel_elems = self.__parse_javascript_file()

        # テンプレートファイル書き込み
        self.__writing_to_template(locator_elems=locator_elems, pagemodel_elems=pagemodel_elems)

        return


if __name__ == '__main__':
    uploader = SeleniumTemplate(
        display_name='Uploader',
        locators_file="locators/uploader_page.py",
        pagemodels_file="page_model/uploader_page.py",
        javascript_file="tool/index.js",
        locators_tpl='tool/templates/locators_template',
        pagemodes_tpl='tool/templates/pagemodels_template',
        is_override=True
    )
    uploader.main()
