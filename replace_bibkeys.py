import re
import sys

# The dictionary of duplicate bibkeys as output by parse_bbl.py
duplicate_bibkeys = {'andrews18-dsharp1': ['2018-andrews-dsharp1'],
                     'software-astropy1': ['astropy:2013'],
                     'software-astropy2': ['astropy:2018'],
                     '2018a-bae-zhu': ['bae+zhu18-spirals1'],
                     '2018b-bae-zhu': ['bae+zhu18-spirals2'],
                     'beck2019': ['beck2019-H2'],
                     'birnstiel2018-dsharp-opac': ['2018-birnstiel-dsharp5'],
                     'boccaletti2020': ['boccaletti2020-abaursphere'],
                     'bollati2021-theory-kinks': ['bollati21-theory-of-kinks-2d'],
                     'casassus21-filament-spirals-hd135344B': ['2021-casassus-filament'],
                     'dong2015-GIspirals-scatteredlight': ['2015ApJ...812L..32D'],
                     'dong2018-gi-or-planets': ['2018b-dong'],
                     'dullemond2018-dsharp6': ['dullemond18-dsharp6'],
                     'ginski2016-scatteredlight': ['ginski16-hd97048-sphere'],
                     'goldreich-tremaine79': ['1979-goldreich'],
                     'goodman-rafikov2001': ['goodman-rafikov01'],
                     'hall2019-temporalGIspiralsALMA': ['hall19-GI-spirals-ALMA'],
                     'software-numpy': ['harris2020array'],
                     'huang18-dsharp2': ['2018a-huang-dsharp2'],
                     'huang18-dsharp3-spirals': ['2018-huang-dsharp3-spirals'],
                     'software-matplotlib': ['Hunter:2007'],
                     'jennings20-frank': ['2020-jennings-frank'],
                     'meru2017-elias27': ['meru17-elias27', '2017-meru-elias227'],
                     'miranda-rafikov20-cooling-basictheory': ['2020a-miranda-rafikov'],
                     'ogilvie-lubow2002': ['2002-ogilvie'],
                     'paneque2021-elias27': ['paneque-carreno21-elias27-GI', 'panequecarreno2021-elias27', 'paneque-carreno22-vertical-stratification'],
                     '2019-pavlyuchenkov': ['pavlyuchenkov19-spectralindex'],
                     'perez2016-elias27': ['perez16-elias27'],
                     'rosotti2020-hd100453': ['rosotti20-hd100453', '2020-rosotti-HD100453'],
                     'tang2012-abaur-envelope': ['tang2012-abaur'],
                     'teague2019-eddy': ['teague19-eddy'],
                     'software-gofish': ['teague2019-gofish-joss'],
                     'software-cmasher': ['2020-cmasher'],
                     'veronesi2021-elias227': ['veronesi2021-elias27'],
                     'software-scipy': ['2020SciPy-NMeth'],
                     'zhang-zhu20-radiative-cooling': ['2020-zhang-zhu-cooling', 'zhang-zhu2020-SG-beta'],
                     'zhang18-dsharp7-planetdiskinteractions': ['2018-zhang-dsharp7'],
                     'zhu15-3dstructure-spiralshocks': ['2015-zhu-dong-shocks', 'zhu2015-cooling']
                     }


def replace_bibkeys(input_file, output_file):
    # Open and read the content of the input .tex file
    with open(input_file, 'r') as file:
        content = file.read()

    # Go through each entry in the dictionary
    for key, bibkeys in duplicate_bibkeys.items():
        # Replace each bibkey in the content with the dictionary key
        for bibkey in bibkeys:
            # Define the regex pattern to match bibkeys in the text, accounting for all possible citation formats
            pattern = r'(?<!\w)'+re.escape(bibkey)+r'(?!\w)'  # Match the bibkey, ensuring it doesn't match part of another word

            # Replace the bibkey with the dictionary key
            content = re.sub(pattern, key, content)

    # Write the modified content to the output file
    with open(output_file, 'w') as file:
        file.write(content)
    print(f"Replaced citations have been saved to {output_file}")

if __name__ == "__main__":
    # Ensure the script takes the filename as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python replace_bibkeys.py <input_file.tex>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.replace('.tex', '_replaced.tex')

    # Call the function to replace bibkeys in the file
    replace_bibkeys(input_file, output_file)
