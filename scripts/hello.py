#!/usr/bin/env python3
from dev_aberto import hello
import gettext

gettext.bindtextdomain('base', 'locale')
gettext.textdomain('base')
_ = gettext.gettext

if __name__ == '__main__':
    date, name = hello()
    print(_('Last commit made on: ') + date + _(' by ') + name)
