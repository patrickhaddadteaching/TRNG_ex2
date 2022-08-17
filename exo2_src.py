from ipywidgets import widgets,interactive
import numpy as np
from time import time, sleep
import matplotlib.pyplot as plt
from datetime import datetime
from os.path import abspath,exists
from os import mkdir

image_value_relativ_sigma=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x87\x00\x00\x00\xa1\x08\x06\x00\x00\x00\xed\x12\xac!\x00\x00\x14\x08IDATx^\xed\x9d\x8f\xf1\xf3H\x11D\x8f\x0c \x05\xc8\x00R\x80\x0c \x85#\x03H\x012\x80\x14 \x03H\x012\xe0R\x80\x0c\x00u\x15}5\xdf\xf0\xb4jk\xd6\xc6\xc5\xb9\xea\xbd\x82\xb3{v\xf5g-\xad%}?\x7f\xf5\xd5W1\xdf\x0b\xfc\xc1\xe1\xd7\x87\xbf;\xfc\xdb\xe1\xdf\x0f\xffy\xf8/P\xafw)\xd7\xfd\xc7\xe1_\x0f\x7fqX\xfb&\xea\xfb+\x894GP\xed\xc4\xb7\x87\x16\xdajGi\x87i\xe7\xa5;=\xcd\x9d\xa9AR\x97\x81\xa8\xef\xaf$\xd2\x1cA\xb5\x13\xdf\x1eZ\xe8\x9f\x1c~sXwZ\xba\xd3\xd3\xdc\x99\xea\xb7.\x0bQ\xdf_I\xa49\x82j\'\xbe=}\x81\x7f{H;-\xdd\xe9i\xee\xcc_\x1f\xd6\xe5!\xea\xfb+\x894GP\xed\xc4\xb7\xc7\x0b\xfa\xa3C\x9fBH\xefh\xcd7<\xefX\xe5\xec_\x0e\xd5\xee\x95\x7f<\xec\xf3\rI\xf4\xcc\x99D\x9a#\xa8v\xe2\xdb\xa3\x85\xd4\xc0\xd0\xb9\x9ev\xb6\xfc\xfd\xe1O\x0f;\xaa\xd5\x0e\xfd\xf3\xa1\xb3}p\xfc\xf8\xb0n\x90G%(G\x12i\x8e\xa0\xda\x89o\xcfj`\xd4C<QW\xf4\x97\x87\xaa\xe9\x83\xe3O\x875\xf7\xa8\x04\xe5H"\xcd\x11T;\xf1\xad\xf9\xe1!\r\x0cM\n5h\xaeV\xa4\xbe/5\x98\xfa\xe0\x90\x9a\xe0\xf6l*A9\x92Hs\x04\xd5N\xfc\x9fA\x0b\xd3\xed\xdfH\xa4\xce\xff\x04\xd5\x13\x9a\x8f\xf4\xc1\xa1\xd3RR\xdb3g\x12\x94#\'P{\xa9\x04\xe5\xc8\t\xd8\x1e\xbdX\xd5\x04\x90\x06\x86\xde#z\xfdYN\x17\xcb\xfa\xe0\xe8_O\xcfj{\xe6L\x82r\xe4\x04j/\x95\xa0\x1c9\x01\xdb\xa3\x17\xad&\x91}`H\x9fJ\x88\xde\xc6YN\xa7\xaa>8\xd4\xb6\xae\xb2^\xd5\xd6\xf7W\x12\x94#\'P{\xa9\x04\xe5\xc8\t\xd8\x1e\xbd(\xb5\x93h\x9e\xa1\t\xa53Dmc\x95\x1348\xfa\xbc\x83\xa8\xef\xaf$\xfc^\x1f\x84\xdd\t\xd4^*A9\x92\xf8\xfe\x7f\xfe\xf7\nl\x8f^\x94:\xff\xf7\x81q\xf7\xaa\xe4\x1948\x9e}\xcfD\x93a\xaf\x0f\xcdq\xec\x04j/\x95\xa0\x1cY\xf9\xd5\xa1\xb7\xab\xeeu]\x81\xed\xd1\x8b\xfaTy\x03V\xebQC\x12\xf5\xfdUN\xd4\x81!\'}\x90\x1d]K\xe9\xebtv\x04\x99@\xed\xa5\x12\x94#\x8d\xd6\xb3o\xdb\xab#\x08\xb6G/\xd2Q\xa3\xdf\xe8\x92D\xcf\x9c\xe5D_\x01\xf5\xf3\xcc#\x87>A}\xbd\xa8NN\xa0\xf6R\t\xca\x91F\xeb\xd9\xb7\xed\x15\xd8^\x7f\xe1\xec\xa8\xd1\xefeH\xa2g\xcerg\x13\xd2g\xce9\xfa\xa5|]\xb1\xa5:9\x81\xdaK%(G\x1a?*au\x81\xf1\nl\xaf\xbf\xe0+\x98\xdd~\xb1K\x12=s\x96\xa3C\x1f\xf5C\xd4\xf7WV<\x18\xeb:\xd1\x80\xb7\x13\xa8\xbdT\x82r\xa4\xa0\x0f\x9d\xe6\x1fW\x9c\xb5\xf7\x05\x1ae\xbdq]\xb0\xa2\xe2T\xa2N\x98\xacv\x18\xd5\'^\xe1\xeb*up\xf8(\x95\xd2\xfb<\xabMs\x13\xa8\x0fI\x1f\xee\xbbW\x9e\xff\x8b\xbe\xc3\xe4o\x0e\xa98\x95\xf8\xc3a\xef\x87\xe65\xa9W\xb8?o\xb0\xdaWJ\xedoU\x9b\xe6&P\x1f\xb2_\xb4\xdc\xb6M\x7f~\xd8w\x98\xd4\x9dV*N%\xfayQj\xc5\xa8>\xf1\n\xf7\xe7\x8dV\xfbJ\xa9\xfd\xadj\xd3\xdc\x04\xeaC\xf6kS\xdb\xb6\xa9\x8e\x10}\x87IA\xc5\xa9\x1d:/JzN#uE\xed\xcf\x1b\xed\xeab\x1eQ\xfb[\xd5\xa6\xb9\t\xd4\x87\xe6ku`\xf4\xf5|\xd4/\xa0\xaf@\x9ao\x08*N\xed\xd0|CRm\xea\x8az\x1f\xc7\x1b\xadN|Sj\x7f\xab\xda47\x81\xfa\xa0\xf9\x06}\x91H\xfd\x02\x9a\x8c\xea\\-\xa88\xb5Cwd\x9f\xf1<\x87\xa9\xf3\x1bm\xb0~\x1eN\xa95\xabZ\xbf\xa7\xcb\x02\xdaa:\xb4\xebI7\x9f\xda\xf4\xbf\xfao\x1d\xa9\xf5\xad\xed\x0eu\x19\xec\xce\xf9\x86\xfc\x02\xdai\xfe\x1aD\xc5\xa9\x95\xb3S\xcad^\xf3\xb3C\x9a\xc3\x90u\xe3\xd9\xfa\xbe\x8f\x94\x04\xf5M\xe8\xdbA}\xeaMz@\xe8C\xd0\xb7\xb3^K\x06\x89\xb6Q\x9f;\xdd\x95\xee\x80w\xbf@\x0b_\x17Z\xea\x90,\xa88\xb5B\xf3\x1am\x1cA\xb5\x89g\x0f\x0f\x91\xb4\xa1\xea\xfb\x93\xc1\xa1K\xd4:J\xd5\xb6\xf5i\xd6`\xe9\xe8C\xd2\x8f\xd4\xde\xd6g\xd4\xd3q\xed\xe3\x8e\x0f\x0f\x8e\xbe\xb0\xd2\xcf\x84Rq\xaa\xd1\xc6\xeb\xedKm(A\xb5\xa9B\xedw\xfb\xfcF\x1bF;K\x87|\xeb\xec\x15g\xfd\x8a\xfaMO}\xe8\x90\xae#Z\xcfu\xfa<O\xed\\\xa1e\xad\xcb/\xeb\rE\xdb\xd7\xd3\xd6\xe5_\xf9\xc5\x7f\xd0=\x15\xaf\xe0\x84U\xfbW_)\xfd^5E\xd9\xdd\xe7\xe1\xae\xe8\x03PG\xe0G\x06[\xff\xfayg\x12\xa9\xf5\xac\xcb\xa0\xd3\xcf\x98\xda\x01=\xdc\xe3\xaf\x97\x13TO_\xb3th\xab#\x99\xf0{\xd5\x14e\xfb\x86\xaf\x83q\x87\xfd4\xa9\x9d\x92\x0c\x0c\xe16\xfa\xb7\x8c\xd5=\x9f3\xb5\x9eu9\xfcEbD\xed@;\xaa.\xa4\xf4\xfd\x87\t\xaa\xef\x134\xd9?!D}\x7f\x95#h@\xae\xee\xa7<\xaavj\xdd!\xd2\xa7\xc8\x04\xb7\xa3\xc3\x7f_\xceG\x8e\x1e^\xcf\xba\x1c\xfe"1\xa2w\xd4w\xa2G\xf1\x04:\x1f\xd2\x05/\xa2g\xcer\x04}\xef\xd7\x8e\xa06\x1f\xd5;t\xb2C\xdc\x16}(\xb5\xec\xb5\xbf\x95^\xcf\xba,w\xbf"\x7fA\xefHs\x8c\xbe\xa0Z\xf8\xbbh\x82\xd5\xdb;\xfb\xf4\x12i\x8ex\xe6|C\xa7D\xb5\xe9\x9dq\xe7\x1c_\xdb\xab\xcb)\x1f9\xfdy=\'\xcb\x82Pg\xfd\xe8\xa1\x9dy\x07\xcf\xe0k[\xabK\xe4D\x9a#\xfa|\xe3\xce\xb9\x9c\xacG$\xef\x90;\x87\xf1\xdaf]N\xf9\xc8\xb2z=\xbd,\xbe40\x86:\xd3\x91\xa2o\xd8G\xce\xa5\xa2~ES\xbd\xda\xbb:\xa4\x13i\xae\xa3\xe5\xad\xcb/w\xcd7\xea\xb6\xf1:\xa6\x93\xd0\x8a\xdb\xa3\xb9\x91\xff\xf9\xc7\x95\xb5\xd6\xcb\xb2e\xbe!\xa8C\xa9N\xebF\xd0\xa1*9\x8f)\xd3/\xa6\xe9S\x90L\xb0\x884\xd7\xd1\x05%/\xbb\xdd1\xdf\xe8\xdf\xe8\xb4~Z\xdf;\x9c\xb5)\xd3#\x07\x1d\xc5\xb6\xcc7\x04uh\xb5C\xfb\xb9U_\xdd\xfaQD\x9f\x1a\x9dB\xfa\xa0\xd0\xd5\xc6G.\x8b\x13i\xae\xf3\xc8\xf3\xa2\x8f\xd8O\xb9Z\xcf\xbb\x9fT\xb7I\x7f\xceb\xf5d|\xb5^;\xf2v\x7f)\xfa\x14\xea\xc8\xe1\xce\xa5\xfe\x9b\xee\xc5h!\xb5\x01\xaff\xdb\xc4$\xd7\xd5\xa0\xae\xcb\xb5:\x0fS=\xa1\xd7\xbd#\xea\x0ey\xf4\x94\xdb\xa1+\xd3W\x03\xce\xcb\xe9\x0f\xaf}d\xaer\xe5C\xe8(\xa0O\xa4\x8e\x10\x1e,\xfa_\xfd\xb7.\xbah\x85\xeaE\xad\x95\xc4$W\xf5W\xc3tcS\x1b\x04\xcd\r\xd4\xf6\x94\xba\x9c\xf6j\xc0i\x19\xe9+\xf0\xce\xeb8\xdb\xa1NHb\x92\xab\xfa\x1c^7\xf6\xea<Lm\x10\xf45\xff\xee|\xc3\xe8\x03W\x97S&mj\x19i\xae\xb2\xeb:\x8e\xdc\x0euB\x12\x93\\\xd5\xe7\xe1\xba\xc1WP\x1bD\x9d\xfcY\x1dI\'\xf4\x1bo2\x99\xc3h\x19\xe9^U_\x8f\x89\xdb\xa1NHb\x92\xab\xf6I\xf4\xd5\xf7~\xd5\xe8\x10\xad\xf3\xb5\xaf\xc3\x10\xf4I\xbd;\x19\x15\x9a\xc8\xd7A!u\x9aN\xa8\xebi\x93\xf9F_\xcf\x95\xdb\xa1NHb\x92\xb3\xf5<\xec\r\x9eL\xee\xfc\x8d\xc1\xdf\x12\x08_2\xaf^=\x83\xb1\x82\x9emIn\xd9\x8b\xbb\xf3\x8d\xbe\x9e+\xb7C\x9d\x90\xc4$g\xeb\xbc\xc0\x1b\xfc\xea{\x7f\xdd\xd0\xbe\x1eC\xe8u\xe7\xec\xe4\xc8Q\x07\x85|\xe4\xca&\xcd\x7f\xae\xe6\x1b\xb4\x9e+\xb7C\x9d\x90\xc4$g\xf5\xe9\xf1\x06\xf0F\xbf\xc2\xe7\xee\xfai"\xf4\xba\x0e\xc9n_\xde\x9ds\xd4\xe7Z\xe5\xea\t4\xa2\xae\xa7\xf5\xb2\x9fI\xeb\xb9r;\xd4\tILr\xd6\x1b@&\x1b]\xdf\x16\x94\xd5\xd5`}\xb2\xdc\x0e\xa1\xd7\xfb\'\xf6\xd1\x9d*t\xb4\xa9\x03C\xf3\x8cG/\xbf\xd7\xf5\x94\x9a\x7fx\xd9I/w_\xcf\x95\xf8"\x99B\xb5d\n\xd5\x92\xa6nxm\x8c~\x8f\xa2\xa2k\t\xcei\xe3\x9d\xe5\x8c\xdf\xebG\x8f\xab\x0b~\xd5\xfe\x8dG;\xf5\xea\x10O\xf4\x01v\xf6\xf5W\xf5\xf5\xfa\x8c\xd63\xa6/\xc8\x99)TK\xa6P-i4\xbf\xf0\x06\xf3\xc6?\xcb\xf9B\x1e\xed\\\xc2\xef\xe9\x93W\xbf)\xa4\x9f\xc6\xfeiO\xbe]H\xa2\xae\xa7<;\x82i\x1e\xe2{d^\xcf\x98\xbe g\xa6P-\x99B\xb5d\xc5\xdf\x02\xbc\x13\xeaDM\xd4O\x9d\xfe\x7fm\xa7\xe6:\xf5}\r\x06\x1d\x95\xdc\x87v\xc0\xd9\xd7C\xcd\x0f\xbc\x83\x9c}\xe4hsF\xff\xb6\xd3\'\xdeZ7\xf7Y\xbf\xc9\xc4\xd4\x85X\x99B\xb5d\n\xd5\x92\x1d\xfa\'\x02\xfa\xa4\xfah\xa1O\xda\xea\xc9z\x82r\xfd\xa6\x99v\xbc\xfaQ\x7f\xfd:\x84\xdeK\xbenvW\xf4\x89\xad\xfe[\xdfz\xbc\x9eZ\x86\xe4\x94\x89\xd4\xa2\x95)TK\xa6P-I\xe8\x88Qw\x92\xfeW\x1b\xae_KH\xdb\xa3\x9c\xd4QDG\x02\r\x8a: \xf4\xff\xf5\x9a\x06\xd0\xd5\xd7\xcc\x95W\xe8\x88\xa1A\xa1\x01\xef\x81\xef\xf5\xbc\xd3\xde\xb7P1\x99B\xb5d\n\xd5\x92\xc4+r\xafp\xc2\xa8=*&S\xa8\x96L\xa1Z\x92xE\xee\x15N\x18\xb5G\xc5d\n\xd5\x92)TK\x12\xaf\xc8\xbd\xc2\t\xa3\xf6\xa8\x98L\xa1Z2\x85jI\xe2\x15\xb9W8aw{\xd8 IP.\x95\xa0\\jJZK92\x85j\xc9\t\xd4\x1e\x19C\xc5$A\xb9T\x82r\xa9)i-\xe5\xc8\x14\xaa%\'P{d\x0c\x15\x93\x04\xe5R\t\xca\xa5\xa6\xa4\xb5\x94#S\xa8\x96\x9c@\xed\x911TL\x12\x94K%(\x97\x9a\x92\xd6R\x8eL\xa1Zr\x02\xb5G\xc6P1IP.\x95\xa0\\jJZK92\x85j\xc9\t\xd4\x1e\x19C\xc5$A\xb9T\x82r\xa9)i-\xe5\xc8\x14\xaa%\'P{d\x0c\x15\x93\x04\xe5R\t\xca\xa5\xa6\xa4\xb5\x94#S\xa8\x96\x9c@\xed\x911TL\x12\x94K%(\x97\x9a\x92\xd6R\x8eL\xa1Zr\x02\xb5G\xc6P1IP.\x95\xa0\\jJZK92\x85j\xc9\t\xd4\x1e9"mp\x92#\x894GP-\x99\xf2N\xb5\xa9\xdbI;\x99\xe4H"\xcd\x11TK\xa6\xbcSm\xeav\xd2N&9\x92Hs\x04\xd5\x92)\xefT\x9b\xba\x9d\xb4\x93I\x8e$\xd2\x1cA\xb5d\xca;\xd5\xa6n\'\xedd\x92#\x894GP-\x99\xf2N\xb5\xa9\xdbI;\x99\xe4H"\xcd\x11TK\xa6\xbcSm\xeav\xd2N&9\x92Hs\x04\xd5\x92)\xefT\x9b\x1aS\x9f\\^\xe9\x87f\xab\xbbsdZK9\x92jI\xaa%\xdf\xa96\x95\xda#\xf1E2\xedd\x92#\xd3Z\xca\x91TKR-\xf9N\xb5\xa9\xd4\x1e\x89/\x92\xd4Ij\xda\x1e\xe5\xc8\xb4\x96r$\xd5\x92\xbbk\xc9\xdd\xb5$\xd5\x92XLRqj\xda\x1e\xe5\xc8\xb4\x96r$\xd5\x92\xbbk\xc9\xdd\xb5$\xd5\x9214\xb1I%\xd2\x1c\x91\xd6R\x8eL\xd9]K\x12\x94#S\xa8\x96\x8c\xa1\xe2T"\xcd\x11i-\xe5\xc8\x94\xdd\xb5$A92\x85j\xc9\x18*N%\xd2\x1c\x91\xd6R\x8eL\xd9]K\x12\x94#S\xa8\x96\x8c\xa1\xe2T"\xcd\x11i-\xe5\xc8\x94\xdd\xb5$A92\x85j\xc9\x18*N%\xd2\x1c\x91\xd6R\x8eL\xd9]K\x12\x94#S\xa8\x96\x8c\xa1\xe2T"\xcd\x11i-\xe5\xc8\x94\xdd\xb5$A92\x85j\xc9\x18*N%\xd2\x1c\x91\xd6R\x8eL\xd9]K\x12\x94#S\xa8\x96\xc4\x17wK\xa4\xb9\x94\xb4=\xca\x91)i-\xe5R\t\xca\x91\x04\xe5H|q\xb7D\x9aKI\xdb\xa3\x1c\x99\x92\xd6R.\x95\xa0\x1cIP\x8e\xc4\x17wK\xa4\xb9\x94\xb4=\xca\x91)i-\xe5R\t\xca\x91\x04\xe5H|q\xb7D\x9aKI\xdb\xa3\x1c\x99\x92\xd6R.\x95\xa0\x1cIP\x8e\xc4\x17wK\xa4\xb9\x94\xb4=\xca\x91)i-\xe5R\t\xca\x91\x04\xe5H|q\xb7D\x9aKI\xdb\xa3\x1c\x99\x92\xd6R.\x95\xa0\x1cIP\x8e\xc4\x17wK\xa4\xb9\x94\xb4=\xca\x91)i-\xe5R\t\xca\x91\x04\xe5H|q\xb7D\x9aKI\xdb\xa3\x1c\x99\x92\xd6R.\x95\xa0\x1cIP\x8e\xc4\x17wK\xa4\xb9\x94\xb4=\xca\x91)i-\xe5R\t\xca\x91\x04\xe5H|\x91\xdcM\xda\xc7$\x97\x9aB\xb5dJZ;\xc9\x91\x04\xe6\xe8Er7i\x1f\x93\\j\n\xd5\x92)i\xed$G\x12\x98\xa3\x17\xc9\xdd\xa4}Lr\xa9)TK\xa6\xa4\xb5\x93\x1cI`\x8e^$w\xe3v\xf5G\xdb\xf5\xc7\xe2\xa5\xfe\xca\x7f\xd7\xefU\xd3\\*\xb5GR\xad\xec\xbf\x80\x90RkV\xb5\x93\x1cI`\x8e^$w\xa36\xfd\xebA6}\x186\xcd\xa5R{$\xd5\xda\xfas\x1a)\xceW\x89I\x8e$0G/\x92\xbbQ\x9b\xfaE\x83\xba\x81\xd3\x1d\x92\xe6R\xa9=\x92jm\xfd\xd9\x8a\x14\xe7\xab\xc4$G\x12\x98\xa3\x17\xc9\xdd\xa8\xcd\xbe\x81\xeb\x8e\xd0\xcfB\xe8\xc7\xf5t\xd8\xd6\xa7R?I\xa1\x9f\xa3\x92\xfa=\xb4\xae~\xd6B\xef)\xdf\xdb\xad\xea\'.\xdc\x96j$\xb5\xa7\x9f\xf8\xd2OU\xe8g)tJ\xe9\xbf\xdf\xd2U;\x8fn+\xe7\xab\xc4$G\x12\x98\xa3\x17\xc9\xdd\xd0\x0f\xf8jPh@\xd4\xdfqO\x97\xc5\xefi\xc7\xf7v\xad~\x0c\xa7\xb6cS\x94\xed?\xc5e\xef\xb6\xd7%&9\x92\xc0\x1c\xbdH\xee\xa6\x9fR\xf4\x93X\xf4\xe3\xfe\xe9\xb2\xf8=M\x0ek\xbbU\xf5Y\xdb\xb1)\xce\xf7_gZ\xfd\xc8\xe0\x8aZ\xb3\xaa\x9d\xe4H"\xcd\xc5P\x83$QO!\xfaeC\x1d\xca\tj\x8f4\xfdg\xad\xaag\xbf\xf6L\xed]\xe9\xdflS\xbb\xea\xf3\x0e\xd4.\x91\xe6\x88I\xed\x08\xea\x98\xech\'y\x87]\xfd\xa6*\xb5G\x1a\xff\xb6\x199\x1d\x80U\x1f\xf9\xd4\xae\xe6$w\xa0v\x894GLjGP\xc7dG\xbf?\xe6\x1dv\xf6i6\xd4\x1e)\xfc;\xb1\xe4\xd9Ok\nj\xefJO|\xd5\xf6\xd5:\x9cA\xed\x12i\x8e\x98\xd4\x8e\xa0\x8e\xc9\x8ewX\xf2\xdb\xed\xd4\x1e)\xbe>t\xdb\xdd\xd5\xcf\x8aS{Wzn\xa3\xb6i\xae\x94@\xed\x12i\x8e\x98\xd4\x8e\xa0\x8e\xc9J=\xa5\xf4\xdfA%\xa8=R\xdc\x99o\x08j\xef\xca:8\xeeB\xed\x12i\x8e\x98\xd4\x8e\xa0\x8e\xc9\x8aO)\xc9QCP{\xa4\xb83\xdf\x10\xd4\xde\x95>\xad\xacNWWP\xbbD\x9a#&\xb5#\xa8c\xd2h\x07yg\xf9\x07\x7f\xaf\xa0\xf6\xc8\xbb\xf3\rA\xed]\xe9\xaf\xb3\xe9 \'\xa8]"\xcd\x11\x93\xda\x11\xd41i<\'x\xe4\xd3F\xed\x91w\xe7\x1b\x82\xda\xbb\xd2\xdfV\xf4\x93\xe1w\xa1v\x894GLjGP\xc7\xa4\xf1)\xe5\x91\xaf~\xd4\x1eyw\xbe!\xa8\xbd+\xfd;\xf6\x1a\x94w\xa1v\x894GLjg\xc5!jS\xf7\x1e\xb41e\xbd\x0fQ%(G\xfa\xa2\x14y\xd6\x9f\xbd\x83\xe77tz\xa4>\xc8\x94\xdd\xb5$\x12\x07\x07\xa8M\xcf\xee\xfb\xa5\xe6*A\xb9\xaen\xa2\xf5\x01a\xcf\xee\xa7T\xef\xe0\xa3\x12Mt\xa9\x0f2ew-\x89\xc4\xc1\x01j\xd3\x87\xe1\xfe`L\x95\xa0\\wu?E7\xca\xa8\xa6\xfa(\x9e\xfc\xea\xe8AP\x1fd\xca\xeeZ\x12\x89\x83\x03\xd4\xa6>\xc1W\x9fb\x82r\xdd~\x13\xaf\xba\x1a\x8c\xf6Q<8\xce\xee\xa9P\x1fd\xca\xeeZ\x12\x89\x83\x03\xd4\xa6\xce\xfbw\xce\xfd\x94\xeb\xae\xe6\x1b:\xe5PM\xf5\x0e\xab\xab\xa2\xd4\x07\x99\xb2\xbb\x96D\xe2\xe0\x00\xea\x83$(W\x9d\xce7\xe4n\xa8\x0f2ew-\x89\xc4\xc1\x01\xd4\x07IP\xae\xba\x9ao\x9c=\xbf\xd1\xdd\r\xf5A\xa6\xec\xae%\x9188\x80\xfa \t\xcaU\xa7\xf3\r\xb9\x1b\xea\x83L\xd9]K"qp\x00\xf5A\x12\x94\xabN\xe7\x1br7\xd4\x07\x99\xb2\xbb\x96D\xd2 \xe5R\x9fE\xbd\x9f\xd2\x07\x86\x06\r\xb1{\xf9\xa8\xbd\x89D\x9a\xdbN\xda1\xe5R\x9fE\xbd\x9f\xd2\x07\x87N7\xc4\xee\xe5\xa3\xf6&\x12in;i\xc7\x94K}\x16\xf5~J\x1f\x1c\x9ao\x10\xbb\x97\x8f\xda\x9bH\xa4\xb9\xed\xa4\x1dS.\xf5Y\xd4\xe77\xfa\xe0\xd0|\x83\xd8\xbd|\xd4\xdeD"\xcdm\'\xed\x98r\xa9\xcf\xa0?\xbfQ\x07\x86\xafo\x10}\xd9\xcer)\xd4\xdeD"\xcdm\'\xed\x98r\xa9\xcf\xa0?\xbfQ\x07\x87\xafo\x10}\xd9\xcer)\xd4\xdeD"\xcdm\'\xed\x98r\xa9\xcf\xa0?\xbfQ\x07\x87\xafo\x10}\xd9\xcer)\xd4^W\xb7\r|\xe3\xb1\xfe\x9bZ\x92Hs\xdbI;\xa6\\\xea3\xe8\xcf\x8b\xd6\xc1\xe1\xeb\x1bD_\xb6\xb3\\\n\xb5W\xd5`\xf8\xe6\xd0\xcb\xa6gO)g\x894\xb7\x9d\xb4c\xca\xa5\xee\xa6\xcf7\xea\xe0\xa8\xf7S\x88\xba\\\xab\\\n\xb5\'\xf5o\x81\xf5\x8f\xb6\xbd\\\xf6\xffrp\x10i-\xe5H\x82r\xf4\xbc\xa87~\xbd\x9fB\xd4vv\xa8\x87}4X\xf5D\x98\x96K\xcf\xab\xd2S\xf048\x88\xda\xf6+E\xe2 \x90\xd6R\x8e$(G\xcf\x8bz\xe3\xd7\xfb)Dmg\xaa\x06b_\x0e\xab\x87\xa8\xe9:\xccgp4(G\x12\x94[}2\xeb\xfd\x14\xa2\xb63\xd5\x83C\xcb\xe3\xc1\xa0\x87\xa7\xfd\x8f\xb5\xf4\xbf}\xf9>\x83\xa3A9\x92\xe8\x19\xed|o\xf0\xaa6|\x7f~\x83\xa8\xef\xefp\xc5gp4\t\xca\x91D\xcf\xe8\xb4Q\x07E\xdd\xf8u\xbe!\x89\xfa\xfe\x0eW|\x06G\x93\xa0\x1cI\xf4\x8c\x1e\x18\xae\x83\xa2n\xfc\xfe\xfc\x06Q\xdf\xdf\xe1\x8a\xcf\xe0h\x12\x94#\x89\x9e\xd15\x83:(\xea\xc6\xef\xcfo\x10\xf5\xfd\x1d\xae\xf8\x0c\x8e&A9\x92\xa8\xef\xebJ\xa36p\x1d\x14\xb6\xcf7$\xd13SW|\x06G\x93\xa0\x1cI\xd4\xf7\xfdG\xe6\xea\xa0\xb0}\xbe!\x89\x9e\x99\xba\xe238\x9a\x04\xe5H\xa2\xbe\xef\xbf\xe4W\x07\x85\xed\xf3\x8dgHP\xce\xd2_6\xac\x83\x83$\xd2\x1cA\xb5\xa9\xfcbHZK9\x92\xa8\xef\xfb\x1e\x05\r\x8e>\xdfx\x86\x04\xe5\xecgp4\t\xca\x91\x84\xdf\xf3|C\xf6\x81\xa1\x8bP\xb5\x9dgIP\xce~\x06G\x93\xa0\x1cI\xf8\xbd\xfaGm\xfb\xe0\xd0\x95\xc9\xda\xce\xb3$(g?\x83\xa3IP\x8e$\xfc^\xfd\xcb\xc1}p\xe8\x86Wm\xe7Y\x12\x94\xb3\x9f\xc1\xd1$(G\x12~\xaf>\x13\xd1\x07\x87\xee\x8a\xd6v\x9e%A9\xfb\x19\x1cM\x82r$\xa1\xd7\xeb|C\xd6\x81\xa1\xf9\x86\xe8m=C\x82r\xf638\x9a\x04\xe5HB\xaf\xf7?\xa2_\x07\x87\xe6\x1b\xa2\xb7\xf5\x0c\t\xca\xd9\xcf\xe0h\x12\x94#\t\xbd\xae\x0b\\u\x03\xd7\xc1\xa1\xf9\x86\xe8m=C\x82r\xf6;38(\x97\x9arV\xdb\x9f\xdf\xa8\x1b\xfb\x95\xcf\x8b\x12\xab>\xea\x15R{\xf5\xc7\xf2\xa8=\x92\xa0\\*\x92\x06)\x97\x9aB\xb5\xf5/\x1e\xdb:8\xfc\x07a\x88\xde\xd6Yn\xc2\xaa\x8f\xcf\xe0\x08L\xa95\xda\xe9:\x04\xf7\x8d+\xeb\xe0\xf0a\x9a\xa8\xed\xd9\xdd\xac\xfa\xf8\x0c\x8e\xc0\x8a6\x986\x90\xfe\xb8\xab\xd4\x03\xb9Vs\x0b=\xb1\xad;\xac\xde\xf9}\xe3\xca:8\xac\x1e\xd3\xd3\xdf9\xd5\x04\xd5\xed\xe9\xda\x88\xfe\xd2\xb0\\\xfd[\x96\t}]k\x1f\x9f\xc1\x11X\xd1N\xec\x1b\xcc\xd2N\xdf\x99\xd3\xfcd7\xab\xf5\xfd\x0c\x8e\xc0\x8a\xff\x8a\xb1\xd5d\xd3\xeaBWU\xffJL\xbf\xe2\xd4\xd5\xeb\xb2f5\xe8\xa4\xdbR\xdbu`(\xdf\x97e\x07}]k\x1f\x9f\xc1\x11\x98\x92\xd6\xee\xceMX\xf5\xf1\x19\x1c\x81)i\xed\xee\xdc\x84U\x1f\x9f\xc1\x11\x98\x92\xd6\xee\xceMX\xf5\xf1\x9d\x19\x1c\xc4\xa46\x85\xfa \'P{$A9{u\x85\x94\xa8\xf5+_\xc2\xa4\xe3Im\n\xf5AN\xa0\xf6H\x82r\xf638\x9a\xbb\xa1>\xc8\t\xd4\x1eIP\xce~\x06Gs7\xd4\x079\x81\xda#\t\xca\xd9\xcf\xe0h\xee\x86\xfa \'P{$A9\xab?\xdc\xf2\x19\x1c\xc5\xddP\x1f\xe4\x04j\x8f$(g5\x10\xfa\xe0\xa8\xff\xbe\x86\xa8\xf5+_\xc2\xa4\xe3Im\n\xf5AN\xa0\xf6HB7\x08\xab\xbaD\xaf#\x06\r\x0c\xab{>\xca\xe8\xf1F\xfd\xf1\x97*\xf5K\xbe\x84I\xc7\x93\xda\x14\xea\x83\x9c@\xed\x91\x1d\xfd5\x1f\xda\xf9\xa9\xfd\x1a\x88\xac\xa7\x9d\x95/a\xd2\xf1\xa46\x85\xfa \'P{d\xa7\x0e\x0e\xddI\xb6\xf5\x9e\x8f\xef\x03\xd1\xfd\xa0z_\xe9\xed\x06\xc7\xbf\x01N M\x08\xcc\xbb\x8c\xa1\x00\x00\x00 tEXtlatex\x00\\frac{\\sigma_{tot}}{T_{1}}\x9c\x94$\x0e\x00\x00\x00\x0etEXtresolution\x00600\xf2~\xdd&\x00\x00\x00\x0ctEXtcolor\x00000000\xc2\x9f\xf6\xa1\x00\x00\x00\x16tEXtSoftware\x00latex2png.comJ\x05\xa9\n\x00\x00\x00\x00IEND\xaeB`\x82'
image_value_M=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00E\x00\x00\x00&\x08\x06\x00\x00\x00\x92\xedV\xdd\x00\x00\x05\xa5IDATx^\x9d\x9a\r\xb1$E\x10\x84\xdf9\x00\x0b\xe0\x00,\x80\x03\xb0\x00\x0e\xc0\x028\x00\x0b\xe0\x00,\x80\x03\xb0\x00\x0e\xe0\xfa\xdb\xb8o#\xb7.\xbbg\xdfEd\xc6\xedTwe\xff\xd7T\xcf\xbb\x97\x97\x97-\xbeZ\xfcs\xf1\xdfw\xe4\xf7\xcf\x8b\x9f.\xbey\xc7\x06\xcb\xe4\xc7\x8bh\xfd\xb4\xf8\xc7"Z\xff/\xfe\xb7\xf8\xd7\xe2/\x8b\xdf.N=\xfd\xaf\x80/\xfd\xfa{Q\xed\x7f\x16\xd5\xfef\xf1\xa3E\xf5v\x9aW\xe5\xb7\x01\xd0i\x1apR\xf8-\x7f\\\xbc\x12g2\xe8,\xf5\xd1\x92<3\x80i\x83\xdf-\x8aS\x07\x19d\xf61I_S[~\xbfx\xd2\xb4\xec\xa1\\\x83\x03\xa1\xe3\x9f-\x8a\x1f\x16\xb3\x11VA\xa4 \xa4\x03hP\x8fUc\x00jY\x07\xb0\x83\xa8\x93\x83\xfa}1\xb5\x92\x80\x95O\x1f\xb5s7\xb0 _/\xa6.>\xbf-&R;y\x07\x0f\n1\xdb\x08O0@\xc4%\x1d\x04)\xc8\xa0\xecH\xae\xbc\xb0\x9e`@\xd6\x97,LjJw\x07t\xe5\x13\xb3\xfe\xe7\x8bj\xea\x87\x86\x98\xf5\xe5\xc3\x03\xbb\x03\x01Vp\x82\xf2\x1c\xb0\xbc\x89,\xb0R\xc4\x0c\x1a\xe6\xdfO\x16S[\x8a\xb4\xb1\xeb\xec\xb44v\tV\x99\xf6\x88m\x94\x89\xd4\x11i\xc3\x0f\xbd\xec\xf3\xdc\xb5\x93\xf7\x1f\xee\x12\x1am\xa0\x8eG+I\xa0\x03NHnQ\xb5\x93"m\x1e\xa3\xa4\xbb\x058\xb0<Z\xc2\xe7\x9d\xad\x1dQwK\xd6K\xde\xc1d\xe4 \x1bX\xd1\x14\xa71\x1ap\xa5\xe7\x99\x15\xb5\xc1\x80\xdb\x1c\r\xc9\x11\xa6\xbe\x0b\xc1\x844\xa4\xb6L\xe4\x11\x92j\xef|n`\xab\xebP+\xbc\x03\xbb!\xc5s\x10\x94\xedpl|\x81\xf85\xf5xf\x81\xf8\x97c\xbd\xf3Mm\x99\xe0\xa8\xd9\xdf$m\xee|n\x06\xdf\x163\xf2O\x10hS8\x070c@"5eb\xd7q\x88>\x8b\x06\xaetD\x96\xe3k\x1f\xa7f\xd6{\x00\x86<:\xbb\x8a\x04\xd2&\x0e\x89G\xcdG\xa4f\xab\xf7\xe5b\xea&[\xee\xb2\xd3\x11Y\xfe\xc5\xe2\xab\'\x05\xe84W;\x9dZ\xc0\x82Lh\xd6kl\xc8rs\x8fI\xb2\xd2\xd7\xa0\xb5\xe7\x11L]\x9e[\xcaq\x873\x99\xc1G\xf8\x0c\xcd\x11rB \x81,\xeb56dy\xe6\x1f\xc9\x96\x1a\x9c\xd0\xda3P\xa7\xaec\xdd\x82\x94\x1d\xa7Lj\x84\x8d@V-\x85\xa1\xc15\xeb}\x08\xd5\xce\xc9&~\x81\xac\xf7,\xd2\xa7i\xb7\x97B\xfa\xdc\xce3\x01\xd6`\x96\xb0\x12[-\'C\x92\xfa\x83\x14|-S;;\xder\x89gq\xa5m\xbf\x13\xb5\x9d4N\x12H\x9b8\x13\xda\xea\xcbg\xe0\xf1\x9d\xda\x19\xbc\x1bE\xb3\x89L\nS\x9b6\'\xaaN\x1a\'9\x97M\xbc\xd5M>\x83\xbch\xa6\xf6\xcc#&E\xb3\x89\x8cU\xa9\xddPu\xd289\xaf\xfa\xf0\x94\xacM4M\x81\x8e\x9av\x9a@(\x9a\x0fH\xfb\x8e\xe8\xa8i\x1bd\xdd\x96\'\xd2\xef\x8e4&Y\xb1\x14\x95\xed\\\xee\xd0tEj:\x80_\x17E\xf3\x01io\x9c\t\xa1m\x90\xf7X\'\x91\xbew\xa41\xe9E1;\x0f\xdb\xb9\xdc\xa1\xe9\x82\x8c\'\xd0\x01\xe4\xfdk\xfa\x88\xb47\x9a\xa5K\xdb\xe0\x86l\x9dD\xfa\xd6\n\x89\x99C\xd8\xc8\xc9\xe7\x04\xdb\x83\xb3\xe3\x92U\x16Y\xbf1\x91\xb6\xf9*\xe6\xb7\xc9`\xf3}\xc0U\x85\x99\x9f\xd0\x80Y\xec\x87\xc0\xf6`\xfb>3\x13\xab\xac\xdf\x98\xd0\xe6}\xc7\xfeB~\xcf\x14b\x0b+$\x85\xf1d\xd2o\xb4\x8d\x89S9\xbf\xa7.\x1d\xcf\xcf\x9c`\xfa\xcb\x06\xcb\x88\x1bN\x8aD\xff\x94}?\xe0T\xc1x2y\xcaO\x12\xa7\xf2\xf6\x9d\x83\xce\xfb\x89S4\r\xd8`Y\xbe\xd1\xa4\x9f\x1fv|@3jkw\x12:?}|\xde1\xa1\xad\xad&\x9c\x99\xf5\x95\xce,\xcf\xa3\x03\x9d\xf0\xb6\xbb\x13\x0f\xf6S\x856\xe3y+\x16>\xef\x98\xd0\xe6\'\xc6\xa4\xf7\x9d\xc4\x95\xce,\xcfd\x10:)~\x01\x98\xf5\x05\xbb\x9fT\x80\x90q\xc7t\xd8\xc5\x93\xa7\xef\r\x81,\x97M{\xc6\x93\x89\xa6\x93\xe0\x99@\x9d\x93\x02yY\xec|\x84/\x14?j\xdf\x90Np\xf7\xe1\xe7\xe9{C \xcba\x8b\'p\xc6\x93\x89\xa9\x03\x13\xf6yNJ&l\xd3\x07\xe4\x91\xbb!+\'\xfd\xa4 u\xe2\x0b\xdc\tMkb\x17O\xae\xb6x\xb3\xa7\xad\xfd\xb5\x01>\x1c\x89\x80~\x8e\x95\xe3\xc3\xf3\xbd`\xd2O\x94\x92N\x9b\xfc\x9c\xd0\xb4&v\xf1\xe4\xca\xb7\xd9\xd3\x96w\x1d\xe9w\xe7\x06\xfd\xfc{\x97o\xd5-\xe8h\x8a\xf3\xcc\xdbH\xa1tN[\xb2\x01{\xea\xaaM<\x99\xfe\x93\'\xb4\x84\r\xb6\xbfb&=r-\xc8?\xc0;I\x8a\xf3\xcc\xf7\x89\x14\x14iK6\x9c\xf2\x93\xa6\x91<!\xefQ\xa9\xedqoz\xd0\x13\xf1\x10\xcfZE\xcf\x98\x8d\xc8\x19O\x9a\xef\x15v\xd9f\x8b\'\'\xbdY\xde&\xc5+\xc3NG\x9f\xf7v\x89NIg\xcfF`\x8b\'\xcd\xf7\n-\x9ed\xe7\'w\x98\xe5\xbcJ\xd5sRZN\x95\xf05\xfc\xde\x07r\x9d\x92\x8a\'\xfd\xdbn\xe3k\xd0\x82\xa1\xf9I\xd3L[cbj\xe7w\x99\t\xe2#u\xe6\x1f\x00o\x9a\xd3\xc0\x99o\x93r\xfaf\xfa,\x08\x86\xd9i\xd9\x82\xa1H[c\xc2\xbf\xf1H\x06\xdc`\xd6\xcb[\x87\xd7\xf5I\xf3\x06:\xe8Dd\x03:7L\xd1\x1dw\x17\xccS\xee\xd3t\x92\x13\\MR;\xff\xdb\x05\x0b\xee\xe7\n&$\xdb=i\xd6\x80\x95\x97\xa9\x86\x14<\xb1\xbdy8\x96\'4\x9d\xe4\x04\x03\xe5\xd8\xa8\xcf8\x88\x1d\xd9\xe6{w\x9c\x85\x93\xe6\rl/"2gt\xde.\x1b\xb2\xfc\x8a|mC\x17\x1a\xa7N\x98\xfe\x93\r\xd8\xc9?\xd8\x15\x8c\x83\x89\xa1=&\xc3\x04m\xfaj{\xf3\x16\xdf~\xd6G]t\xf9\xc0\x00\x00\x00\x07tEXtlatex\x00mZ\x8a\xbf \x00\x00\x00\x0etEXtresolution\x00600\xf2~\xdd&\x00\x00\x00\x0ctEXtcolor\x00000000\xc2\x9f\xf6\xa1\x00\x00\x00\x16tEXtSoftware\x00latex2png.comJ\x05\xa9\n\x00\x00\x00\x00IEND\xaeB`\x82'
image_value_D=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x009\x08\x06\x00\x00\x00\x86D-\xd7\x00\x00\x06\xc5IDATx^\x9d\x9a\x81\x91\xe54\x10D\x97\x0c \x05\xc8\x00R\x80\x0c \x05\xc8\x00R\x80\x0c \x05\xc8\x00R\xb8\xcb\x00R\x80\x0c\xe0\xd4\xbf\xb6\xcds\xbb%\xebo\xd5\xeb\xaa\xf5\xcchF\xd6\xb7,[\xde\x97\x97\x97\x97\x8f^\xd5\xb0\xaf\xc5\xfc>\xf4\xef\xd0\x7f\xaf\xd2\xdfV\xb3=#\xb7\xa7\xe8\xffs\xe8\xdd\xd0oC\xbf\x0c}9d\xb2\xcf\x949\xd9\xd2I\x18\xc8\x98\x8f\x87\xb2\xb3\xec`\xb3=#\xb7\xa7Vq>\xfeu\xe8\xab\xa1\xec\xb7eN\xb6t\x12\x06f\xcc\xb7C?\x0f\xe9\x17\x90T\\W\xc5\xdfC\xabN[\x8aU\xfb&\xe7\xa4\x9c_\xbf\xbes\xb4::~?\xf4\xc5\xd0\xac\xff\'\xdb\xd2\xb9\x80q\x19\xabKs6\x00\x1a ]A\xd9\x9e9vl\xba\xec5X\x99\x9f\x83"\x7f\xe3\x94\x8bI\xc5\xc9\xb9\x80q\x19\xfb\xc3\xd0l\x00\xbe\x1f\x12\xd9\x9e9vmF9\x9d\x9f\x03 \xe9^\x91\x9cre\xd2\x93s\x01\xe32vu\x05|:$\xb2=s\xec\xda\x88\xf2\xeads\x00$\xd9u\xd5\x99S\xaeUR\x06fL\xb3\x99\x7f\x86\xdc\x11Jv\xe6\xcb\x1c\xcf\xfa,\xf2\xc7\x10kr\x10\xcc\xa9mKb\x18\x981\xcd&\xf4K\xb0\x03\x94\xae\x0c\xe6\xcb\x1c\xcf\xfa,\xa2c\xdd\x04]\x93W\xc2\x8fC\xe2\xd4\xf6\xf8\xa3\xc0\xc0\x8ci6\xa1\xd5\x81\'M}7\xc4|\x99\xe3Y\x9fEt\xfc\xc9\x90kr\x00$\xdd<Omy0\x93\xd9\xf1y\xfegq\x1d\x7f6\xc4\xb6;Z\xb1\x8a\xd1\xaf\xed\xba\xd4_C\'Xl&\xb3\xe3\xe3\xfc\xe7\x00\xcc\xe6\xff\x9dV\xacbt\xd3\xe33\t\xf5\xf5\xd0\x01\x8b\xcdd\xee|\xfa\x85Y\x88\x030\x9b\xffwZq\x17\xa3\xe7\x00\xf6\xc7jK\xe32\xd9\xaeO\xf3_\'\xebB\x1c\x00\xf9\x84\xe3)\x93\xc73\xd8v\xa5o\x86\xd8\x07K}\xf3\x93\xe2\x81\x1b5v}z\\u\x81\x1c\x80g\xd6\xff;\xd8v%\xdd\x0c\xd9\x07K}\xfbiH1\x07n\xd4\xd8\xf5i\xce\xb9\x00\x07@v\xe3x\xca\xe4\xf1\x0c\xb6\xbd\x13\xdf\x1d,\xf5MK\xa5\xfc\x07n@lk\xbe\x84\xf3\x9f\x85$\xcd\xff\x1dZ\x1d\xd6o~\xb1\xf2i\xbeg\x7f||\xa2%`\xe2\xf4%Z\xe3\xb3\x80\x8f\xe5\xdb\xa1\xd5a\xfd\xe6\x17+\x9f\xa7%\xfb\xe3c\xee#\xd4\x04L\x9c\xbe\xa4\xad\xff>\xd6\xd5\xb1C\xab\xc3\xfa\xcd/V>\xbe1f\xff|c~\xd0\x120q\xfa\x92\xb6\xfe\xebo\xaf\xff;\xb4:\xb6Q\xc9\xca\xb7\x1a\x80\xc7\x9bi6l\xc9\xf2X0N\xbf\xb0\x93f!]\x82\x82\xf1\x12I\x1b\xe3\xd2\'\x9a-q\xccj\x00\x1e\xef\x06\x99\xcc\xc7\xcdF\x18\xa79\xee\xa4Yh\xb6\xfe\x93\xb41.}\xa2\xd9\x12\xc7x\xef2\xfb%=6L2\x99\x8f\x9b\x8d0N\xf3\xdfI\xb3\xd0\xe7C\x82\xf1\x12I\x1b\xe3\xd2\'\x9a-q\xccj\x15\xf0\xd5y\xc2\r\x9b\x08m^\xffS|\xfeOl\xa7\x8f\xb6\x14i\xfe\x94\x99\xdd\x9b$\xed5^h\xc9,b\x9b\x9e\xf0x\xd2\x946\'Z[a;}\xb4\xa5H\xf3\xa7\x8cO\xb6\r\x80\x9e\x06/\xb4d\x16\xb1\xcd\xcf\xffM\xda\x1blm\x85\xed\xf4\xd1\x96"\xcd\x9f\x12\x9a~\xab\x01P\xff.\xcc\x92\xcd\xd0e\xc4"\x92\x0by\xfe\x8bU\xae\x9d:\x8e\xd9\x8d\x13z\xedm\xfd\xf2\xb1^\x96.\xb0\x10\x93\xcd\xd0\x06\x03\x8bH.DV\xb9v\xea8f7N\xe4\xebp\x0e@}@c!&kh\xd3\x81\x05,\x15\xd1\xf2CV\xb9\xee\xea\x08\xc7\xec\xc6\t\xad\x00\xd9/\x0e\xc0)\x97\x1b6\x99\xb4\xeb\x12b\x01KE\xbc\xffo\xdc\xc60\xcf\xca\xf7V\xd4\xd6}\xc9\x13\x97\xa6o\x83M&\xedm\xfeK*\xc6\xf9/\xdc\xc60\xcf\xca\xf7V\xb4\xe1\xe1\xbe\xb4\x01\x98\xee\x074\x99\xb4\xb7\xf9/\xa9X\xe26\x86yV\xbe\xb7\xa2\x13t_\xda\x00\x1c;B;\x85Z\x8c\xbf\x10;!\x0bq\xfdom\xc5\xae\xaf\xc54\x7f\xca\x1b!<i\xf7\xef\xf4\x80v\xfc\xb1\xa0\xc5h\x89a\x01\'\x97\xb8\xfe\xb7\xb6b\xd7\xd7b\x9a\x9f\xe2VX\x1b\x00M]\xc7\xfe\xff\xc7\x82\x16\xe3\xb7\xac6\x00\xabO\xd3f\xd7\xd7b\x9a\x9f\xe2\xcbY\x1b\x00\xf6\xef\x02\x13%\xf4\xe5%\xe6\xe4Rk\xcf\xb63_\x83m2n\xe6\xcb\xe5\x8f}\xac[\xe2$\x93\x11\xdb\xdb%\xe6c\xad\xff\xad\xbdm+_\x83m2\xae\xf9\xfcn\xc2\x13g\x1fO\x1fE\x1aL\x96\xd8\xce\xfdv&\x97\xb4\xfe\xb7\xf6\xb6\xad|\r\xb6\xc9\xb8\xe6\x9b}\x12\x93t\xd5\xde\xc2d\x89\xed\xba\x89\xcc\x06@\xeb\x7fko\xdb\xca\xd7`\x9b\x8ck\xbe\xdc\x9a\xa7n\x7f}\xd1\x92\xa6\xb8\xfe\xe7@\xc8o\xb2\xdd\xae\xee\x98\xc5\xe9\xcd\xd4\xfdH\xf9\xc9\xef6\xbf\x83f\xe2\xa7g\x89\x03\xe0\xf5\xdfd\xdb]\xdd1\x8b\x9b}\x0c\x95\x96w~\xe2\xa0\x99\xf2\xf9\x9f\x03\xe0\xf5\xdfd\xdb]\xdd\xd1\xe2\xbc/\xc1\xbeY\\\xf7/\xf9\xd3\xc8\xc0\x94\xe0.k\x16<\x1e/_\xc9\xb6\xa4\xf9Z,\xe3Rd\xf6Y\x8e\xcb^kw1\xfa\xb8I\xe4\xb76\x0e\x00\xe3D\xb6%\xcd\xd7b\x19\x972\xb3\xado\rJ\xfb\xe7\xa8\x13i\xf4q\x93\x9f\xff)\x17l\xfb\x7fl\x9b4_\x8be\\J\xe8\xf3V\xeb\x8f\xfe>}\xfa\x1a\xb0\xdd\x01\x13^\x9c\x81\x9f\xff\x9b\xf8\xfe\x9f9[\xde\xe6\x9b\xc5\x8a\x16/tE\xfa\xa4\xa9\xdc\x8f\x10\xccq\xe4\xba\x18\x16\xe4\xfc\xa7\xda\xfe\xdf*o\xf3\xcdbE\x8b\xcf\xffG\xb0f_\xa3\x99\xe3\xc8u1,\xc8\xf9O\x91\xcc\xd9\xf26\xdf,Vd\xbc\x9f\xf8\xa4<\xf9\x9d\x1c\xd6\xc1\xc50``\xfe\xb7\x05\x8bj\xfe\x13\xb6\x9b\x89\xa4\x8dqMm\xb3C\xd2\x15\x9a\xb1$}\'\xff\xc50``\xfe\xbf\r\x07 \xf7\xd7\xd9n&\x926\xc6\xa5\xdagx\xc9s>\xe3I\xfaN\xfe\x8ba\xc0@>\xffK\x1c\x00\xfd\x8f>a\xbb\x99H\xda\x18gi\x0b\x9b\xff\x01*\xb9/\xfc\xce\x9f\xedH\xfaN\xfe\xa5s\xb0;\xff\xdfB\xd6\xcb>\xe43\xbe\xebj\x9d\xbf[\xea2\x97h\xb6\x931\x9d\xab\xef\x7f\xb7\x1b\x0c\x1bd=\x1f\xeb\xcaR~\xd5\xc9\x01\xd0\xbe\x03\x1fr\xcc,\xd7\x9d\xeddL\'\xef\xb8\xa9\xb6\xde>K\xd6\xd3\xfdF7V\xfe\xda>ymh\xae^k3\x97\x8f\xefl\x07tJ|\xf9\xe1\x89\xdb&\x7fM4\xc8\\\xb38\xcdo\xe5\xd1}\x86\x9f\xb3\xb3\xe6\xecFG\x99<\x16\xcd\xf6\xb8\x8c4\xc7\xf4+k\x19Q\'t\xa7\xd5/\xb0\xea\x8cm\x8aQ\xbc\xda*\x07\xa5\xe5*\xa58=\xc0\xe8\x12\xd6\xe5\xbdz\x85\x95t\xef\xc9\xab\xcc\'\xd2d\xf2X4\xdb\xe5\xe9\xaeu\xc2Z\xc5\xd17\x8b\xd9\x8d\xd3\xa0\xea\x87\xc8\xd5\xc5\xf8D\x9aL\x1e\x8bf{\x8c\xee\xaa3\xd4*\x8e\xbeYL\xc6\xe9\xd7\xd7/\xac\xe5M\'\xac\xed\xec\xdcRo\xd0\x9f2y,.\xb6\x0fV\xd8\x96\xd3\xd8-\x91\xec\x00\x00\x00\x07tEXtlatex\x00D\x188\'L\x00\x00\x00\x0etEXtresolution\x00600\xf2~\xdd&\x00\x00\x00\x0ctEXtcolor\x00000000\xc2\x9f\xf6\xa1\x00\x00\x00\x16tEXtSoftware\x00latex2png.comJ\x05\xa9\n\x00\x00\x00\x00IEND\xaeB`\x82'


image_height=250
image_width=150
param_height=15


mean_delay=3.125e-10 
log10_jitter_min=-4
log10_jitter_max=-2
nb_log10_jitter=int(1E5)
v_log10_jitter=log10_jitter_min+(log10_jitter_max-log10_jitter_min)*np.arange(nb_log10_jitter,dtype=np.float64)/(nb_log10_jitter-1)
v_jitter=10**(v_log10_jitter)

log10_ratio_period_sample_min=2
log10_ratio_period_sample_max=6

nb_log10_ratio_period_sample=int(10**(log10_ratio_period_sample_max)-10**(log10_ratio_period_sample_min))

v_log10_ratio_period_sample=log10_ratio_period_sample_min+(log10_ratio_period_sample_max-log10_ratio_period_sample_min)*np.arange(nb_log10_ratio_period_sample,dtype=np.float64)/(nb_log10_ratio_period_sample-1)
v_ratio_period_sample=np.array((10**(v_log10_ratio_period_sample))*np.pi*0.5,dtype=np.uint64)
p_opt=5
nb_bits=20000
nb_nibble=int((nb_bits)/4)

v_std_dev_value_widgets_option=[]
for i in range(v_jitter.shape[0]):
    v_std_dev_value_widgets_option.append('%.2e'%(v_jitter[i]))
    
    
std_dev_value_widgets=widgets.SelectionSlider(options=v_std_dev_value_widgets_option,layout=widgets.Layout(height='%dpx'%(2*param_height),width='%dpx'%(2*image_width)))
std_dev_value_widgets_png_desc=widgets.Image(value=image_value_relativ_sigma,format='png',layout=widgets.Layout(height='%dpx'%(2*param_height)))    

sample_period_value_widgets=widgets.SelectionSlider(options=list(v_ratio_period_sample),layout=widgets.Layout(height='%dpx'%(2*param_height),width='%dpx'%(2*image_width)))
sample_period_value_widgets_png_desc=widgets.Image(value=image_value_D,format='png',layout=widgets.Layout(height='%dpx'%(param_height)))    

m_value_widgets=widgets.IntSlider(value=1,min=1,max=8,step=1,layout=widgets.Layout(height='%dpx'%(2*param_height),width='%dpx'%(2*image_width)),readout_format='d')
m_value_widgets_png_desc=widgets.Image(value=image_value_M,format='png',layout=widgets.Layout(height='%dpx'%(param_height)))    

raw_bytes=widgets.Textarea(value='',rows=5000,placeholder='',description='',disabled=True,layout=widgets.Layout(height='%dpx'%(image_height),width='%dpx'%(0.5*image_width)))

progressbar_widgets=widgets.IntProgress(value=0,min=0,max=nb_bits,description='',bar_style='',style={'bar_color': 'maroon'},orientation='horizontal',layout=widgets.Layout(height='%dpx'%(2*param_height),width='%dpx'%(2*image_width)))

html_download=widgets.HTML(value='',layout=widgets.Layout(width='%dpx'%(6*image_width)))
save_data_in_file_widgets=widgets.Checkbox(value=False,description='SAVE RANDOM NUMBERS IN A TEXT FILE',disabled=False,button_style='', tooltip='Description',icon='check',layout=widgets.Layout(width='%dpx'%(2*image_width)),style={'description_width': 'initial'})

v_list_nb_premiers=[5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,199]

v_x=np.array([ 0,  1,  2,  4,  8,  3,  5,  6,  9, 10, 12,  7, 11, 13, 14, 15], dtype=np.uint8)
v_s_x=['0000', '0001', '0010', '0100', '1000', '0011', '0101', '0110', '1001', '1010', '1100', '0111', '1011', '1101', '1110', '1111']
nb_tau=100 

if not('T0' in locals()):
    T0=3*mean_delay*2

if not('v_T' in locals()):
    v_T=np.array(v_list_nb_premiers)*mean_delay*2

"""    
print('T0=%e sec.'%T0)
for i in range(m_value_widgets.max):
    print('T%d=%e sec.'%(i+1,v_T[i]))
"""    

def generate_rnd(std_dev_value_widgets_in,sample_period_value,m_value,save_data_in_file):
    
    std_dev_value=v_jitter[v_std_dev_value_widgets_option.index(std_dev_value_widgets_in)]
    duty_cycle_value=0.5


    T_sampling=sample_period_value*T0    
    
    raw_bytes.value=''
    m_raw_bits=np.zeros((nb_bits,m_value),dtype=np.uint8)
    
    for m_index in range(m_value):
        half_period=0.5*v_T[m_index]


        M=((T_sampling)/half_period)
        M-=p_opt*np.sqrt(M)*std_dev_value
        if M>=0:
            M=int(M)
        else:
            M=0
        half_M=int(M/2)

        ros_state=(np.random.rand())<duty_cycle_value
        m_raw_bits[0,m_index]=ros_state
        tmp_half_per=half_period*2*abs(ros_state-duty_cycle_value)
        current_phase=np.random.rand()*tmp_half_per
        progressbar_widgets.value=0
        t0=time()
        for i in range(1,nb_bits):

            tmp_half_per=half_period*2*abs(0-duty_cycle_value)
            current_phase+=half_M*tmp_half_per+std_dev_value*tmp_half_per*np.sqrt(half_M)*np.random.randn()

            tmp_half_per=half_period*2*abs(1-duty_cycle_value)
            current_phase+=half_M*tmp_half_per+std_dev_value*tmp_half_per*np.sqrt(half_M)*np.random.randn()

            while (current_phase<=(i*T_sampling)):
                ros_state^=1
                tmp_half_per=half_period*2*abs(ros_state-duty_cycle_value)
                current_phase+=tmp_half_per+tmp_half_per*std_dev_value*np.random.randn()
            m_raw_bits[i,m_index]=ros_state^1
            if (time()-t0)>0.01:
                progressbar_widgets.value=int(m_index*(nb_bits/m_value)+(i/m_value))
                t0=time()
            
    v_raw_bits=np.array((m_raw_bits.sum(1))%2,dtype=np.uint8)
    
    progressbar_widgets.value=nb_bits
    v_nibble=np.zeros((nb_nibble,),dtype=np.uint8)
    for i in range(4):
        v_nibble+=np.array(v_raw_bits[i:4*nb_nibble:4],dtype=np.uint8)*(2**i)

    v_hist=np.zeros((16,),dtype=np.uint32)
    for i in range(16):
        v_hist[i]=((v_nibble==v_x[i]).sum())
        

    nb_words_to_be_used=v_nibble.shape[0]-nb_tau
    v_T5=np.zeros((nb_tau,),dtype=np.float64)
    for tau in range(nb_tau):
        v_T5[tau]=(((v_nibble[:nb_words_to_be_used])^(v_nibble[tau+1:tau+nb_words_to_be_used+1])).mean())-7.5
    
    fig_height=image_height/80
    sleep(1)
    fig, ax = plt.subplots(2, 1,figsize=[fig_height*1.5,fig_height])
    ax[0].bar(np.arange(16),v_hist)
    ax[0].set_title('4-bits words distribution', fontsize=8)
    ax[0].set_xlabel('4-bits word value', fontsize=8)
    ax[0].set_xticks(np.arange(16))
    ax[0].set_xticklabels(v_s_x,rotation='vertical')
    ax[0].tick_params(axis='x', labelsize=8)
    ax[0].tick_params(axis='y', labelsize=8)
    
    ax[0].plot(np.arange(17)-0.5,np.ones(17)*370,'r')
    ax[0].plot(np.arange(17)-0.5,np.ones(17)*254,'r')
    
    
    ax[1].plot(v_T5)
    ax[1].set_xlabel('Lag', fontsize=8)
    ax[1].set_title('4-bits words Autocorrelation', fontsize=8)
    ax[1].plot(np.arange(nb_tau),np.ones(nb_tau)*0.23,'r')
    ax[1].plot(np.arange(nb_tau),np.ones(nb_tau)*(-0.23),'r')

    ax[1].tick_params(axis='x', labelsize=8)
    ax[1].tick_params(axis='y', labelsize=8)

    
    fig.tight_layout(pad=0, h_pad=2.0, w_pad=None)
    plt.show()
    s_line_raw_bytes_value=''
    for i in range(nb_nibble):
        s_line_raw_bytes_value='%s%X'%(s_line_raw_bytes_value,v_nibble[i])
    raw_bytes.value=s_line_raw_bytes_value   
    
    if save_data_in_file==True:
        s_line=''
        now = datetime.now()
        str_time = now.strftime("%d-%m-%Y_%Hh%Mm%Ss%fms")
        randomvalues_file_name='ex1_a%s_jit%s_D%d_%s.txt'%(duty_cycle_value,std_dev_value,sample_period_value,str_time)
        if exists('random_values')==False:
            mkdir('random_values')
            
        fid_rnd_file=open('random_values/%s'%randomvalues_file_name,'w')
        fid_rnd_file.write(s_line)
        fid_rnd_file.close()

        path_to_download='%s'%(randomvalues_file_name)
        s_line_for_download='<p> random numbers are saved in the following file %s stored in %s</p>'%(path_to_download,abspath('random_values'))
        html_download.value=s_line_for_download
    else:
        s_line_for_download=''
        html_download.value=s_line_for_download

interactive_plot = interactive(generate_rnd,{'manual': True}, std_dev_value_widgets_in =std_dev_value_widgets ,sample_period_value=sample_period_value_widgets ,m_value=m_value_widgets,save_data_in_file=save_data_in_file_widgets)
interactive_plot.children[-2].description='GENERATE RANDOM NUMBERS'
for i in range(3):
    interactive_plot.children[i].description=''
interactive_plot.children[-2].layout=widgets.Layout(width='%dpx'%(2*image_width))  
v_box_top=widgets.VBox([widgets.HBox([widgets.VBox([interactive_plot.children[-2],widgets.HBox([m_value_widgets_png_desc,m_value_widgets]),widgets.HBox([std_dev_value_widgets_png_desc,std_dev_value_widgets]),widgets.HBox([sample_period_value_widgets_png_desc,sample_period_value_widgets]),progressbar_widgets,save_data_in_file_widgets]),raw_bytes,interactive_plot.children[-1]]),html_download])
#display(v_box_top)    