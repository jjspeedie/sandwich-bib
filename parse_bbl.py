import re
from collections import defaultdict

def parse_bbl(bbl_content):

    # Regex patterns to match the necessary fields
    bibitem_pattern = r'\\bibitem\[\{(.*?)\}\]\{(.*?)\}.*?\\dodoi\{(.*?)\}'  # Capture citation, bibkey, and DOI
    # This pattern will now capture the whole bibitem and DOI, even across multiple lines

    # Create a defaultdict to hold the duplicates
    bib_dict = defaultdict(list)

    # Extract all \bibitem entries including DOIs
    bib_items = re.findall(bibitem_pattern, bbl_content, flags=re.DOTALL)

    # Debug print to show all bibitems found
    print("Extracted BibItems:")
    for item in bib_items:
        print(item)

    # To track seen DOIs and store references
    seen_dois = {}

    # Iterate through the bibitems
    for citation, bibkey, doi in bib_items:
        print(f"Processing: citation: {citation}, bibkey: {bibkey}, DOI: {doi}")
        
        # Check if the DOI has already been seen
        if doi in seen_dois:
            print(f"Duplicate DOI found: {doi}, adding bibkey {bibkey} to list")
            bib_dict[seen_dois[doi]].append(bibkey)
        else:
            # Store the DOI and corresponding bibkey
            print(f"Storing DOI: {doi} with bibkey: {bibkey}")
            seen_dois[doi] = bibkey

    return dict(bib_dict)

# Example usage
# if __name__ == "__main__":
    # Paste the content of the .bbl file as a string (ensure to escape newlines properly)
bbl_content = r"""

\bibitem[{{Andr{\'e}} {et~al.}(2010){Andr{\'e}}, {Men'shchikov}, {Bontemps}, {K{\"o}nyves}, {Motte}, {Schneider}, {Didelon}, {Minier}, {Saraceno}, {Ward-Thompson}, {di Francesco}, {White}, {Molinari}, {Testi}, {Abergel}, {Griffin}, {Henning}, {Royer}, {Mer{\'\i}n}, {Vavrek}, {Attard}, {Arzoumanian}, {Wilson}, {Ade}, {Aussel}, {Baluteau}, {Benedettini}, {Bernard}, {Blommaert}, {Cambr{\'e}sy}, {Cox}, {di Giorgio}, {Hargrave}, {Hennemann}, {Huang}, {Kirk}, {Krause}, {Launhardt}, {Leeks}, {Le Pennec}, {Li}, {Martin}, {Maury}, {Olofsson}, {Omont}, {Peretto}, {Pezzuto}, {Prusti}, {Roussel}, {Russeil}, {Sauvage}, {Sibthorpe}, {Sicilia-Aguilar}, {Spinoglio}, {Waelkens}, {Woodcraft}, \& {Zavagno}}]{andre2010-KPGT_pandre_1}
{Andr{\'e}}, P., {Men'shchikov}, A., {Bontemps}, S., {et~al.} 2010, \aap, 518, L102, \dodoi{10.1051/0004-6361/201014666}

\bibitem[{{Andrews} {et~al.}(2024){Andrews}, {Teague}, {Wirth}, {Huang}, \& {Zhu}}]{andrews2024-behemoth}
{Andrews}, S.~M., {Teague}, R., {Wirth}, C.~P., {Huang}, J., \& {Zhu}, Z. 2024, \apj, 970, 153, \dodoi{10.3847/1538-4357/ad5285}

\bibitem[{{Andrews} {et~al.}(2018{\natexlab{a}}){Andrews}, {Huang}, {P{\'e}rez}, {Isella}, {Dullemond}, {Kurtovic}, {Guzm{\'a}n}, {Carpenter}, {Wilner}, {Zhang}, {Zhu}, {Birnstiel}, {Bai}, {Benisty}, {Hughes}, {{\"O}berg}, \& {Ricci}}]{2018-andrews-dsharp1}
{Andrews}, S.~M., {Huang}, J., {P{\'e}rez}, L.~M., {et~al.} 2018{\natexlab{a}}, \apjl, 869, L41, \dodoi{10.3847/2041-8213/aaf741}

\bibitem[{{Andrews} {et~al.}(2018{\natexlab{b}}){Andrews}, {Huang}, {P{\'e}rez}, {Isella}, {Dullemond}, {Kurtovic}, {Guzm{\'a}n}, {Carpenter}, {Wilner}, {Zhang}, {Zhu}, {Birnstiel}, {Bai}, {Benisty}, {Hughes}, {{\"O}berg}, \& {Ricci}}]{andrews18-dsharp1}
---. 2018{\natexlab{b}}, \apjl, 869, L41, \dodoi{10.3847/2041-8213/aaf741}

\bibitem[{{Andrews} {et~al.}(2021){Andrews}, {Elder}, {Zhang}, {Huang}, {Benisty}, {Kurtovic}, {Wilner}, {Zhu}, {Carpenter}, {P{\'e}rez}, {Teague}, {Isella}, \& {Ricci}}]{andrews21-frank-dsharp}
{Andrews}, S.~M., {Elder}, W., {Zhang}, S., {et~al.} 2021, \apj, 916, 51, \dodoi{10.3847/1538-4357/ac00b9}

\bibitem[{{Aota} {et~al.}(2015){Aota}, {Inoue}, \& {Aikawa}}]{aota2015}
{Aota}, T., {Inoue}, T., \& {Aikawa}, Y. 2015, \apj, 799, 141, \dodoi{10.1088/0004-637X/799/2/141}

\bibitem[{{Arzamasskiy} \& {Rafikov}(2018)}]{2018-arzamasskiy}
{Arzamasskiy}, L., \& {Rafikov}, R.~R. 2018, \apj, 854, 84, \dodoi{10.3847/1538-4357/aaa8e8}

\bibitem[{{Astropy Collaboration} {et~al.}(2013{\natexlab{a}}){Astropy Collaboration}, {Robitaille}, {Tollerud}, {Greenfield}, {Droettboom}, {Bray}, {Aldcroft}, {Davis}, {Ginsburg}, {Price-Whelan}, {Kerzendorf}, {Conley}, {Crighton}, {Barbary}, {Muna}, {Ferguson}, {Grollier}, {Parikh}, {Nair}, {Unther}, {Deil}, {Woillez}, {Conseil}, {Kramer}, {Turner}, {Singer}, {Fox}, {Weaver}, {Zabalza}, {Edwards}, {Azalee Bostroem}, {Burke}, {Casey}, {Crawford}, {Dencheva}, {Ely}, {Jenness}, {Labrie}, {Lim}, {Pierfederici}, {Pontzen}, {Ptak}, {Refsdal}, {Servillat}, \& {Streicher}}]{astropy:2013}
{Astropy Collaboration}, {Robitaille}, T.~P., {Tollerud}, E.~J., {et~al.} 2013{\natexlab{a}}, \aap, 558, A33, \dodoi{10.1051/0004-6361/201322068}

\bibitem[{{Astropy Collaboration} {et~al.}(2013{\natexlab{b}}){Astropy Collaboration}, {Robitaille}, {Tollerud}, {Greenfield}, {Droettboom}, {Bray}, {Aldcroft}, {Davis}, {Ginsburg}, {Price-Whelan}, {Kerzendorf}, {Conley}, {Crighton}, {Barbary}, {Muna}, {Ferguson}, {Grollier}, {Parikh}, {Nair}, {Unther}, {Deil}, {Woillez}, {Conseil}, {Kramer}, {Turner}, {Singer}, {Fox}, {Weaver}, {Zabalza}, {Edwards}, {Azalee Bostroem}, {Burke}, {Casey}, {Crawford}, {Dencheva}, {Ely}, {Jenness}, {Labrie}, {Lim}, {Pierfederici}, {Pontzen}, {Ptak}, {Refsdal}, {Servillat}, \& {Streicher}}]{software-astropy1}
---. 2013{\natexlab{b}}, \aap, 558, A33, \dodoi{10.1051/0004-6361/201322068}

\bibitem[{{Astropy Collaboration} {et~al.}(2018{\natexlab{a}}){Astropy Collaboration}, {Price-Whelan}, {Sip{\H{o}}cz}, {G{\"u}nther}, {Lim}, {Crawford}, {Conseil}, {Shupe}, {Craig}, {Dencheva}, {Ginsburg}, {Vand erPlas}, {Bradley}, {P{\'e}rez-Su{\'a}rez}, {de Val-Borro}, {Aldcroft}, {Cruz}, {Robitaille}, {Tollerud}, {Ardelean}, {Babej}, {Bach}, {Bachetti}, {Bakanov}, {Bamford}, {Barentsen}, {Barmby}, {Baumbach}, {Berry}, {Biscani}, {Boquien}, {Bostroem}, {Bouma}, {Brammer}, {Bray}, {Breytenbach}, {Buddelmeijer}, {Burke}, {Calderone}, {Cano Rodr{\'\i}guez}, {Cara}, {Cardoso}, {Cheedella}, {Copin}, {Corrales}, {Crichton}, {D'Avella}, {Deil}, {Depagne}, {Dietrich}, {Donath}, {Droettboom}, {Earl}, {Erben}, {Fabbro}, {Ferreira}, {Finethy}, {Fox}, {Garrison}, {Gibbons}, {Goldstein}, {Gommers}, {Greco}, {Greenfield}, {Groener}, {Grollier}, {Hagen}, {Hirst}, {Homeier}, {Horton}, {Hosseinzadeh}, {Hu}, {Hunkeler}, {Ivezi{\'c}}, {Jain}, {Jenness}, {Kanarek}, {Kendrew}, {Kern}, {Kerzendorf}, {Khvalko}, {King}, {Kirkby},
  {Kulkarni}, {Kumar}, {Lee}, {Lenz}, {Littlefair}, {Ma}, {Macleod}, {Mastropietro}, {McCully}, {Montagnac}, {Morris}, {Mueller}, {Mumford}, {Muna}, {Murphy}, {Nelson}, {Nguyen}, {Ninan}, {N{\"o}the}, {Ogaz}, {Oh}, {Parejko}, {Parley}, {Pascual}, {Patil}, {Patil}, {Plunkett}, {Prochaska}, {Rastogi}, {Reddy Janga}, {Sabater}, {Sakurikar}, {Seifert}, {Sherbert}, {Sherwood-Taylor}, {Shih}, {Sick}, {Silbiger}, {Singanamalla}, {Singer}, {Sladen}, {Sooley}, {Sornarajah}, {Streicher}, {Teuben}, {Thomas}, {Tremblay}, {Turner}, {Terr{\'o}n}, {van Kerkwijk}, {de la Vega}, {Watkins}, {Weaver}, {Whitmore}, {Woillez}, {Zabalza}, \& {Astropy Contributors}}]{astropy:2018}
{Astropy Collaboration}, {Price-Whelan}, A.~M., {Sip{\H{o}}cz}, B.~M., {et~al.} 2018{\natexlab{a}}, \aj, 156, 123, \dodoi{10.3847/1538-3881/aabc4f}

\bibitem[{{Astropy Collaboration} {et~al.}(2018{\natexlab{b}}){Astropy Collaboration}, {Price-Whelan}, {Sip{\H{o}}cz}, {G{\"u}nther}, {Lim}, {Crawford}, {Conseil}, {Shupe}, {Craig}, {Dencheva}, {Ginsburg}, {VanderPlas}, {Bradley}, {P{\'e}rez-Su{\'a}rez}, {de Val-Borro}, {Aldcroft}, {Cruz}, {Robitaille}, {Tollerud}, {Ardelean}, {Babej}, {Bach}, {Bachetti}, {Bakanov}, {Bamford}, {Barentsen}, {Barmby}, {Baumbach}, {Berry}, {Biscani}, {Boquien}, {Bostroem}, {Bouma}, {Brammer}, {Bray}, {Breytenbach}, {Buddelmeijer}, {Burke}, {Calderone}, {Cano Rodr{\'\i}guez}, {Cara}, {Cardoso}, {Cheedella}, {Copin}, {Corrales}, {Crichton}, {D'Avella}, {Deil}, {Depagne}, {Dietrich}, {Donath}, {Droettboom}, {Earl}, {Erben}, {Fabbro}, {Ferreira}, {Finethy}, {Fox}, {Garrison}, {Gibbons}, {Goldstein}, {Gommers}, {Greco}, {Greenfield}, {Groener}, {Grollier}, {Hagen}, {Hirst}, {Homeier}, {Horton}, {Hosseinzadeh}, {Hu}, {Hunkeler}, {Ivezi{\'c}}, {Jain}, {Jenness}, {Kanarek}, {Kendrew}, {Kern}, {Kerzendorf}, {Khvalko}, {King}, {Kirkby},
  {Kulkarni}, {Kumar}, {Lee}, {Lenz}, {Littlefair}, {Ma}, {Macleod}, {Mastropietro}, {McCully}, {Montagnac}, {Morris}, {Mueller}, {Mumford}, {Muna}, {Murphy}, {Nelson}, {Nguyen}, {Ninan}, {N{\"o}the}, {Ogaz}, {Oh}, {Parejko}, {Parley}, {Pascual}, {Patil}, {Patil}, {Plunkett}, {Prochaska}, {Rastogi}, {Reddy Janga}, {Sabater}, {Sakurikar}, {Seifert}, {Sherbert}, {Sherwood-Taylor}, {Shih}, {Sick}, {Silbiger}, {Singanamalla}, {Singer}, {Sladen}, {Sooley}, {Sornarajah}, {Streicher}, {Teuben}, {Thomas}, {Tremblay}, {Turner}, {Terr{\'o}n}, {van Kerkwijk}, {de la Vega}, {Watkins}, {Weaver}, {Whitmore}, {Woillez}, {Zabalza}, \& {Astropy Contributors}}]{software-astropy2}
---. 2018{\natexlab{b}}, \aj, 156, 123, \dodoi{10.3847/1538-3881/aabc4f}

\bibitem[{{Bae} {et~al.}(2015){Bae}, {Hartmann}, \& {Zhu}}]{bae2015-infall-rwi}
{Bae}, J., {Hartmann}, L., \& {Zhu}, Z. 2015, \apj, 805, 15, \dodoi{10.1088/0004-637X/805/1/15}

\bibitem[{{Bae} \& {Zhu}(2018{\natexlab{a}})}]{2018a-bae-zhu}
{Bae}, J., \& {Zhu}, Z. 2018{\natexlab{a}}, \apj, 859, 118, \dodoi{10.3847/1538-4357/aabf8c}

\bibitem[{{Bae} \& {Zhu}(2018{\natexlab{b}})}]{2018b-bae-zhu}
---. 2018{\natexlab{b}}, \apj, 859, 119, \dodoi{10.3847/1538-4357/aabf93}

\bibitem[{{Bae} \& {Zhu}(2018{\natexlab{c}})}]{bae+zhu18-spirals1}
---. 2018{\natexlab{c}}, \apj, 859, 118, \dodoi{10.3847/1538-4357/aabf8c}

\bibitem[{{Bae} \& {Zhu}(2018{\natexlab{d}})}]{bae+zhu18-spirals2}
---. 2018{\natexlab{d}}, \apj, 859, 119, \dodoi{10.3847/1538-4357/aabf93}

\bibitem[{{Bae} {et~al.}(2017){Bae}, {Zhu}, \& {Hartmann}}]{2017-bae}
{Bae}, J., {Zhu}, Z., \& {Hartmann}, L. 2017, \apj, 850, 201, \dodoi{10.3847/1538-4357/aa9705}

\bibitem[{{Bae} {et~al.}(2022){Bae}, {Teague}, {Andrews}, {Benisty}, {Facchini}, {Galloway-Sprietsma}, {Loomis}, {Aikawa}, {Alarcon}, {Bergin}, {Bergner}, {Booth}, {Cataldi}, {Cleeves}, {Czekala}, {Guzman}, {Huang}, {Ilee}, {Kurtovic}, {Law}, {Le Gal}, {Liu}, {Long}, {Menard}, {Oberg}, {Perez}, {Qi}, {Schwarz}, {Sierra}, {Walsh}, {Wilner}, \& {Zhang}}]{bae22-AS209-CPD}
{Bae}, J., {Teague}, R., {Andrews}, S.~M., {et~al.} 2022, arXiv e-prints, arXiv:2207.05923.
\newblock \doarXiv{2207.05923}

\bibitem[{{Bate} {et~al.}(1995){Bate}, {Bonnell}, \& {Price}}]{bate1995}
{Bate}, M.~R., {Bonnell}, I.~A., \& {Price}, N.~M. 1995, \mnras, 277, 362, \dodoi{10.1093/mnras/277.2.362}

\bibitem[{{Beck} \& {Bary}(2019{\natexlab{a}})}]{beck2019-H2}
{Beck}, T.~L., \& {Bary}, J.~S. 2019{\natexlab{a}}, \apj, 884, 159, \dodoi{10.3847/1538-4357/ab4259}

\bibitem[{{Beck} \& {Bary}(2019{\natexlab{b}})}]{beck2019}
---. 2019{\natexlab{b}}, \apj, 884, 159, \dodoi{10.3847/1538-4357/ab4259}

\bibitem[{{Beckwith} {et~al.}(1990){Beckwith}, {Sargent}, {Chini}, \& {Guesten}}]{1990-beckwith}
{Beckwith}, S. V.~W., {Sargent}, A.~I., {Chini}, R.~S., \& {Guesten}, R. 1990, \aj, 99, 924, \dodoi{10.1086/115385}

\bibitem[{{Benisty} {et~al.}(2018){Benisty}, {Juh{\'a}sz}, {Facchini}, {Pinilla}, {de Boer}, {P{\'e}rez}, {Keppler}, {Muro-Arena}, {Villenave}, {Andrews}, {Dominik}, {Dullemond}, {Gallenne}, {Garufi}, {Ginski}, \& {Isella}}]{benisty18-hd143006-SL}
{Benisty}, M., {Juh{\'a}sz}, A., {Facchini}, S., {et~al.} 2018, \aap, 619, A171, \dodoi{10.1051/0004-6361/201833913}

\bibitem[{{Ben{\'\i}tez-Llambay} \& {Masset}(2016)}]{2016-benitez-llambay-masset}
{Ben{\'\i}tez-Llambay}, P., \& {Masset}, F.~S. 2016, \apjs, 223, 11, \dodoi{10.3847/0067-0049/223/1/11}

\bibitem[{{Berghea} {et~al.}(2024){Berghea}, {Bayyari}, {Sitko}, {Drake}, {Mosquera}, {Garraffo}, {Petit}, {Russell}, \& {Assani}}]{berghea2024-dracula}
{Berghea}, C.~T., {Bayyari}, A., {Sitko}, M.~L., {et~al.} 2024, \apjl, 967, L3, \dodoi{10.3847/2041-8213/ad43e3}

\bibitem[{{Biddle} {et~al.}(2024){Biddle}, {Bowler}, {Zhou}, {Franson}, \& {Zhang}}]{biddle2024-pabeta-ABAur}
{Biddle}, L.~I., {Bowler}, B.~P., {Zhou}, Y., {Franson}, K., \& {Zhang}, Z. 2024, \aj, 167, 172, \dodoi{10.3847/1538-3881/ad2a52}

\bibitem[{{Birnstiel} {et~al.}(2018{\natexlab{a}}){Birnstiel}, {Dullemond}, {Zhu}, {Andrews}, {Bai}, {Wilner}, {Carpenter}, {Huang}, {Isella}, {Benisty}, {P{\'e}rez}, \& {Zhang}}]{2018-birnstiel-dsharp5}
{Birnstiel}, T., {Dullemond}, C.~P., {Zhu}, Z., {et~al.} 2018{\natexlab{a}}, \apjl, 869, L45, \dodoi{10.3847/2041-8213/aaf743}

\bibitem[{{Birnstiel} {et~al.}(2018{\natexlab{b}}){Birnstiel}, {Dullemond}, {Zhu}, {Andrews}, {Bai}, {Wilner}, {Carpenter}, {Huang}, {Isella}, {Benisty}, {P{\'e}rez}, \& {Zhang}}]{birnstiel2018-dsharp-opac}
---. 2018{\natexlab{b}}, \apjl, 869, L45, \dodoi{10.3847/2041-8213/aaf743}

\bibitem[{{Boccaletti} {et~al.}(2020{\natexlab{a}}){Boccaletti}, {Di Folco}, {Pantin}, {Dutrey}, {Guilloteau}, {Tang}, {Pi{\'e}tu}, {Habart}, {Milli}, {Beck}, \& {Maire}}]{boccaletti2020-abaursphere}
{Boccaletti}, A., {Di Folco}, E., {Pantin}, E., {et~al.} 2020{\natexlab{a}}, \aap, 637, L5, \dodoi{10.1051/0004-6361/202038008}

\bibitem[{{Boccaletti} {et~al.}(2020{\natexlab{b}}){Boccaletti}, {Di Folco}, {Pantin}, {Dutrey}, {Guilloteau}, {Tang}, {Pi{\'e}tu}, {Habart}, {Milli}, {Beck}, \& {Maire}}]{boccaletti2020}
---. 2020{\natexlab{b}}, \aap, 637, L5, \dodoi{10.1051/0004-6361/202038008}

\bibitem[{{Boccaletti} {et~al.}(2021){Boccaletti}, {Pantin}, {M{\'e}nard}, {Galicher}, {Langlois}, {Benisty}, {Gratton}, {Chauvin}, {Ginski}, {Lagrange}, {Zurlo}, {Biller}, {Bonavita}, {Bonnefoy}, {Brown-Sevilla}, {Cantalloube}, {Desidera}, {D'Orazi}, {Feldt}, {Hagelberg}, {Lazzoni}, {Mesa}, {Meyer}, {Perrot}, {Vigan}, {Sauvage}, {Ramos}, {Rousset}, \& {Magnard}}]{2021-boccaletti-MWC758}
{Boccaletti}, A., {Pantin}, E., {M{\'e}nard}, F., {et~al.} 2021, \aap, 652, L8, \dodoi{10.1051/0004-6361/202141177}

\bibitem[{{Bohn} {et~al.}(2022){Bohn}, {Benisty}, {Perraut}, {van der Marel}, {W{\"o}lfer}, {van Dishoeck}, {Facchini}, {Manara}, {Teague}, {Francis}, {Berger}, {Garcia-Lopez}, {Ginski}, {Henning}, {Kenworthy}, {Kraus}, {M{\'e}nard}, {M{\'e}rand}, \& {P{\'e}rez}}]{bohn22-misalignments}
{Bohn}, A.~J., {Benisty}, M., {Perraut}, K., {et~al.} 2022, \aap, 658, A183, \dodoi{10.1051/0004-6361/202142070}

\bibitem[{{Bollati} {et~al.}(2021{\natexlab{a}}){Bollati}, {Lodato}, {Price}, \& {Pinte}}]{bollati21-theory-of-kinks-2d}
{Bollati}, F., {Lodato}, G., {Price}, D.~J., \& {Pinte}, C. 2021{\natexlab{a}}, \mnras, 504, 5444, \dodoi{10.1093/mnras/stab1145}

\bibitem[{{Bollati} {et~al.}(2021{\natexlab{b}}){Bollati}, {Lodato}, {Price}, \& {Pinte}}]{bollati2021-theory-kinks}
---. 2021{\natexlab{b}}, \mnras, 504, 5444, \dodoi{10.1093/mnras/stab1145}

\bibitem[{{Bondi}(1952)}]{bondi1952}
{Bondi}, H. 1952, \mnras, 112, 195, \dodoi{10.1093/mnras/112.2.195}

\bibitem[{{Booth} \& {Clarke}(2016)}]{booth-clarke2016-dustySG}
{Booth}, R.~A., \& {Clarke}, C.~J. 2016, \mnras, 458, 2676, \dodoi{10.1093/mnras/stw488}

\bibitem[{{Booth} {et~al.}(2015){Booth}, {Sijacki}, \& {Clarke}}]{2015-booth}
{Booth}, R.~A., {Sijacki}, D., \& {Clarke}, C.~J. 2015, \mnras, 452, 3932, \dodoi{10.1093/mnras/stv1486}

\bibitem[{{Boss}(1997)}]{boss1997}
{Boss}, A.~P. 1997, Science, 276, 1836, \dodoi{10.1126/science.276.5320.1836}

\bibitem[{{Bouwman} {et~al.}(2000){Bouwman}, {de Koter}, {van den Ancker}, \& {Waters}}]{bouwman2000}
{Bouwman}, J., {de Koter}, A., {van den Ancker}, M.~E., \& {Waters}, L.~B.~F.~M. 2000, \aap, 360, 213

\bibitem[{{Braun} \& {Walterbos}(1985)}]{braun-walterbos1985}
{Braun}, R., \& {Walterbos}, R.~A.~M. 1985, \aap, 143, 307

\bibitem[{{Brown-Sevilla} {et~al.}(2021){Brown-Sevilla}, {Keppler}, {Barraza-Alfaro}, {Melon Fuksman}, {Kurtovic}, {Pinilla}, {Feldt}, {Brandner}, {Ginski}, {Henning}, {Klahr}, {Asensio-Torres}, {Cantalloube}, {Garufi}, {van Holstein}, {Langlois}, {Menard}, {Rickman}, {Benisty}, {Chauvin}, {Zurlo}, {Weber}, {Pavlov}, {Ramos}, {Rochat}, \& {Roelfsema}}]{2021-brown-sevilla-waoph6}
{Brown-Sevilla}, S.~B., {Keppler}, M., {Barraza-Alfaro}, M., {et~al.} 2021, arXiv e-prints, arXiv:2107.13560.
\newblock \doarXiv{2107.13560}

\bibitem[{{Burke} \& {Hollenbach}(1983)}]{1983-burke-hollenbach}
{Burke}, J.~R., \& {Hollenbach}, D.~J. 1983, \apj, 265, 223, \dodoi{10.1086/160667}

\bibitem[{{Cacciapuoti} {et~al.}(2024){Cacciapuoti}, {Macias}, {Gupta}, {Testi}, {Miotello}, {Espaillat}, {K{\"u}ffmeier}, {van Terwisga}, {Tobin}, {Grant}, {Manara}, {Segura-Cox}, {Wendeborn}, {Klessen}, {Maury}, {Lebreuilly}, {Hennebelle}, \& {Molinari}}]{cacciapuoti2024-dusty-shrimp}
{Cacciapuoti}, L., {Macias}, E., {Gupta}, A., {et~al.} 2024, \aap, 682, A61, \dodoi{10.1051/0004-6361/202347486}

\bibitem[{{Cadman} {et~al.}(2021){Cadman}, {Rice}, \& {Hall}}]{cadman2021}
{Cadman}, J., {Rice}, K., \& {Hall}, C. 2021, \mnras, 504, 2877, \dodoi{10.1093/mnras/stab905}

\bibitem[{{Calcino} {et~al.}(2022){Calcino}, {Hilder}, {Price}, {Pinte}, {Bollati}, {Lodato}, \& {Norfolk}}]{calcino22-hd163296}
{Calcino}, J., {Hilder}, T., {Price}, D.~J., {et~al.} 2022, \apjl, 929, L25, \dodoi{10.3847/2041-8213/ac64a7}

\bibitem[{{Calcino} {et~al.}(2024){Calcino}, {Price}, {Hilder}, {Christiaens}, {Speedie}, \& {Ormel}}]{calcino2024-anatomyofafall}
{Calcino}, J., {Price}, D.~J., {Hilder}, T., {et~al.} 2024, arXiv e-prints, arXiv:2410.18521, \dodoi{10.48550/arXiv.2410.18521}

\bibitem[{{Casassus} {et~al.}(2022){Casassus}, {C{\'a}rcamo}, {Hales}, {Weber}, \& {Dent}}]{casassus22-hd100546-eruption}
{Casassus}, S., {C{\'a}rcamo}, M., {Hales}, A., {Weber}, P., \& {Dent}, B. 2022, \apjl, 933, L4, \dodoi{10.3847/2041-8213/ac75e8}

\bibitem[{{Casassus} \& {P{\'e}rez}(2019)}]{casassus19-hd100546}
{Casassus}, S., \& {P{\'e}rez}, S. 2019, \apjl, 883, L41, \dodoi{10.3847/2041-8213/ab4425}

\bibitem[{{Casassus} {et~al.}(2021{\natexlab{a}}){Casassus}, {Christiaens}, {C{\'a}rcamo}, {P{\'e}rez}, {Weber}, {Ercolano}, {van der Marel}, {Pinte}, {Dong}, {Baruteau}, {Cieza}, {van Dishoeck}, {Jordan}, {Price}, {Absil}, {Arce-Tord}, {Faramaz}, {Flores}, \& {Reggiani}}]{2021-casassus-filament}
{Casassus}, S., {Christiaens}, V., {C{\'a}rcamo}, M., {et~al.} 2021{\natexlab{a}}, \mnras, \dodoi{10.1093/mnras/stab2359}

\bibitem[{{Casassus} {et~al.}(2021{\natexlab{b}}){Casassus}, {Christiaens}, {C{\'a}rcamo}, {P{\'e}rez}, {Weber}, {Ercolano}, {van der Marel}, {Pinte}, {Dong}, {Baruteau}, {Cieza}, {van Dishoeck}, {Jordan}, {Price}, {Absil}, {Arce-Tord}, {Faramaz}, {Flores}, \& {Reggiani}}]{casassus21-filament-spirals-hd135344B}
---. 2021{\natexlab{b}}, \mnras, 507, 3789, \dodoi{10.1093/mnras/stab2359}

\bibitem[{{Chiang} \& {Youdin}(2010)}]{chiang-youdin-2010-review}
{Chiang}, E., \& {Youdin}, A.~N. 2010, Annual Review of Earth and Planetary Sciences, 38, 493, \dodoi{10.1146/annurev-earth-040809-152513}

\bibitem[{{Chiang} \& {Goldreich}(1997)}]{chiang-goldreich97}
{Chiang}, E.~I., \& {Goldreich}, P. 1997, \apj, 490, 368, \dodoi{10.1086/304869}

\bibitem[{{Cornwell}(2008)}]{cornwell2008}
{Cornwell}, T.~J. 2008, IEEE Journal of Selected Topics in Signal Processing, 2, 793, \dodoi{10.1109/JSTSP.2008.2006388}

\bibitem[{{Cossins} {et~al.}(2009){Cossins}, {Lodato}, \& {Clarke}}]{cossins2009}
{Cossins}, P., {Lodato}, G., \& {Clarke}, C.~J. 2009, \mnras, 393, 1157, \dodoi{10.1111/j.1365-2966.2008.14275.x}

\bibitem[{{Cullen} \& {Dehnen}(2010)}]{cullendehnen2010}
{Cullen}, L., \& {Dehnen}, W. 2010, \mnras, 408, 669, \dodoi{10.1111/j.1365-2966.2010.17158.x}

\bibitem[{{Currie}(2024)}]{currie2024-pabeta-ABAur}
{Currie}, T. 2024, Research Notes of the American Astronomical Society, 8, 146, \dodoi{10.3847/2515-5172/ad50ce}

\bibitem[{{Currie} {et~al.}(2022){Currie}, {Lawson}, {Schneider}, {Lyra}, {Wisniewski}, {Grady}, {Guyon}, {Tamura}, {Kotani}, {Kawahara}, {Brandt}, {Uyama}, {Muto}, {Dong}, {Kudo}, {Hashimoto}, {Fukagawa}, {Wagner}, {Lozi}, {Chilcote}, {Tobin}, {Groff}, {Ward-Duong}, {Januszewski}, {Norris}, {Tuthill}, {van der Marel}, {Sitko}, {Deo}, {Vievard}, {Jovanovic}, {Martinache}, \& {Skaf}}]{currie2022-abaurb}
{Currie}, T., {Lawson}, K., {Schneider}, G., {et~al.} 2022, Nature Astronomy, 6, 751, \dodoi{10.1038/s41550-022-01634-x}

\bibitem[{{Czekala} {et~al.}(2021){Czekala}, {Loomis}, {Teague}, {Booth}, {Huang}, {Cataldi}, {Ilee}, {Law}, {Walsh}, {Bosman}, {Guzm{\'a}n}, {Le Gal}, {{\"O}berg}, {Yamato}, {Aikawa}, {Andrews}, {Bae}, {Bergin}, {Bergner}, {Cleeves}, {Kurtovic}, {M{\'e}nard}, {Nomura}, {P{\'e}rez}, {Qi}, {Schwarz}, {Tsukagoshi}, {Waggoner}, {Wilner}, \& {Zhang}}]{czekala2021-maps2}
{Czekala}, I., {Loomis}, R.~A., {Teague}, R., {et~al.} 2021, \apjs, 257, 2, \dodoi{10.3847/1538-4365/ac1430}

\bibitem[{{de Val-Borro} {et~al.}(2006){de Val-Borro}, {Edgar}, {Artymowicz}, {Ciecielag}, {Cresswell}, {D'Angelo}, {Delgado-Donate}, {Dirksen}, {Fromang}, {Gawryszczak}, {Klahr}, {Kley}, {Lyra}, {Masset}, {Mellema}, {Nelson}, {Paardekooper}, {Peplinski}, {Pierens}, {Plewa}, {Rice}, {Sch{\"a}fer}, \& {Speith}}]{2006-deval-borro}
{de Val-Borro}, M., {Edgar}, R.~G., {Artymowicz}, P., {et~al.} 2006, \mnras, 370, 529, \dodoi{10.1111/j.1365-2966.2006.10488.x}

\bibitem[{{Deng} {et~al.}(2021){Deng}, {Mayer}, \& {Helled}}]{deng2021-magnetic-fragmentation}
{Deng}, H., {Mayer}, L., \& {Helled}, R. 2021, Nature Astronomy, 5, 440, \dodoi{10.1038/s41550-020-01297-6}

\bibitem[{{DeWarf} {et~al.}(2003){DeWarf}, {Sepinsky}, {Guinan}, {Ribas}, \& {Nadalin}}]{dewarf2003}
{DeWarf}, L.~E., {Sepinsky}, J.~F., {Guinan}, E.~F., {Ribas}, I., \& {Nadalin}, I. 2003, \apj, 590, 357, \dodoi{10.1086/374979}

\bibitem[{{Dipierro} {et~al.}(2014){Dipierro}, {Lodato}, {Testi}, \& {de Gregorio Monsalvo}}]{dipierro2014}
{Dipierro}, G., {Lodato}, G., {Testi}, L., \& {de Gregorio Monsalvo}, I. 2014, \mnras, 444, 1919, \dodoi{10.1093/mnras/stu1584}

\bibitem[{{Disk Dynamics Collaboration} {et~al.}(2020){Disk Dynamics Collaboration}, {Armitage}, {Bae}, {Benisty}, {Bergin}, {Casassus}, {Czekala}, {Facchini}, {Fung}, {Hall}, {Ilee}, {Keppler}, {Kuznetsova}, {Le Gal}, {Loomis}, {Lyra}, {Manger}, {Perez}, {Pinte}, {Price}, {Rosotti}, {Szulagyi}, {Schwarz}, {Simon}, {Teague}, \& {Zhang}}]{diskdynamicscollab20}
{Disk Dynamics Collaboration}, {Armitage}, P.~J., {Bae}, J., {et~al.} 2020, arXiv e-prints, arXiv:2009.04345.
\newblock \doarXiv{2009.04345}

\bibitem[{{Doi} \& {Kataoka}(2021)}]{2021-doi-kataoka}
{Doi}, K., \& {Kataoka}, A. 2021, \apj, 912, 164, \dodoi{10.3847/1538-4357/abe5a6}

\bibitem[{{Dong} \& {Fung}(2017{\natexlab{a}})}]{2017-dong-fung}
{Dong}, R., \& {Fung}, J. 2017{\natexlab{a}}, \apj, 835, 146, \dodoi{10.3847/1538-4357/835/2/146}

\bibitem[{{Dong} \& {Fung}(2017{\natexlab{b}})}]{dong-fung17-bright-spirals-SL}
---. 2017{\natexlab{b}}, \apj, 835, 38, \dodoi{10.3847/1538-4357/835/1/38}

\bibitem[{{Dong} {et~al.}(2016{\natexlab{a}}){Dong}, {Fung}, \& {Chiang}}]{dong2016-spirals-scatteredlight}
{Dong}, R., {Fung}, J., \& {Chiang}, E. 2016{\natexlab{a}}, \apj, 826, 75, \dodoi{10.3847/0004-637X/826/1/75}

\bibitem[{{Dong} {et~al.}(2015{\natexlab{a}}){Dong}, {Hall}, {Rice}, \& {Chiang}}]{2015ApJ...812L..32D}
{Dong}, R., {Hall}, C., {Rice}, K., \& {Chiang}, E. 2015{\natexlab{a}}, \apjl, 812, L32, \dodoi{10.1088/2041-8205/812/2/L32}

\bibitem[{{Dong} {et~al.}(2015{\natexlab{b}}){Dong}, {Hall}, {Rice}, \& {Chiang}}]{dong2015-GIspirals-scatteredlight}
---. 2015{\natexlab{b}}, \apjl, 812, L32, \dodoi{10.1088/2041-8205/812/2/L32}

\bibitem[{{Dong} {et~al.}(2017){Dong}, {Li}, {Chiang}, \& {Li}}]{2017-dong-multiple1}
{Dong}, R., {Li}, S., {Chiang}, E., \& {Li}, H. 2017, \apj, 843, 127, \dodoi{10.3847/1538-4357/aa72f2}

\bibitem[{{Dong} {et~al.}(2018{\natexlab{a}}){Dong}, {Li}, {Chiang}, \& {Li}}]{2018-dong-multiple2}
---. 2018{\natexlab{a}}, \apj, 866, 110, \dodoi{10.3847/1538-4357/aadadd}

\bibitem[{{Dong} {et~al.}(2018{\natexlab{b}}){Dong}, {Najita}, \& {Brittain}}]{2018b-dong}
{Dong}, R., {Najita}, J.~R., \& {Brittain}, S. 2018{\natexlab{b}}, \apj, 862, 103, \dodoi{10.3847/1538-4357/aaccfc}

\bibitem[{{Dong} {et~al.}(2018{\natexlab{c}}){Dong}, {Najita}, \& {Brittain}}]{dong2018-gi-or-planets}
---. 2018{\natexlab{c}}, \apj, 862, 103, \dodoi{10.3847/1538-4357/aaccfc}

\bibitem[{{Dong} {et~al.}(2011{\natexlab{a}}){Dong}, {Rafikov}, \& {Stone}}]{2011b-dong}
{Dong}, R., {Rafikov}, R.~R., \& {Stone}, J.~M. 2011{\natexlab{a}}, \apj, 741, 57, \dodoi{10.1088/0004-637X/741/1/57}

\bibitem[{{Dong} {et~al.}(2011{\natexlab{b}}){Dong}, {Rafikov}, {Stone}, \& {Petrovich}}]{2011a-dong}
{Dong}, R., {Rafikov}, R.~R., {Stone}, J.~M., \& {Petrovich}, C. 2011{\natexlab{b}}, \apj, 741, 56, \dodoi{10.1088/0004-637X/741/1/56}

\bibitem[{{Dong} {et~al.}(2016{\natexlab{b}}){Dong}, {Vorobyov}, {Pavlyuchenkov}, {Chiang}, \& {Liu}}]{dong16protostellar}
{Dong}, R., {Vorobyov}, E., {Pavlyuchenkov}, Y., {Chiang}, E., \& {Liu}, H.~B. 2016{\natexlab{b}}, \apj, 823, 141, \dodoi{10.3847/0004-637X/823/2/141}

\bibitem[{{Dong} {et~al.}(2018{\natexlab{d}}){Dong}, {Liu}, {Eisner}, {Andrews}, {Fung}, {Zhu}, {Chiang}, {Hashimoto}, {Liu}, {Casassus}, {Esposito}, {Hasegawa}, {Muto}, {Pavlyuchenkov}, {Wilner}, {Akiyama}, {Tamura}, \& {Wisniewski}}]{2018-dong-MWC758}
{Dong}, R., {Liu}, S.-y., {Eisner}, J., {et~al.} 2018{\natexlab{d}}, \apj, 860, 124, \dodoi{10.3847/1538-4357/aac6cb}

\bibitem[{{Dr{\k{a}}{\.z}kowska} {et~al.}(2023){Dr{\k{a}}{\.z}kowska}, {Bitsch}, {Lambrechts}, {Mulders}, {Harsono}, {Vazan}, {Liu}, {Ormel}, {Kretke}, \& {Morbidelli}}]{drazkowska2023-ppvii}
{Dr{\k{a}}{\.z}kowska}, J., {Bitsch}, B., {Lambrechts}, M., {et~al.} 2023, in Astronomical Society of the Pacific Conference Series, Vol. 534, Protostars and Planets VII, ed. S.~{Inutsuka}, Y.~{Aikawa}, T.~{Muto}, K.~{Tomida}, \& M.~{Tamura}, 717, \dodoi{10.48550/arXiv.2203.09759}

\bibitem[{{Duffell} \& {Chiang}(2015)}]{2015-duffell-chiang}
{Duffell}, P.~C., \& {Chiang}, E. 2015, \apj, 812, 94, \dodoi{10.1088/0004-637X/812/2/94}

\bibitem[{{Dullemond} {et~al.}(2001){Dullemond}, {Dominik}, \& {Natta}}]{dullemond01-irradiated}
{Dullemond}, C.~P., {Dominik}, C., \& {Natta}, A. 2001, \apj, 560, 957, \dodoi{10.1086/323057}

\bibitem[{{Dullemond} {et~al.}(2022){Dullemond}, {Kimmig}, \& {Zanazzi}}]{dullemond2022-kimmig-zanazzi}
{Dullemond}, C.~P., {Kimmig}, C.~N., \& {Zanazzi}, J.~J. 2022, \mnras, 511, 2925, \dodoi{10.1093/mnras/stab2791}

\bibitem[{{Dullemond} {et~al.}(2019){Dullemond}, {K{\"u}ffmeier}, {Goicovic}, {Fukagawa}, {Oehl}, \& {Kramer}}]{dullemond2019-cloudlet}
{Dullemond}, C.~P., {K{\"u}ffmeier}, M., {Goicovic}, F., {et~al.} 2019, \aap, 628, A20, \dodoi{10.1051/0004-6361/201832632}

\bibitem[{{Dullemond} {et~al.}(2018{\natexlab{a}}){Dullemond}, {Birnstiel}, {Huang}, {Kurtovic}, {Andrews}, {Guzm{\'a}n}, {P{\'e}rez}, {Isella}, {Zhu}, {Benisty}, {Wilner}, {Bai}, {Carpenter}, {Zhang}, \& {Ricci}}]{dullemond18-dsharp6}
{Dullemond}, C.~P., {Birnstiel}, T., {Huang}, J., {et~al.} 2018{\natexlab{a}}, \apjl, 869, L46, \dodoi{10.3847/2041-8213/aaf742}

\bibitem[{{Dullemond} {et~al.}(2018{\natexlab{b}}){Dullemond}, {Birnstiel}, {Huang}, {Kurtovic}, {Andrews}, {Guzm{\'a}n}, {P{\'e}rez}, {Isella}, {Zhu}, {Benisty}, {Wilner}, {Bai}, {Carpenter}, {Zhang}, \& {Ricci}}]{dullemond2018-dsharp6}
---. 2018{\natexlab{b}}, \apjl, 869, L46, \dodoi{10.3847/2041-8213/aaf742}

\bibitem[{{Dutrey} {et~al.}(2024){Dutrey}, {Chapillon}, {Guilloteau}, {Tang}, {Boccaletti}, {Bouscasse}, {Collin-Dufresne}, {Di Folco}, {Fuente}, {Pi{\'e}tu}, {Rivi{\`e}re-Marichalar}, \& {Semenov}}]{dutrey2024-abaur-SO}
{Dutrey}, A., {Chapillon}, E., {Guilloteau}, S., {et~al.} 2024, arXiv e-prints, arXiv:2408.14276, \dodoi{10.48550/arXiv.2408.14276}

\bibitem[{{Edgar}(2004)}]{edgar2004-review}
{Edgar}, R. 2004, \nar, 48, 843, \dodoi{10.1016/j.newar.2004.06.001}

\bibitem[{{Ediss} {et~al.}(2004){Ediss}, {Carter}, {Cheng}, {Effland}, {Grammer}, {Horner}, {Kerr}, {Koller}, {Lauria}, {Morris}, {Pan}, {Reiland}, \& {Sullivan}}]{ediss2004-band6}
{Ediss}, G.~A., {Carter}, M., {Cheng}, J., {et~al.} 2004, in Fifteenth International Symposium on Space Terahertz Technology, ed. G.~{Narayanan}, 181--188

\bibitem[{{Fairbairn} \& {Rafikov}(2022)}]{fairbairn22-eccentricplanet-spirals}
{Fairbairn}, C.~W., \& {Rafikov}, R.~R. 2022, arXiv e-prints, arXiv:2207.14637.
\newblock \doarXiv{2207.14637}

\bibitem[{{Faridani} {et~al.}(2018){Faridani}, {Bigiel}, {Fl{\"o}er}, {Kerp}, \& {Stanimirovi{\'c}}}]{faridani2018-shortspacingcorrection}
{Faridani}, S., {Bigiel}, F., {Fl{\"o}er}, L., {Kerp}, J., \& {Stanimirovi{\'c}}, S. 2018, Astronomische Nachrichten, 339, 87, \dodoi{10.1002/asna.201713381}

\bibitem[{{Flores} {et~al.}(2023){Flores}, {Ohashi}, {Tobin}, {J{\o}rgensen}, {Takakuwa}, {Li}, {Lin}, {van't Hoff}, {Plunkett}, {Yamato}, {Sai (Insa Choi)}, {Koch}, {Yen}, {Aikawa}, {Aso}, {de Gregorio-Monsalvo}, {Kido}, {Kwon}, {Lee}, {Lee}, {Looney}, {Santamar{\'\i}a-Miranda}, {Sharma}, {Thieme}, {Williams}, {Han}, {Narayanan}, \& {Lai}}]{flores2023-edisk-irs63}
{Flores}, C., {Ohashi}, N., {Tobin}, J.~J., {et~al.} 2023, \apj, 958, 98, \dodoi{10.3847/1538-4357/acf7c1}

\bibitem[{{Fuente} {et~al.}(2010){Fuente}, {Cernicharo}, {Ag{\'u}ndez}, {Bern{\'e}}, {Goicoechea}, {Alonso-Albi}, \& {Marcelino}}]{fuente-2010-iram-abaur}
{Fuente}, A., {Cernicharo}, J., {Ag{\'u}ndez}, M., {et~al.} 2010, \aap, 524, A19, \dodoi{10.1051/0004-6361/201014905}

\bibitem[{{Fukagawa} {et~al.}(2004){Fukagawa}, {Hayashi}, {Tamura}, {Itoh}, {Hayashi}, {Oasa}, {Takeuchi}, {Morino}, {Murakawa}, {Oya}, {Yamashita}, {Suto}, {Mayama}, {Naoi}, {Ishii}, {Pyo}, {Nishikawa}, {Takato}, {Usuda}, {Ando}, {Iye}, {Miyama}, \& {Kaifu}}]{fukagawa2004}
{Fukagawa}, M., {Hayashi}, M., {Tamura}, M., {et~al.} 2004, \apjl, 605, L53, \dodoi{10.1086/420699}

\bibitem[{{Fung} \& {Chiang}(2016)}]{2016-fung-gaps}
{Fung}, J., \& {Chiang}, E. 2016, \apj, 832, 105, \dodoi{10.3847/0004-637X/832/2/105}

\bibitem[{{Fung} \& {Dong}(2015)}]{fung-dong15-inferring-planet-mass-spirals}
{Fung}, J., \& {Dong}, R. 2015, \apjl, 815, L21, \dodoi{10.1088/2041-8205/815/2/L21}

\bibitem[{{Fung} {et~al.}(2014){Fung}, {Shi}, \& {Chiang}}]{2014-fung-gaps}
{Fung}, J., {Shi}, J.-M., \& {Chiang}, E. 2014, \apj, 782, 88, \dodoi{10.1088/0004-637X/782/2/88}

\bibitem[{{Gaia Collaboration} {et~al.}(2016){Gaia Collaboration}, {Prusti}, {de Bruijne}, {Brown}, {Vallenari}, {Babusiaux}, {Bailer-Jones}, {Bastian}, {Biermann}, {Evans}, {Eyer}, {Jansen}, {Jordi}, {Klioner}, {Lammers}, {Lindegren}, {Luri}, {Mignard}, {Milligan}, {Panem}, {Poinsignon}, {Pourbaix}, {Randich}, {Sarri}, {Sartoretti}, {Siddiqui}, {Soubiran}, {Valette}, {van Leeuwen}, {Walton}, {Aerts}, {Arenou}, {Cropper}, {Drimmel}, {H{\o}g}, {Katz}, {Lattanzi}, {O'Mullane}, {Grebel}, {Holland}, {Huc}, {Passot}, {Bramante}, {Cacciari}, {Casta{\~n}eda}, {Chaoul}, {Cheek}, {De Angeli}, {Fabricius}, {Guerra}, {Hern{\'a}ndez}, {Jean-Antoine-Piccolo}, {Masana}, {Messineo}, {Mowlavi}, {Nienartowicz}, {Ord{\'o}{\~n}ez-Blanco}, {Panuzzo}, {Portell}, {Richards}, {Riello}, {Seabroke}, {Tanga}, {Th{\'e}venin}, {Torra}, {Els}, {Gracia-Abril}, {Comoretto}, {Garcia-Reinaldos}, {Lock}, {Mercier}, {Altmann}, {Andrae}, {Astraatmadja}, {Bellas-Velidis}, {Benson}, {Berthier}, {Blomme}, {Busso}, {Carry}, {Cellino}, {Clementini},
  {Cowell}, {Creevey}, {Cuypers}, {Davidson}, {De Ridder}, {de Torres}, {Delchambre}, {Dell'Oro}, {Ducourant}, {Fr{\'e}mat}, {Garc{\'\i}a-Torres}, {Gosset}, {Halbwachs}, {Hambly}, {Harrison}, {Hauser}, {Hestroffer}, {Hodgkin}, {Huckle}, {Hutton}, {Jasniewicz}, {Jordan}, {Kontizas}, {Korn}, {Lanzafame}, {Manteiga}, {Moitinho}, {Muinonen}, {Osinde}, {Pancino}, {Pauwels}, {Petit}, {Recio-Blanco}, {Robin}, {Sarro}, {Siopis}, {Smith}, {Smith}, {Sozzetti}, {Thuillot}, {van Reeven}, {Viala}, {Abbas}, {Abreu Aramburu}, {Accart}, {Aguado}, {Allan}, {Allasia}, {Altavilla}, {{\'A}lvarez}, {Alves}, {Anderson}, {Andrei}, {Anglada Varela}, {Antiche}, {Antoja}, {Ant{\'o}n}, {Arcay}, {Atzei}, {Ayache}, {Bach}, {Baker}, {Balaguer-N{\'u}{\~n}ez}, {Barache}, {Barata}, {Barbier}, {Barblan}, {Baroni}, {Barrado y Navascu{\'e}s}, {Barros}, {Barstow}, {Becciani}, {Bellazzini}, {Bellei}, {Bello Garc{\'\i}a}, {Belokurov}, {Bendjoya}, {Berihuete}, {Bianchi}, {Bienaym{\'e}}, {Billebaud}, {Blagorodnova}, {Blanco-Cuaresma}, {Boch},
  {Bombrun}, {Borrachero}, {Bouquillon}, {Bourda}, {Bouy}, {Bragaglia}, {Breddels}, {Brouillet}, {Br{\"u}semeister}, {Bucciarelli}, {Budnik}, {Burgess}, {Burgon}, {Burlacu}, {Busonero}, {Buzzi}, {Caffau}, {Cambras}, {Campbell}, {Cancelliere}, {Cantat-Gaudin}, {Carlucci}, {Carrasco}, {Castellani}, {Charlot}, {Charnas}, {Charvet}, {Chassat}, {Chiavassa}, {Clotet}, {Cocozza}, {Collins}, {Collins}, {Costigan}, {Crifo}, {Cross}, {Crosta}, {Crowley}, {Dafonte}, {Damerdji}, {Dapergolas}, {David}, {David}, {De Cat}, {de Felice}, {de Laverny}, {De Luise}, {De March}, {de Martino}, {de Souza}, {Debosscher}, {del Pozo}, {Delbo}, {Delgado}, {Delgado}, {di Marco}, {Di Matteo}, {Diakite}, {Distefano}, {Dolding}, {Dos Anjos}, {Drazinos}, {Dur{\'a}n}, {Dzigan}, {Ecale}, {Edvardsson}, {Enke}, {Erdmann}, {Escolar}, {Espina}, {Evans}, {Eynard Bontemps}, {Fabre}, {Fabrizio}, {Faigler}, {Falc{\~a}o}, {Farr{\`a}s Casas}, {Faye}, {Federici}, {Fedorets}, {Fern{\'a}ndez-Hern{\'a}ndez}, {Fernique}, {Fienga}, {Figueras}, {Filippi},
  {Findeisen}, {Fonti}, {Fouesneau}, {Fraile}, {Fraser}, {Fuchs}, {Furnell}, {Gai}, {Galleti}, {Galluccio}, {Garabato}, {Garc{\'\i}a-Sedano}, {Gar{\'e}}, {Garofalo}, {Garralda}, {Gavras}, {Gerssen}, {Geyer}, {Gilmore}, {Girona}, {Giuffrida}, {Gomes}, {Gonz{\'a}lez-Marcos}, {Gonz{\'a}lez-N{\'u}{\~n}ez}, {Gonz{\'a}lez-Vidal}, {Granvik}, {Guerrier}, {Guillout}, {Guiraud}, {G{\'u}rpide}, {Guti{\'e}rrez-S{\'a}nchez}, {Guy}, {Haigron}, {Hatzidimitriou}, {Haywood}, {Heiter}, {Helmi}, {Hobbs}, {Hofmann}, {Holl}, {Holland}, {Hunt}, {Hypki}, {Icardi}, {Irwin}, {Jevardat de Fombelle}, {Jofr{\'e}}, {Jonker}, {Jorissen}, {Julbe}, {Karampelas}, {Kochoska}, {Kohley}, {Kolenberg}, {Kontizas}, {Koposov}, {Kordopatis}, {Koubsky}, {Kowalczyk}, {Krone-Martins}, {Kudryashova}, {Kull}, {Bachchan}, {Lacoste-Seris}, {Lanza}, {Lavigne}, {Le Poncin-Lafitte}, {Lebreton}, {Lebzelter}, {Leccia}, {Leclerc}, {Lecoeur-Taibi}, {Lemaitre}, {Lenhardt}, {Leroux}, {Liao}, {Licata}, {Lindstr{\o}m}, {Lister}, {Livanou}, {Lobel}, {L{\"o}ffler},
  {L{\'o}pez}, {Lopez-Lozano}, {Lorenz}, {Loureiro}, {MacDonald}, {Magalh{\~a}es Fernandes}, {Managau}, {Mann}, {Mantelet}, {Marchal}, {Marchant}, {Marconi}, {Marie}, {Marinoni}, {Marrese}, {Marschalk{\'o}}, {Marshall}, {Mart{\'\i}n-Fleitas}, {Martino}, {Mary}, {Matijevi{\v{c}}}, {Mazeh}, {McMillan}, {Messina}, {Mestre}, {Michalik}, {Millar}, {Miranda}, {Molina}, {Molinaro}, {Molinaro}, {Moln{\'a}r}, {Moniez}, {Montegriffo}, {Monteiro}, {Mor}, {Mora}, {Morbidelli}, {Morel}, {Morgenthaler}, {Morley}, {Morris}, {Mulone}, {Muraveva}, {Musella}, {Narbonne}, {Nelemans}, {Nicastro}, {Noval}, {Ord{\'e}novic}, {Ordieres-Mer{\'e}}, {Osborne}, {Pagani}, {Pagano}, {Pailler}, {Palacin}, {Palaversa}, {Parsons}, {Paulsen}, {Pecoraro}, {Pedrosa}, {Pentik{\"a}inen}, {Pereira}, {Pichon}, {Piersimoni}, {Pineau}, {Plachy}, {Plum}, {Poujoulet}, {Pr{\v{s}}a}, {Pulone}, {Ragaini}, {Rago}, {Rambaux}, {Ramos-Lerate}, {Ranalli}, {Rauw}, {Read}, {Regibo}, {Renk}, {Reyl{\'e}}, {Ribeiro}, {Rimoldini}, {Ripepi}, {Riva}, {Rixon},
  {Roelens}, {Romero-G{\'o}mez}, {Rowell}, {Royer}, {Rudolph}, {Ruiz-Dern}, {Sadowski}, {Sagrist{\`a} Sell{\'e}s}, {Sahlmann}, {Salgado}, {Salguero}, {Sarasso}, {Savietto}, {Schnorhk}, {Schultheis}, {Sciacca}, {Segol}, {Segovia}, {Segransan}, {Serpell}, {Shih}, {Smareglia}, {Smart}, {Smith}, {Solano}, {Solitro}, {Sordo}, {Soria Nieto}, {Souchay}, {Spagna}, {Spoto}, {Stampa}, {Steele}, {Steidelm{\"u}ller}, {Stephenson}, {Stoev}, {Suess}, {S{\"u}veges}, {Surdej}, {Szabados}, {Szegedi-Elek}, {Tapiador}, {Taris}, {Tauran}, {Taylor}, {Teixeira}, {Terrett}, {Tingley}, {Trager}, {Turon}, {Ulla}, {Utrilla}, {Valentini}, {van Elteren}, {Van Hemelryck}, {van Leeuwen}, {Varadi}, {Vecchiato}, {Veljanoski}, {Via}, {Vicente}, {Vogt}, {Voss}, {Votruba}, {Voutsinas}, {Walmsley}, {Weiler}, {Weingrill}, {Werner}, {Wevers}, {Whitehead}, {Wyrzykowski}, {Yoldas}, {{\v{Z}}erjal}, {Zucker}, {Zurbach}, {Zwitter}, {Alecu}, {Allen}, {Allende Prieto}, {Amorim}, {Anglada-Escud{\'e}}, {Arsenijevic}, {Azaz}, {Balm}, {Beck}, {Bernstein},
  {Bigot}, {Bijaoui}, {Blasco}, {Bonfigli}, {Bono}, {Boudreault}, {Bressan}, {Brown}, {Brunet}, {Bunclark}, {Buonanno}, {Butkevich}, {Carret}, {Carrion}, {Chemin}, {Ch{\'e}reau}, {Corcione}, {Darmigny}, {de Boer}, {de Teodoro}, {de Zeeuw}, {Delle Luche}, {Domingues}, {Dubath}, {Fodor}, {Fr{\'e}zouls}, {Fries}, {Fustes}, {Fyfe}, {Gallardo}, {Gallegos}, {Gardiol}, {Gebran}, {Gomboc}, {G{\'o}mez}, {Grux}, {Gueguen}, {Heyrovsky}, {Hoar}, {Iannicola}, {Isasi Parache}, {Janotto}, {Joliet}, {Jonckheere}, {Keil}, {Kim}, {Klagyivik}, {Klar}, {Knude}, {Kochukhov}, {Kolka}, {Kos}, {Kutka}, {Lainey}, {LeBouquin}, {Liu}, {Loreggia}, {Makarov}, {Marseille}, {Martayan}, {Martinez-Rubi}, {Massart}, {Meynadier}, {Mignot}, {Munari}, {Nguyen}, {Nordlander}, {Ocvirk}, {O'Flaherty}, {Olias Sanz}, {Ortiz}, {Osorio}, {Oszkiewicz}, {Ouzounis}, {Palmer}, {Park}, {Pasquato}, {Peltzer}, {Peralta}, {P{\'e}turaud}, {Pieniluoma}, {Pigozzi}, {Poels}, {Prat}, {Prod'homme}, {Raison}, {Rebordao}, {Risquez}, {Rocca-Volmerange}, {Rosen},
  {Ruiz-Fuertes}, {Russo}, {Sembay}, {Serraller Vizcaino}, {Short}, {Siebert}, {Silva}, {Sinachopoulos}, {Slezak}, {Soffel}, {Sosnowska}, {Strai{\v{z}}ys}, {ter Linden}, {Terrell}, {Theil}, {Tiede}, {Troisi}, {Tsalmantza}, {Tur}, {Vaccari}, {Vachier}, {Valles}, {Van Hamme}, {Veltz}, {Virtanen}, {Wallut}, {Wichmann}, {Wilkinson}, {Ziaeepour}, \& {Zschocke}}]{gaia-mission-2016}
{Gaia Collaboration}, {Prusti}, T., {de Bruijne}, J.~H.~J., {et~al.} 2016, \aap, 595, A1, \dodoi{10.1051/0004-6361/201629272}

\bibitem[{{Gaia Collaboration} {et~al.}(2023){Gaia Collaboration}, {Vallenari}, {Brown}, {Prusti}, {de Bruijne}, {Arenou}, {Babusiaux}, {Biermann}, {Creevey}, {Ducourant}, {Evans}, {Eyer}, {Guerra}, {Hutton}, {Jordi}, {Klioner}, {Lammers}, {Lindegren}, {Luri}, {Mignard}, {Panem}, {Pourbaix}, {Randich}, {Sartoretti}, {Soubiran}, {Tanga}, {Walton}, {Bailer-Jones}, {Bastian}, {Drimmel}, {Jansen}, {Katz}, {Lattanzi}, {van Leeuwen}, {Bakker}, {Cacciari}, {Casta{\~n}eda}, {De Angeli}, {Fabricius}, {Fouesneau}, {Fr{\'e}mat}, {Galluccio}, {Guerrier}, {Heiter}, {Masana}, {Messineo}, {Mowlavi}, {Nicolas}, {Nienartowicz}, {Pailler}, {Panuzzo}, {Riclet}, {Roux}, {Seabroke}, {Sordo}, {Th{\'e}venin}, {Gracia-Abril}, {Portell}, {Teyssier}, {Altmann}, {Andrae}, {Audard}, {Bellas-Velidis}, {Benson}, {Berthier}, {Blomme}, {Burgess}, {Busonero}, {Busso}, {C{\'a}novas}, {Carry}, {Cellino}, {Cheek}, {Clementini}, {Damerdji}, {Davidson}, {de Teodoro}, {Nu{\~n}ez Campos}, {Delchambre}, {Dell'Oro}, {Esquej},
  {Fern{\'a}ndez-Hern{\'a}ndez}, {Fraile}, {Garabato}, {Garc{\'\i}a-Lario}, {Gosset}, {Haigron}, {Halbwachs}, {Hambly}, {Harrison}, {Hern{\'a}ndez}, {Hestroffer}, {Hodgkin}, {Holl}, {Jan{\ss}en}, {Jevardat de Fombelle}, {Jordan}, {Krone-Martins}, {Lanzafame}, {L{\"o}ffler}, {Marchal}, {Marrese}, {Moitinho}, {Muinonen}, {Osborne}, {Pancino}, {Pauwels}, {Recio-Blanco}, {Reyl{\'e}}, {Riello}, {Rimoldini}, {Roegiers}, {Rybizki}, {Sarro}, {Siopis}, {Smith}, {Sozzetti}, {Utrilla}, {van Leeuwen}, {Abbas}, {{\'A}brah{\'a}m}, {Abreu Aramburu}, {Aerts}, {Aguado}, {Ajaj}, {Aldea-Montero}, {Altavilla}, {{\'A}lvarez}, {Alves}, {Anders}, {Anderson}, {Anglada Varela}, {Antoja}, {Baines}, {Baker}, {Balaguer-N{\'u}{\~n}ez}, {Balbinot}, {Balog}, {Barache}, {Barbato}, {Barros}, {Barstow}, {Bartolom{\'e}}, {Bassilana}, {Bauchet}, {Becciani}, {Bellazzini}, {Berihuete}, {Bernet}, {Bertone}, {Bianchi}, {Binnenfeld}, {Blanco-Cuaresma}, {Blazere}, {Boch}, {Bombrun}, {Bossini}, {Bouquillon}, {Bragaglia}, {Bramante}, {Breedt},
  {Bressan}, {Brouillet}, {Brugaletta}, {Bucciarelli}, {Burlacu}, {Butkevich}, {Buzzi}, {Caffau}, {Cancelliere}, {Cantat-Gaudin}, {Carballo}, {Carlucci}, {Carnerero}, {Carrasco}, {Casamiquela}, {Castellani}, {Castro-Ginard}, {Chaoul}, {Charlot}, {Chemin}, {Chiaramida}, {Chiavassa}, {Chornay}, {Comoretto}, {Contursi}, {Cooper}, {Cornez}, {Cowell}, {Crifo}, {Cropper}, {Crosta}, {Crowley}, {Dafonte}, {Dapergolas}, {David}, {David}, {de Laverny}, {De Luise}, {De March}, {De Ridder}, {de Souza}, {de Torres}, {del Peloso}, {del Pozo}, {Delbo}, {Delgado}, {Delisle}, {Demouchy}, {Dharmawardena}, {Di Matteo}, {Diakite}, {Diener}, {Distefano}, {Dolding}, {Edvardsson}, {Enke}, {Fabre}, {Fabrizio}, {Faigler}, {Fedorets}, {Fernique}, {Fienga}, {Figueras}, {Fournier}, {Fouron}, {Fragkoudi}, {Gai}, {Garcia-Gutierrez}, {Garcia-Reinaldos}, {Garc{\'\i}a-Torres}, {Garofalo}, {Gavel}, {Gavras}, {Gerlach}, {Geyer}, {Giacobbe}, {Gilmore}, {Girona}, {Giuffrida}, {Gomel}, {Gomez}, {Gonz{\'a}lez-N{\'u}{\~n}ez},
  {Gonz{\'a}lez-Santamar{\'\i}a}, {Gonz{\'a}lez-Vidal}, {Granvik}, {Guillout}, {Guiraud}, {Guti{\'e}rrez-S{\'a}nchez}, {Guy}, {Hatzidimitriou}, {Hauser}, {Haywood}, {Helmer}, {Helmi}, {Sarmiento}, {Hidalgo}, {Hilger}, {H{\l}adczuk}, {Hobbs}, {Holland}, {Huckle}, {Jardine}, {Jasniewicz}, {Jean-Antoine Piccolo}, {Jim{\'e}nez-Arranz}, {Jorissen}, {Juaristi Campillo}, {Julbe}, {Karbevska}, {Kervella}, {Khanna}, {Kontizas}, {Kordopatis}, {Korn}, {K{\'o}sp{\'a}l}, {Kostrzewa-Rutkowska}, {Kruszy{\'n}ska}, {Kun}, {Laizeau}, {Lambert}, {Lanza}, {Lasne}, {Le Campion}, {Lebreton}, {Lebzelter}, {Leccia}, {Leclerc}, {Lecoeur-Taibi}, {Liao}, {Licata}, {Lindstr{\o}m}, {Lister}, {Livanou}, {Lobel}, {Lorca}, {Loup}, {Madrero Pardo}, {Magdaleno Romeo}, {Managau}, {Mann}, {Manteiga}, {Marchant}, {Marconi}, {Marcos}, {Marcos Santos}, {Mar{\'\i}n Pina}, {Marinoni}, {Marocco}, {Marshall}, {Martin Polo}, {Mart{\'\i}n-Fleitas}, {Marton}, {Mary}, {Masip}, {Massari}, {Mastrobuono-Battisti}, {Mazeh}, {McMillan}, {Messina}, {Michalik},
  {Millar}, {Mints}, {Molina}, {Molinaro}, {Moln{\'a}r}, {Monari}, {Mongui{\'o}}, {Montegriffo}, {Montero}, {Mor}, {Mora}, {Morbidelli}, {Morel}, {Morris}, {Muraveva}, {Murphy}, {Musella}, {Nagy}, {Noval}, {Oca{\~n}a}, {Ogden}, {Ordenovic}, {Osinde}, {Pagani}, {Pagano}, {Palaversa}, {Palicio}, {Pallas-Quintela}, {Panahi}, {Payne-Wardenaar}, {Pe{\~n}alosa Esteller}, {Penttil{\"a}}, {Pichon}, {Piersimoni}, {Pineau}, {Plachy}, {Plum}, {Poggio}, {Pr{\v{s}}a}, {Pulone}, {Racero}, {Ragaini}, {Rainer}, {Raiteri}, {Rambaux}, {Ramos}, {Ramos-Lerate}, {Re Fiorentin}, {Regibo}, {Richards}, {Rios Diaz}, {Ripepi}, {Riva}, {Rix}, {Rixon}, {Robichon}, {Robin}, {Robin}, {Roelens}, {Rogues}, {Rohrbasser}, {Romero-G{\'o}mez}, {Rowell}, {Royer}, {Ruz Mieres}, {Rybicki}, {Sadowski}, {S{\'a}ez N{\'u}{\~n}ez}, {Sagrist{\`a} Sell{\'e}s}, {Sahlmann}, {Salguero}, {Samaras}, {Sanchez Gimenez}, {Sanna}, {Santove{\~n}a}, {Sarasso}, {Schultheis}, {Sciacca}, {Segol}, {Segovia}, {S{\'e}gransan}, {Semeux}, {Shahaf}, {Siddiqui}, {Siebert},
  {Siltala}, {Silvelo}, {Slezak}, {Slezak}, {Smart}, {Snaith}, {Solano}, {Solitro}, {Souami}, {Souchay}, {Spagna}, {Spina}, {Spoto}, {Steele}, {Steidelm{\"u}ller}, {Stephenson}, {S{\"u}veges}, {Surdej}, {Szabados}, {Szegedi-Elek}, {Taris}, {Taylor}, {Teixeira}, {Tolomei}, {Tonello}, {Torra}, {Torra}, {Torralba Elipe}, {Trabucchi}, {Tsounis}, {Turon}, {Ulla}, {Unger}, {Vaillant}, {van Dillen}, {van Reeven}, {Vanel}, {Vecchiato}, {Viala}, {Vicente}, {Voutsinas}, {Weiler}, {Wevers}, {Wyrzykowski}, {Yoldas}, {Yvard}, {Zhao}, {Zorec}, {Zucker}, \& {Zwitter}}]{gaiaDR3-2023}
{Gaia Collaboration}, {Vallenari}, A., {Brown}, A.~G.~A., {et~al.} 2023, \aap, 674, A1, \dodoi{10.1051/0004-6361/202243940}

\bibitem[{{Gammie}(2001)}]{gammie2001}
{Gammie}, C.~F. 2001, \apj, 553, 174, \dodoi{10.1086/320631}

\bibitem[{{Garaud} {et~al.}(2004){Garaud}, {Barri{\`e}re-Fouchet}, \& {Lin}}]{2004-garaud}
{Garaud}, P., {Barri{\`e}re-Fouchet}, L., \& {Lin}, D.~N.~C. 2004, \apj, 603, 292, \dodoi{10.1086/381385}

\bibitem[{{Garufi} {et~al.}(2022{\natexlab{a}}){Garufi}, {Dominik}, {Ginski}, {Benisty}, {van Holstein}, {Henning}, {Pawellek}, {Pinte}, {Avenhaus}, {Facchini}, {Galicher}, {Gratton}, {M{\'e}nard}, {Muro-Arena}, {Milli}, {Stolker}, {Vigan}, {Villenave}, {Moulin}, {Origne}, {Rigal}, {Sauvage}, \& {Weber}}]{garufi22-sphere}
{Garufi}, A., {Dominik}, C., {Ginski}, C., {et~al.} 2022{\natexlab{a}}, \aap, 658, A137, \dodoi{10.1051/0004-6361/202141692}

\bibitem[{{Garufi} {et~al.}(2022{\natexlab{b}}){Garufi}, {Podio}, {Codella}, {Segura-Cox}, {Vander Donckt}, {Mercimek}, {Bacciotti}, {Fedele}, {Kasper}, {Pineda}, {Humphreys}, \& {Testi}}]{garufi2022-hltau-dgtau}
{Garufi}, A., {Podio}, L., {Codella}, C., {et~al.} 2022{\natexlab{b}}, \aap, 658, A104, \dodoi{10.1051/0004-6361/202141264}

\bibitem[{{Garufi} {et~al.}(2024){Garufi}, {Ginski}, {van Holstein}, {Benisty}, {Manara}, {P{\'e}rez}, {Pinilla}, {Ribas}, {Weber}, {Williams}, {Cieza}, {Dominik}, {Facchini}, {Huang}, {Zurlo}, {Bae}, {Hagelberg}, {Henning}, {Hogerheijde}, {Janson}, {M{\'e}nard}, {Messina}, {Meyer}, {Pinte}, {Quanz}, {Rigliaco}, {Roccatagliata}, {Schmid}, {Szul{\'a}gyi}, {van Boekel}, {Wahhaj}, {Antichi}, {Baruffolo}, \& {Moulin}}]{garufi2024-destinys-taurus}
{Garufi}, A., {Ginski}, C., {van Holstein}, R.~G., {et~al.} 2024, arXiv e-prints, arXiv:2403.02158, \dodoi{10.48550/arXiv.2403.02158}

\bibitem[{{Ginski} {et~al.}(2016{\natexlab{a}}){Ginski}, {Stolker}, {Pinilla}, {Dominik}, {Boccaletti}, {de Boer}, {Benisty}, {Biller}, {Feldt}, {Garufi}, {Keller}, {Kenworthy}, {Maire}, {M{\'e}nard}, {Mesa}, {Milli}, {Min}, {Pinte}, {Quanz}, {van Boekel}, {Bonnefoy}, {Chauvin}, {Desidera}, {Gratton}, {Girard}, {Keppler}, {Kopytova}, {Lagrange}, {Langlois}, {Rouan}, \& {Vigan}}]{ginski16-hd97048-sphere}
{Ginski}, C., {Stolker}, T., {Pinilla}, P., {et~al.} 2016{\natexlab{a}}, \aap, 595, A112, \dodoi{10.1051/0004-6361/201629265}

\bibitem[{{Ginski} {et~al.}(2016{\natexlab{b}}){Ginski}, {Stolker}, {Pinilla}, {Dominik}, {Boccaletti}, {de Boer}, {Benisty}, {Biller}, {Feldt}, {Garufi}, {Keller}, {Kenworthy}, {Maire}, {M{\'e}nard}, {Mesa}, {Milli}, {Min}, {Pinte}, {Quanz}, {van Boekel}, {Bonnefoy}, {Chauvin}, {Desidera}, {Gratton}, {Girard}, {Keppler}, {Kopytova}, {Lagrange}, {Langlois}, {Rouan}, \& {Vigan}}]{ginski2016-scatteredlight}
---. 2016{\natexlab{b}}, \aap, 595, A112, \dodoi{10.1051/0004-6361/201629265}

\bibitem[{{Ginski} {et~al.}(2021){Ginski}, {Facchini}, {Huang}, {Benisty}, {Vaendel}, {Stapper}, {Dominik}, {Bae}, {M{\'e}nard}, {Muro-Arena}, {Hogerheijde}, {McClure}, {van Holstein}, {Birnstiel}, {Boehler}, {Bohn}, {Flock}, {Mamajek}, {Manara}, {Pinilla}, {Pinte}, \& {Ribas}}]{ginski2021-SUAur}
{Ginski}, C., {Facchini}, S., {Huang}, J., {et~al.} 2021, \apjl, 908, L25, \dodoi{10.3847/2041-8213/abdf57}

\bibitem[{{Goldreich} \& {Tremaine}(1978)}]{1978-goldreich}
{Goldreich}, P., \& {Tremaine}, S. 1978, The Astrophysical Journal, 222, 850, \dodoi{10.1086/156203}

\bibitem[{{Goldreich} \& {Tremaine}(1979{\natexlab{a}})}]{1979-goldreich}
---. 1979{\natexlab{a}}, The Astrophysical Journal, 233, 857, \dodoi{10.1086/157448}

\bibitem[{{Goldreich} \& {Tremaine}(1979{\natexlab{b}})}]{goldreich-tremaine79}
---. 1979{\natexlab{b}}, \apj, 233, 857, \dodoi{10.1086/157448}

\bibitem[{{Goldreich} \& {Tremaine}(1980)}]{1980-goldreich}
---. 1980, The Astrophysical Journal, 241, 425, \dodoi{10.1086/158356}

\bibitem[{{Goodman} \& {Rafikov}(2001{\natexlab{a}})}]{goodman-rafikov01}
{Goodman}, J., \& {Rafikov}, R.~R. 2001{\natexlab{a}}, \apj, 552, 793, \dodoi{10.1086/320572}

\bibitem[{{Goodman} \& {Rafikov}(2001{\natexlab{b}})}]{goodman-rafikov2001}
---. 2001{\natexlab{b}}, \apj, 552, 793, \dodoi{10.1086/320572}

\bibitem[{{Grady} {et~al.}(1999){Grady}, {Woodgate}, {Bruhweiler}, {Boggess}, {Plait}, {Lindler}, {Clampin}, \& {Kalas}}]{grady1999-hst}
{Grady}, C.~A., {Woodgate}, B., {Bruhweiler}, F.~C., {et~al.} 1999, \apjl, 523, L151, \dodoi{10.1086/312270}

\bibitem[{{Griffin} {et~al.}(2010){Griffin}, {Abergel}, {Abreu}, {Ade}, {Andr{\'e}}, {Augueres}, {Babbedge}, {Bae}, {Baillie}, {Baluteau}, {Barlow}, {Bendo}, {Benielli}, {Bock}, {Bonhomme}, {Brisbin}, {Brockley-Blatt}, {Caldwell}, {Cara}, {Castro-Rodriguez}, {Cerulli}, {Chanial}, {Chen}, {Clark}, {Clements}, {Clerc}, {Coker}, {Communal}, {Conversi}, {Cox}, {Crumb}, {Cunningham}, {Daly}, {Davis}, {de Antoni}, {Delderfield}, {Devin}, {di Giorgio}, {Didschuns}, {Dohlen}, {Donati}, {Dowell}, {Dowell}, {Duband}, {Dumaye}, {Emery}, {Ferlet}, {Ferrand}, {Fontignie}, {Fox}, {Franceschini}, {Frerking}, {Fulton}, {Garcia}, {Gastaud}, {Gear}, {Glenn}, {Goizel}, {Griffin}, {Grundy}, {Guest}, {Guillemet}, {Hargrave}, {Harwit}, {Hastings}, {Hatziminaoglou}, {Herman}, {Hinde}, {Hristov}, {Huang}, {Imhof}, {Isaak}, {Israelsson}, {Ivison}, {Jennings}, {Kiernan}, {King}, {Lange}, {Latter}, {Laurent}, {Laurent}, {Leeks}, {Lellouch}, {Levenson}, {Li}, {Li}, {Lilienthal}, {Lim}, {Liu}, {Lu}, {Madden}, {Mainetti}, {Marliani},
  {McKay}, {Mercier}, {Molinari}, {Morris}, {Moseley}, {Mulder}, {Mur}, {Naylor}, {Nguyen}, {O'Halloran}, {Oliver}, {Olofsson}, {Olofsson}, {Orfei}, {Page}, {Pain}, {Panuzzo}, {Papageorgiou}, {Parks}, {Parr-Burman}, {Pearce}, {Pearson}, {P{\'e}rez-Fournon}, {Pinsard}, {Pisano}, {Podosek}, {Pohlen}, {Polehampton}, {Pouliquen}, {Rigopoulou}, {Rizzo}, {Roseboom}, {Roussel}, {Rowan-Robinson}, {Rownd}, {Saraceno}, {Sauvage}, {Savage}, {Savini}, {Sawyer}, {Scharmberg}, {Schmitt}, {Schneider}, {Schulz}, {Schwartz}, {Shafer}, {Shupe}, {Sibthorpe}, {Sidher}, {Smith}, {Smith}, {Smith}, {Spencer}, {Stobie}, {Sudiwala}, {Sukhatme}, {Surace}, {Stevens}, {Swinyard}, {Trichas}, {Tourette}, {Triou}, {Tseng}, {Tucker}, {Turner}, {Vaccari}, {Valtchanov}, {Vigroux}, {Virique}, {Voellmer}, {Walker}, {Ward}, {Waskett}, {Weilert}, {Wesson}, {White}, {Whitehouse}, {Wilson}, {Winter}, {Woodcraft}, {Wright}, {Xu}, {Zavagno}, {Zemcov}, {Zhang}, \& {Zonca}}]{griffin2010-spire}
{Griffin}, M.~J., {Abergel}, A., {Abreu}, A., {et~al.} 2010, \aap, 518, L3, \dodoi{10.1051/0004-6361/201014519}

\bibitem[{{Gupta} {et~al.}(2024){Gupta}, {Miotello}, {Williams}, {Birnstiel}, {Kuffmeier}, \& {Yen}}]{gupta2024-tipsy-hltau-scra}
{Gupta}, A., {Miotello}, A., {Williams}, J.~P., {et~al.} 2024, \aap, 683, A133, \dodoi{10.1051/0004-6361/202348007}

\bibitem[{{Gupta} {et~al.}(2023){Gupta}, {Miotello}, {Manara}, {Williams}, {Facchini}, {Beccari}, {Birnstiel}, {Ginski}, {Hacar}, {K{\"u}ffmeier}, {Testi}, {Tychoniec}, \& {Yen}}]{gupta2023-reflection-nebulae}
{Gupta}, A., {Miotello}, A., {Manara}, C.~F., {et~al.} 2023, \aap, 670, L8, \dodoi{10.1051/0004-6361/202245254}

\bibitem[{{Guzm{\'a}n-D{\'\i}az} {et~al.}(2021){Guzm{\'a}n-D{\'\i}az}, {Mendigut{\'\i}a}, {Montesinos}, {Oudmaijer}, {Vioque}, {Rodrigo}, {Solano}, {Meeus}, \& {Marcos-Arenal}}]{guzman-diaz2021-herbig-study}
{Guzm{\'a}n-D{\'\i}az}, J., {Mendigut{\'\i}a}, I., {Montesinos}, B., {et~al.} 2021, \aap, 650, A182, \dodoi{10.1051/0004-6361/202039519}

\bibitem[{{Haffert} {et~al.}(2019){Haffert}, {Bohn}, {de Boer}, {Snellen}, {Brinchmann}, {Girard}, {Keller}, \& {Bacon}}]{2019-haffert-PDS70}
{Haffert}, S.~Y., {Bohn}, A.~J., {de Boer}, J., {et~al.} 2019, Nature Astronomy, 3, 749, \dodoi{10.1038/s41550-019-0780-5}

\bibitem[{{Hall} {et~al.}(2019{\natexlab{a}}){Hall}, {Dong}, {Rice}, {Harries}, {Najita}, {Alexander}, \& {Brittain}}]{hall19-GI-spirals-ALMA}
{Hall}, C., {Dong}, R., {Rice}, K., {et~al.} 2019{\natexlab{a}}, \apj, 871, 228, \dodoi{10.3847/1538-4357/aafac2}

\bibitem[{{Hall} {et~al.}(2019{\natexlab{b}}){Hall}, {Dong}, {Rice}, {Harries}, {Najita}, {Alexander}, \& {Brittain}}]{hall2019-temporalGIspiralsALMA}
---. 2019{\natexlab{b}}, \apj, 871, 228, \dodoi{10.3847/1538-4357/aafac2}

\bibitem[{{Hall} {et~al.}(2016){Hall}, {Forgan}, {Rice}, {Harries}, {Klaassen}, \& {Biller}}]{hall2016-continuumGIspirals}
{Hall}, C., {Forgan}, D., {Rice}, K., {et~al.} 2016, \mnras, 458, 306, \dodoi{10.1093/mnras/stw296}

\bibitem[{{Hall} {et~al.}(2020){Hall}, {Dong}, {Teague}, {Terry}, {Pinte}, {Paneque-Carre{\~n}o}, {Veronesi}, {Alexander}, \& {Lodato}}]{hall2020}
{Hall}, C., {Dong}, R., {Teague}, R., {et~al.} 2020, \apj, 904, 148, \dodoi{10.3847/1538-4357/abac17}

\bibitem[{{Hanawa} {et~al.}(2024){Hanawa}, {Garufi}, {Podio}, {Codella}, \& {Segura-Cox}}]{hanawa2024-cloudlet-capture-DGtau}
{Hanawa}, T., {Garufi}, A., {Podio}, L., {Codella}, C., \& {Segura-Cox}, D. 2024, \mnras, 528, 6581, \dodoi{10.1093/mnras/stae338}

\bibitem[{{Harada} {et~al.}(2023){Harada}, {Tokuda}, {Yamasaki}, {Sato}, {Omura}, {Hirano}, {Onishi}, {Tachihara}, \& {Machida}}]{harada2023-DKCha}
{Harada}, N., {Tokuda}, K., {Yamasaki}, H., {et~al.} 2023, \apj, 945, 63, \dodoi{10.3847/1538-4357/acb930}

\bibitem[{Harris {et~al.}(2020)Harris, Millman, van~der Walt, Gommers, Virtanen, Cournapeau, Wieser, Taylor, Berg, Smith, Kern, Picus, Hoyer, van Kerkwijk, Brett, Haldane, del R{\'{i}}o, Wiebe, Peterson, G{\'{e}}rard-Marchant, Sheppard, Reddy, Weckesser, Abbasi, Gohlke, \& Oliphant}]{harris2020array}
Harris, C.~R., Millman, K.~J., van~der Walt, S.~J., {et~al.} 2020, Nature, 585, 357, \dodoi{10.1038/s41586-020-2649-2}

\bibitem[{{Harris} {et~al.}(2020){Harris}, {Millman}, {van der Walt}, {Gommers}, {Virtanen}, {Cournapeau}, {Wieser}, {Taylor}, {Berg}, {Smith}, {Kern}, {Picus}, {Hoyer}, {van Kerkwijk}, {Brett}, {Haldane}, {del R{\'\i}o}, {Wiebe}, {Peterson}, {G{\'e}rard-Marchant}, {Sheppard}, {Reddy}, {Weckesser}, {Abbasi}, {Gohlke}, \& {Oliphant}}]{software-numpy}
{Harris}, C.~R., {Millman}, K.~J., {van der Walt}, S.~J., {et~al.} 2020, \nat, 585, 357, \dodoi{10.1038/s41586-020-2649-2}

\bibitem[{{Harsono} {et~al.}(2011){Harsono}, {Alexander}, \& {Levin}}]{harsono2011-GI-infall}
{Harsono}, D., {Alexander}, R.~D., \& {Levin}, Y. 2011, \mnras, 413, 423, \dodoi{10.1111/j.1365-2966.2010.18146.x}

\bibitem[{{Hartmann} {et~al.}(1998){Hartmann}, {Calvet}, {Gullbring}, \& {D'Alessio}}]{hartmann1998}
{Hartmann}, L., {Calvet}, N., {Gullbring}, E., \& {D'Alessio}, P. 1998, \apj, 495, 385, \dodoi{10.1086/305277}

\bibitem[{{Hashimoto} {et~al.}(2011){Hashimoto}, {Tamura}, {Muto}, {Kudo}, {Fukagawa}, {Fukue}, {Goto}, {Grady}, {Henning}, {Hodapp}, {Honda}, {Inutsuka}, {Kokubo}, {Knapp}, {McElwain}, {Momose}, {Ohashi}, {Okamoto}, {Takami}, {Turner}, {Wisniewski}, {Janson}, {Abe}, {Brandner}, {Carson}, {Egner}, {Feldt}, {Golota}, {Guyon}, {Hayano}, {Hayashi}, {Hayashi}, {Ishii}, {Kandori}, {Kusakabe}, {Matsuo}, {Mayama}, {Miyama}, {Morino}, {Moro-Martin}, {Nishimura}, {Pyo}, {Suto}, {Suzuki}, {Takato}, {Terada}, {Thalmann}, {Tomono}, {Watanabe}, {Yamada}, {Takami}, \& {Usuda}}]{hashimoto2011}
{Hashimoto}, J., {Tamura}, M., {Muto}, T., {et~al.} 2011, \apjl, 729, L17, \dodoi{10.1088/2041-8205/729/2/L17}

\bibitem[{{Hennebelle} {et~al.}(2017){Hennebelle}, {Lesur}, \& {Fromang}}]{hennebelle2017-infall-spirals}
{Hennebelle}, P., {Lesur}, G., \& {Fromang}, S. 2017, \aap, 599, A86, \dodoi{10.1051/0004-6361/201629779}

\bibitem[{{Henning} {et~al.}(1998){Henning}, {Burkert}, {Launhardt}, {Leinert}, \& {Stecklum}}]{henning1998}
{Henning}, T., {Burkert}, A., {Launhardt}, R., {Leinert}, C., \& {Stecklum}, B. 1998, \aap, 336, 565

\bibitem[{{HGBS Team}(2020)}]{10.26131/irsa72}
{HGBS Team}. 2020, Herschel Gould Belt Survey,  IPAC, \dodoi{10.26131/IRSA72}

\bibitem[{{Hilder} {et~al.}(2023){Hilder}, {Fasano}, {Bollati}, \& {Vandenberg}}]{hilder2023-wakeflow-joss}
{Hilder}, T., {Fasano}, D., {Bollati}, F., \& {Vandenberg}, J. 2023, The Journal of Open Source Software, 8, 4863, \dodoi{10.21105/joss.04863}

\bibitem[{{Hillenbrand} {et~al.}(1992){Hillenbrand}, {Strom}, {Vrba}, \& {Keene}}]{hillenbrand1992-Teff}
{Hillenbrand}, L.~A., {Strom}, S.~E., {Vrba}, F.~J., \& {Keene}, J. 1992, \apj, 397, 613, \dodoi{10.1086/171819}

\bibitem[{{Holdaway}(1999)}]{holdaway1999}
{Holdaway}, M.~A. 1999, in Astronomical Society of the Pacific Conference Series, Vol. 180, Synthesis Imaging in Radio Astronomy II, ed. G.~B. {Taylor}, C.~L. {Carilli}, \& R.~A. {Perley}, 401

\bibitem[{{Huang} {et~al.}(2024){Huang}, {Bergin}, {Le Gal}, {Andrews}, {Bae}, {Keyte}, \& {Sturm}}]{huang2024-drtau-so}
{Huang}, J., {Bergin}, E.~A., {Le Gal}, R., {et~al.} 2024, arXiv e-prints, arXiv:2407.01679, \dodoi{10.48550/arXiv.2407.01679}

\bibitem[{{Huang} {et~al.}(2018{\natexlab{a}}){Huang}, {Andrews}, {Dullemond}, {Isella}, {P{\'e}rez}, {Guzm{\'a}n}, {{\"O}berg}, {Zhu}, {Zhang}, {Bai}, {Benisty}, {Birnstiel}, {Carpenter}, {Hughes}, {Ricci}, {Weaver}, \& {Wilner}}]{2018a-huang-dsharp2}
{Huang}, J., {Andrews}, S.~M., {Dullemond}, C.~P., {et~al.} 2018{\natexlab{a}}, \apjl, 869, L42, \dodoi{10.3847/2041-8213/aaf740}

\bibitem[{{Huang} {et~al.}(2018{\natexlab{b}}){Huang}, {Andrews}, {P{\'e}rez}, {Zhu}, {Dullemond}, {Isella}, {Benisty}, {Bai}, {Birnstiel}, {Carpenter}, {Guzm{\'a}n}, {Hughes}, {{\"O}berg}, {Ricci}, {Wilner}, \& {Zhang}}]{2018-huang-dsharp3-spirals}
{Huang}, J., {Andrews}, S.~M., {P{\'e}rez}, L.~M., {et~al.} 2018{\natexlab{b}}, \apjl, 869, L43, \dodoi{10.3847/2041-8213/aaf7a0}

\bibitem[{{Huang} {et~al.}(2018{\natexlab{c}}){Huang}, {Andrews}, {Cleeves}, {{\"O}berg}, {Wilner}, {Bai}, {Birnstiel}, {Carpenter}, {Hughes}, {Isella}, {P{\'e}rez}, {Ricci}, \& {Zhu}}]{huang18-twhya}
{Huang}, J., {Andrews}, S.~M., {Cleeves}, L.~I., {et~al.} 2018{\natexlab{c}}, \apj, 852, 122, \dodoi{10.3847/1538-4357/aaa1e7}

\bibitem[{{Huang} {et~al.}(2018{\natexlab{d}}){Huang}, {Andrews}, {Dullemond}, {Isella}, {P{\'e}rez}, {Guzm{\'a}n}, {{\"O}berg}, {Zhu}, {Zhang}, {Bai}, {Benisty}, {Birnstiel}, {Carpenter}, {Hughes}, {Ricci}, {Weaver}, \& {Wilner}}]{huang18-dsharp2}
{Huang}, J., {Andrews}, S.~M., {Dullemond}, C.~P., {et~al.} 2018{\natexlab{d}}, \apjl, 869, L42, \dodoi{10.3847/2041-8213/aaf740}

\bibitem[{{Huang} {et~al.}(2018{\natexlab{e}}){Huang}, {Andrews}, {P{\'e}rez}, {Zhu}, {Dullemond}, {Isella}, {Benisty}, {Bai}, {Birnstiel}, {Carpenter}, {Guzm{\'a}n}, {Hughes}, {{\"O}berg}, {Ricci}, {Wilner}, \& {Zhang}}]{huang18-dsharp3-spirals}
{Huang}, J., {Andrews}, S.~M., {P{\'e}rez}, L.~M., {et~al.} 2018{\natexlab{e}}, \apjl, 869, L43, \dodoi{10.3847/2041-8213/aaf7a0}

\bibitem[{{Huang} {et~al.}(2021){Huang}, {Bergin}, {{\"O}berg}, {Andrews}, {Teague}, {Law}, {Kalas}, {Aikawa}, {Bae}, {Bergner}, {Booth}, {Bosman}, {Calahan}, {Cataldi}, {Cleeves}, {Czekala}, {Ilee}, {Le Gal}, {Guzm{\'a}n}, {Long}, {Loomis}, {M{\'e}nard}, {Nomura}, {Qi}, {Schwarz}, {Tsukagoshi}, {van't Hoff}, {Walsh}, {Wilner}, {Yamato}, \& {Zhang}}]{huang2021-MAPS-GMAur}
{Huang}, J., {Bergin}, E.~A., {{\"O}berg}, K.~I., {et~al.} 2021, \apjs, 257, 19, \dodoi{10.3847/1538-4365/ac143e}

\bibitem[{Hunter(2007)}]{Hunter:2007}
Hunter, J.~D. 2007, Computing in Science \& Engineering, 9, 90, \dodoi{10.1109/MCSE.2007.55}

\bibitem[{{Hunter}(2007)}]{software-matplotlib}
{Hunter}, J.~D. 2007, Computing in Science and Engineering, 9, 90, \dodoi{10.1109/MCSE.2007.55}

\bibitem[{{Ilee} {et~al.}(2022){Ilee}, {Walsh}, {Jennings}, {Booth}, {Rosotti}, {Teague}, {Tsukagoshi}, \& {Nomura}}]{ilee22-twhya-deep}
{Ilee}, J.~D., {Walsh}, C., {Jennings}, J., {et~al.} 2022, \mnras, 515, L23, \dodoi{10.1093/mnrasl/slac048}

\bibitem[{{Izquierdo} {et~al.}(2022){Izquierdo}, {Facchini}, {Rosotti}, {van Dishoeck}, \& {Testi}}]{izquierdo22-hd163296}
{Izquierdo}, A.~F., {Facchini}, S., {Rosotti}, G.~P., {van Dishoeck}, E.~F., \& {Testi}, L. 2022, \apj, 928, 2, \dodoi{10.3847/1538-4357/ac474d}

\bibitem[{{Jennings} {et~al.}(2021){Jennings}, {Booth}, {Tazzari}, {Clarke}, \& {Rosotti}}]{2021-jennings-dsharp}
{Jennings}, J., {Booth}, R.~A., {Tazzari}, M., {Clarke}, C.~J., \& {Rosotti}, G.~P. 2021, arXiv e-prints, arXiv:2103.02392.
\newblock \doarXiv{2103.02392}

\bibitem[{{Jennings} {et~al.}(2022{\natexlab{a}}){Jennings}, {Booth}, {Tazzari}, {Clarke}, \& {Rosotti}}]{jennings22-frank-dsharp}
---. 2022{\natexlab{a}}, \mnras, 509, 2780, \dodoi{10.1093/mnras/stab3185}

\bibitem[{{Jennings} {et~al.}(2020{\natexlab{a}}){Jennings}, {Booth}, {Tazzari}, {Rosotti}, \& {Clarke}}]{2020-jennings-frank}
{Jennings}, J., {Booth}, R.~A., {Tazzari}, M., {Rosotti}, G.~P., \& {Clarke}, C.~J. 2020{\natexlab{a}}, \mnras, 495, 3209, \dodoi{10.1093/mnras/staa1365}

\bibitem[{{Jennings} {et~al.}(2020{\natexlab{b}}){Jennings}, {Booth}, {Tazzari}, {Rosotti}, \& {Clarke}}]{jennings20-frank}
---. 2020{\natexlab{b}}, \mnras, 495, 3209, \dodoi{10.1093/mnras/staa1365}

\bibitem[{{Jennings} {et~al.}(2022{\natexlab{b}}){Jennings}, {Tazzari}, {Clarke}, {Booth}, \& {Rosotti}}]{jennings22-frank-taurus}
{Jennings}, J., {Tazzari}, M., {Clarke}, C.~J., {Booth}, R.~A., \& {Rosotti}, G.~P. 2022{\natexlab{b}}, \mnras, 514, 6053, \dodoi{10.1093/mnras/stac1770}

\bibitem[{{Johansen} \& {Lambrechts}(2017)}]{johansen-lambrechts2017-review}
{Johansen}, A., \& {Lambrechts}, M. 2017, Annual Review of Earth and Planetary Sciences, 45, 359, \dodoi{10.1146/annurev-earth-063016-020226}

\bibitem[{{Jorsater} \& {van Moorsel}(1995)}]{JvM1995-correction}
{Jorsater}, S., \& {van Moorsel}, G.~A. 1995, \aj, 110, 2037, \dodoi{10.1086/117668}

\bibitem[{{Juh{\'a}sz} \& {Rosotti}(2018)}]{juhasz-rosotti18-pluto}
{Juh{\'a}sz}, A., \& {Rosotti}, G.~P. 2018, \mnras, 474, L32, \dodoi{10.1093/mnrasl/slx182}

\bibitem[{{Kanagawa} {et~al.}(2021){Kanagawa}, {Muto}, \& {Tanaka}}]{2021-kanagawa-footprint}
{Kanagawa}, K.~D., {Muto}, T., \& {Tanaka}, H. 2021, arXiv e-prints, arXiv:2109.09579.
\newblock \doarXiv{2109.09579}

\bibitem[{{Kataoka} {et~al.}(2015{\natexlab{a}}){Kataoka}, {Muto}, {Momose}, {Tsukagoshi}, {Fukagawa}, {Shibai}, {Hanawa}, {Murakawa}, \& {Dullemond}}]{2015-kataoka}
{Kataoka}, A., {Muto}, T., {Momose}, M., {et~al.} 2015{\natexlab{a}}, \apj, 809, 78, \dodoi{10.1088/0004-637X/809/1/78}

\bibitem[{{Kataoka} {et~al.}(2015{\natexlab{b}}){Kataoka}, {Muto}, {Momose}, {Tsukagoshi}, {Fukagawa}, {Shibai}, {Hanawa}, {Murakawa}, \& {Dullemond}}]{kataoka15-dustscattering}
---. 2015{\natexlab{b}}, \apj, 809, 78, \dodoi{10.1088/0004-637X/809/1/78}

\bibitem[{{Kepley} {et~al.}(2020){Kepley}, {Tsutsumi}, {Brogan}, {Indebetouw}, {Yoon}, {Mason}, \& {Donovan Meyer}}]{kepley2020-automultithresh}
{Kepley}, A.~A., {Tsutsumi}, T., {Brogan}, C.~L., {et~al.} 2020, \pasp, 132, 024505, \dodoi{10.1088/1538-3873/ab5e14}

\bibitem[{{Krapp} {et~al.}(2021){Krapp}, {Kratter}, \& {Youdin}}]{krapp-2021}
{Krapp}, L., {Kratter}, K.~M., \& {Youdin}, A.~N. 2021, arXiv e-prints, arXiv:2110.02428.
\newblock \doarXiv{2110.02428}

\bibitem[{{Kratter} \& {Lodato}(2016{\natexlab{a}})}]{kratter-lodato-2016}
{Kratter}, K., \& {Lodato}, G. 2016{\natexlab{a}}, \araa, 54, 271, \dodoi{10.1146/annurev-astro-081915-023307}

\bibitem[{{Kratter} \& {Lodato}(2016{\natexlab{b}})}]{kratter-lodato2016}
---. 2016{\natexlab{b}}, \araa, 54, 271, \dodoi{10.1146/annurev-astro-081915-023307}

\bibitem[{{Kraus} {et~al.}(2017){Kraus}, {Kreplin}, {Fukugawa}, {Muto}, {Sitko}, {Young}, {Bate}, {Grady}, {Harries}, {Monnier}, {Willson}, \& {Wisniewski}}]{2017-kraus-v1247}
{Kraus}, S., {Kreplin}, A., {Fukugawa}, M., {et~al.} 2017, \apjl, 848, L11, \dodoi{10.3847/2041-8213/aa8edc}

\bibitem[{{Kruegel}(2003)}]{kruegel2003}
{Kruegel}, E. 2003, {The physics of interstellar dust}, IoP Series in astronomy and astrophysics (Bristol, UK: The Institute of Physics)

\bibitem[{{Kuffmeier} {et~al.}(2021){Kuffmeier}, {Dullemond}, {Reissl}, \& {Goicovic}}]{kuffmeier2021-infall-misalignments}
{Kuffmeier}, M., {Dullemond}, C.~P., {Reissl}, S., \& {Goicovic}, F.~G. 2021, \aap, 656, A161, \dodoi{10.1051/0004-6361/202039614}

\bibitem[{{Kuffmeier} {et~al.}(2018){Kuffmeier}, {Frimann}, {Jensen}, \& {Haugb{\o}lle}}]{kuffmeier2018-infall-instabilities}
{Kuffmeier}, M., {Frimann}, S., {Jensen}, S.~S., \& {Haugb{\o}lle}, T. 2018, \mnras, 475, 2642, \dodoi{10.1093/mnras/sty024}

\bibitem[{{Kuffmeier} {et~al.}(2020){Kuffmeier}, {Goicovic}, \& {Dullemond}}]{kuffmeier2020-late-encounters}
{Kuffmeier}, M., {Goicovic}, F.~G., \& {Dullemond}, C.~P. 2020, \aap, 633, A3, \dodoi{10.1051/0004-6361/201936820}

\bibitem[{{Kuffmeier} {et~al.}(2023){Kuffmeier}, {Jensen}, \& {Haugb{\o}lle}}]{kuffmeier2023-rejuvenating-infall}
{Kuffmeier}, M., {Jensen}, S.~S., \& {Haugb{\o}lle}, T. 2023, European Physical Journal Plus, 138, 272, \dodoi{10.1140/epjp/s13360-023-03880-y}

\bibitem[{{Kuffmeier} {et~al.}(2024){Kuffmeier}, {Pineda}, {Segura-Cox}, \& {Haugb{\o}lle}}]{kuffmeier2024-reorientation}
{Kuffmeier}, M., {Pineda}, J.~E., {Segura-Cox}, D., \& {Haugb{\o}lle}, T. 2024, arXiv e-prints, arXiv:2405.12670, \dodoi{10.48550/arXiv.2405.12670}

\bibitem[{{Kurtovic} {et~al.}(2018){Kurtovic}, {P{\'e}rez}, {Benisty}, {Zhu}, {Zhang}, {Huang}, {Andrews}, {Dullemond}, {Isella}, {Bai}, {Carpenter}, {Guzm{\'a}n}, {Ricci}, \& {Wilner}}]{2018-kurtovic-dsharp4}
{Kurtovic}, N.~T., {P{\'e}rez}, L.~M., {Benisty}, M., {et~al.} 2018, \apjl, 869, L44, \dodoi{10.3847/2041-8213/aaf746}

\bibitem[{{Kuznetsova} {et~al.}(2022){Kuznetsova}, {Bae}, {Hartmann}, \& {Mac Low}}]{kuznetsova2022-infall-pressurebumps-vortices}
{Kuznetsova}, A., {Bae}, J., {Hartmann}, L., \& {Mac Low}, M.-M. 2022, \apj, 928, 92, \dodoi{10.3847/1538-4357/ac54a8}

\bibitem[{{Law} {et~al.}(2021){Law}, {Teague}, {Loomis}, {Bae}, {{\"O}berg}, {Czekala}, {Andrews}, {Aikawa}, {Alarc{\'o}n}, {Bergin}, {Bergner}, {Booth}, {Bosman}, {Calahan}, {Cataldi}, {Cleeves}, {Furuya}, {Guzm{\'a}n}, {Huang}, {Ilee}, {Le Gal}, {Liu}, {Long}, {M{\'e}nard}, {Nomura}, {P{\'e}rez}, {Qi}, {Schwarz}, {Soto}, {Tsukagoshi}, {Yamato}, {van't Hoff}, {Walsh}, {Wilner}, \& {Zhang}}]{law21-maps4-emissionsurfaces}
{Law}, C.~J., {Teague}, R., {Loomis}, R.~A., {et~al.} 2021, \apjs, 257, 4, \dodoi{10.3847/1538-4365/ac1439}

\bibitem[{{Leroy} {et~al.}(2021){Leroy}, {Hughes}, {Liu}, {Pety}, {Rosolowsky}, {Saito}, {Schinnerer}, {Schruba}, {Usero}, {Faesi}, {Herrera}, {Chevance}, {Hygate}, {Kepley}, {Koch}, {Querejeta}, {Sliwa}, {Will}, {Wilson}, {Anand}, {Barnes}, {Belfiore}, {Be{\v{s}}li{\'c}}, {Bigiel}, {Blanc}, {Bolatto}, {Boquien}, {Cao}, {Chandar}, {Chastenet}, {Chiang}, {Congiu}, {Dale}, {Deger}, {den Brok}, {Eibensteiner}, {Emsellem}, {Garc{\'\i}a-Rodr{\'\i}guez}, {Glover}, {Grasha}, {Groves}, {Henshaw}, {Jim{\'e}nez Donaire}, {Kim}, {Klessen}, {Kreckel}, {Kruijssen}, {Larson}, {Lee}, {Mayker}, {McElroy}, {Meidt}, {Mok}, {Pan}, {Puschnig}, {Razza}, {S{\'a}nchez-Bl'azquez}, {Sandstrom}, {Santoro}, {Sardone}, {Scheuermann}, {Sun}, {Thilker}, {Turner}, {Ubeda}, {Utomo}, {Watkins}, \& {Williams}}]{leroy2021-phangsalma}
{Leroy}, A.~K., {Hughes}, A., {Liu}, D., {et~al.} 2021, \apjs, 255, 19, \dodoi{10.3847/1538-4365/abec80}

\bibitem[{{Lesur} {et~al.}(2015){Lesur}, {Hennebelle}, \& {Fromang}}]{lesur2015-spiral-accretion}
{Lesur}, G., {Hennebelle}, P., \& {Fromang}, S. 2015, \aap, 582, L9, \dodoi{10.1051/0004-6361/201526734}

\bibitem[{{Li} {et~al.}(2016){Li}, {Pantin}, {Telesco}, {Zhang}, {Wright}, {Barnes}, {Packham}, \& {Mari{\~n}as}}]{li2016-rstar}
{Li}, D., {Pantin}, E., {Telesco}, C.~M., {et~al.} 2016, \apj, 832, 18, \dodoi{10.3847/0004-637X/832/1/18}

\bibitem[{{Lin} {et~al.}(2006){Lin}, {Ohashi}, {Lim}, {Ho}, {Fukagawa}, \& {Tamura}}]{lin2006-possible-molecular-spiralarms}
{Lin}, S.-Y., {Ohashi}, N., {Lim}, J., {et~al.} 2006, \apj, 645, 1297, \dodoi{10.1086/504368}

\bibitem[{{Liu} \& {Ji}(2020)}]{liu-ji-2020-review}
{Liu}, B., \& {Ji}, J. 2020, Research in Astronomy and Astrophysics, 20, 164, \dodoi{10.1088/1674-4527/20/10/164}

\bibitem[{{Liu}(2019)}]{2019-liu}
{Liu}, H.~B. 2019, \apjl, 877, L22, \dodoi{10.3847/2041-8213/ab1f8e}

\bibitem[{{Lodato}(2008)}]{lodato2008}
{Lodato}, G. 2008, New Astronomy Reviews, 52, 21, \dodoi{10.1016/j.newar.2008.04.002}

\bibitem[{{Lodato} \& {Rice}(2004)}]{lodato-rice-2004}
{Lodato}, G., \& {Rice}, W.~K.~M. 2004, \mnras, 351, 630, \dodoi{10.1111/j.1365-2966.2004.07811.x}

\bibitem[{{Lodato} \& {Rice}(2005)}]{lodato-rice-2005}
---. 2005, \mnras, 358, 1489, \dodoi{10.1111/j.1365-2966.2005.08875.x}

\bibitem[{{Lodato} {et~al.}(2019){Lodato}, {Dipierro}, {Ragusa}, {Long}, {Herczeg}, {Pascucci}, {Pinilla}, {Manara}, {Tazzari}, {Liu}, {Mulders}, {Harsono}, {Boehler}, {M{\'e}nard}, {Johnstone}, {Salyk}, {van der Plas}, {Cabrit}, {Edwards}, {Fischer}, {Hendler}, {Nisini}, {Rigliaco}, {Avenhaus}, {Banzatti}, \& {Gully-Santiago}}]{lodato19-newbornplanets-dustgaps}
{Lodato}, G., {Dipierro}, G., {Ragusa}, E., {et~al.} 2019, \mnras, 486, 453, \dodoi{10.1093/mnras/stz913}

\bibitem[{{Lodato} {et~al.}(2023){Lodato}, {Rampinelli}, {Viscardi}, {Longarini}, {Izquierdo}, {Paneque-Carre{\~n}o}, {Testi}, {Facchini}, {Miotello}, {Veronesi}, \& {Hall}}]{lodato2023-gmlup-imlup}
{Lodato}, G., {Rampinelli}, L., {Viscardi}, E., {et~al.} 2023, \mnras, 518, 4481, \dodoi{10.1093/mnras/stac3223}

\bibitem[{{Longarini} {et~al.}(2023){Longarini}, {Armitage}, {Lodato}, {Price}, \& {Ceppi}}]{longarini2023b}
{Longarini}, C., {Armitage}, P.~J., {Lodato}, G., {Price}, D.~J., \& {Ceppi}, S. 2023, \mnras, 522, 6217, \dodoi{10.1093/mnras/stad1400}

\bibitem[{{Longarini} {et~al.}(2021{\natexlab{a}}){Longarini}, {Lodato}, {Toci}, {Veronesi}, {Hall}, {Dong}, \& {Patrick Terry}}]{longarini2021}
{Longarini}, C., {Lodato}, G., {Toci}, C., {et~al.} 2021{\natexlab{a}}, \apjl, 920, L41, \dodoi{10.3847/2041-8213/ac2df6}

\bibitem[{{Longarini} {et~al.}(2021{\natexlab{b}}){Longarini}, {Lodato}, {Toci}, {Veronesi}, {Hall}, {Dong}, \& {Terry}}]{2021-longarini-privatecomm}
---. 2021{\natexlab{b}}, arXiv e-prints, arXiv:2108.11387.
\newblock \doarXiv{2108.11387}

\bibitem[{{Luhman}(2023)}]{luhman2023-taurus-gaia}
{Luhman}, K.~L. 2023, \aj, 165, 37, \dodoi{10.3847/1538-3881/ac9da3}

\bibitem[{{Martire} {et~al.}(2024){Martire}, {Longarini}, {Lodato}, {Rosotti}, {Winter}, {Facchini}, {Hardiman}, {Benisty}, {Stadler}, {Izquierdo}, \& {Testi}}]{martire2024-maps}
{Martire}, P., {Longarini}, C., {Lodato}, G., {et~al.} 2024, \aap, 686, A9, \dodoi{10.1051/0004-6361/202348546}

\bibitem[{{Mathis} {et~al.}(1977){Mathis}, {Rumpl}, \& {Nordsieck}}]{mathis1977}
{Mathis}, J.~S., {Rumpl}, W., \& {Nordsieck}, K.~H. 1977, \apj, 217, 425, \dodoi{10.1086/155591}

\bibitem[{{Mawet} {et~al.}(2012){Mawet}, {Absil}, {Montagnier}, {Riaud}, {Surdej}, {Ducourant}, {Augereau}, {R{\"o}ttinger}, {Girard}, {Krist}, \& {Stapelfeldt}}]{2012-mawet-imlup}
{Mawet}, D., {Absil}, O., {Montagnier}, G., {et~al.} 2012, \aap, 544, A131, \dodoi{10.1051/0004-6361/201219662}

\bibitem[{{McKinney}(2011)}]{2011-mckinney-pandas}
{McKinney}, W. 2011, Python for High Performance and Scientific Computing, 14, 1

\bibitem[{{McMullin} {et~al.}(2007{\natexlab{a}}){McMullin}, {Waters}, {Schiebel}, {Young}, \& {Golap}}]{2007-mcmullin-casa}
{McMullin}, J.~P., {Waters}, B., {Schiebel}, D., {Young}, W., \& {Golap}, K. 2007{\natexlab{a}}, in Astronomical Society of the Pacific Conference Series, Vol. 376, Astronomical Data Analysis Software and Systems XVI, ed. R.~A. {Shaw}, F.~{Hill}, \& D.~J. {Bell}, 127

\bibitem[{{McMullin} {et~al.}(2007{\natexlab{b}}){McMullin}, {Waters}, {Schiebel}, {Young}, \& {Golap}}]{mcmullin2007-casa}
---. 2007{\natexlab{b}}, in Astronomical Society of the Pacific Conference Series, Vol. 376, Astronomical Data Analysis Software and Systems XVI, ed. R.~A. {Shaw}, F.~{Hill}, \& D.~J. {Bell}, 127

\bibitem[{{McNally} {et~al.}(2019){McNally}, {Nelson}, {Paardekooper}, \& {Ben{\'\i}tez-Llambay}}]{2019-mcnally}
{McNally}, C.~P., {Nelson}, R.~P., {Paardekooper}, S.-J., \& {Ben{\'\i}tez-Llambay}, P. 2019, \mnras, 484, 728, \dodoi{10.1093/mnras/stz023}

\bibitem[{{Mendoza} {et~al.}(2009){Mendoza}, {Tejeda}, \& {Nagel}}]{mendoza2009}
{Mendoza}, S., {Tejeda}, E., \& {Nagel}, E. 2009, \mnras, 393, 579, \dodoi{10.1111/j.1365-2966.2008.14210.x}

\bibitem[{{Meru} {et~al.}(2017{\natexlab{a}}){Meru}, {Juh{\'a}sz}, {Ilee}, {Clarke}, {Rosotti}, \& {Booth}}]{2017-meru-elias227}
{Meru}, F., {Juh{\'a}sz}, A., {Ilee}, J.~D., {et~al.} 2017{\natexlab{a}}, \apjl, 839, L24, \dodoi{10.3847/2041-8213/aa6837}

\bibitem[{{Meru} {et~al.}(2017{\natexlab{b}}){Meru}, {Juh{\'a}sz}, {Ilee}, {Clarke}, {Rosotti}, \& {Booth}}]{meru17-elias27}
---. 2017{\natexlab{b}}, \apjl, 839, L24, \dodoi{10.3847/2041-8213/aa6837}

\bibitem[{{Meru} {et~al.}(2017{\natexlab{c}}){Meru}, {Juh{\'a}sz}, {Ilee}, {Clarke}, {Rosotti}, \& {Booth}}]{meru2017-elias27}
---. 2017{\natexlab{c}}, \apjl, 839, L24, \dodoi{10.3847/2041-8213/aa6837}

\bibitem[{{Meru} {et~al.}(2019){Meru}, {Rosotti}, {Booth}, {Nazari}, \& {Clarke}}]{2019-meru-insideout}
{Meru}, F., {Rosotti}, G.~P., {Booth}, R.~A., {Nazari}, P., \& {Clarke}, C.~J. 2019, \mnras, 482, 3678, \dodoi{10.1093/mnras/sty2847}

\bibitem[{{Miranda} \& {Rafikov}(2019{\natexlab{a}})}]{2019-miranda-rafikov}
{Miranda}, R., \& {Rafikov}, R.~R. 2019{\natexlab{a}}, \apj, 875, 37, \dodoi{10.3847/1538-4357/ab0f9e}

\bibitem[{{Miranda} \& {Rafikov}(2019{\natexlab{b}})}]{2019-miranda-rafikov-planet-interpretation}
---. 2019{\natexlab{b}}, \apjl, 878, L9, \dodoi{10.3847/2041-8213/ab22a7}

\bibitem[{{Miranda} \& {Rafikov}(2020{\natexlab{a}})}]{2020b-miranda-rafikov}
---. 2020{\natexlab{a}}, \apj, 904, 121, \dodoi{10.3847/1538-4357/abbee7}

\bibitem[{{Miranda} \& {Rafikov}(2020{\natexlab{b}})}]{2020a-miranda-rafikov}
---. 2020{\natexlab{b}}, \apj, 892, 65, \dodoi{10.3847/1538-4357/ab791a}

\bibitem[{{Miranda} \& {Rafikov}(2020{\natexlab{c}})}]{miranda-rafikov20-cooling-basictheory}
---. 2020{\natexlab{c}}, \apj, 892, 65, \dodoi{10.3847/1538-4357/ab791a}

\bibitem[{{Miura} {et~al.}(2017){Miura}, {Yamamoto}, {Nomura}, {Nakamoto}, {Tanaka}, {Tanaka}, \& {Nagasawa}}]{miura2017-desorption-SO}
{Miura}, H., {Yamamoto}, T., {Nomura}, H., {et~al.} 2017, \apj, 839, 47, \dodoi{10.3847/1538-4357/aa67df}

\bibitem[{{Monsch} {et~al.}(2024){Monsch}, {Lovell}, {Berghea}, {Edenhofer}, {Keating}, {Andrews}, {Bayyari}, {Drake}, \& {Wilner}}]{monsch2024-dracula}
{Monsch}, K., {Lovell}, J.~B., {Berghea}, C.~T., {et~al.} 2024, \apjl, 967, L2, \dodoi{10.3847/2041-8213/ad3bb0}

\bibitem[{{Mori} {et~al.}(2024){Mori}, {Aikawa}, {Oya}, {Yamamoto}, \& {Sakai}}]{mori2024}
{Mori}, S., {Aikawa}, Y., {Oya}, Y., {Yamamoto}, S., \& {Sakai}, N. 2024, \apj, 961, 31, \dodoi{10.3847/1538-4357/ad0634}

\bibitem[{{Muley} {et~al.}(2021){Muley}, {Dong}, \& {Fung}}]{2021-muley}
{Muley}, D., {Dong}, R., \& {Fung}, J. 2021, arXiv e-prints, arXiv:2107.06323.
\newblock \doarXiv{2107.06323}

\bibitem[{{Muto} {et~al.}(2012){Muto}, {Grady}, {Hashimoto}, {Fukagawa}, {Hornbeck}, {Sitko}, {Russell}, {Werren}, {Cur{\'e}}, {Currie}, {Ohashi}, {Okamoto}, {Momose}, {Honda}, {Inutsuka}, {Takeuchi}, {Dong}, {Abe}, {Brandner}, {Brandt}, {Carson}, {Egner}, {Feldt}, {Fukue}, {Goto}, {Guyon}, {Hayano}, {Hayashi}, {Hayashi}, {Henning}, {Hodapp}, {Ishii}, {Iye}, {Janson}, {Kandori}, {Knapp}, {Kudo}, {Kusakabe}, {Kuzuhara}, {Matsuo}, {Mayama}, {McElwain}, {Miyama}, {Morino}, {Moro-Martin}, {Nishimura}, {Pyo}, {Serabyn}, {Suto}, {Suzuki}, {Takami}, {Takato}, {Terada}, {Thalmann}, {Tomono}, {Turner}, {Watanabe}, {Wisniewski}, {Yamada}, {Takami}, {Usuda}, \& {Tamura}}]{muto12-spirals-hd135344B}
{Muto}, T., {Grady}, C.~A., {Hashimoto}, J., {et~al.} 2012, \apjl, 748, L22, \dodoi{10.1088/2041-8205/748/2/L22}

\bibitem[{{Nakajima} \& {Golimowski}(1995)}]{nakajima-golimowski1995-palomar}
{Nakajima}, T., \& {Golimowski}, D.~A. 1995, \aj, 109, 1181, \dodoi{10.1086/117351}

\bibitem[{{Natta} {et~al.}(2001){Natta}, {Prusti}, {Neri}, {Wooden}, {Grinin}, \& {Mannings}}]{natta2001-Teff}
{Natta}, A., {Prusti}, T., {Neri}, R., {et~al.} 2001, \aap, 371, 186, \dodoi{10.1051/0004-6361:20010334}

\bibitem[{{Nayakshin} {et~al.}(2020){Nayakshin}, {Tsukagoshi}, {Hall}, {Vazan}, {Helled}, {Humphries}, {Meru}, {Neunteufel}, \& {Panic}}]{nayakshin20-twhya}
{Nayakshin}, S., {Tsukagoshi}, T., {Hall}, C., {et~al.} 2020, \mnras, 495, 285, \dodoi{10.1093/mnras/staa1132}

\bibitem[{{Nazari} {et~al.}(2019){Nazari}, {Booth}, {Clarke}, {Rosotti}, {Tazzari}, {Juhasz}, \& {Meru}}]{2019-nazari}
{Nazari}, P., {Booth}, R.~A., {Clarke}, C.~J., {et~al.} 2019, \mnras, 485, 5914, \dodoi{10.1093/mnras/stz836}

\bibitem[{{Newton}(1687)}]{newton1687}
{Newton}, I. 1687, {Philosophiae Naturalis Principia Mathematica.}, \dodoi{10.3931/e-rara-440}

\bibitem[{{Norfolk} {et~al.}(2022{\natexlab{a}}){Norfolk}, {Pinte}, {Calcino}, {Hammond}, {van der Marel}, {Price}, {Maddison}, {Christiaens}, {Gonzalez}, {Blakely}, {Rosotti}, \& {Ginski}}]{norfolk22-hd100546}
{Norfolk}, B.~J., {Pinte}, C., {Calcino}, J., {et~al.} 2022{\natexlab{a}}, arXiv e-prints, arXiv:2208.02542.
\newblock \doarXiv{2208.02542}

\bibitem[{{Norfolk} {et~al.}(2022{\natexlab{b}}){Norfolk}, {Pinte}, {Calcino}, {Hammond}, {van der Marel}, {Price}, {Maddison}, {Christiaens}, {Gonzalez}, {Blakely}, {Rosotti}, \& {Ginski}}]{norfolk2022-hd100546}
---. 2022{\natexlab{b}}, \apjl, 936, L4, \dodoi{10.3847/2041-8213/ac85ed}

\bibitem[{{Ogilvie} \& {Lubow}(2002{\natexlab{a}})}]{2002-ogilvie}
{Ogilvie}, G.~I., \& {Lubow}, S.~H. 2002{\natexlab{a}}, \mnras, 330, 950, \dodoi{10.1046/j.1365-8711.2002.05148.x}

\bibitem[{{Ogilvie} \& {Lubow}(2002{\natexlab{b}})}]{ogilvie-lubow2002}
---. 2002{\natexlab{b}}, \mnras, 330, 950, \dodoi{10.1046/j.1365-8711.2002.05148.x}

\bibitem[{{Oppenheimer} {et~al.}(2008){Oppenheimer}, {Brenner}, {Hinkley}, {Zimmerman}, {Sivaramakrishnan}, {Soummer}, {Kuhn}, {Graham}, {Perrin}, {Lloyd}, {Roberts}, \& {Harrington}}]{oppenheimer2008-abaur}
{Oppenheimer}, B.~R., {Brenner}, D., {Hinkley}, S., {et~al.} 2008, \apj, 679, 1574, \dodoi{10.1086/587778}

\bibitem[{{Ormel}(2017)}]{ormel2017-review}
{Ormel}, C.~W. 2017, in Astrophysics and Space Science Library, Vol. 445, Formation, Evolution, and Dynamics of Young Solar Systems, ed. M.~{Pessah} \& O.~{Gressel}, 197, \dodoi{10.1007/978-3-319-60609-5_7}

\bibitem[{{Oya} {et~al.}(2016){Oya}, {Sakai}, {L{\'o}pez-Sepulcre}, {Watanabe}, {Ceccarelli}, {Lefloch}, {Favre}, \& {Yamamoto}}]{oya2016}
{Oya}, Y., {Sakai}, N., {L{\'o}pez-Sepulcre}, A., {et~al.} 2016, \apj, 824, 88, \dodoi{10.3847/0004-637X/824/2/88}

\bibitem[{{Pacheco-V{\'a}zquez} {et~al.}(2016){Pacheco-V{\'a}zquez}, {Fuente}, {Baruteau}, {Bern{\'e}}, {Ag{\'u}ndez}, {Neri}, {Goicoechea}, {Cernicharo}, \& {Bachiller}}]{pacheco-vazquez2016-SO}
{Pacheco-V{\'a}zquez}, S., {Fuente}, A., {Baruteau}, C., {et~al.} 2016, \aap, 589, A60, \dodoi{10.1051/0004-6361/201527089}

\bibitem[{{Paneque-Carre{\~n}o} {et~al.}(2022){Paneque-Carre{\~n}o}, {Miotello}, {van Dishoeck}, {Tabone}, {Izquierdo}, \& {Facchini}}]{paneque-carreno22-vertical-stratification}
{Paneque-Carre{\~n}o}, T., {Miotello}, A., {van Dishoeck}, E.~F., {et~al.} 2022, arXiv e-prints, arXiv:2210.01130.
\newblock \doarXiv{2210.01130}

\bibitem[{{Paneque-Carre{\~n}o} {et~al.}(2021{\natexlab{a}}){Paneque-Carre{\~n}o}, {P{\'e}rez}, {Benisty}, {Hall}, {Veronesi}, {Lodato}, {Sierra}, {Carpenter}, {Andrews}, {Bae}, {Henning}, {Kwon}, {Linz}, {Loinard}, {Pinte}, {Ricci}, {Tazzari}, {Testi}, \& {Wilner}}]{2021-paneque-carreno-elias227}
{Paneque-Carre{\~n}o}, T., {P{\'e}rez}, L.~M., {Benisty}, M., {et~al.} 2021{\natexlab{a}}, \apj, 914, 88, \dodoi{10.3847/1538-4357/abf243}

\bibitem[{{Paneque-Carre{\~n}o} {et~al.}(2021{\natexlab{b}}){Paneque-Carre{\~n}o}, {P{\'e}rez}, {Benisty}, {Hall}, {Veronesi}, {Lodato}, {Sierra}, {Carpenter}, {Andrews}, {Bae}, {Henning}, {Kwon}, {Linz}, {Loinard}, {Pinte}, {Ricci}, {Tazzari}, {Testi}, \& {Wilner}}]{paneque-carreno21-elias27-GI}
---. 2021{\natexlab{b}}, \apj, 914, 88, \dodoi{10.3847/1538-4357/abf243}

\bibitem[{{Paneque-Carre{\~n}o} {et~al.}(2021{\natexlab{c}}){Paneque-Carre{\~n}o}, {P{\'e}rez}, {Benisty}, {Hall}, {Veronesi}, {Lodato}, {Sierra}, {Carpenter}, {Andrews}, {Bae}, {Henning}, {Kwon}, {Linz}, {Loinard}, {Pinte}, {Ricci}, {Tazzari}, {Testi}, \& {Wilner}}]{panequecarreno2021-elias27}
---. 2021{\natexlab{c}}, \apj, 914, 88, \dodoi{10.3847/1538-4357/abf243}

\bibitem[{{Paneque-Carre{\~n}o} {et~al.}(2021{\natexlab{d}}){Paneque-Carre{\~n}o}, {P{\'e}rez}, {Benisty}, {Hall}, {Veronesi}, {Lodato}, {Sierra}, {Carpenter}, {Andrews}, {Bae}, {Henning}, {Kwon}, {Linz}, {Loinard}, {Pinte}, {Ricci}, {Tazzari}, {Testi}, \& {Wilner}}]{paneque2021-elias27}
---. 2021{\natexlab{d}}, \apj, 914, 88, \dodoi{10.3847/1538-4357/abf243}

\bibitem[{{Pavlyuchenkov} {et~al.}(2019{\natexlab{a}}){Pavlyuchenkov}, {Akimkin}, {Wiebe}, \& {Vorobyov}}]{2019-pavlyuchenkov}
{Pavlyuchenkov}, Y., {Akimkin}, V., {Wiebe}, D., \& {Vorobyov}, E. 2019{\natexlab{a}}, \mnras, 486, 3907, \dodoi{10.1093/mnras/stz1046}

\bibitem[{{Pavlyuchenkov} {et~al.}(2019{\natexlab{b}}){Pavlyuchenkov}, {Akimkin}, {Wiebe}, \& {Vorobyov}}]{pavlyuchenkov19-spectralindex}
---. 2019{\natexlab{b}}, \mnras, 486, 3907, \dodoi{10.1093/mnras/stz1046}

\bibitem[{{Pelkonen} {et~al.}(2024){Pelkonen}, {Padoan}, {Juvela}, {Haugb{\o}lle}, \& {Nordlund}}]{pelkonen2024-BHL}
{Pelkonen}, V.-M., {Padoan}, P., {Juvela}, M., {Haugb{\o}lle}, T., \& {Nordlund}, {\r{A}}. 2024, arXiv e-prints, arXiv:2405.06520, \dodoi{10.48550/arXiv.2405.06520}

\bibitem[{{P{\'e}rez} {et~al.}(2016{\natexlab{a}}){P{\'e}rez}, {Carpenter}, {Andrews}, {Ricci}, {Isella}, {Linz}, {Sargent}, {Wilner}, {Henning}, {Deller}, {Chandler}, {Dullemond}, {Lazio}, {Menten}, {Corder}, {Storm}, {Testi}, {Tazzari}, {Kwon}, {Calvet}, {Greaves}, {Harris}, \& {Mundy}}]{perez16-elias27}
{P{\'e}rez}, L.~M., {Carpenter}, J.~M., {Andrews}, S.~M., {et~al.} 2016{\natexlab{a}}, Science, 353, 1519, \dodoi{10.1126/science.aaf8296}

\bibitem[{{P{\'e}rez} {et~al.}(2016{\natexlab{b}}){P{\'e}rez}, {Carpenter}, {Andrews}, {Ricci}, {Isella}, {Linz}, {Sargent}, {Wilner}, {Henning}, {Deller}, {Chandler}, {Dullemond}, {Lazio}, {Menten}, {Corder}, {Storm}, {Testi}, {Tazzari}, {Kwon}, {Calvet}, {Greaves}, {Harris}, \& {Mundy}}]{perez2016-elias27}
---. 2016{\natexlab{b}}, Science, 353, 1519, \dodoi{10.1126/science.aaf8296}

\bibitem[{{P{\'e}rez} {et~al.}(2018){P{\'e}rez}, {Benisty}, {Andrews}, {Isella}, {Dullemond}, {Huang}, {Kurtovic}, {Guzm{\'a}n}, {Zhu}, {Birnstiel}, {Zhang}, {Carpenter}, {Wilner}, {Ricci}, {Bai}, {Weaver}, \& {{\"O}berg}}]{perezL18-hd143006}
{P{\'e}rez}, L.~M., {Benisty}, M., {Andrews}, S.~M., {et~al.} 2018, \apjl, 869, L50, \dodoi{10.3847/2041-8213/aaf745}

\bibitem[{{P{\'e}rez} {et~al.}(2019){P{\'e}rez}, {Casassus}, {Baruteau}, {Dong}, {Hales}, \& {Cieza}}]{2019-perez-mininep}
{P{\'e}rez}, S., {Casassus}, S., {Baruteau}, C., {et~al.} 2019, \aj, 158, 15, \dodoi{10.3847/1538-3881/ab1f88}

\bibitem[{{P{\'e}rez} {et~al.}(2020){P{\'e}rez}, {Casassus}, {Hales}, {Marino}, {Cheetham}, {Zurlo}, {Cieza}, {Dong}, {Alarc{\'o}n}, {Ben{\'\i}tez-Llambay}, {Fomalont}, \& {Avenhaus}}]{perez20-hd100546}
{P{\'e}rez}, S., {Casassus}, S., {Hales}, A., {et~al.} 2020, \apjl, 889, L24, \dodoi{10.3847/2041-8213/ab6b2b}

\bibitem[{{Perrin} {et~al.}(2009){Perrin}, {Schneider}, {Duchene}, {Pinte}, {Grady}, {Wisniewski}, \& {Hines}}]{perrin2009}
{Perrin}, M.~D., {Schneider}, G., {Duchene}, G., {et~al.} 2009, \apjl, 707, L132, \dodoi{10.1088/0004-637X/707/2/L132}

\bibitem[{{Pi{\'e}tu} {et~al.}(2005){Pi{\'e}tu}, {Guilloteau}, \& {Dutrey}}]{pietu2005}
{Pi{\'e}tu}, V., {Guilloteau}, S., \& {Dutrey}, A. 2005, \aap, 443, 945, \dodoi{10.1051/0004-6361:20042050}

\bibitem[{{Pilbratt} {et~al.}(2010){Pilbratt}, {Riedinger}, {Passvogel}, {Crone}, {Doyle}, {Gageur}, {Heras}, {Jewell}, {Metcalfe}, {Ott}, \& {Schmidt}}]{pilbratt2010-herschel}
{Pilbratt}, G.~L., {Riedinger}, J.~R., {Passvogel}, T., {et~al.} 2010, \aap, 518, L1, \dodoi{10.1051/0004-6361/201014759}

\bibitem[{{Pineda} {et~al.}(2020){Pineda}, {Segura-Cox}, {Caselli}, {Cunningham}, {Zhao}, {Schmiedeke}, {Maureira}, \& {Neri}}]{pineda2020-natast}
{Pineda}, J.~E., {Segura-Cox}, D., {Caselli}, P., {et~al.} 2020, Nature Astronomy, 4, 1158, \dodoi{10.1038/s41550-020-1150-z}

\bibitem[{{Pineda} {et~al.}(2023){Pineda}, {Arzoumanian}, {Andre}, {Friesen}, {Zavagno}, {Clarke}, {Inoue}, {Chen}, {Lee}, {Soler}, \& {Kuffmeier}}]{pineda2023-ppvii}
{Pineda}, J.~E., {Arzoumanian}, D., {Andre}, P., {et~al.} 2023, in Astronomical Society of the Pacific Conference Series, Vol. 534, Protostars and Planets VII, ed. S.~{Inutsuka}, Y.~{Aikawa}, T.~{Muto}, K.~{Tomida}, \& M.~{Tamura}, 233, \dodoi{10.48550/arXiv.2205.03935}

\bibitem[{{Pinte} {et~al.}(2009){Pinte}, {Harries}, {Min}, {Watson}, {Dullemond}, {Woitke}, {M{\'e}nard}, \& {Dur{\'a}n-Rojas}}]{pinte2009}
{Pinte}, C., {Harries}, T.~J., {Min}, M., {et~al.} 2009, \aap, 498, 967, \dodoi{10.1051/0004-6361/200811555}

\bibitem[{{Pinte} {et~al.}(2006){Pinte}, {M{\'e}nard}, {Duch{\^e}ne}, \& {Bastien}}]{pinte2006}
{Pinte}, C., {M{\'e}nard}, F., {Duch{\^e}ne}, G., \& {Bastien}, P. 2006, \aap, 459, 797, \dodoi{10.1051/0004-6361:20053275}

\bibitem[{{Pinte} {et~al.}(2022){Pinte}, {Teague}, {Flaherty}, {Hall}, {Facchini}, \& {Casassus}}]{pinte22-ppvii}
{Pinte}, C., {Teague}, R., {Flaherty}, K., {et~al.} 2022, arXiv e-prints, arXiv:2203.09528.
\newblock \doarXiv{2203.09528}

\bibitem[{{Pinte} {et~al.}(2018{\natexlab{a}}){Pinte}, {Price}, {M{\'e}nard}, {Duch{\^e}ne}, {Dent}, {Hill}, {de Gregorio-Monsalvo}, {Hales}, \& {Mentiplay}}]{pinte18-hd163296}
{Pinte}, C., {Price}, D.~J., {M{\'e}nard}, F., {et~al.} 2018{\natexlab{a}}, \apjl, 860, L13, \dodoi{10.3847/2041-8213/aac6dc}

\bibitem[{{Pinte} {et~al.}(2018{\natexlab{b}}){Pinte}, {M{\'e}nard}, {Duch{\^e}ne}, {Hill}, {Dent}, {Woitke}, {Maret}, {van der Plas}, {Hales}, {Kamp}, {Thi}, {de Gregorio-Monsalvo}, {Rab}, {Quanz}, {Avenhaus}, {Carmona}, \& {Casassus}}]{pinte2018-altitude-of-CO}
{Pinte}, C., {M{\'e}nard}, F., {Duch{\^e}ne}, G., {et~al.} 2018{\natexlab{b}}, \aap, 609, A47, \dodoi{10.1051/0004-6361/201731377}

\bibitem[{{Pinte} {et~al.}(2018{\natexlab{c}}){Pinte}, {Price}, {M{\'e}nard}, {Duch{\^e}ne}, {Dent}, {Hill}, {de Gregorio-Monsalvo}, {Hales}, \& {Mentiplay}}]{pinte2018-hd97048}
{Pinte}, C., {Price}, D.~J., {M{\'e}nard}, F., {et~al.} 2018{\natexlab{c}}, \apjl, 860, L13, \dodoi{10.3847/2041-8213/aac6dc}

\bibitem[{{Pinte} {et~al.}(2019){Pinte}, {van der Plas}, {M{\'e}nard}, {Price}, {Christiaens}, {Hill}, {Mentiplay}, {Ginski}, {Choquet}, {Boehler}, {Duch{\^e}ne}, {Perez}, \& {Casassus}}]{pinte19-hd97048}
{Pinte}, C., {van der Plas}, G., {M{\'e}nard}, F., {et~al.} 2019, Nature Astronomy, 3, 1109, \dodoi{10.1038/s41550-019-0852-6}

\bibitem[{{Pinte} {et~al.}(2020){Pinte}, {Price}, {M{\'e}nard}, {Duch{\^e}ne}, {Christiaens}, {Andrews}, {Huang}, {Hill}, {van der Plas}, {Perez}, {Isella}, {Boehler}, {Dent}, {Mentiplay}, \& {Loomis}}]{pinte20-dsharpkinks}
{Pinte}, C., {Price}, D.~J., {M{\'e}nard}, F., {et~al.} 2020, \apjl, 890, L9, \dodoi{10.3847/2041-8213/ab6dda}

\bibitem[{{Poglitsch} {et~al.}(2010){Poglitsch}, {Waelkens}, {Geis}, {Feuchtgruber}, {Vandenbussche}, {Rodriguez}, {Krause}, {Renotte}, {van Hoof}, {Saraceno}, {Cepa}, {Kerschbaum}, {Agn{\`e}se}, {Ali}, {Altieri}, {Andreani}, {Augueres}, {Balog}, {Barl}, {Bauer}, {Belbachir}, {Benedettini}, {Billot}, {Boulade}, {Bischof}, {Blommaert}, {Callut}, {Cara}, {Cerulli}, {Cesarsky}, {Contursi}, {Creten}, {De Meester}, {Doublier}, {Doumayrou}, {Duband}, {Exter}, {Genzel}, {Gillis}, {Gr{\"o}zinger}, {Henning}, {Herreros}, {Huygen}, {Inguscio}, {Jakob}, {Jamar}, {Jean}, {de Jong}, {Katterloher}, {Kiss}, {Klaas}, {Lemke}, {Lutz}, {Madden}, {Marquet}, {Martignac}, {Mazy}, {Merken}, {Montfort}, {Morbidelli}, {M{\"u}ller}, {Nielbock}, {Okumura}, {Orfei}, {Ottensamer}, {Pezzuto}, {Popesso}, {Putzeys}, {Regibo}, {Reveret}, {Royer}, {Sauvage}, {Schreiber}, {Stegmaier}, {Schmitt}, {Schubert}, {Sturm}, {Thiel}, {Tofani}, {Vavrek}, {Wetzstein}, {Wieprecht}, \& {Wiezorrek}}]{poglitsch2010-pacs}
{Poglitsch}, A., {Waelkens}, C., {Geis}, N., {et~al.} 2010, \aap, 518, L2, \dodoi{10.1051/0004-6361/201014535}

\bibitem[{{Price} {et~al.}(2018){Price}, {Wurster}, {Tricco}, {Nixon}, {Toupin}, {Pettitt}, {Chan}, {Mentiplay}, {Laibe}, {Glover}, {Dobbs}, {Nealon}, {Liptai}, {Worpel}, {Bonnerot}, {Dipierro}, {Ballabio}, {Ragusa}, {Federrath}, {Iaconi}, {Reichardt}, {Forgan}, {Hutchison}, {Constantino}, {Ayliffe}, {Hirsh}, \& {Lodato}}]{price2018-phantom}
{Price}, D.~J., {Wurster}, J., {Tricco}, T.~S., {et~al.} 2018, \pasa, 35, e031, \dodoi{10.1017/pasa.2018.25}

\bibitem[{{Quillen} {et~al.}(2003){Quillen}, {Varniere}, {Minchev}, \& {Frank}}]{2003-quillen}
{Quillen}, A.~C., {Varniere}, P., {Minchev}, I., \& {Frank}, A. 2003, arXiv e-prints, astro.
\newblock \doarXiv{astro-ph/0312647}

\bibitem[{{Rafikov}(2002{\natexlab{a}})}]{rafikov02-spirals}
{Rafikov}, R.~R. 2002{\natexlab{a}}, \apj, 569, 997, \dodoi{10.1086/339399}

\bibitem[{{Rafikov}(2002{\natexlab{b}})}]{rafikov2002}
---. 2002{\natexlab{b}}, \apj, 569, 997, \dodoi{10.1086/339399}

\bibitem[{{Remijan} {et~al.}(2019){Remijan}, {Biggs}, {Cortes}, {Dent}, {Di Franceso}, {Fomalont}, {Hales}, {Kameno}, {Mason}, {Philips}, {Saini}, {Vila Vilaro}, \& {Villard}}]{alma-technical-handbook2019}
{Remijan}, A., {Biggs}, A., {Cortes}, P.~A., {et~al.} 2019, {ALMA Technical Handbook,ALMA Doc. 7.3, ver. 1.1}, 2019, ALMA Technical Handbook,ALMA Doc. 7.3, ver. 1.1ISBN 978-3-923524-66-2, \dodoi{10.5281/zenodo.4511522}

\bibitem[{{Ren} {et~al.}(2020){Ren}, {Dong}, {van Holstein}, {Ruffio}, {Calvin}, {Girard}, {Benisty}, {Boccaletti}, {Esposito}, {Choquet}, {Mawet}, {Pueyo}, {Stolker}, {Chiang}, {Boer}, {Debes}, {Garufi}, {Grady}, {Hines}, {Maire}, {M{\'e}nard}, {Millar-Blanchaer}, {Perrin}, {Poteet}, \& {Schneider}}]{2020-ren-mwc758}
{Ren}, B., {Dong}, R., {van Holstein}, R.~G., {et~al.} 2020, \apjl, 898, L38, \dodoi{10.3847/2041-8213/aba43e}

\bibitem[{{Ribas} {et~al.}(2017){Ribas}, {Espaillat}, {Mac{\'\i}as}, {Bouy}, {Andrews}, {Calvet}, {Naylor}, {Riviere-Marichalar}, {van der Wiel}, \& {Wilner}}]{ribas2017-herschel}
{Ribas}, {\'A}., {Espaillat}, C.~C., {Mac{\'\i}as}, E., {et~al.} 2017, \apj, 849, 63, \dodoi{10.3847/1538-4357/aa8e99}

\bibitem[{{Rice} \& {Armitage}(2009)}]{rice-armitage-2009}
{Rice}, W.~K.~M., \& {Armitage}, P.~J. 2009, \mnras, 396, 2228, \dodoi{10.1111/j.1365-2966.2009.14879.x}

\bibitem[{{Rice} {et~al.}(2003){Rice}, {Armitage}, {Bonnell}, {Bate}, {Jeffers}, \& {Vine}}]{rice2003}
{Rice}, W.~K.~M., {Armitage}, P.~J., {Bonnell}, I.~A., {et~al.} 2003, \mnras, 346, L36, \dodoi{10.1111/j.1365-2966.2003.07317.x}

\bibitem[{{Rice} {et~al.}(2004){Rice}, {Lodato}, {Pringle}, {Armitage}, \& {Bonnell}}]{rice2004}
{Rice}, W.~K.~M., {Lodato}, G., {Pringle}, J.~E., {Armitage}, P.~J., \& {Bonnell}, I.~A. 2004, \mnras, 355, 543, \dodoi{10.1111/j.1365-2966.2004.08339.x}

\bibitem[{{Rivi{\`e}re-Marichalar} {et~al.}(2020){Rivi{\`e}re-Marichalar}, {Fuente}, {Le Gal}, {Baruteau}, {Neri}, {Navarro-Almaida}, {Trevi{\~n}o-Morales}, {Mac{\'\i}as}, {Bachiller}, \& {Osorio}}]{riviere2020-rosetta1}
{Rivi{\`e}re-Marichalar}, P., {Fuente}, A., {Le Gal}, R., {et~al.} 2020, \aap, 642, A32, \dodoi{10.1051/0004-6361/202038549}

\bibitem[{{Rivi{\`e}re-Marichalar} {et~al.}(2024){Rivi{\`e}re-Marichalar}, {Mac{\'\i}as}, {Baruteau}, {Fuente}, {Neri}, {Ribas}, {Esplugues}, {Navarro-Almaida}, {Osorio}, \& {Anglada}}]{rivieremarichalar2024-rosettastone-3}
{Rivi{\`e}re-Marichalar}, P., {Mac{\'\i}as}, E., {Baruteau}, C., {et~al.} 2024, \aap, 683, A141, \dodoi{10.1051/0004-6361/202347464}

\bibitem[{Robitaille {et~al.}(2018)Robitaille, Beaumont, Qian, Borkin, \& Goodman}]{robitaille2018-glue-pvextractor}
Robitaille, T., Beaumont, C., Qian, P., Borkin, M., \& Goodman, A. 2018, glueviz v0.13.1: multidimensional data exploration, 0.13.1,  Zenodo, \dodoi{10.5281/zenodo.1237692}

\bibitem[{{Rodr{\'\i}guez} {et~al.}(2014){Rodr{\'\i}guez}, {Zapata}, {Dzib}, {Ortiz-Le{\'o}n}, {Loinard}, {Mac{\'\i}as}, \& {Anglada}}]{rodrigues2014-abaur-outflow}
{Rodr{\'\i}guez}, L.~F., {Zapata}, L.~A., {Dzib}, S.~A., {et~al.} 2014, \apjl, 793, L21, \dodoi{10.1088/2041-8205/793/1/L21}

\bibitem[{{Rosotti} {et~al.}(2016){Rosotti}, {Juhasz}, {Booth}, \& {Clarke}}]{2016-rosotti}
{Rosotti}, G.~P., {Juhasz}, A., {Booth}, R.~A., \& {Clarke}, C.~J. 2016, \mnras, 459, 2790, \dodoi{10.1093/mnras/stw691}

\bibitem[{{Rosotti} {et~al.}(2020{\natexlab{a}}){Rosotti}, {Benisty}, {Juh{\'a}sz}, {Teague}, {Clarke}, {Dominik}, {Dullemond}, {Klaassen}, {Matr{\`a}}, \& {Stolker}}]{2020-rosotti-HD100453}
{Rosotti}, G.~P., {Benisty}, M., {Juh{\'a}sz}, A., {et~al.} 2020{\natexlab{a}}, \mnras, 491, 1335, \dodoi{10.1093/mnras/stz3090}

\bibitem[{{Rosotti} {et~al.}(2020{\natexlab{b}}){Rosotti}, {Benisty}, {Juh{\'a}sz}, {Teague}, {Clarke}, {Dominik}, {Dullemond}, {Klaassen}, {Matr{\`a}}, \& {Stolker}}]{rosotti20-hd100453}
---. 2020{\natexlab{b}}, \mnras, 491, 1335, \dodoi{10.1093/mnras/stz3090}

\bibitem[{{Rosotti} {et~al.}(2020{\natexlab{c}}){Rosotti}, {Benisty}, {Juh{\'a}sz}, {Teague}, {Clarke}, {Dominik}, {Dullemond}, {Klaassen}, {Matr{\`a}}, \& {Stolker}}]{rosotti2020-hd100453}
---. 2020{\natexlab{c}}, \mnras, 491, 1335, \dodoi{10.1093/mnras/stz3090}

\bibitem[{{Rowther} {et~al.}(2020){Rowther}, {Meru}, {Kennedy}, {Nealon}, \& {Pinte}}]{2020-rowther-meru}
{Rowther}, S., {Meru}, F., {Kennedy}, G.~M., {Nealon}, R., \& {Pinte}, C. 2020, \apjl, 904, L18, \dodoi{10.3847/2041-8213/abc704}

\bibitem[{{Rowther} {et~al.}(2022){Rowther}, {Nealon}, \& {Meru}}]{rowther22-GI-planet-spirals}
{Rowther}, S., {Nealon}, R., \& {Meru}, F. 2022, \mnras, \dodoi{10.1093/mnras/stac3106}

\bibitem[{{Rowther} {et~al.}(2024{\natexlab{a}}){Rowther}, {Nealon}, {Meru}, {Wurster}, {Aly}, {Alexander}, {Rice}, \& {Booth}}]{rowther2024-dustconcentration-GI}
{Rowther}, S., {Nealon}, R., {Meru}, F., {et~al.} 2024{\natexlab{a}}, \mnras, 528, 2490, \dodoi{10.1093/mnras/stae167}

\bibitem[{{Rowther} {et~al.}(2024{\natexlab{b}}){Rowther}, {Price}, {Pinte}, {Nealon}, {Meru}, \& {Alexander}}]{rowther2024-shortlivedGI}
{Rowther}, S., {Price}, D.~J., {Pinte}, C., {et~al.} 2024{\natexlab{b}}, \mnras, \dodoi{10.1093/mnras/stae2167}

\bibitem[{{Sai} {et~al.}(2020){Sai}, {Ohashi}, {Saigo}, {Matsumoto}, {Aso}, {Takakuwa}, {Aikawa}, {Kurose}, {Yen}, {Tomisaka}, {Tomida}, \& {Machida}}]{sai2020-L1489-warp}
{Sai}, J., {Ohashi}, N., {Saigo}, K., {et~al.} 2020, \apj, 893, 51, \dodoi{10.3847/1538-4357/ab8065}

\bibitem[{{Sakai} {et~al.}(2014){Sakai}, {Sakai}, {Hirota}, {Watanabe}, {Ceccarelli}, {Kahane}, {Bottinelli}, {Caux}, {Demyk}, {Vastel}, {Coutens}, {Taquet}, {Ohashi}, {Takakuwa}, {Yen}, {Aikawa}, \& {Yamamoto}}]{sakai2014-nat}
{Sakai}, N., {Sakai}, T., {Hirota}, T., {et~al.} 2014, \nat, 507, 78, \dodoi{10.1038/nature13000}

\bibitem[{{Sakai} {et~al.}(2017){Sakai}, {Oya}, {Higuchi}, {Aikawa}, {Hanawa}, {Ceccarelli}, {Lefloch}, {L{\'o}pez-Sepulcre}, {Watanabe}, {Sakai}, {Hirota}, {Caux}, {Vastel}, {Kahane}, \& {Yamamoto}}]{sakai2017}
{Sakai}, N., {Oya}, Y., {Higuchi}, A.~E., {et~al.} 2017, \mnras, 467, L76, \dodoi{10.1093/mnrasl/slx002}

\bibitem[{{Salyk} {et~al.}(2013){Salyk}, {Herczeg}, {Brown}, {Blake}, {Pontoppidan}, \& {van Dishoeck}}]{salyk2013-accretion}
{Salyk}, C., {Herczeg}, G.~J., {Brown}, J.~M., {et~al.} 2013, \apj, 769, 21, \dodoi{10.1088/0004-637X/769/1/21}

\bibitem[{{Shakura} \& {Sunyaev}(1973)}]{1973-shakura}
{Shakura}, N.~I., \& {Sunyaev}, R.~A. 1973, \aap, 500, 33

\bibitem[{{Sicilia-Aguilar} {et~al.}(2010){Sicilia-Aguilar}, {Henning}, \& {Hartmann}}]{sicilia-aguilar2010}
{Sicilia-Aguilar}, A., {Henning}, T., \& {Hartmann}, L.~W. 2010, \apj, 710, 597, \dodoi{10.1088/0004-637X/710/1/597}

\bibitem[{{Sierra} \& {Lizano}(2020)}]{2020-sierra-lizano}
{Sierra}, A., \& {Lizano}, S. 2020, \apj, 892, 136, \dodoi{10.3847/1538-4357/ab7d32}

\bibitem[{{Speedie} {et~al.}(2022){Speedie}, {Booth}, \& {Dong}}]{speedie22-alma-dustspirals}
{Speedie}, J., {Booth}, R.~A., \& {Dong}, R. 2022, \apj, 930, 40, \dodoi{10.3847/1538-4357/ac5cc0}

\bibitem[{{Speedie} {et~al.}(2024){Speedie}, {Dong}, {Hall}, {Longarini}, {Veronesi}, {Paneque-Carre{\~n}o}, {Lodato}, {Tang}, {Teague}, \& {Hashimoto}}]{speedie2024}
{Speedie}, J., {Dong}, R., {Hall}, C., {et~al.} 2024, arXiv e-prints, arXiv:2409.02196, \dodoi{10.48550/arXiv.2409.02196}

\bibitem[{{Stapper} {et~al.}(2023){Stapper}, {Hogerheijde}, {van Dishoeck}, {Lin}, {Ahmadi}, {Booth}, {Grant}, {Immer}, {Leemker}, \& {P{\'e}rez-S{\'a}nchez}}]{stapper2023-herbig-gas-masses}
{Stapper}, L.~M., {Hogerheijde}, M.~R., {van Dishoeck}, E.~F., {et~al.} 2023, arXiv e-prints, arXiv:2312.03835.
\newblock \doarXiv{2312.03835}

\bibitem[{{Sturm} {et~al.}(2020{\natexlab{a}}){Sturm}, {Rosotti}, \& {Dominik}}]{2020-sturm}
{Sturm}, J.~A., {Rosotti}, G.~P., \& {Dominik}, C. 2020{\natexlab{a}}, \aap, 643, A92, \dodoi{10.1051/0004-6361/202038919}

\bibitem[{{Sturm} {et~al.}(2020{\natexlab{b}}){Sturm}, {Rosotti}, \& {Dominik}}]{sturm20-dustspirals}
---. 2020{\natexlab{b}}, \aap, 643, A92, \dodoi{10.1051/0004-6361/202038919}

\bibitem[{Sullivan \& Kaszynski(2019)}]{sullivan2019pyvista}
Sullivan, C.~B., \& Kaszynski, A. 2019, Journal of Open Source Software, 4, 1450, \dodoi{10.21105/joss.01450}

\bibitem[{{Szul{\'a}gyi} {et~al.}(2018){Szul{\'a}gyi}, {Plas}, {Meyer}, {Pohl}, {Quanz}, {Mayer}, {Daemgen}, \& {Tamburello}}]{2018-szulagyi-CPDalma}
{Szul{\'a}gyi}, J., {Plas}, G. v.~d., {Meyer}, M.~R., {et~al.} 2018, \mnras, 473, 3573, \dodoi{10.1093/mnras/stx2602}

\bibitem[{{Takeuchi} \& {Lin}(2002)}]{2002-takeuchi-lin}
{Takeuchi}, T., \& {Lin}, D.~N.~C. 2002, \apj, 581, 1344, \dodoi{10.1086/344437}

\bibitem[{{Tang} {et~al.}(2012{\natexlab{a}}){Tang}, {Guilloteau}, {Pi{\'e}tu}, {Dutrey}, {Ohashi}, \& {Ho}}]{tang2012-abaur}
{Tang}, Y.~W., {Guilloteau}, S., {Pi{\'e}tu}, V., {et~al.} 2012{\natexlab{a}}, \aap, 547, A84, \dodoi{10.1051/0004-6361/201219414}

\bibitem[{{Tang} {et~al.}(2012{\natexlab{b}}){Tang}, {Guilloteau}, {Pi{\'e}tu}, {Dutrey}, {Ohashi}, \& {Ho}}]{tang2012-abaur-envelope}
---. 2012{\natexlab{b}}, \aap, 547, A84, \dodoi{10.1051/0004-6361/201219414}

\bibitem[{{Tang} {et~al.}(2017){Tang}, {Guilloteau}, {Dutrey}, {Muto}, {Shen}, {Gu}, {Inutsuka}, {Momose}, {Pietu}, {Fukagawa}, {Chapillon}, {Ho}, {di Folco}, {Corder}, {Ohashi}, \& {Hashimoto}}]{tang2017-abaur12COspirals}
{Tang}, Y.-W., {Guilloteau}, S., {Dutrey}, A., {et~al.} 2017, \apj, 840, 32, \dodoi{10.3847/1538-4357/aa6af7}

\bibitem[{{Teague}(2019{\natexlab{a}})}]{teague19-eddy}
{Teague}, R. 2019{\natexlab{a}}, The Journal of Open Source Software, 4, 1220, \dodoi{10.21105/joss.01220}

\bibitem[{{Teague}(2019{\natexlab{b}})}]{software-gofish}
---. 2019{\natexlab{b}}, The Journal of Open Source Software, 4, 1632, \dodoi{10.21105/joss.01632}

\bibitem[{{Teague}(2019{\natexlab{c}})}]{teague2019-statistical-uncertainties}
---. 2019{\natexlab{c}}, Research Notes of the American Astronomical Society, 3, 74, \dodoi{10.3847/2515-5172/ab2125}

\bibitem[{{Teague}(2019{\natexlab{d}})}]{teague2019-eddy}
---. 2019{\natexlab{d}}, The Journal of Open Source Software, 4, 1220, \dodoi{10.21105/joss.01220}

\bibitem[{{Teague}(2019{\natexlab{e}})}]{teague2019-gofish-joss}
---. 2019{\natexlab{e}}, The Journal of Open Source Software, 4, 1632, \dodoi{10.21105/joss.01632}

\bibitem[{Teague(2020)}]{teague2020-keplerianmask-zenodo}
Teague, R. 2020, richteague/keplerian\_mask: Initial Release, 1.0,  Zenodo, \dodoi{10.5281/zenodo.4321137}

\bibitem[{{Teague} \& {Foreman-Mackey}(2018{\natexlab{a}})}]{teague2018-robust-linecentroids}
{Teague}, R., \& {Foreman-Mackey}, D. 2018{\natexlab{a}}, Research Notes of the American Astronomical Society, 2, 173, \dodoi{10.3847/2515-5172/aae265}

\bibitem[{{Teague} \& {Foreman-Mackey}(2018{\natexlab{b}})}]{teague2018-bettermoments}
---. 2018{\natexlab{b}}, {bettermoments: A robust method to measure line centroids}, v1.0, Zenodo,  Zenodo, \dodoi{10.5281/zenodo.1419754}

\bibitem[{{Teague} {et~al.}(2021{\natexlab{a}}){Teague}, {Law}, {Huang}, \& {Meng}}]{software-disksurf}
{Teague}, R., {Law}, C., {Huang}, J., \& {Meng}, F. 2021{\natexlab{a}}, The Journal of Open Source Software, 6, 3827, \dodoi{10.21105/joss.03827}

\bibitem[{{Teague} {et~al.}(2021{\natexlab{b}}){Teague}, {Bae}, {Aikawa}, {Andrews}, {Bergin}, {Bergner}, {Boehler}, {Booth}, {Bosman}, {Cataldi}, {Czekala}, {Guzm{\'a}n}, {Huang}, {Ilee}, {Law}, {Le Gal}, {Long}, {Loomis}, {M{\'e}nard}, {{\"O}berg}, {P{\'e}rez}, {Schwarz}, {Sierra}, {Walsh}, {Wilner}, {Yamato}, \& {Zhang}}]{teague21-maps18-hd163296-mwc480}
{Teague}, R., {Bae}, J., {Aikawa}, Y., {et~al.} 2021{\natexlab{b}}, \apjs, 257, 18, \dodoi{10.3847/1538-4365/ac1438}

\bibitem[{{Teague} {et~al.}(2022){Teague}, {Bae}, {Andrews}, {Benisty}, {Bergin}, {Facchini}, {Huang}, {Longarini}, \& {Wilner}}]{teague22-twhya-kinematics}
{Teague}, R., {Bae}, J., {Andrews}, S.~M., {et~al.} 2022, arXiv e-prints, arXiv:2208.04837.
\newblock \doarXiv{2208.04837}

\bibitem[{{Terry} {et~al.}(2022){Terry}, {Hall}, {Longarini}, {Lodato}, {Toci}, {Veronesi}, {Paneque-Carre{\~n}o}, \& {Pinte}}]{terry2022-diskmass}
{Terry}, J.~P., {Hall}, C., {Longarini}, C., {et~al.} 2022, \mnras, 510, 1671, \dodoi{10.1093/mnras/stab3513}

\bibitem[{{The pandas development team}(2020)}]{software-pandas}
{The pandas development team}. 2020, \dodoi{10.5281/zenodo.3509134}

\bibitem[{{Thieme} {et~al.}(2022){Thieme}, {Lai}, {Lin}, {Cheong}, {Lee}, {Yen}, {Li}, {Lam}, \& {Zhao}}]{thieme2022}
{Thieme}, T.~J., {Lai}, S.-P., {Lin}, S.-J., {et~al.} 2022, \apj, 925, 32, \dodoi{10.3847/1538-4357/ac382b}

\bibitem[{{Tomida} {et~al.}(2017){Tomida}, {Machida}, {Hosokawa}, {Sakurai}, \& {Lin}}]{tomida17-elias27-GI}
{Tomida}, K., {Machida}, M.~N., {Hosokawa}, T., {Sakurai}, Y., \& {Lin}, C.~H. 2017, \apjl, 835, L11, \dodoi{10.3847/2041-8213/835/1/L11}

\bibitem[{{Valdivia-Mena} {et~al.}(2022){Valdivia-Mena}, {Pineda}, {Segura-Cox}, {Caselli}, {Neri}, {L{\'o}pez-Sepulcre}, {Cunningham}, {Bouscasse}, {Semenov}, {Henning}, {Pi{\'e}tu}, {Chapillon}, {Dutrey}, {Fuente}, {Guilloteau}, {Hsieh}, {Jim{\'e}nez-Serra}, {Marino}, {Maureira}, {Smirnov-Pinchukov}, {Tafalla}, \& {Zhao}}]{valdiviamena2022-peremb50}
{Valdivia-Mena}, M.~T., {Pineda}, J.~E., {Segura-Cox}, D.~M., {et~al.} 2022, \aap, 667, A12, \dodoi{10.1051/0004-6361/202243310}

\bibitem[{{Valdivia-Mena} {et~al.}(2023){Valdivia-Mena}, {Pineda}, {Segura-Cox}, {Caselli}, {Schmiedeke}, {Choudhury}, {Offner}, {Neri}, {Goodman}, \& {Fuller}}]{valdiviamena2023-b5}
---. 2023, \aap, 677, A92, \dodoi{10.1051/0004-6361/202346357}

\bibitem[{{van den Ancker} {et~al.}(1997){van den Ancker}, {The}, {Tjin A Djie}, {Catala}, {de Winter}, {Blondel}, \& {Waters}}]{vandenancker1997}
{van den Ancker}, M.~E., {The}, P.~S., {Tjin A Djie}, H.~R.~E., {et~al.} 1997, \aap, 324, L33

\bibitem[{{van der Marel} {et~al.}(2019){van der Marel}, {Dong}, {di Francesco}, {Williams}, \& {Tobin}}]{2019-vandermarel-gaps}
{van der Marel}, N., {Dong}, R., {di Francesco}, J., {Williams}, J.~P., \& {Tobin}, J. 2019, \apj, 872, 112, \dodoi{10.3847/1538-4357/aafd31}

\bibitem[{{van der Marel} {et~al.}(2021){van der Marel}, {Birnstiel}, {Garufi}, {Ragusa}, {Christiaens}, {Price}, {Sallum}, {Muley}, {Francis}, \& {Dong}}]{vandermarel2021-diversity-asymmetries}
{van der Marel}, N., {Birnstiel}, T., {Garufi}, A., {et~al.} 2021, \aj, 161, 33, \dodoi{10.3847/1538-3881/abc3ba}

\bibitem[{{van der Velden}(2020{\natexlab{a}})}]{2020-cmasher}
{van der Velden}, E. 2020{\natexlab{a}}, The Journal of Open Source Software, 5, 2004, \dodoi{10.21105/joss.02004}

\bibitem[{{van der Velden}(2020{\natexlab{b}})}]{software-cmasher}
---. 2020{\natexlab{b}}, The Journal of Open Source Software, 5, 2004, \dodoi{10.21105/joss.02004}

\bibitem[{{van Gelder} {et~al.}(2021){van Gelder}, {Tabone}, {van Dishoeck}, \& {Godard}}]{vangelder2021-shocks-sulphur}
{van Gelder}, M.~L., {Tabone}, B., {van Dishoeck}, E.~F., \& {Godard}, B. 2021, \aap, 653, A159, \dodoi{10.1051/0004-6361/202141591}

\bibitem[{{Veronesi} {et~al.}(2019){Veronesi}, {Lodato}, {Dipierro}, {Ragusa}, {Hall}, \& {Price}}]{2019-veronesi-diskmass}
{Veronesi}, B., {Lodato}, G., {Dipierro}, G., {et~al.} 2019, \mnras, 489, 3758, \dodoi{10.1093/mnras/stz2384}

\bibitem[{{Veronesi} {et~al.}(2021{\natexlab{a}}){Veronesi}, {Paneque-Carre{\~n}o}, {Lodato}, {Testi}, {P{\'e}rez}, {Bertin}, \& {Hall}}]{veronesi2021-elias27}
{Veronesi}, B., {Paneque-Carre{\~n}o}, T., {Lodato}, G., {et~al.} 2021{\natexlab{a}}, \apjl, 914, L27, \dodoi{10.3847/2041-8213/abfe6a}

\bibitem[{{Veronesi} {et~al.}(2021{\natexlab{b}}){Veronesi}, {Paneque-Carre{\~n}o}, {Lodato}, {Testi}, {P{\'e}rez}, {Bertin}, \& {Hall}}]{veronesi2021-elias227}
---. 2021{\natexlab{b}}, \apjl, 914, L27, \dodoi{10.3847/2041-8213/abfe6a}

\bibitem[{Virtanen {et~al.}(2020)Virtanen, Gommers, Oliphant, Haberland, Reddy, Cournapeau, Burovski, Peterson, Weckesser, Bright, {van der Walt}, Brett, Wilson, Millman, Mayorov, Nelson, Jones, Kern, Larson, Carey, Polat, Feng, Moore, {VanderPlas}, Laxalde, Perktold, Cimrman, Henriksen, Quintero, Harris, Archibald, Ribeiro, Pedregosa, {van Mulbregt}, \& {SciPy 1.0 Contributors}}]{2020SciPy-NMeth}
Virtanen, P., Gommers, R., Oliphant, T.~E., {et~al.} 2020, Nature Methods, 17, 261, \dodoi{10.1038/s41592-019-0686-2}

\bibitem[{{Virtanen} {et~al.}(2020){Virtanen}, {Gommers}, {Oliphant}, {Haberland}, {Reddy}, {Cournapeau}, {Burovski}, {Peterson}, {Weckesser}, {Bright}, {van der Walt}, {Brett}, {Wilson}, {Millman}, {Mayorov}, {Nelson}, {Jones}, {Kern}, {Larson}, {Carey}, {Polat}, {Feng}, {Moore}, {VanderPlas}, {Laxalde}, {Perktold}, {Cimrman}, {Henriksen}, {Quintero}, {Harris}, {Archibald}, {Ribeiro}, {Pedregosa}, {van Mulbregt}, \& {SciPy 1. 0 Contributors}}]{software-scipy}
{Virtanen}, P., {Gommers}, R., {Oliphant}, T.~E., {et~al.} 2020, Nature Methods, 17, 261, \dodoi{10.1038/s41592-019-0686-2}

\bibitem[{{Weber} {et~al.}(2019){Weber}, {P{\'e}rez}, {Ben{\'\i}tez-Llambay}, {Gressel}, {Casassus}, \& {Krapp}}]{2019-weber-migrating}
{Weber}, P., {P{\'e}rez}, S., {Ben{\'\i}tez-Llambay}, P., {et~al.} 2019, \apj, 884, 178, \dodoi{10.3847/1538-4357/ab412f}

\bibitem[{{Whipple}(1972)}]{1972-whipple}
{Whipple}, F.~L. 1972, in From Plasma to Planet, ed. A.~{Elvius}, 211

\bibitem[{{Winter} {et~al.}(2024){Winter}, {Benisty}, \& {Andrews}}]{winter2024-BHL}
{Winter}, A.~J., {Benisty}, M., \& {Andrews}, S.~M. 2024, \apjl, 972, L9, \dodoi{10.3847/2041-8213/ad6d5d}

\bibitem[{{Zhang} \& {Zhu}(2020{\natexlab{a}})}]{2020-zhang-zhu-cooling}
{Zhang}, S., \& {Zhu}, Z. 2020{\natexlab{a}}, \mnras, 493, 2287, \dodoi{10.1093/mnras/staa404}

\bibitem[{{Zhang} \& {Zhu}(2020{\natexlab{b}})}]{zhang-zhu20-radiative-cooling}
---. 2020{\natexlab{b}}, \mnras, 493, 2287, \dodoi{10.1093/mnras/staa404}

\bibitem[{{Zhang} \& {Zhu}(2020{\natexlab{c}})}]{zhang-zhu2020-SG-beta}
---. 2020{\natexlab{c}}, \mnras, 493, 2287, \dodoi{10.1093/mnras/staa404}

\bibitem[{{Zhang} {et~al.}(2018{\natexlab{a}}){Zhang}, {Zhu}, {Huang}, {Guzm{\'a}n}, {Andrews}, {Birnstiel}, {Dullemond}, {Carpenter}, {Isella}, {P{\'e}rez}, {Benisty}, {Wilner}, {Baruteau}, {Bai}, \& {Ricci}}]{2018-zhang-dsharp7}
{Zhang}, S., {Zhu}, Z., {Huang}, J., {et~al.} 2018{\natexlab{a}}, \apjl, 869, L47, \dodoi{10.3847/2041-8213/aaf744}

\bibitem[{{Zhang} {et~al.}(2018{\natexlab{b}}){Zhang}, {Zhu}, {Huang}, {Guzm{\'a}n}, {Andrews}, {Birnstiel}, {Dullemond}, {Carpenter}, {Isella}, {P{\'e}rez}, {Benisty}, {Wilner}, {Baruteau}, {Bai}, \& {Ricci}}]{zhang18-dsharp7-planetdiskinteractions}
---. 2018{\natexlab{b}}, \apjl, 869, L47, \dodoi{10.3847/2041-8213/aaf744}

\bibitem[{{Zhang} {et~al.}(2023){Zhang}, {Ginski}, {Huang}, {Zurlo}, {Beust}, {Bae}, {Benisty}, {Garufi}, {Hogerheijde}, {van Holstein}, {Kenworthy}, {Langlois}, {Manara}, {Pinilla}, {Rab}, {Ribas}, {Rosotti}, \& {Williams}}]{zhang2023-destinys}
{Zhang}, Y., {Ginski}, C., {Huang}, J., {et~al.} 2023, \aap, 672, A145, \dodoi{10.1051/0004-6361/202245577}

\bibitem[{{Zhou} {et~al.}(2023){Zhou}, {Bowler}, {Yang}, {Sanghi}, {Herczeg}, {Kraus}, {Bae}, {Long}, {Follette}, {Ward-Duong}, {Zhu}, {Biddle}, {Close}, {Yushu Jiang}, \& {Wu}}]{zhou2023-abaurb}
{Zhou}, Y., {Bowler}, B.~P., {Yang}, H., {et~al.} 2023, arXiv e-prints, arXiv:2308.16223, \dodoi{10.48550/arXiv.2308.16223}

\bibitem[{{Zhu} {et~al.}(2015{\natexlab{a}}){Zhu}, {Dong}, {Stone}, \& {Rafikov}}]{2015-zhu-dong-shocks}
{Zhu}, Z., {Dong}, R., {Stone}, J.~M., \& {Rafikov}, R.~R. 2015{\natexlab{a}}, \apj, 813, 88, \dodoi{10.1088/0004-637X/813/2/88}

\bibitem[{{Zhu} {et~al.}(2015{\natexlab{b}}){Zhu}, {Dong}, {Stone}, \& {Rafikov}}]{zhu15-3dstructure-spiralshocks}
---. 2015{\natexlab{b}}, \apj, 813, 88, \dodoi{10.1088/0004-637X/813/2/88}

\bibitem[{{Zhu} {et~al.}(2015{\natexlab{c}}){Zhu}, {Dong}, {Stone}, \& {Rafikov}}]{zhu2015-cooling}
---. 2015{\natexlab{c}}, \apj, 813, 88, \dodoi{10.1088/0004-637X/813/2/88}

\bibitem[{{Zhu} {et~al.}(2012){Zhu}, {Hartmann}, {Nelson}, \& {Gammie}}]{zhu2012-challenges-clumps}
{Zhu}, Z., {Hartmann}, L., {Nelson}, R.~P., \& {Gammie}, C.~F. 2012, \apj, 746, 110, \dodoi{10.1088/0004-637X/746/1/110}

\bibitem[{{Zhu} \& {Zhang}(2022)}]{zhu22-eccentric-spirals}
{Zhu}, Z., \& {Zhang}, R.~M. 2022, \mnras, 510, 3986, \dodoi{10.1093/mnras/stab3641}

\bibitem[{{Zhu} {et~al.}(2019){Zhu}, {Zhang}, {Jiang}, {Kataoka}, {Birnstiel}, {Dullemond}, {Andrews}, {Huang}, {P{\'e}rez}, {Carpenter}, {Bai}, {Wilner}, \& {Ricci}}]{2019-zhu-scattering}
{Zhu}, Z., {Zhang}, S., {Jiang}, Y.-F., {et~al.} 2019, \apjl, 877, L18, \dodoi{10.3847/2041-8213/ab1f8c}

\bibitem[{{Ziampras} {et~al.}(2020){Ziampras}, {Ataiee}, {Kley}, {Dullemond}, \& {Baruteau}}]{2020-ziampras-iceline}
{Ziampras}, A., {Ataiee}, S., {Kley}, W., {Dullemond}, C.~P., \& {Baruteau}, C. 2020, \aap, 633, A29, \dodoi{10.1051/0004-6361/201936495}

"""

mapping_dict = parse_bbl(bbl_content)

# Output the final dictionary of duplicates
print("\n*********************************************")
print("Final Output:")
for key in mapping_dict:
    print(key, ":", mapping_dict[key])

print(mapping_dict)


# *********************************************
# Final Output:
# 2018-andrews-dsharp1 : ['andrews18-dsharp1']
# astropy:2013 : ['software-astropy1']
# astropy:2018 : ['software-astropy2']
# 2018a-bae-zhu : ['bae+zhu18-spirals1']
# 2018b-bae-zhu : ['bae+zhu18-spirals2']
# beck2019-H2 : ['beck2019']
# 2018-birnstiel-dsharp5 : ['birnstiel2018-dsharp-opac']
# boccaletti2020-abaursphere : ['boccaletti2020']
# bollati21-theory-of-kinks-2d : ['bollati2021-theory-kinks']
# 2021-casassus-filament : ['casassus21-filament-spirals-hd135344B']
# 2015ApJ...812L..32D : ['dong2015-GIspirals-scatteredlight']
# 2018b-dong : ['dong2018-gi-or-planets']
# dullemond18-dsharp6 : ['dullemond2018-dsharp6']
# ginski16-hd97048-sphere : ['ginski2016-scatteredlight']
# 1979-goldreich : ['goldreich-tremaine79']
# goodman-rafikov01 : ['goodman-rafikov2001']
# hall19-GI-spirals-ALMA : ['hall2019-temporalGIspiralsALMA']
# harris2020array : ['software-numpy']
# 2018a-huang-dsharp2 : ['huang18-dsharp2']
# 2018-huang-dsharp3-spirals : ['huang18-dsharp3-spirals']
# Hunter:2007 : ['software-matplotlib']
# 2020-jennings-frank : ['jennings20-frank']
# 2021-kanagawa-footprint : ['kataoka15-dustscattering']
# krapp-2021 : ['kratter-lodato2016']
# 2017-meru-elias227 : ['meru17-elias27', 'meru2017-elias27']
# 2020a-miranda-rafikov : ['miranda-rafikov20-cooling-basictheory']
# 2002-ogilvie : ['ogilvie-lubow2002']
# paneque-carreno22-vertical-stratification : ['paneque-carreno21-elias27-GI', 'panequecarreno2021-elias27', 'paneque2021-elias27']
# 2019-pavlyuchenkov : ['pavlyuchenkov19-spectralindex']
# perez16-elias27 : ['perez2016-elias27']
# pinte22-ppvii : ['pinte2018-hd97048']
# 2003-quillen : ['rafikov2002']
# 2020-rosotti-HD100453 : ['rosotti20-hd100453', 'rosotti2020-hd100453']
# stapper2023-herbig-gas-masses : ['sturm20-dustspirals']
# tang2012-abaur : ['tang2012-abaur-envelope']
# teague19-eddy : ['teague2019-eddy']
# software-gofish : ['teague2019-gofish-joss']
# 2020-cmasher : ['software-cmasher']
# veronesi2021-elias27 : ['veronesi2021-elias227']
# 2020SciPy-NMeth : ['software-scipy']
# 2020-zhang-zhu-cooling : ['zhang-zhu20-radiative-cooling', 'zhang-zhu2020-SG-beta']
# 2018-zhang-dsharp7 : ['zhang18-dsharp7-planetdiskinteractions']
# 2015-zhu-dong-shocks : ['zhu15-3dstructure-spiralshocks', 'zhu2015-cooling']
# {'2018-andrews-dsharp1': ['andrews18-dsharp1'], 'astropy:2013': ['software-astropy1'], 'astropy:2018': ['software-astropy2'], '2018a-bae-zhu': ['bae+zhu18-spirals1'], '2018b-bae-zhu': ['bae+zhu18-spirals2'], 'beck2019-H2': ['beck2019'], '2018-birnstiel-dsharp5': ['birnstiel2018-dsharp-opac'], 'boccaletti2020-abaursphere': ['boccaletti2020'], 'bollati21-theory-of-kinks-2d': ['bollati2021-theory-kinks'], '2021-casassus-filament': ['casassus21-filament-spirals-hd135344B'], '2015ApJ...812L..32D': ['dong2015-GIspirals-scatteredlight'], '2018b-dong': ['dong2018-gi-or-planets'], 'dullemond18-dsharp6': ['dullemond2018-dsharp6'], 'ginski16-hd97048-sphere': ['ginski2016-scatteredlight'], '1979-goldreich': ['goldreich-tremaine79'], 'goodman-rafikov01': ['goodman-rafikov2001'], 'hall19-GI-spirals-ALMA': ['hall2019-temporalGIspiralsALMA'], 'harris2020array': ['software-numpy'], '2018a-huang-dsharp2': ['huang18-dsharp2'], '2018-huang-dsharp3-spirals': ['huang18-dsharp3-spirals'], 'Hunter:2007': ['software-matplotlib'], '2020-jennings-frank': ['jennings20-frank'], '2021-kanagawa-footprint': ['kataoka15-dustscattering'], 'krapp-2021': ['kratter-lodato2016'], '2017-meru-elias227': ['meru17-elias27', 'meru2017-elias27'], '2020a-miranda-rafikov': ['miranda-rafikov20-cooling-basictheory'], '2002-ogilvie': ['ogilvie-lubow2002'], 'paneque-carreno22-vertical-stratification': ['paneque-carreno21-elias27-GI', 'panequecarreno2021-elias27', 'paneque2021-elias27'], '2019-pavlyuchenkov': ['pavlyuchenkov19-spectralindex'], 'perez16-elias27': ['perez2016-elias27'], 'pinte22-ppvii': ['pinte2018-hd97048'], '2003-quillen': ['rafikov2002'], '2020-rosotti-HD100453': ['rosotti20-hd100453', 'rosotti2020-hd100453'], 'stapper2023-herbig-gas-masses': ['sturm20-dustspirals'], 'tang2012-abaur': ['tang2012-abaur-envelope'], 'teague19-eddy': ['teague2019-eddy'], 'software-gofish': ['teague2019-gofish-joss'], '2020-cmasher': ['software-cmasher'], 'veronesi2021-elias27': ['veronesi2021-elias227'], '2020SciPy-NMeth': ['software-scipy'], '2020-zhang-zhu-cooling': ['zhang-zhu20-radiative-cooling', 'zhang-zhu2020-SG-beta'], '2018-zhang-dsharp7': ['zhang18-dsharp7-planetdiskinteractions'], '2015-zhu-dong-shocks': ['zhu15-3dstructure-spiralshocks', 'zhu2015-cooling']}
