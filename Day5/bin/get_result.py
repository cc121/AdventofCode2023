import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2

input_list = '''seeds: 4043382508 113348245 3817519559 177922221 3613573568 7600537 773371046 400582097 2054637767 162982133 2246524522 153824596 1662955672 121419555 2473628355 846370595 1830497666 190544464 230006436 483872831

seed-to-soil map:
4064811 506246814 25615317
1520011681 1661018909 106057083
1007960598 8836276 47579700
1055540298 679332386 82196064
2377475243 3574057730 33434621
2323567163 2090355001 53908080
2724594670 4209189177 35645909
3247614896 4244835086 50132210
2793935335 3209861711 43002393
2560156404 2081665194 8689807
3490249256 2918928471 290933240
1399066513 1515349965 120856915
3383052312 1779636204 107196944
1634905040 1464437422 50912543
0 849557294 4064811
2155322314 2548120606 2883579
3362202103 2803876083 20850209
465575436 853622105 310104399
3781182496 3252864104 5074346
3297747106 3844665588 64454997
1779636204 2144263081 375686110
2765805312 2519990583 28130023
1325393680 605659553 73672833
1211533784 841842038 7715256
164952771 1163726504 300622665
2197289480 3607492351 121111676
54492157 395786200 110460614
3835840979 3257938450 316119280
1685817583 162560616 944821
1626068764 0 8836276
2760240579 3728604027 5564733
1219249040 56415976 106144640
2836937728 3734168760 105330821
2994742998 2551004185 252871898
4246162438 3909120585 48804858
775679835 163505437 232280763
2410909864 3957925443 149246540
3786256842 4107171983 49584137
2158205893 1886833148 39083587
29680128 1636206880 24812029
2994701606 2519949191 41392
1137736362 531862131 73797422
1686762404 761528450 80313588
2942268549 4156756120 52433057
1519923428 1464349169 88253
4151960259 2824726292 94202179
2568846211 1925916735 155748459
2318401156 3839499581 5166007

soil-to-fertilizer map:
664927065 1834026871 25712908
1735589252 664927065 98272608
2065221534 1506193032 310617880
2375839414 4115277554 6678312
3253816560 1859739779 203737617
1850812956 4108908733 6368821
2919962848 2399006039 522616
468677210 108672893 44408648
1401161152 2664100077 99602261
1500763413 2164180200 234825839
3984134761 1144008481 310832535
3804009398 3016674464 2139313
963394967 763199673 148819056
2382517726 2954526136 62148328
2596720874 2399528655 264571422
1112214023 3018813777 288947129
1874397736 2763702338 190823798
2920485464 4108473866 434867
2496018070 2063477396 100702804
3824353112 3447611199 78601908
690639973 3526213107 99743564
3806148711 928969825 18204401
2861292296 3388940647 58670552
0 356321399 298014179
3902955020 3307760906 81179741
360004317 0 108672893
790383537 4121955866 173011430
3457554177 3762018645 346455221
1833861860 912018729 16951096
3056982305 947174226 131597944
2444666054 1454841016 51352016
3188580249 1078772170 65236311
513085858 153081541 141249720
1857181777 1816810912 17215959
298014179 294331261 61990138
2920920331 3625956671 136061974

fertilizer-to-water map:
1314722794 2859771596 110470422
925980570 2089240080 7623550
2161966099 923823182 18764610
4126382841 3495278690 168584455
1914851626 1547043780 6792197
3603209919 3780725227 292923781
2451774221 919021074 4802108
3495278690 4073649008 66625331
3896133700 3663863145 116862082
2180730709 506275893 271043512
3141265861 2645889920 57381085
3136392798 1603951687 4873063
1538199090 942587792 376652536
620357722 2970242018 228404928
422454208 1814118646 197903514
1921643823 265953617 240322276
3561904021 4140274339 41305898
2758272184 2474071507 63802901
1065005613 777319405 141701669
4012995782 4181580237 113387059
2822075085 1553835977 50115710
1425193216 2361065633 113005874
933604120 1682717153 131401493
1206707282 2537874408 108015512
2872190795 2096863630 264202003
2684379781 1608824750 73892403
0 2703271005 156500591
156500591 0 265953617
2456576329 1319240328 227803452
848762650 2012022160 77217920

water-to-light map:
3911747472 2911922447 51421887
2536764367 3668005785 140896771
1212477776 97723896 242971514
3654733164 2831217728 80704719
2181820500 1577059176 179170851
1585336302 2992871942 130403154
3625205556 2963344334 29527608
637624684 802080725 399476166
3348594580 2554606752 276610976
2677661138 1756230027 290805772
1715739456 3808902556 44864370
1760603826 3853766926 127009556
263054927 0 97723896
3735437883 3980776482 176309589
2052216401 4165363197 129604099
3963169359 2047035799 96879299
1037100850 340695410 175376926
2968466910 3287878115 380127670
4292066496 2319688114 2900800
360778823 516072336 276845861
1577059176 4157086071 8277126
0 1201556891 263054927
2360991351 2143915098 175773016
1455449290 792918197 9162528
1887613382 3123275096 164603019
4060048658 2322588914 232017838

light-to-temperature map:
2208796188 2205653945 16706445
3202718202 3702799517 119048394
1789679483 2433538636 64618493
3035078142 2303892266 86108184
2549270997 3861079544 160369770
1016521015 833146166 1531563
2446163080 1924420264 78302216
3321766596 2112712346 92941599
8948937 233013740 2442944
1900324808 3247280742 118974530
215056009 134795275 63846376
3929651545 3821847911 39231633
3841595991 3463600348 88055554
3968883178 1812769444 68270872
2709640767 1707931127 104838317
1494154584 2498157129 295524899
0 1122900024 8948937
4037154050 1450117881 257813246
2814479084 2793682028 220599058
3121186326 2222360390 81531876
3568078009 4021449314 273517982
393292224 0 134795275
1251655629 2390000450 43538186
2154776907 3193261461 54019281
1854297976 1447593855 2524026
1153492607 3551655902 98163022
2019299338 3057783892 135477569
93266807 850231816 121789202
2225502633 3649818924 52980593
377738137 834677729 15554087
361270479 972021018 16467658
1018052578 988488676 113796383
72651842 1102285059 20614965
3458088143 2002722480 109989866
326898390 198641651 34372089
1295193815 1248633086 198960769
2278483226 3366255272 97345076
2375828302 1153492607 70334778
1856822002 3014281086 43502806
278902385 235456684 47996005
2524465296 1223827385 24805701
11391881 283452689 61259961
528087499 344712650 488433516
3414708195 1881040316 43379948

temperature-to-humidity map:
1719782869 425080238 132898807
1852681676 2807250453 270691921
1309417343 2396884927 410365526
963471708 0 345945635
2998807771 345945635 79134603
2123373597 557979045 875434174
0 1433413219 963471708

humidity-to-location map:
3506221501 3772218811 141412231
862456464 199991593 70194315
3126163959 2720338622 159394827
2437060415 0 153033469
1749227774 1174286868 159521600
349850270 652576354 37663076
158202776 305209374 55106503
663092217 153033469 46958124
1358475419 819305682 231265535
1589740954 2171223218 159486820
1296848852 450545479 26971073
213309279 2375483203 136540991
501031877 1333808468 54731739
2272970697 690239430 129066252
427251734 1050571217 73780143
1918845890 1626226842 116689237
3494757929 2708875050 11463572
2781047724 3224629140 67922856
3442916224 4132386344 51841705
932650779 1388540207 237686635
387513346 1742916079 39738388
3866389034 3340362984 418348873
710050341 587492729 57697450
3342406366 4184228049 100509858
0 360315877 90229602
812520956 1124351360 49935508
2162994520 477516552 109976177
2035535127 1901779730 127459393
2719729782 3758711857 13506954
2733236736 3292551996 47810988
2652027470 3156926828 67702312
767747791 2330710038 44773165
2848970580 2879733449 277193379
1170337414 645190179 7386175
1177723589 1782654467 119125263
3285558786 2652027470 56847580
1323819925 2136567724 34655494
1908749374 2512024194 10096516
3647633732 3913631042 218755302
555763616 2029239123 107328601
2402036949 270185908 35023466
90229602 2522120710 67973174'''

print(f"My result for part 1 is: {part1(input_list)}")
print(f"My result for part 2 is: {part2(input_list)}")
