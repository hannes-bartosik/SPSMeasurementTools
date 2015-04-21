from scipy.interpolate import interp1d
from numpy import array
beta_opt_lib={}

beta_opt_lib['SPS.BWS.41677.H_ROT:Q26'] = 38.03
beta_opt_lib['SPS.BWS.41677.V_ROT:Q26'] = 62.96

beta_opt_lib['SPS.BWS.41677.H_ROT:Q20'] = 49.19
beta_opt_lib['SPS.BWS.41677.V_ROT:Q20'] = 71.02

beta_opt_lib['SPS.BWS.51995.H_ROT:Q26'] = 81.49
beta_opt_lib['SPS.BWS.51995.V_ROT:Q26'] = 28.15

beta_opt_lib['SPS.BWS.51995.H_ROT:Q20'] = 86.8
beta_opt_lib['SPS.BWS.51995.V_ROT:Q20'] = 39.6


#~ LHC_accel_betagamma=array([  14.38815188,   14.39454661,   14.41373082,   14.44570449,
         #~ 14.49046763,   14.54802023,   14.66577926,   14.89116167,
         #~ 15.22416745,   15.66479661,   16.21304914,   16.86892505,
         #~ 17.63242434,   18.503547  ,   19.44673056,   20.34639699,
         #~ 21.19365567,   21.9885066 ,   22.73094977,   23.42098518,
         #~ 24.05861285,   24.64383276,   25.17664492,   25.65704932,
         #~ 26.08504597,   26.46063487,   26.78381601,   27.05458941,
         #~ 27.27295504,   27.43891293,   27.55246306,   27.61360544,
         #~ 27.62525161,   27.62525161,   27.62525161,   27.6268306 ,
         #~ 27.63156757,   27.63946253,   27.65051548,   27.6647264 ,
         #~ 27.68209531,   27.70262221,   27.72630708,   27.75314994,
         #~ 27.78315079,   27.81630962,   27.85262643,   27.89210122,
         #~ 27.934734  ,   27.98052477,   28.02947351,   28.08158024,
         #~ 28.13684496,   28.19526765,   28.25684834,   28.321587  ,
         #~ 28.38948365,   28.46053828,   28.5347509 ,   28.61212149,
         #~ 28.69265008,   28.77633664,   28.86318119,   28.95318373,
         #~ 29.04634425,   29.14266275,   29.24213923,   29.3447737 ,
         #~ 29.45056615,   29.55951659,   29.67162501,   29.78689141,
         #~ 29.9053158 ,   30.02689817,   30.15163852,   30.27953686,
         #~ 30.41059318,   30.54480748,   30.68217977,   30.82271004,
         #~ 30.9663983 ,   31.11324454,   31.26324876,   31.41641097,
         #~ 31.57273116,   31.73220933,   31.89484549,   32.06063963,
         #~ 32.22959176,   32.40170187,   32.57696996,   32.75539603,
         #~ 32.93698009,   33.12172214,   33.30962216,   33.50068017,
         #~ 33.69489617,   33.89227014,   34.09280211,   34.29649205,
         #~ 34.50333998,   34.71334589,   34.92650979,   35.14283167,
         #~ 35.36231153,   35.58494938,   35.81074521,   36.03969902,
         #~ 36.27181082,   36.5070806 ,   36.74550836,   36.98709411,
         #~ 37.23183785,   37.47973956,   37.73079926,   37.98501694,
         #~ 38.24239261,   38.50292626,   38.7666179 ,   39.03346751,
         #~ 39.30347511,   39.5766407 ,   39.85296427,   40.13244582,
         #~ 40.41508536,   40.70088288,   40.98983838,   41.28195187,
         #~ 41.57722334,   41.87565279,   42.17724023,   42.48198565,
         #~ 42.78988906,   43.10095044,   43.41516982,   43.73254717,
         #~ 44.05308251,   44.37677584,   44.70362714,   45.03363643,
         #~ 45.36680371,   45.70312897,   46.04261221,   46.38525343,
         #~ 46.73105264,   47.08000983,   47.43212501,   47.78739817,
         #~ 48.14582931,   48.50741844,   48.87216555,   49.24007064,
         #~ 49.61113372,   49.98535478,   50.36273383,   50.74327086,
         #~ 51.12696587,   51.51381887,   51.90382985,   52.29699881,
         #~ 52.69332576,   53.09281069,   53.4954536 ,   53.9012545 ,
         #~ 54.31021338,   54.72233025,   55.1376051 ,   55.55603793,
         #~ 55.97762874,   56.40237754,   56.83028433,   57.26134909,
         #~ 57.69557185,   58.13295258,   58.5734913 ,   59.017188  ,
         #~ 59.46404268,   59.91405535,   60.36722601,   60.82355464,
         #~ 61.28304126,   61.74568587,   62.21148845,   62.68044902,
         #~ 63.15256758,   63.62784412,   64.10627864,   64.58787114,
         #~ 65.07262163,   65.56053011,   66.05159656,   66.545821  ,
         #~ 67.04320343,   67.54374383,   68.04744222,   68.5542986 ,
         #~ 69.06431296,   69.5774853 ,   70.09381562,   70.61330393,
         #~ 71.13595023,   71.6617545 ,   72.19071676,   72.72283701,
         #~ 73.25811523,   73.79655144,   74.33814564,   74.88289782,
         #~ 75.43080798,   75.98187612,   76.53610225,   77.09348637,
         #~ 77.65402846,   78.21772854,   78.78458661,   79.35460265,
         #~ 79.92777668,   80.5041087 ,   81.0835987 ,   81.66624668,
         #~ 82.25205265,   82.84101659,   83.43313853,   84.02841844,
         #~ 84.62685634,   85.22845223,   85.8332061 ,   86.44111795,
         #~ 87.05218778,   87.6664156 ,   88.2838014 ,   88.90434519,
         #~ 89.52804696,   90.15490671,   90.78492445,   91.41810017,
         #~ 92.05443387,   92.69392556,   93.33657523,   93.98238288,
         #~ 94.63134852,   95.28347214,   95.93875375,   96.59719334,
         #~ 97.25879091,   97.92354647,   98.59146001,   99.26253153,
         #~ 99.93676104,  100.61414853,  101.29469401,  101.97839746,
        #~ 102.66525891,  103.35527833,  104.04845574,  104.74479113,
        #~ 105.44428451,  106.14693587,  106.85274522,  107.56171254,
        #~ 108.27383785,  108.98912115,  109.70756243,  110.42916169,
        #~ 111.15391894,  111.88183417,  112.61290738,  113.34713858,
        #~ 114.08452776,  114.82507492,  115.56878007,  116.3156432 ,
        #~ 117.06566431,  117.81884341,  118.57518049,  119.33467556,
        #~ 120.09732861,  120.86313964,  121.63210866,  122.40423566,
        #~ 123.17952064,  123.95796361,  124.73956456,  125.5243235 ,
        #~ 126.31224042,  127.10331532,  127.89754821,  128.69493908,
        #~ 129.49548793,  130.29919477,  131.10605959,  131.91608239,
        #~ 132.72926318,  133.54560195,  134.3650987 ,  135.18775344,
        #~ 136.01356617,  136.84253687,  137.67466556,  138.50995223,
        #~ 139.34839689,  140.18999953,  141.03476016,  141.88267876,
        #~ 142.73375536,  143.58798993,  144.44538249,  145.30593303,
        #~ 146.16964156,  147.03650807,  147.90653256,  148.77971504,
        #~ 149.6560555 ,  150.53555394,  151.41821037,  152.30402478,
        #~ 153.19299718,  154.08512756,  154.98041592,  155.87886227,
        #~ 156.78046659,  157.68522891,  158.59314921,  159.50422749,
        #~ 160.41846375,  161.335858  ,  162.25641023,  163.18012045,
        #~ 164.10698864,  165.03701483,  165.97019899,  166.90654114,
        #~ 167.84604128,  168.78869939,  169.73451549,  170.68348958,
        #~ 171.63562165,  172.5909117 ,  173.54935973,  174.51096575,
        #~ 175.47572976,  176.44365174,  177.41473171,  178.38896966,
        #~ 179.3663656 ,  180.34691952,  181.33063143,  182.31750132,
        #~ 183.30752919,  184.30071504,  189.27453928,  190.26930413,
        #~ 192.25883382,  197.23265806,  199.22218775,  201.21171745,
        #~ 202.20648229,  203.20124714,  204.19601199,  208.17507138,
        #~ 210.16460107,  212.15413076,  213.14889561,  214.14366046,
        #~ 215.13842531,  216.13319015,  219.11748469,  220.11224954,
        #~ 221.10701439,  222.10177924,  223.09654408,  225.08607378,
        #~ 226.08083863,  227.07560347,  228.07036832,  229.06513317,
        #~ 230.05989801,  233.04419256,  234.0389574 ,  235.03372225,
        #~ 236.0284871 ,  237.02325194,  238.01801679,  241.00231133,
        #~ 241.99707618,  242.99184103,  243.98660588,  246.97090042,
        #~ 247.96566526,  248.96043011,  249.95519496,  250.94995981,
        #~ 251.94472465,  252.9394895 ,  253.93425435,  254.92901919,
        #~ 255.92378404,  256.91854889,  259.90284343,  260.89760828,
        #~ 261.89237313,  262.88713797,  263.88190282,  264.87666767,
        #~ 265.87143251,  266.86619736,  267.86096221,  268.85572706,
        #~ 269.8504919 ,  270.84525675,  271.8400216 ,  272.83478644,
        #~ 273.82955129,  276.81384583,  277.80861068,  278.80337553,
        #~ 279.79814037,  280.79290522,  281.78767007,  282.78243492,
        #~ 283.77719976,  284.77196461,  285.76672946,  286.76149431,
        #~ 287.75625915,  288.751024  ,  289.74578885,  290.74055369,
        #~ 294.71961308,  296.70914278,  298.69867247,  299.69343732,
        #~ 301.68296701,  303.67249671,  304.66726156,  305.6620264 ,
        #~ 308.64632094,  310.63585064,  315.60967487,  316.60443972,
        #~ 317.59920457,  318.59396942,  319.58873426,  321.57826396,
        #~ 325.55732335,  326.55208819,  330.53114758,  331.52591243,
        #~ 332.52067728,  333.51544212,  334.51020697,  335.50497182,
        #~ 336.49973667,  337.49450151,  338.48926636,  339.48403121,
        #~ 343.4630906 ,  344.45785544,  346.44738514,  347.44214999,
        #~ 348.43691483,  349.43167968,  350.42644453,  351.42120937,
        #~ 352.41597422,  353.41073907,  354.40550392,  357.38979846,
        #~ 359.37932815,  363.35838754,  364.35315239,  365.34791724,
        #~ 366.34268208,  367.33744693,  369.32697662,  370.32174147,
        #~ 371.31650632,  372.31127117,  373.30603601,  375.29556571,
        #~ 379.2746251 ,  380.26938994,  381.26415479,  382.25891964,
        #~ 383.25368448,  384.24844933,  385.24321418,  386.23797903,
        #~ 387.23274387,  388.22750872,  392.20656811,  393.20133296,
        #~ 395.19086265,  396.1856275 ,  397.18039235,  398.17515719,
        #~ 399.16992204,  400.16468689,  401.15945173,  402.15421658,
        #~ 403.14898143,  406.13327597,  408.12280567,  416.08092444,
        #~ 417.07568929,  418.07045414,  419.06521898,  420.05998383,
        #~ 421.05474868,  422.04951353,  424.03904322,  430.0076323 ,
        #~ 431.00239715,  431.997162  ,  432.99192685,  433.98669169,
        #~ 434.98145654,  435.97622139,  436.97098623,  437.96575108,
        #~ 439.95528078,  447.91339955,  448.9081644 ,  449.90292925,
        #~ 450.8976941 ,  451.89245894,  452.88722379,  453.88198864,
        #~ 454.87675348,  455.87151833,  456.86628318,  457.86104803,
        #~ 458.85581287,  462.83487226,  463.82963711,  464.82440196,
        #~ 465.8191668 ,  466.81393165,  467.8086965 ,  468.80346135,
        #~ 469.79822619,  471.78775589,  472.78252073,  473.74336913,
        #~ 474.63638462,  475.46156721,  476.21891689,  476.90843367,
        #~ 477.53011755,  478.08396852,  478.56998658,  478.98817175,
        #~ 479.33852401,  479.62104336,  479.83845533,  480.02619161,
        #~ 480.19515426,  480.34534328,  480.47675867,  480.58940044,
        #~ 480.68326858,  480.75836309,  480.81468397,  480.85223123,
        #~ 480.87335156,  480.87335156])
        #~ 
#~ t_prog=array([  0.00000000e+00,   6.00000000e+00,   1.20000000e+01,
         #~ 1.80000000e+01,   2.40000000e+01,   3.00000000e+01,
         #~ 3.60000000e+01,   4.20000000e+01,   4.80000000e+01,
         #~ 5.40000000e+01,   6.00000000e+01,   6.60000000e+01,
         #~ 7.20000000e+01,   7.80000000e+01,   8.40000000e+01,
         #~ 9.00000000e+01,   9.60000000e+01,   1.02000000e+02,
         #~ 1.08000000e+02,   1.14000000e+02,   1.20000000e+02,
         #~ 1.26000000e+02,   1.32000000e+02,   1.38000000e+02,
         #~ 1.44000000e+02,   1.50000000e+02,   1.56000000e+02,
         #~ 1.62000000e+02,   1.68000000e+02,   1.74000000e+02,
         #~ 1.80000000e+02,   1.86000000e+02,   1.92000000e+02,
         #~ 6.25000000e+02,   1.14850000e+04,   1.14970000e+04,
         #~ 1.15090000e+04,   1.15210000e+04,   1.15330000e+04,
         #~ 1.15450000e+04,   1.15570000e+04,   1.15690000e+04,
         #~ 1.15810000e+04,   1.15930000e+04,   1.16050000e+04,
         #~ 1.16170000e+04,   1.16290000e+04,   1.16410000e+04,
         #~ 1.16530000e+04,   1.16650000e+04,   1.16770000e+04,
         #~ 1.16890000e+04,   1.17010000e+04,   1.17130000e+04,
         #~ 1.17250000e+04,   1.17370000e+04,   1.17490000e+04,
         #~ 1.17610000e+04,   1.17730000e+04,   1.17850000e+04,
         #~ 1.17970000e+04,   1.18090000e+04,   1.18210000e+04,
         #~ 1.18330000e+04,   1.18450000e+04,   1.18570000e+04,
         #~ 1.18690000e+04,   1.18810000e+04,   1.18930000e+04,
         #~ 1.19050000e+04,   1.19170000e+04,   1.19290000e+04,
         #~ 1.19410000e+04,   1.19530000e+04,   1.19650000e+04,
         #~ 1.19770000e+04,   1.19890000e+04,   1.20010000e+04,
         #~ 1.20130000e+04,   1.20250000e+04,   1.20370000e+04,
         #~ 1.20490000e+04,   1.20610000e+04,   1.20730000e+04,
         #~ 1.20850000e+04,   1.20970000e+04,   1.21090000e+04,
         #~ 1.21210000e+04,   1.21330000e+04,   1.21450000e+04,
         #~ 1.21570000e+04,   1.21690000e+04,   1.21810000e+04,
         #~ 1.21930000e+04,   1.22050000e+04,   1.22170000e+04,
         #~ 1.22290000e+04,   1.22410000e+04,   1.22530000e+04,
         #~ 1.22650000e+04,   1.22770000e+04,   1.22890000e+04,
         #~ 1.23010000e+04,   1.23130000e+04,   1.23250000e+04,
         #~ 1.23370000e+04,   1.23490000e+04,   1.23610000e+04,
         #~ 1.23730000e+04,   1.23850000e+04,   1.23970000e+04,
         #~ 1.24090000e+04,   1.24210000e+04,   1.24330000e+04,
         #~ 1.24450000e+04,   1.24570000e+04,   1.24690000e+04,
         #~ 1.24810000e+04,   1.24930000e+04,   1.25050000e+04,
         #~ 1.25170000e+04,   1.25290000e+04,   1.25410000e+04,
         #~ 1.25530000e+04,   1.25650000e+04,   1.25770000e+04,
         #~ 1.25890000e+04,   1.26010000e+04,   1.26130000e+04,
         #~ 1.26250000e+04,   1.26370000e+04,   1.26490000e+04,
         #~ 1.26610000e+04,   1.26730000e+04,   1.26850000e+04,
         #~ 1.26970000e+04,   1.27090000e+04,   1.27210000e+04,
         #~ 1.27330000e+04,   1.27450000e+04,   1.27570000e+04,
         #~ 1.27690000e+04,   1.27810000e+04,   1.27930000e+04,
         #~ 1.28050000e+04,   1.28170000e+04,   1.28290000e+04,
         #~ 1.28410000e+04,   1.28530000e+04,   1.28650000e+04,
         #~ 1.28770000e+04,   1.28890000e+04,   1.29010000e+04,
         #~ 1.29130000e+04,   1.29250000e+04,   1.29370000e+04,
         #~ 1.29490000e+04,   1.29610000e+04,   1.29730000e+04,
         #~ 1.29850000e+04,   1.29970000e+04,   1.30090000e+04,
         #~ 1.30210000e+04,   1.30330000e+04,   1.30450000e+04,
         #~ 1.30570000e+04,   1.30690000e+04,   1.30810000e+04,
         #~ 1.30930000e+04,   1.31050000e+04,   1.31170000e+04,
         #~ 1.31290000e+04,   1.31410000e+04,   1.31530000e+04,
         #~ 1.31650000e+04,   1.31770000e+04,   1.31890000e+04,
         #~ 1.32010000e+04,   1.32130000e+04,   1.32250000e+04,
         #~ 1.32370000e+04,   1.32490000e+04,   1.32610000e+04,
         #~ 1.32730000e+04,   1.32850000e+04,   1.32970000e+04,
         #~ 1.33090000e+04,   1.33210000e+04,   1.33330000e+04,
         #~ 1.33450000e+04,   1.33570000e+04,   1.33690000e+04,
         #~ 1.33810000e+04,   1.33930000e+04,   1.34050000e+04,
         #~ 1.34170000e+04,   1.34290000e+04,   1.34410000e+04,
         #~ 1.34530000e+04,   1.34650000e+04,   1.34770000e+04,
         #~ 1.34890000e+04,   1.35010000e+04,   1.35130000e+04,
         #~ 1.35250000e+04,   1.35370000e+04,   1.35490000e+04,
         #~ 1.35610000e+04,   1.35730000e+04,   1.35850000e+04,
         #~ 1.35970000e+04,   1.36090000e+04,   1.36210000e+04,
         #~ 1.36330000e+04,   1.36450000e+04,   1.36570000e+04,
         #~ 1.36690000e+04,   1.36810000e+04,   1.36930000e+04,
         #~ 1.37050000e+04,   1.37170000e+04,   1.37290000e+04,
         #~ 1.37410000e+04,   1.37530000e+04,   1.37650000e+04,
         #~ 1.37770000e+04,   1.37890000e+04,   1.38010000e+04,
         #~ 1.38130000e+04,   1.38250000e+04,   1.38370000e+04,
         #~ 1.38490000e+04,   1.38610000e+04,   1.38730000e+04,
         #~ 1.38850000e+04,   1.38970000e+04,   1.39090000e+04,
         #~ 1.39210000e+04,   1.39330000e+04,   1.39450000e+04,
         #~ 1.39570000e+04,   1.39690000e+04,   1.39810000e+04,
         #~ 1.39930000e+04,   1.40050000e+04,   1.40170000e+04,
         #~ 1.40290000e+04,   1.40410000e+04,   1.40530000e+04,
         #~ 1.40650000e+04,   1.40770000e+04,   1.40890000e+04,
         #~ 1.41010000e+04,   1.41130000e+04,   1.41250000e+04,
         #~ 1.41370000e+04,   1.41490000e+04,   1.41610000e+04,
         #~ 1.41730000e+04,   1.41850000e+04,   1.41970000e+04,
         #~ 1.42090000e+04,   1.42210000e+04,   1.42330000e+04,
         #~ 1.42450000e+04,   1.42570000e+04,   1.42690000e+04,
         #~ 1.42810000e+04,   1.42930000e+04,   1.43050000e+04,
         #~ 1.43170000e+04,   1.43290000e+04,   1.43410000e+04,
         #~ 1.43530000e+04,   1.43650000e+04,   1.43770000e+04,
         #~ 1.43890000e+04,   1.44010000e+04,   1.44130000e+04,
         #~ 1.44250000e+04,   1.44370000e+04,   1.44490000e+04,
         #~ 1.44610000e+04,   1.44730000e+04,   1.44850000e+04,
         #~ 1.44970000e+04,   1.45090000e+04,   1.45210000e+04,
         #~ 1.45330000e+04,   1.45450000e+04,   1.45570000e+04,
         #~ 1.45690000e+04,   1.45810000e+04,   1.45930000e+04,
         #~ 1.46050000e+04,   1.46170000e+04,   1.46290000e+04,
         #~ 1.46410000e+04,   1.46530000e+04,   1.46650000e+04,
         #~ 1.46770000e+04,   1.46890000e+04,   1.47010000e+04,
         #~ 1.47130000e+04,   1.47250000e+04,   1.47370000e+04,
         #~ 1.47490000e+04,   1.47610000e+04,   1.47730000e+04,
         #~ 1.47850000e+04,   1.47970000e+04,   1.48090000e+04,
         #~ 1.48210000e+04,   1.48330000e+04,   1.48450000e+04,
         #~ 1.48570000e+04,   1.48690000e+04,   1.48810000e+04,
         #~ 1.48930000e+04,   1.49050000e+04,   1.49170000e+04,
         #~ 1.49290000e+04,   1.49410000e+04,   1.49530000e+04,
         #~ 1.49650000e+04,   1.49770000e+04,   1.49890000e+04,
         #~ 1.50010000e+04,   1.50130000e+04,   1.50250000e+04,
         #~ 1.50370000e+04,   1.50490000e+04,   1.50610000e+04,
         #~ 1.50730000e+04,   1.50850000e+04,   1.50970000e+04,
         #~ 1.51090000e+04,   1.51210000e+04,   1.51330000e+04,
         #~ 1.51450000e+04,   1.51570000e+04,   1.51690000e+04,
         #~ 1.51810000e+04,   1.51930000e+04,   1.52050000e+04,
         #~ 1.52170000e+04,   1.52290000e+04,   1.52410000e+04,
         #~ 1.52530000e+04,   1.52650000e+04,   1.53250000e+04,
         #~ 1.53370000e+04,   1.53610000e+04,   1.54210000e+04,
         #~ 1.54450000e+04,   1.54690000e+04,   1.54810000e+04,
         #~ 1.54930000e+04,   1.55050000e+04,   1.55530000e+04,
         #~ 1.55770000e+04,   1.56010000e+04,   1.56130000e+04,
         #~ 1.56250000e+04,   1.56370000e+04,   1.56490000e+04,
         #~ 1.56850000e+04,   1.56970000e+04,   1.57090000e+04,
         #~ 1.57210000e+04,   1.57330000e+04,   1.57570000e+04,
         #~ 1.57690000e+04,   1.57810000e+04,   1.57930000e+04,
         #~ 1.58050000e+04,   1.58170000e+04,   1.58530000e+04,
         #~ 1.58650000e+04,   1.58770000e+04,   1.58890000e+04,
         #~ 1.59010000e+04,   1.59130000e+04,   1.59490000e+04,
         #~ 1.59610000e+04,   1.59730000e+04,   1.59850000e+04,
         #~ 1.60210000e+04,   1.60330000e+04,   1.60450000e+04,
         #~ 1.60570000e+04,   1.60690000e+04,   1.60810000e+04,
         #~ 1.60930000e+04,   1.61050000e+04,   1.61170000e+04,
         #~ 1.61290000e+04,   1.61410000e+04,   1.61770000e+04,
         #~ 1.61890000e+04,   1.62010000e+04,   1.62130000e+04,
         #~ 1.62250000e+04,   1.62370000e+04,   1.62490000e+04,
         #~ 1.62610000e+04,   1.62730000e+04,   1.62850000e+04,
         #~ 1.62970000e+04,   1.63090000e+04,   1.63210000e+04,
         #~ 1.63330000e+04,   1.63450000e+04,   1.63810000e+04,
         #~ 1.63930000e+04,   1.64050000e+04,   1.64170000e+04,
         #~ 1.64290000e+04,   1.64410000e+04,   1.64530000e+04,
         #~ 1.64650000e+04,   1.64770000e+04,   1.64890000e+04,
         #~ 1.65010000e+04,   1.65130000e+04,   1.65250000e+04,
         #~ 1.65370000e+04,   1.65490000e+04,   1.65970000e+04,
         #~ 1.66210000e+04,   1.66450000e+04,   1.66570000e+04,
         #~ 1.66810000e+04,   1.67050000e+04,   1.67170000e+04,
         #~ 1.67290000e+04,   1.67650000e+04,   1.67890000e+04,
         #~ 1.68490000e+04,   1.68610000e+04,   1.68730000e+04,
         #~ 1.68850000e+04,   1.68970000e+04,   1.69210000e+04,
         #~ 1.69690000e+04,   1.69810000e+04,   1.70290000e+04,
         #~ 1.70410000e+04,   1.70530000e+04,   1.70650000e+04,
         #~ 1.70770000e+04,   1.70890000e+04,   1.71010000e+04,
         #~ 1.71130000e+04,   1.71250000e+04,   1.71370000e+04,
         #~ 1.71850000e+04,   1.71970000e+04,   1.72210000e+04,
         #~ 1.72330000e+04,   1.72450000e+04,   1.72570000e+04,
         #~ 1.72690000e+04,   1.72810000e+04,   1.72930000e+04,
         #~ 1.73050000e+04,   1.73170000e+04,   1.73530000e+04,
         #~ 1.73770000e+04,   1.74250000e+04,   1.74370000e+04,
         #~ 1.74490000e+04,   1.74610000e+04,   1.74730000e+04,
         #~ 1.74970000e+04,   1.75090000e+04,   1.75210000e+04,
         #~ 1.75330000e+04,   1.75450000e+04,   1.75690000e+04,
         #~ 1.76170000e+04,   1.76290000e+04,   1.76410000e+04,
         #~ 1.76530000e+04,   1.76650000e+04,   1.76770000e+04,
         #~ 1.76890000e+04,   1.77010000e+04,   1.77130000e+04,
         #~ 1.77250000e+04,   1.77730000e+04,   1.77850000e+04,
         #~ 1.78090000e+04,   1.78210000e+04,   1.78330000e+04,
         #~ 1.78450000e+04,   1.78570000e+04,   1.78690000e+04,
         #~ 1.78810000e+04,   1.78930000e+04,   1.79050000e+04,
         #~ 1.79410000e+04,   1.79650000e+04,   1.80610000e+04,
         #~ 1.80730000e+04,   1.80850000e+04,   1.80970000e+04,
         #~ 1.81090000e+04,   1.81210000e+04,   1.81330000e+04,
         #~ 1.81570000e+04,   1.82290000e+04,   1.82410000e+04,
         #~ 1.82530000e+04,   1.82650000e+04,   1.82770000e+04,
         #~ 1.82890000e+04,   1.83010000e+04,   1.83130000e+04,
         #~ 1.83250000e+04,   1.83490000e+04,   1.84450000e+04,
         #~ 1.84570000e+04,   1.84690000e+04,   1.84810000e+04,
         #~ 1.84930000e+04,   1.85050000e+04,   1.85170000e+04,
         #~ 1.85290000e+04,   1.85410000e+04,   1.85530000e+04,
         #~ 1.85650000e+04,   1.85770000e+04,   1.86250000e+04,
         #~ 1.86370000e+04,   1.86490000e+04,   1.86610000e+04,
         #~ 1.86730000e+04,   1.86850000e+04,   1.86970000e+04,
         #~ 1.87090000e+04,   1.87330000e+04,   1.87450000e+04,
         #~ 1.87570000e+04,   1.87690000e+04,   1.87810000e+04,
         #~ 1.87930000e+04,   1.88050000e+04,   1.88170000e+04,
         #~ 1.88290000e+04,   1.88410000e+04,   1.88530000e+04,
         #~ 1.88650000e+04,   1.88770000e+04,   1.88890000e+04,
         #~ 1.89010000e+04,   1.89130000e+04,   1.89250000e+04,
         #~ 1.89370000e+04,   1.89490000e+04,   1.89610000e+04,
         #~ 1.89730000e+04,   1.89850000e+04,   1.89970000e+04,
         #~ 1.90150000e+04,   1.98500000e+04])
         #~ 
#~ f_beta_gamma_interp_LHCcycle= interp1d(t_prog, LHC_accel_betagamma, kind='linear')

def retrieve_betagamma(cycle_type, t_in_cycle_ms):
	if cycle_type=='26GeV_FB':
		return 27.607
	elif cycle_type=='270GeV_coast':
		return 287.6
	#~ elif cycle_type=='LHC_type_18BP': %it is the pre LS1 cycle, now it is longer by one BP!!!!!!!!
		#~ if t_in_cycle_ms<t_prog[-1]:
			#~ return float(f_beta_gamma_interp_LHCcycle(t_in_cycle_ms))
		#~ else:
			#~ return LHC_accel_betagamma[-1]
	else:
		raise ValueError("""Cyclename not valid! (Supported: '26GeV_FB', '270GeV_coast')""")


        

