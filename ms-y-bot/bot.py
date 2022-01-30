import time
import random
import datetime
import coloredlogs, logging

import numpy as numpy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sched, time

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", logger=logger)
scheduler = sched.scheduler(time.time, time.sleep)
bob = ['tsukinomoriuk', 'isabella.cheng', 'horaceli103', 'c.bukk', 'vcee604', 'colaho', 'yeungdenise', 'peggytsang34', 'southiscis', 'goodboy_louis', 'harry.w124', 'tungmi', 'yingkyip', 'doggiethemiu', 'terryterry_tc', 'chow_pooh', 'leungfong_1999', 'marcocoho', 'wai.wong.90410', 'pomagg', 'anthonytsang100', 'billcheng0925', 'im_juno_chan_', 'yatonykoo', 'l__y__h__', 'ronin.tattooist', '16.05_colin', 'gweepetopia', 'dearjoanne', 'shuttercat', 'tracykwann', 'lorraineee_chan', 'sethfung', 'iamnotannabelle', 'chunyujohn', 'casssey__', 'robertcastalano', 'swada', 'mark_s.l', 'albertlausy', 'heyjesswong', 'ir.i.des.cent', 'anguskm', 'laililian88', 'kin.chan.5891', 'shelleyluk', 'losanloo', 'kevin.funggg', 'samreikoken', 'gigismy', 'shirley._.leung', 'leemsms', 'eeleelyam', 'hiuyanl', 'feybbb', 'fakfakseng', 'lamchikwong', 'missy.ivy', 'kawing0913', 'choi_bong_', 'xkcoolx', 'iultenaj', 'tabi_tab', 'cliffu', 'babylinclon1001', 'moneykwok', 'jack_cheung888', 'makkkristy', 'l.meisze', 'philip.fok', 'yhm716', 'sophiesofi', 'g8_emily_momo', 'patrickchan__', 'ngsuenho', 'lawkayan', 'matthlam', 'mandidi', 'carolyippppp', 'chan.jerry.351', 'maliama2011', 'cseeleng', 'feii.lilac', 'tesslau2007', 'pkcheung', 'square.mimi', 'tinggiterry', 'melomelomelody59', 'yaoxiang.deng', 'alex18tung', 'amnget', 'szew_0303', '_venusz_', 'nicoleoiyi', 'cwy_kellly', 'cch_arthur', 'henrylau1979', 'on999isme', 'lampard6019', 'cindyngan911', 'ddsiuyu', 'wingh.y', 'tangjoannamy', 'tobiahyue', 'lilila_laa', 'andrewhk88', 'matthew_526', 'arpaddy', 'leungsn', 'ningkyoong', 'amymy', 'tiffanylawaletta', 'ronaldgum', 'auntie_japjap', 'keeno_c', 'chezycherry', 'hhazelll.t', 'clara_peekaboo', 'scofield_lyp', 'okpatbb', 'natalie_tai', 'kopingching', 'jacksonnnnnnnnnnnn', 'dinduck2', 'idgaftoyall', 'kenneth_ip_hk', 'cat_cyl', 'danny.danny003', 'card1ary', '100cpp', 'wym_____', 'kit.tsz', 'shaz1728', 'pps_chan', 'edisonlee0821', 'leungclj', 'saeleesarah', 'kelvin_poon167', 'theodorayeahyeah', 'alanchan11_10', '_hin0103', 'nikki_yw_lau', '456bbbbbbbb', 'poyee.t', '_.mbykysjwiahj._', 'mankitkitt', 'jessicachann', 'christytwc', '_____ts2k1n', 'edithyed__', 'cptttim', 'lckjasonb', 'idylfm', 'swsflorence', 'yeegugu', 'drew_llm', 'gogoau', '206ecaroh', 'ray_lamk', 'mscching', 'kennis.c', 'aa_in_uk', 'double.aitchh', 'roywong0909', 'leungyanki', 'marco_ccc_', 'coconut_ng', 'louie.tk', 'free_aroma_', 'mhy_iris', 'powpow_0211', 'louise_tsj', 'itsmekhaiyee', 'hzcheung', 'makbilly711', 's.t.l.am0304', 'chakwanglee', 'fungmarcello', 'victoriachan681', 'superb_eugene', 'allan__chen', 'kenson0516', 'pak.kit', 'wong_keung', 'complicated.wld', 'burdonhorizz', 'au__poee', 'maisanleung', 'rlau114', 'shannonchoyy', 'kenny_lo04', 'joeyandben', 'hungharry', 'a.ma.teurtrader', 'magmagkiki', 'virginiashum', 'ycw5849', 'aiiiyahhh', 'tyrone_hk_', 'chunchunchunchunchunchunchun', 'wang9511', 'yu__dung', 'chingxxching', 'ricky.816', 'chaochaoleooo', 'xxoscarrrrrrrrrr', 'pollyng615', 'fsodu._', 'calvin.chan.197488', 'marcella.lau', 'nsb180699', 'yanny_hy_s', 'top_london_', 'woja_i', 'kawing_lo', 'hellodomo', 'velkhana_waka', '1ly.ty', 'kayim48', 'jameskct', 'grace.chow.5036', 'lau.c.shun', 'cb.newlife', 'mkl615178520', 'tira.lai', 'ju.li.a.na.so', 'wingyful', 'rainnnnnnnn_', 'nft206', 'uk.irrelephant', 'tayinvillage', 'yv_nne1314', 'therealfoodieee', 'beatricewonggg', 'lapyinto', 'hennmle', 'jasonlemontse_mkii', 'w.fong520', 'marc.1027', 'tsung1220', 'lyttttt9418', 'au_out_out', 'ngankiki', 'tommychan1719', 'jcchingliu', 'tak_lung', 'oooooscarice', 'eunisisatrash', 'fr_ankiez', 'im.jooo', 'tifftiffchu415', 'minminako_dir', 'info_showbusi', 'fan_li_gp8524', 'kayttakatie', 'hinn0413', 'billkpchan', '_natalie1025_', 'mariavictoria__celestino', 'elviscwc0908', 'cooliecool.cc', 'gafa_production', 'eric_huii', 'vincentjan1', '_bruceeee.c_', 'acheukk', 'stev.li', 'seirrehc', 'applec2004', 'jnseestheworld', 'leuunnngggyyy', 'cubaboyz', 'wayne160392', 'athenameiiiiii', '_.c.c.c.c.c.c.c.c._', 'anson_k_c', 'jadepacc', 'jon_llam', 'nhy_lo', '6.lmmm', 'chanchor', 'zoeeeltl_', '_00.a._k._', 'yiulamtam', 'gilbert_sin0000', 'lnsy.1832', 'puipuiyu', 'pkwok9', 'leungbart', 'franciswong_bug', 'waterisuncountablenoun', 'hcl030201', 'fionfionn', 'as.k.dn', 'bennyyip16409', 'leehtchris', 'hkpod_shop', 'edward0360', 'tszzchinggggg', 'danny_jiah', 'harvellous', 'so9jed', 'nlwwhy', 'charcharchu', 'florachan0118', 'kirkhenry.12', 'chi_momo1', 'tingkwok_0221', 'sobrinoreal', 'b.abm', 'wainanawainana', 'kaakaac', 'marcosohk', 'ks0820171', 'mar.cus_99', 'mr_pootis__', 'p11h22c', 'patrick.leung.9527', 'runrunrachel', 'corey.s_b', 'daniell28', 'matthew_waiwai', 'kayk.fan', '_iyiu9', 'qubbbie', 'honsing1516', 'iam_eddy_19_', 'xyxjojov', 'eryatw', 'carlos_clau', 'anson_chaulh', 'seanwongck', 'keshalms', 'kylecheung_ccf', 'jayzlok', 'leungmermaid', 'rextsoi716', 'lad222lad', 'waiyipleung', 'pepechan67', 'hugo_cylui', 'loklok_lau', 'dummyrunner28', 'miss.peggy.w', 'qqqrayppp', 'sifuken', 'chongwnam', 'sylai531', 'kwokkin_poon', 'in.voked_1101', '6uo_____w', 'nk.kathy', 'moonmewnnn', 'felixchan1221', 'arthur.c0212', 'sim0n1ee', 'marco465354', 'sstay21', 'good_old_bridge', 't.c_k', '__thy___', 'pasu0214', 'cozyccm925', 'timls', 'whatevergoodla', 'eric_cthhh', 'joshua.sham.908', 'lilliancsk', 'noifjejfemmf', 'andersonchan', 'asd202202', 'venusswingyi', 'antonio_tamtam', 'mryeungkf', 'mina_mc', 'benjamin.yeung', '519ye', 'lkmc1014', 'manl.lee', '__jasssmine610', 'queenielcm', 'wongyuntung', 'm.waiyi', 'cuddle_me', 'kch.1976', 'acelauwl', 'lmingkit', 'jimmyc17', 'sam_nebula_', 'lisaawong', 'aaronlo.z', 'ohno999', 'chrisnatalie2004', 'nicholaschui', 'hohoho111234', 'jasontam_jt', 'homanlan', 'ebino_shi', 'divinexa', 'sinwailon', 'mareky_collections', 'cykuk', 'kinkenttt', 'kotobanohana_teichin', '13a1111', 'sincheukhheii', 'sagittarius_chiro', 'ckh823', '_insidethemoonlight', 'brand0425', 'mikecatboy', 'jeffreychoi59', 'devilorindetail', 'charnotyours', 'ka_yee16', 'zet_chu', 'trolleydollywalluby', '_tangjaci_', 'cl.8333', 'marcus_li_05', 'krissslok', 'jckwc_r', 'lo.erin', 'flores.chef', 'fionalihw', 'maybnextimelol', 'dereklam712', 'yingying.au_', 'qequeenie', 'lovefreelifestyle.fitness', 'kennywongggg', 'yvonnelau0616', 'megusta.hk', 'bri_411', 'zooeyleeyau', 'dylantfw', 'sq_tc_leung', 'myw82006670', 'mrsspeckyowl', 'joshyu31', 'sekwanfan', '2100_rapidltd.exp', 'candyleeaaan', 'enakeung', 'wrufoto2019', 'y.s_____.y', 'endy.lam', 'chechechan', 'bobalouiehasafarm', 'eeeeecccc', 'wasistdasssss', 'windycly', 'simon_sysy', 'hertzcheung', 'jchow928', 'rabbitwywinnie', 'messi_cici', 'sor.9rylor', 'burburleo', 'raymondng603152022', 'millyyys', 'leunny211', 'ako1116', 'ling51129', 'laisandy18', 'dustbinbae', 'agsnx_ka', 'smy_hkuker', 'onfg_cct', 'ken3213212000', '03.terry', 'kamanwongg__', 'wnkugen', 'jiaxtwo', 'hk_lui123', 'weknow.hk', 'kelvinmini', 'raychow1125', 'jimmykhan_mars', 'mk.vinkws', 'rion_vegetto', 'kwanying_life', 'r.cchlol', '_0719ctc_si', 'jengchingying', 'tbwjournal', '2isnaashc_', '_nicolenc_', 'cheungcherie', 'iammrsyam', 'sinyi.1216', 'waikiki888', 'wakakaka_25', 'jennifermindmatter', 'llamaislandnft', 'ruby.c.1919', 'joy_hm_nurse', 'larry_lloonn', 'baabaatony', 'thmaychange', 'changiwayyy', 'ig_iwhkg1128', 'wong_hanghang', 'tungsunny', '00123zx', 'fuckmarkzuckerberg1234', 'connie.cmwong', 'kylieeee.cheng', 'n96.95', 'hinsonlo727', 'ffyiammm', 'leoyuenhiufung', 'peko.na', 'jojo199004', '_.foreveryoung.___', 'tonetoneyiu', 'cat_li_rex', 'leungwhhenry', 'terencewong_wcy', 'kkl0612', 'crystalkate86', 'kin_wong2046', 'deb_bie_bie', 'ginsontang', 'jyc0114', 'ykk_tommy', 'eugenia_lam', 'ardiswhl', 'stephie_to__', 'hanleeson', 'dempseyhihi', 'minami_hayama_lv', 'kinglong_li', 'hins022', 'iris_cklllll', 'ruka_metal', 'fatkidinheaven', 'timothy_timho', 'ly_hulk', 'joycexxwong', 'rustau__', 'my.tracyfung', 'carol_li_siu_nga', 'chris._.yip', 'vincredible26', 'moon.lightstranger', 'justinlee8964', 'chan.chanoscar', 'oja.ma.jo', 'lonaldtsoi', 'simonterry_lam', 'bonbonshop213', 'aurorooooo1', 'fatmingrestaurant', 'fungmavix', 'broken_limbs_lyn', 'kayuz510', 'ylamwong', 'j0el0ng', 'wuvvvvv_', 'jkyk.wong96', 'bigca', 'vmeeow', 'iehnk', 'yauyau1016', 'mariapark0426', 'carson_cs', 'pangtong_shiyuan', 'vania.fcw', 'jasonxzxzxz', 'rekzilla', 'lalagarden2828', 'lukelo_ss', 'mart_yeung', 'monya_wawa', 'yt__tung', 'i_hate_kiwifruit', 'chubbyconstance', 'marco_lee.1', 'charmywongg', '0101angus', 'tracyncl', '____qqtamama', 'hotlala_foodie', 'jjjj201920192019', 'pennymac', 'lonita_tong', 'bobobbb', 'tsundokuleben', '_me232', 'namchan_hk', 'carman.tai', 'cgl12_9', 'carsoncheng130', 'japland.uk', 'scuderiaderek1471', 'viviansinwy', 'tivolipoon', 'uklengmui', 'tracycyl_fe', 'luxifer_w_1110', 'x.ckl__', 'ytwong102030', 'ltwandrew1', 'whtmar', 'lok_1874', 'debbbbi', 'hinnnnn_10', 'janeleungyc', '852lovecollar', 'lawrence__________________wong', 'vahrem.w', 'tommyhinhin123', 'geranium1314', 'spoiled_by', 'yaunam_', 'smithchan1234', 'jox3h', 'karinaaa.ckk', 'vincetongtong', 'awake_meditation', 'leungsirclement', 'hotspring._', 'laimarthk', 'wscj_0317', 'mang_resing44', 'swy.realm', 'aliliwww', 'tsut_pri', 'kl_professional', 'kwokkiho', 'taibo_cheung', 'danjclu', 'oscarlam_spotter', 'orangelau11', 'awc903', 'i.wanttotravel', 'dickson.tt', 'joanna_jl', 'is_me_mariooo', 'mavis_sheep_', 'thomas_w0ng', 'lkf_fff', 'bbl0327', 'foodnfeline', 'kenneth.kahei', 'manleethx', 'julia_mashimaro', 'tsetincheck', 'jenniferferfer2.0', 'jason_yhl', 'paultsang87uk', 'hassan1h', '__2hsssy0', 'ktbil_ly', '_jaden_chow', 'stefanste96', 'cheng_pit_kai', 'mantontsoi', 'ontheroad_31', 'ng___yuki', 'wuskywu1029', 'yuhinluk', 'jandamannnnn', 'chan_c_fu', 'lagwanchunhin', 'angiesiusiu', 'theo.huii', '96tse_ellen', 'nat_natalieee', 'tobybyy', 'tu._0915', 'matthew_yuen1016', 'sandy_sthy', 'szud6_9_0_0', 'jesschakyw', 'wanlamines', 'marcus_tennis_hk', 'shawnlch', '0oturbokingo0', 'rhlchou', '_matthew_0895', 'maonshan_johnnydepp', 'kkl_z', 'mandyeung27612', 'chloechanreal', 'c.hungsang', 'xuyjyjyjy', 'jandy_chim', 'little_heyso', 'uakenneth', 'hellomynameis358', 'black.chh', 'gargarbo', 'kims_smiks', 'drewchan1205', 'y.ant', 'timothy113', 'ricky_yuen_hairstylist', 'tomlung1016', 'winstonthegolden2021', 'cathoolala', 'makkachunnnn', 'jeffho312', 'mck.k_', 'henrychow326', 'koli_can_cook', 'xiaoming6281', 'mrjonathanchan', '1d0o1o', 'chris_fcy', 'samanwks', 'helenlee128', 'bear._.iam', 'ataka.hk', 'sabrinaaaayan', 'thatck', 'tourmaline868', 'ting._bo', 'strangejoanne', 'kaho_cheung', 'sheliatse', 'alexlee9801', 'p._perry0117', 'moonology', 'lucas_yiu._.0308', 'merripui', 'zetachileelo', 'nike_tony', 'titan_ho', 'holong27', 'msyl____', 'bkboyboy', '_eva._.eva._.eva_', 'kennytongtky', 'lorenz.1209_', 'kel22_lau', 'sophiee0329', 'losuettching', 'kenneth_sin', 'raymondng343', 'saiii1014', 'mayflyinmayfair', 'ksw.76', 'alex_wongc', 'leottin', 'kasin904', 'jasoncwj_731', 'djmansing', 'ourheadz', 'kobayashi.suki', 'azusaaajp', 'sweethomeinuk', 'sandy_ng_ng_', 'i_am_nwl', 'bana.r_69', 'ansonfung920', 'ben199135', 'loislau', 'kitkwok1022', 'adowell105', 'chop.per.mot', 'hongkongnufc', 'yut.a_1', '_wwiu_', 'nossalai', 'useriousd', 'ryanklw_', 'fp_hkg', 'yiuyan', 'ronaldlee82', 'fafayanks', 'sikjikngsikjik', 'nabi_littleshan', 'planfreak', 't.kkaa', 'hosik.uk', 'alexpaklong', 'siucakeb', 'kayi_serendipity', 'silversurfer0506', 'me_mormor', 'sunnyszzz', 'alice5pm', 'sarahchan8866', 'patrick_ngai_', 'ko.be226', 'hllee0128', 'sumyuklo919', 'trix9200', 'kennis.kan', 'manninnnnn', 'daniel_bodenstein1', 'irisay804', 'phat_him', 'kkcoxox', 'sunnysunnychung', 'p1ka34.c', 'johnnghy', 'godyett', '_3_3.3k', 'plccheung', 'martinisking', 'bernice_chm', 'explode._.explore', 'leochancp0810', 'mikecdot', 'waichi.yip.3', 'jasxwong', 'sumthingsss', 'kristykko', 'carribeanskyline', 'jonathanhui88', 'janicethy', 'dabkaka', 'hk_kenfong', 'ywcbilly', 'changde.wu.9', 'chakmarco', 'w.mky__', '_w_cs.l', 'yuekalong', 'tyk_4.6.9.8', 'anton.wor', '_eddiecheng', 'andrewy7788', 'advent.ca', 'yuenua', 'jacky_chau123', 'bababebellie', 'shiuwaichung', 'chan_kinny', 'samcheng__', '_miss_yuenwoon', 'jennyts111', 'shoyo_da', 'monkeystuffs', 'waiman1031', 'rw.hok', 'oscarwu_', 'kkk.sml438', 'gig3975', 'wsl_02156', 'sforho', 'leaxnechan', 'polaris_r154', 'jerryhtchan', 'yarrrpin', 'be_a_happyguy', 'oscar422_', 'train_frds_', 'tammytammm', 'wongtaishing', 'kenkam62', 'elysesss', 'ml.0206_ec', 'sharon_wcy', 'kekakakebb', 'student_chenggggg', 'shunliu', 'rebeccasin2014', 'hm_mhy', 'cheung_1124', 'c1arenceee', 'sky_lee_619', 'sesamecha', 'samlamsl', 'jc.post2.0', 'show_quali', 'lhmfantasy', 'hoifung1223', 'vivianyu718', 'god_of_hea', 'frederine_', 'byronkwokch', 'rebecca_liu_1998', 'feejee_mermaid', 'munsandy', 'mclauhk', 'inlokyu', 'apieceofsummmer', 'ronronron172', 'jackycct_', 'seamatch.rs', 'takonl', 'ginasuen', 'tk1357901', 'celiaaak', 'thianyit', 'eunice.sun1', 'catlinwww', 'jaslou__', 'fifi_on_therock', 'jenniferlamkwan', 'rac_lovecook', 'blossomsss.boutique', 'summdimsum', 'tam.c.9', 'momoseto', 'ok.wrong567', 'kit0403', 'shan_cts327', 'joymok100', '21oct3_', '_kristyckk', 'kenny.yh.wan', '_tipofthetung_', '_hy1118', 'loyauyau', 'lula_french', 'simonlee0705', 'aiufami_hk', 'c.ypl', 'm_i_good_', 'lui.matthew', 'flamingobloomhk', 'gown__gallery__', 'mdycm13', 'makyiulong', 'ivychuchu', 'elaine.wong.3998', 'kolll0225', 'shunleongye', 'bbcreambb1', 'ginnynnnn', 'tony_wwt', 'winki_fan', 'jakelyw', 'shirsuetsuetley', 'watersportsgroup', 'ckwai22336', 'nicholas.kklw', 'lam.tracy', 'hm.wong0629', 'jenny2chiu', 'allahhafizblb', 'xy31858a', 'rar24567', 'ben_bang_bam_6969', 'chanpuiting4321', 'ty529_', 'ztpv_daily', 'dannyhkp', 'jeffchan', 'ellesse716', 'ckckckckck8888', 'cw1323', 'bryanlolctk', 'harry_ckh_1031', 'chandickie', 'jessiekyw1319', 'merakiii.music', 'leo_chan_hi', 'wjs__09', 'tsz._.kiii_', 'ki_pri._.01', 'bulobak', 'prudence_ho', 'kitcck8', 'kayu_h', 'kylelaw_0722', 'wongkalailai', 'samtam_yoga', 'katttttie_chan', 'hangry_leung', 'emily_hanyh', 'jiu_anne', 'mandyman8', 'wilson208pri', 'seazzll', 'edberebdeee', 'kraftwerkthemodel', 'oceansuun', 'auyeungki', 'lui_chi_lok', 'wissy_11', 'irisleung1997', 'sharonhungusa', '6012_jv3756', 'carloslkn', 'the_healthfield', '20160314xdd', 'karenpschoi', 'teresaksini', 'balloon.jjj', 'chantwinklechan', 'chu_olivia_olly', 'dangorgon83', 'criswellkwan13', 'koeylaolao', 'theonewemeet', 'arthur1176', 'gerrygogerry', 'davywong1023', 'abcc_family', 'kachunng98', 'ericpn', 'highland_cattle22', 'tommokyc', 'jun________lin', 'imayukimura', 'chungkwoktsang', 'wanderlust.floral', 'benleungleung', 'kelvinlui2008', 'pammygnews', 'how.is.chelsea', 'anthonytclai', 'wcjdjoshuayung', 'lukepermaul', 'alanklwu', 'suzannewong85', 'yveslau', 'billyfong1211', 'annie_eats_things', 'bonnie.fung.58', 'junco_drinko', 'victorliuyc', 'icecreaminology', 'wingman0127', 'scipio._', 'catherine_choy', 'selinatangw', 'wenyu.mei', 'happyfoodhealer', 'ngfaihung1', 'pwlszeto', 'southbanktower', 'cheukling919', 'yellowyellowsubmarine', 'since_have_mi', 'kunkeongg', 'larosebakery520', 'ericericchoi', 'donnyhaha', 'anniewhone', 'aukawo', 'y._.ching._', 'bosco_man1118', 'mkwwww81', 'tony.t.adl', 'jeff_wong_cy', 'tming.yim', 'gill.fkl', 'vanes_sa_y', 'harharlam', 'henrytam.0718', 'tt.hhh7', 'schanct_714', 'ansontttse', 'wailau250', 'iamkarachan', 'candy_kyanndei', 'yan_chong_', 'vic_ipy', 'mediumrainbow', 'shdprobablygotobed', 'choi_waikit', 'zionhkii', 'iulekim', 'iamwingng', 'kelvinkpl', 'keith_tsang91', 'derek.lomo', 'jeannie728', 'lmszeee_11', '007_fxckingthis9588', 'ltfffff', 'kl_cheung', 'sw129', 'localenjoy100', 'ahegaoreva', 'jacky_tegent', 'mayslee10', 'oobi.oobi.oobi', 'jpyuuu_', 'cowboyskent', 'clasasasa6109', 'r.__.lyk', 'bunnycentre', 'chankinfun', 'monbupi', 'gary180997', 'raymondlee857', 'kanwongmr', 'gyu4gung1', 'edwin_ylk', 'crystal_sell666', 'ordinary_._night', 'dorraa_128', 'davisfung_', 'tsloverbb', '98wai_20220105', 'florence.yim', 'queen.kitling', 'miranda.mio', 'mattylauu', 'vuikkic', 'pandas_976', 'samanfaccccc', 'cavinceng', 'ivanlo5401', 'eiknarf_14', 'mosquitontk', 'bettacwk', 'anguz_129', '_kimmychong_', 'tyhk1223', 'cpwin.18', 'ray.hs.leung', 'jlmc23', 'hotunggg', 'psc_dan_', 'anson.cos', 'kitymankit', 'mxman1108', 'gwe_gwe_dog_gu', 'simonleung94', 'manwfung', 'pull_upghost', 'kwun_wing', '__leungwc__', 'chhanng._', 'no.escape_630', 'matt.lo_matt.lo', 'eydw722', 'n.i.g.e.l.c.h.a.n', 'iwanwife', 'thoma.sss.isw', 'diana.woo1', 'henrybakei', 'alienspeter', 'eric__kc', 'tinee_gm', 'betsy77774', 'hs_oxdv369', 'mat21.05', 'henrykong_0120', 'l.enneiviv', 'mr.charles.lo', 'queenwings', 'cml.cheung', 'wouse051', 'leftcolddoor', 'fayelau', 'yiuyuenyee', 'jasonkjyap1', 'sherinechu', 'kawing51', 'squid.001_man', 'himchanimsc', 'chaos.0309', 'channcarmen', 'jumokuso', '_image_not_uploaded', 'sckcarthk', 'jie_jack', 'fruit_pagex', 'wanlaiyen', 'tszyingcrystal', 'claudiamakeupatelier', 'minizespri_', 'chow0yg', 'mr.yearrr', 'claudiactravel', 'maggiepig1102', 'mcty14', 'makwan888', 'frenchbeefhk', 'lwyrita', 'yellowlinkuk', 'lhtingggg', 'felix.kwm', 'jordon.fong', 'consbunny.p', 'pakhoyiu', 'aaaliceccc', 'elton_king_wong', 'lau_yin_yeung', 'lks3970', 'maisie.uta', 'waisubi', 'echia000', 'horace_not_horus', 'parker_______98', 'denisecly', 'forcemax', 'kelvinhllo', 'jurecordne', 'annoying_lindda', '06.04.__', 'man_021116', 'ttfbb._', '_nytng_', 'kinfunglaw', 'askyloveryu', 'jenny.ip.jenny', 'riccolamm', 'dondon_629', 'ng.tuen', 'fung2002', 'chrislai8537', 'tobyfung_lok_yi', 'leong64', 'misswkwong', 'den619', 'ester.vi', 'crazie_epoch', 'recording_the_fading', 'fhdernotaka', 'mandyoey', 'choichoi172', 'alex_ausk', 'usg.usg', 'ko_malalalalalalalala', 'music_sman', 'horacefung_3', 'isabella_chu', 'eifelblc', 'keepitdark._.852', 'jeremymok227', 'itsdamnbro', 'kelvinluk_lkl', 'nwy12', 'calchunlok', 'k2n9', 'ani_ch9', 'cheungkamwing214', 'gloryszeto', 'liuliuliu_official', 'kitmanman', 'meatbarhk', 'victorho19', 'paulocheng63', 'saya_lam', 'isthomas', 'billyccn', 'killmeal', 'ka1019ty', 'heitoto_', 'samue1john', 'fong_isaac', 'iw.lin', 'yikchun___', 'mtcomrades', 'yin1031yin', 'lungjai00', '007daima', 'pandora.phoenix.18', 'chuchu_yan', 'j_kong1008', 'khmarcolee', 'mingtse18', 'hmman1207', 'x.xaaron', 'son.suyeon_', 'edith_csf', 'evanchan2', 'cy.driced', 'cheukhinlee', '__1740114', 'howahyeung_0403', 'kamwing1224', 'joeku36', 'emily_azusa', 'leeahmiu', 'nana10_vip_igot7', 'wwaiyiu', 'pluslam', 'jade.sze', 'a123123', 'littlessm', 'kyatmb', 'vincentyau', 'lo_mau', 'dannykmui', 'thelazyasiangirl', 'dannychingrealty', 'emsandra_', 'magizzz', 'a.l._melody', 'taikitcheong', 'martin.dkj.chan', 'carl.yau', 'dingdingisnotgood', 'rainieyip', 'annalyk1219', 'dicksonchong._', 'bird_kiwi', 'cyrus_4c', '_mi.tung_', 'johnng4352', 'md_hvingfun', 'shingyk', 'lawlululu', 'gsitu09', 'jerrylsu', 'boscomrpandahkg', 'dancouga_hui', 'jenny929', 'anke_ca', 'laimingmar', 'dom.dom.dom_', 'moneywongmanlee', 'john.choi.399', 'big_headb_yuzu', 'lookupyoursht', 'bmwyip', 'maniinuk', 'wesleyoosij', '1amyannis', 'wongjiyuet153', 'kamen_wai', 'jth.wong', 'happyreadingsee', 'haydenchl', '__howard.10_', 'ilynnhoj', 'y.b.d.m_enicay', 'liu6479', 'miletoonnnm', 'hope_neverend', 'tagh5933', 'wongcrazy_', 'tmarriddle', 'jabezchung', 'peggylee0315', 'charlotte_602', 'kaya.kong', 'grantwong0824', 'thejessieli', 'chan_pei', 'taoking64', 'jenlam2016', 'lccerica', 'kam.ming', 'esthersssfun', 'invisibleasdf', 'timothy_kong', 'food_notfound', 'jen_and_her_3js_world', 'ginkhaawdiary', 'shad.mohammad.alharthi', 'yolo_keepmovingforward', 'fatfatlo', 'leo_wong_1217', 'zaf.quin.hilda', 'cwhhhandrew', '_ykmekl_', 'fxp88man', 'david531lee', 'anthonycheung131a', 'stephenchow777', 'optical_master', 'billykhw', 'alexw0922', 'rachelcemac', 'phoenixbighead', 'hahae0201', 'alext013', 'mayng_ht', 'eddca4', '404errorjai', 'tszlong9294', 'pri_irvine', '_.matthewhck._', 'bigboss.0317_vezuviy', 'yangweier', 'w_.wing', 'jay_kay_cookie', 'ylunchung', 'yoyoharu', '_philipppp', 'kristaltk', 'teey_aitch', 'tracykwok43', 'patrickwoo1317', 'hgfdfghvvggggc', 'desmond.wh', 'bubugi.store', 'chelsea_chung_', 'ccpsucks8964', '1aumann', 'cherrylcyy', 'gigiji99', 'edmon.ng', 'mercury77s', '_a.l_41_', 'mailliwho', 'szelui00', 'ccson0703', 'winniec920', 'ansonthy', 'maple.01111', 'gigibubiharry', 'tc.wanyung', 'anson_wong2422', 'atososta', 'andrewchan9888', '1ucasao1', 'isaac_leung_1026', 'markclf', 'jolly_03.29', 'soulenterlam', 'aminggg97', 'manjai0315', 'frankiellm', 'dhy.____.1113', 'cocoafat', '__yansk', 'aughc4', 'w_lokhei', 'eilatan0204', 'yu_lee.3020', 'danny.dyg', 'ohohlulu2021', 'cyrus1229', 'ms_ella_h_', 'sdu213', 'ihcmiynahc', 'a.r.m.y.maka', 'yy_yuyy', 'tiffanygrad', 'tw555222111', 'cwct733', 'giraffeholook', 'louisa_leung_', 'kandiliyu', 'bilabilawinghk', 'ivanhkm', 'joeymiffy', 'minglau1123', 'susssssuet', 'wah9872', 'kc0529w', 'civilian_life2021', 'ernest_tse_ml', 'k_ling', 'jc17367485895', 'kittyauyeung', 'katiechankk', 'marcolau2002', 's.a.m.r.e.i.s', 'tzewahchan', 'sorman_instagram', 'royseng', 'chiyuenwong', 'juliewxng', '_c.fuji', 'lizzytam', 'o.lenyu', 'mikey9to9', 'sssiuling', 'sno.opywong', 'wah.yeung.1960', 'wenan____', 'bgp.mark', 'hirx_93', 'shing_charles', 'health_nutrition_coach', 'haofanayuyuyu', 'hobbyson220', 'yungyungmama', 'lgeo_0523', 'toosiuki', 'beautybijyo', 'littleprogrammerjoel', 'treechibi', 'rickytsang', 'be_a_nicesss', 'hlt_hkg', 'startfrom_2022', 'victoretse', 'keto.8811', 'chi_laihc', 'gpandabj', 'bigpan14', 'van.channn', 'wsytaaa', 'i_am_biscuits', 'kkw11_', 'hungjai330', 'johnma8890', 'martxla_', 'lawhiuhei', 'fungfung222222', 'kahochan1231', 'ming02lau', 'ncksbpqatqnm_8', 'iamjanyu', 'bessieli', 'shiyinnitokyo1', 'jags0.agog', 'yanyanyanchiu', 'phornpatsorns', 'weiqiang2851', 'victorng33', 'ngohailarpsarp', 'jundong444', '__.tszfung__', 'julialcy', 'allisonchan', 'leelee_yee', 'edwinlam0419', 'johnl_21_', 'roy_k3721', 'cls_oppa', 'kalok_law', 'jonas31248', 'fcfc998', 'lo_waiman', 'comeonjames2022', 'jjadebee2', 'gabrieltam_waiho', 'kt47777777', 'te_tttt_tttt', 'jimond', 'enjeru0303', 'markwindy81', 'jason_stillnotbanned', 'eamonlam_', 'samc908', 'minalihoiming316', 'nsc_bren', 'n.o.e.l.l.e.e', 'kahong416', 'colin_ckh831', 'donald1418', 'lemonialaa', 'ccpaustin', 'a.keung676', 'alvaheung', 'joeyjiji', 'karokeiko', 'cycma2003', 'fwk1225', 'nickcyeah', 'syed_certified', 'panandthecake', 'cottonman_', 'ronald1997_930', 'kevinyeewoooo', 'komaisie', 'cakimcapang', 'timckl', 'gloria.auyeung', 'chungminghong', 'janice_ce', 'angel.secret.love', 'cfyip2002', 'jonchau90', 'lufi0401', 'melokwok', 'irisip', 'yip.cy', 'angel_cct', 'sophie5069', 'evannaspriland', 'hj_091205', 'vic_to_ria_b', 'kayilau2021', 'vin.clai', 'psycheheung', 'vanlovesummer', 'fishball.fishskin', 'twitwitwinky512', 'amberbb0707', 'rebeccalau626', 'cw_lee88877', 'cheukyin_417', 'hinchng', 'lawcls', 'chautungyung', 'haydennnnn_10', 'bobbyng', 'winterishere_a', 'hello.ringss', 'stareasonick', 'aka.dull', 'c.y._fung', 'sinkinwine', 'saiyuk4', 'thpkleung', 'yam4608', 'harrykwan_', 'cheung.y.h', 'rachelwuwuwu', 'debbyhty', 'emmawcleung', 'bobbyshum', 'erickksan', 'imoliveln', 'yyfongyy', 'jessielto', 'juliannawu39', 'carson__kimkim', 'heliwong_', 'chin_toshi_hiko', 'duffduffhehe', 'jinchao_cao', 'sharksnrays', '_johnnie_lcy', 'joanneyuen13', 'erinng2000', 'hh.haam', 'nataliela', 'ros_hjn', 'p_dicky.ip', 'rickyybear', 'aunt_dok', 'herosze', 'easonor0628', 'ronniebiscuit_real_account_', 'jorunalingideas', 'eric__choi', 'leekamtong927', 'terencehitchoff', 'lhk.express', 'kaaangie', 'kellychan969', 'harry.tang.swimmer', 'cwsaaaalice', 'livleung', 'kwwncbam', '___anos.16', 'cyszo_4aro', 'oi.chu.7503', 'kcjoeonboy', 'mangi_calicomoggie', 'charleslimad', 'porkchopwing', 'taichijack', 'stayawayxx', 'lawmingkit', 'eievui0314', 'dndyajvmt', 'lam__0915', 'wonglucky11', 'dreeeec', 'tangclive', 'sisisimonemone', 'ggfrmjt_88', 'imfrankieee', 'anthyngai', 'iam_cks', 'winghong.c', 'brianlaihh', 'warrenkks8', 'rubyruby.a', 'leslie._80', 'kuok_hei_', '_tse_0726_', 'chun_910', 'wongkwanyat', 'fongenoch', 'bon.shum', 'letsgobranddon', 'ccc10_77', 'ritalau0907', 'kobe.6921', 'siu_tuung', 'cindykwok113', 'lcsing0502', 'remember.replace', 'yannisyiu', 'fullmoonzi', 'stephenhfwong', 'paklickl', 'toy.fai', 'returntofreud', 'yphsien', 'autumnchau', 'ochaisiupak', 'chiieng.tong', 'kklee06', 'tommylo0327', 'karzz', 'pangpang410', 'jennnnn_yt', 'jesus.christ.doctor', 'famichicki', 'gogogolwy', 'duradesu', 'jeouxlo', '1etmehelpu', 'leechunting2003', 'auhinyeung1995', 'wps.anson', 'lilykwong0822', 'cherry.chanfelita', 'ilovephotouk', 'tintinchowchow', 'oldmoneycollector3402', 'nerukuma_27', 'puipui_1975', 'theatheistchristian_', 'zogigeh', 'bernard_t', 'rieockh', 'i_wasabi_i', 'danielsmlau', 'ltyltyltyltylty', 'kwthryywsf2', 'yinzzzzz', 'airballyou', 'james_ao419', 'kaaasuunnn', 'olivialamlam', 'kahlenchh', 'ho.faat', 'roberttungfy', 'edmundchy', 'connie.hooooo', 'lk12_21', 'leemarjo', 'clam__666', 'phoebecheungbb', 'bernice.chow', 'albe_ngcheukho', 'homaho_ma', 'kimberleyyywong', 'hehetam', 'beebeejeanie', 'ronald709', 'yankibae528', 'naomihui', 'zoe_lee_st', 'piyochow', 'kaitlyn_ltl', 'bunbunyip', '45.67945', 'domoyu', 'tatktp', 'heisnot56', 'seeway25', 'sum_sum_lol', 'kelrackrc', 'platini_ng', 'milkyyvonne', 'iwu3uuejalp', 'adriankmchan', 'sunnyleeyh', 'connie.dodo', 'mister.dex', 'lunglam6688', '12_22_kkc', 'andreaso.lh', 'mushroom.amy', 'nippbluelabel', 'ravkwok', 'wong.terry.5', 'daphnechewxq', 'shachun852', 'gsz.wong', 'tom_tom_1668', 'chingandme', 'sugarwky', 'loudpink', 'barry.yan', 'byron.leung.90', 'milkju72111', 'lcb0719', 'mony_yip', 'raylmh', 'z3040066', 'yi_yi_bu_she', 'yugi_miyake', 'j_y_0731', 'jen.ytlee', 'brigetteeee__', 'bosco_channn', 'jim_wan_hk', 'charles_kw_wong', 'ieatcupnoodles', 'hoyip_x', 'singa_luvar', 'ttti.gni', 'hkchunho819', 'rekundesu_', 'heison99', 'wonglapsun', 'hasan521513', 'tobei747', 'aprilleesk', 'carlyh0_0', 'ilovechingsum', 'chestercky', 'fionahtchan', 'danny.w.wo', 'irissiu_wawa', 'btgkaaa', 'hoiyee.chan.945454', 'prismcarpetcompany', 'mw_hohoho', 'germany_cheung', 'carlcarl56', 'louiskwanz', 'victor_flute_sax', 'dealersing', 'janetwu_wu', 'pkedwardyeung', 'willnnn32', 'akitam13', 'lgniw', 'ppmchan', '__wklam', 'astro27287', 'will_mehsi', 'kathykasasa', 'kkpinga', 'yammy2255', 'jujus_mama', 'michellenywong', 'kennethchu88', 'jimmylwk02', 'semifinalsss', 'klwvg2', 'myeong.ming', 'richardhaha129', 'kwokfredfred', 'connie_estee', 'sunnyso_0312', 'kencheng91', 'chungsaiman', 'rileyssssucks', 'lamsiumuk', 'vickymkc', 'eshopmoo', 'desmolau', 'edzwolf', 'tomfu1023', 'isabelchanhk', 'yannychow', 'swansasa', 'deeleungvv', 'tonyeung23', 'alexcsm01', 'magordad', 'ng.ian.hkfreedom', 'leolauleolau', 'jujusaidhi', 'maggiewyl', 'astroboy1017', 'momorina2046', 'viviansiu97', 'kymherman', 'samluhs', 'mandicechan', 'little.breezee', 'mattlam620', 'kc_jack', 'error2582', 'camerash', 'lamhenry', 'kkkittt', 'ctcheung44', '_onmypillow_', 'ben08son', 'mm_3_143', 'wallylovesmiki', 'tingsiuchun', 'vickyyung1019', 'carni_123', 'riokwan', 'lkf_', 'derick315', 'shashahh', 'nicktse123', 'faifaiivy', 'yang0688', 'ivan.cly.819', 'georginayeung', '01086967440.67132765.24906529_', 'lecaferacer7', 'the_rach_el', 'francoyaya5', 'henrycl_2360', 'tommy_bigwhite', 'wilsonleungwaikiu', 'asa01233210', 'ivy.mamamia', 'kforkitkit', 'wayne_c_y_tsui0826', 'christinepsttt', 'iriscpyan', 'heikechau', 'kathyccy', 'jojojojo1234996', 'andre___au', 'juli_chau', 'tw_lam', 'vhappybird', '_sx_c0', 'bacon.mom', 'cat.toro.16', 'ka_heyoo', 'lulu.nomad.lulu', 'hotdogistasty', 'tiffianylo', 'esther_eleele', 'kenneth.choy.3', 'cotswoldtang', 'ytttuuunnnggg', 'emtiwbiv', 'toitoiiiii', 'ds_bluejh', 'ayden_wong', 'annettett', 'ap_alpha', 'csping_kissssy', 'taiw_c', 'hondaze_', 'happysiuyee', 'jojowong01', 'tinachchch', 'kellvinyim', 'jefftywong', 'wtkwong', 'mavisxdd', 'y__p__k', 'cc_journal', 'sennwing', 'p._lok', 'a_y_c_h_lex', 'karson_hoc', 'jpanguk', 'janet.leews', 'christiney_lilam', 'vyvy2020', 'ip_kaka', 'queenland9896', 'v.vvvvovv', 'uncle_m_eric', '_nahzc_', 'ianchunyat', 'billywanever', 'catherinewly', 'hellojoeyleung', '_._be_a.k0_', 'fook_fook0102', 'chloe.ctz', 'yung_yung_tsoi', 'aoiuminohon', '_m.6uo_', 'samuelshihss', 'nelson_pwl', 'angelyyan', 'asiansempowered', 'timmy.ccf', 'hamprinceeeeee', 'yoanna_misses_japan', 'cokeung', 'ho_wai_tw', 'dexter.yeung', 'aki_tnh', 'abrahamlui', 'banana_shek1220', 'karenleungcc', 'soowingni', 'millyhsf', 'williampan86', 'samuel924', 'megann_wongg', 'ricebandits', 'makbearbear', 'waiwai.c626', 'avennah', 'marywrong', 'k.kwan.l', 'larissa.0930', 'yan_lok_leung', 'godandwin.c', 'autszkix', 'imhhl', 'benny_jai_', 'cymnik_', 'savecomfile', 'cyrus0322_', 'tseyhin', 'clmfoo', 'mygraceg', 'zoe.t.life', 'cheungleung117', 'ttinthehousetastyfood', 'winkie1218', 'natalielc29', 'eveurquhart', 'lifewyyonna', 'tommy_tsui1016', 'janleung0130', 'aqualuxury__', '724kaka', 'lokkk40', 'desmond.kiang', 'joshyip19', 'pinkymak93', 'cattsz111', 'virginiawwy12', 'katherine__u', 'graceli1030', 'buildingfoursea', 'tonylau777', 'woohotin', 'gtsangkh18', 'liuanka', 'love_55699', 'sailouis', 'healthyfood_kindergarten', 'arthur_kc_chan', 'yiumama', 'marsssssstx', 'mariafung123', 'fifa20_career_mode1', 'doreenchan999', 'piusox', 'nunnunyau', 'chassiechan', 'a_s_h_l_y_n_n_c_h_a_n', 'jameshwsuen', 'kanas7763', 'hoyuenshan', 'jkbobe', 'clownray', 'herecomethem', 'chagokingcharles', '9503abrazosfa', 'matthew8765xyz', 'colama2011', 'rogerwong_panpan', 'tuffypig', 'manshingrestaurant', 'szechun202', 'mandy_amj', 'yschim', '3mins.media', 'kalok.wong.90', 'man_janet', 'freedomyau_ceramics', 'msjoanlam', 'kulu720', 'jaijaima', 'bayumak', 'singsingwong14', 'jasonfaye37', 'james_wong2099', 'chiwing7298', 'simonkwok2', 'audreyaudreyccc', 'mick___chu', 'bearbeardon', 'chan_jo_jo', 'mramra282', 'yasmindang1', '_mch.0811_', 'vicmylaw', 'tehcthecoke', 'bean.small_b', 'derek1128', 'emmi.wong', 'halloallison', 'chanjimwing', 'taidorpeople', 'sgcdnjecefjce', 'miss_jean_nie', 'bladenbeans', 'testingabccba', 'chenglam_ho', 'dora_ctw', 'victorpigsty', 'ck5886', 'sltk.2727', 'kaylietanghl', 'chakyutsang', 'maxi.gif', 'bellakwok_', 'woowoo9', 'ruthlaiyan', 'daphnefung', 'nailczz', 'coffeeandtea._._', 'nheroina_', 'chanpancy', 'kitkit0917123', 'rainbow_loveys', 'dhehwjksj', '_hcwlam', 'northstarhk', 'lu__109_', 'yulok0509', '_6unal', 'rubybylym', 'lalasuitcase_eliana', 'candycan_442018', 'patsham16', 'karlhkh', 'rainmakerbing', 'llll_a30p30', 'kassidingg', 'tseman3', 'emily_funfun', 'luk6_yee2', 'patpatchan1992', 'rm1412020', 'nkjcrystal', 'ng_arthur', 'christieccsung', 'cin418', 'el_yeung', 'manmandy116', 'itingxoxo', 'ericaciraa_', 'perry88188', 'tammankitttttttt', 'pakyinnnnnnn', 'hang_0621', 'jessi_ieong', '_spiritchildren', 'spicagnes', 'lamsangchan', 'mathself', 'regina_thorell', 'olo_lpp', 'tilllateno', 'peggylam1913', 'e_book_promotion', 'runn__ok', 'tm46709394', 'gcwcheng1', 'manjoint420', 'vivi_lam', 'lam_tracy', 'henryleung2017', 'liukahang', 'keep_contact', 'mrs_couture', 'joechowkc', 'hor_chi_le', 'eywokuk', 'daniel.04.17', 'carina_so___', 'woo_una_aaa', 'hochintung', 'leontsoo', 'kckk_093', 'nij___c', 'vanya.mmm', 'saraa_l1', 'sheungyib', 'dcarchman', 'abrandnewdayday', 'raywong_kk', 'wendalam', '0423akinyk', 'rachel_112112', "sandeeysl",  'chanceuxnflawlessme', 'sandeeysl', 'terriehoho' , 'rubylam8886', "sandeeysl", 'gpwags', 'mei.kenn_90', 'sarah929', 'yanyiu', 'rubywhc', 'cybersin17', 'kinkilam__', 'anndylee', '_ko2025', 'iammai824', 'cherrrry04', 'wallis__leung', 'kkwong.hh', 'wkw_1114', 'nicolesit93']


def wait(minWaitTime, maxWatitime, operation_name):
    logger.debug("**** [NOT A BOT] buffering: {} ****".format(operation_name))
    time.sleep(random.choice(numpy.arange(minWaitTime, maxWatitime, 1)))

class Bot:
    def __init__(self, username, password):
        # self.driver = webdriver.Chrome("chromedriver")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com"
        self.app_start = datetime.datetime.now()
        self.to_scout = []

    def go_to_user(self, user):
        limit = 5
        while limit >= 0:
            time.sleep(1)
            try:
                self.driver.get("{}/{}/".format(self.base_url, user))
                limit -= 1
                wait(5, 10, "opened user profile: {}".format(user))
                return True
            except (TimeoutException, WebDriverException) as e:
                logger.error("cannot open user profile with reason = {}. Retry initiated.".format(e))
                return False

    def set_value_to_input_by_name(self, name, value):
        input = self.driver.find_element(By.NAME, name)
        input.send_keys(value)

    def login(self):
        logger.info("Logging In: {}".format(self.username))
        self.driver.get("{}/accounts/login".format(self.base_url))
        wait(2, 3, "opened login page")

        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Accept All')]").click()

        time.sleep(2)
        self.set_value_to_input_by_name("username", self.username)
        time.sleep(2)
        self.set_value_to_input_by_name("password", self.password)
        time.sleep(2)
        try:
            logger.debug("Waiting for login form to be clickable")
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.ID, "loginForm"))).click()
        except TimeoutException:
            logger.error("likely blocked by insta temporarily")


        # WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//button[contains(text(), 'Allow All Cookies')]"))).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Not now')]"))).click()

        wait(2, 3, "logged in: {}".format(self.username))

    def find_accounts_to_follow(self, user):
        # go to users/followers
        logger.info("going to account {}".format(user))
        if not self.go_to_user(user):
            logger.error("cannot visit user profile: {}".format(user))
            # TODO
            return

        # followers = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "follower")))
        # waiter.find_element(self.driver, "//a[@href='/instagram/followers/']", XPATH).click()        # followers.click()

        # Wait for the followers modal to load
        logger.info("getting followers from user: {}".format(user))
        # waiter.find_element(self.driver, "//div[@role='dialog']", XPATH)
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers')]"))).click()
        wait(3, 5, "clicked on followers pop up")
        scroll_box = self.driver.find_element(By.CLASS_NAME, "isgrP")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            wait(1, 2, "scrolled down")
            ht = self.driver.execute_script('''
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            ''', scroll_box)
        links = scroll_box.find_elements(By.TAG_NAME, "a")
        names = [name.text for name in links if name.text != '']
        logger.debug("account scrapped: {} ".format(names))
        self.to_scout = names
        return names

    def find_user_profile_element(self, by, identifier):
        try:
            return self.driver.find_element(by, identifier)
        except NoSuchElementException:
            return False

    def check_for_warning(self):
        if self.find_user_profile_element(By.XPATH,
                                          "(//*[contains(text(), 'Your Account Has Been Temporarily Locked')])") or \
                self.find_user_profile_element(By.XPATH, "(//*[contains(text(), 'Confirm it's you to log in')])"):
            logger.fatal("!!!!!!!!!!!!!!!!!warning received, do not process further!!!!!!!!!!!!!")
            self.driver.quit()
            return True
        logger.debug("no warning, safe to proceed")
        return False

    def get_time_elapsed(self):
        app_end = datetime.datetime.now()
        elapsed_time = app_end - self.app_start
        datetime.timedelta(0, 8, 562000)
        seconds_in_day = 24 * 60 * 60
        return divmod(elapsed_time.days * seconds_in_day + elapsed_time.seconds, 60)

    def follow_followers(self):
        follower_list = self.to_scout

        logger.info("Number of accounts to scout: {}".format(len(follower_list)))
        scheduler.enter(3600, 1, self.follow_followers)

        self.app_start = datetime.datetime.now()
        logger.info("new app run started: {}".format(self.app_start))

        followed = []
        failed_to_scout = []
        last_followed = " "
        temp = open("[Followed][{}]".format(self.username), "a+")
        temp.close()

        for username in follower_list:
            if not self.go_to_user(username):
                logger.error("cannot visit user profile: {}".format(username))
                failed_to_scout.append(username)
                pass

            self.check_for_warning()

            if self.find_user_profile_element(By.XPATH, "//*[contains(text(), 'Requested')]"):
                logger.info("skipping: already requested.")
                time.sleep(2)
                continue

            if self.find_user_profile_element(By.XPATH, "//*[contains(text(), 'Follow Back')]"):
                logger.info("skipping: already following you.")
                time.sleep(2)
                continue

            try:
                self.driver.find_element(By.XPATH, "//*[contains(text(), 'This account is private')]")
                with open("[Followed][{}]".format(self.username), "r+") as flist:
                    lines = flist.readlines()
                    if username not in lines:
                        self.driver.find_element(By.XPATH, "(//button[contains(text(),'Follow')])").click()
                        if self.find_user_profile_element(By.XPATH, "(//*[contains(text(), 'Try again later')])"):
                            logger.fatal("!!!!! Temporarily blocked. Exiting Program: retry in a few hours. !!!!!!")
                            self.driver.quit()
                        flist.write(username+"\n")
                        followed.append(username)
                        if len(followed) == 30:
                            diff = self.get_time_elapsed()
                            logger.info("followed 30 account - waiting for the next run. Total time used for the current run: {} mins {}secs".format(diff[0], diff[1]))
                            last_followed = username
                            break
                    else:
                        logger.info("skipping: followed before. Not interested in Ms Y English :( ")
                wait(30, 90, "requested to follow {}".format(username))
                logger.info("followed {} accounts on this run so far".format(len(followed)))
            except NoSuchElementException or ElementClickInterceptedException:
                if self.find_user_profile_element(By.CSS_SELECTOR, "[aria-label='Following']"):
                    logger.info("skipping: you are already following this account")
                else:
                    marketed = self.like_first_six_pics(username, failed_to_scout)
                    if marketed:
                        wait(3, 30, "public account: liked recent photos")
                    else:
                        logger.info("skipping: unmarketable public account")
                pass

        logger.info("requested to follow the following accounts: {}".format(followed))
        logger.info("unable to scout the following accounts due to errors: {}".format(failed_to_scout))
        if len(failed_to_scout) > 0:
            logger.debug("appending users unable to scout back in to scout list for retry later.")
            self.to_scout.extend(failed_to_scout)
        diff = self.get_time_elapsed()
        logger.info("finsihing current run. Total time used: {} mins {}secs".format(diff[0], diff[1]))
        self.to_scout = follower_list[follower_list.index(last_followed) + 1:]
        logger.info("remaining number of accounts to scout: {}".format(len(self.to_scout)))

    def like_first_six_pics(self, user, failed_to_scout):
        images = self.driver.find_elements(By.XPATH, "//div[@class='eLAPa']")
        if len(images) == 0:
            logger.info("no post on public account")
            return False
        for i in range(0, 6 if len(images) >= 6 else len(images)):
            self.driver.execute_script("arguments[0].click();", images[i])
            time.sleep(2)
            #better XPATH
            try:
                like_button = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")))
                if not self.find_user_profile_element(By.CSS_SELECTOR, "[aria-label='Unlike']"):
                    like_button.click()
                else:
                    logger.info("already liked this account's photo recently. Account not interested in Ms Y :( ")
                    return False
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                wait(1, 5, "liked {} photo".format(i + 1))
            except TimeoutException:
                failed_to_scout.append(user)
                logger.error("like_button not found")
                return False
        return True


def start_job_for_day(bot):
    scheduler.enter(1, 1, bot.follow_followers, ())
    scheduler.run()


def scrap_and_follow(bot, target):
    bot.find_accounts_to_follow(target)
    start_job_for_day(bot)


def scrap_only(bot, target):
    bot.find_accounts_to_follow(target)


def follow_only(bot, list_name):
    bot.to_scout = list_name
    start_job_for_day(bot)


def main():
    print('''
                                   __  __      ____  ____  ______
                                   \ \/ /     / __ )/ __ \/_  __/
                                    \  /_____/ __  / / / / / /   
                                    / /_____/ /_/ / /_/ / / /    
                                   /_/     /_____/\____/ /_/                              
 
    ''')

    # my_bot = Bot("ms.y.english", "sS010126:")
    # my_bot = Bot("tessstytest", "testpassword")
    my_bot = Bot("where.reasonsbegin", "sS010126+")
    # my_bot = Bot("chelhihi", "sS0101266")
    # my_bot = Bot("vonniedanse", "sS010126!")
    # my_bot = Bot("yvoniwai", "sS010126@")
    my_bot.login()

    logger.info("app started at: {}".format(my_bot.app_start))

    scrap_and_follow(my_bot, "adellbridges")
    # scrap_only(my_bot, "")
    # follow_only(my_bot, "")

    # my_bot = Bot("*", "*")
    # my_bot.login()

    # logger.info("app started at: ", my_bot.app_start)

    # scrap_and_follow(my_bot, "")
    # scrap_only(my_bot, "")
    # follow_only(my_bot, "")


if __name__ == "__main__":
    main()
