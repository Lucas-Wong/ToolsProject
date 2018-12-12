# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            ToolsProject/__init__.py
 Purpose：         

 Author：          lucas.wang

 Created：         2018-07-30
 Copyright：       (C) lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""
# ! /usr/bin/env python

import configparser
import Run
import Global

cp = configparser.SafeConfigParser()
cp.read('Config.cfg')
# cp.read('MaVie_Config.cfg')

if __name__ == '__main__':

    Global.set_master_1_url(cp.get('Master-1', 'URL'))
    Global.set_master_2_url(cp.get('Master-2', 'URL'))
    Global.set_comm_week(cp.get('Week', 'Run_Week'))

    run = Run.init_run()
    run.main()