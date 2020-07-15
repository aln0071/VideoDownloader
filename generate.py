import sys, getopt, m3u8, os

def show_usage():
    print("Usage: "+sys.argv[0]+" --base_url <base-url> --file <m3u8-file-location>");
    print("\nAccepted options:\n")
    print("\t--base-url or -u\t-\tbase url of the download links (mandatory)")
    print("\t--input-file or -i\t-\tthe m3u8 input file containing the segment details (mandatory)")
    print("\t--output-file or -o\t-\tthe name of the output file (optional) - default is urls.txt")
    print("\t--help or -h\t\t-\tprint this help message\n\n")
    print("Description:\n")
    print("This program accepts a base url and the m3u8 file location. It reads the m3u8 file to get all segment names. These segment names are then appented to the base url to generate the download links. The generated links are written to a file named urls.txt which will contain one url per line. This file is a normal text file and so, it can be opened in a text editor and the data can be verified by the user. This program generates the output file in a format compatible with the wget program in Linux. You can use this program directly with wget to download all video segments.")
argv = sys.argv[1:]
input_file = ''
base_url = ''
output_file = 'urls.txt'
try:
    opts, args = getopt.getopt(argv, "hi:u:o:", ["help", "input-file", "base-url", "output-file"])
except getopt.GetoptError:
    show_usage()
    sys.exit(2)
for opt, arg in opts:
    if opt in ('-h', '--help'):
        show_usage()
        sys.exit(0)
    elif opt in ('-i', '--input-file'):
        input_file = arg
    elif opt in ('-u', '--base-url'):
        base_url = arg
    elif opt in ('-o', '--output-file'):
        output_file = arg

if not input_file or not base_url:
    print("\nError: Mandatory parameter missing; Please refer usage\n")
    show_usage()
    print("\nError: Mandatory parameter missing; Please refer usage")
    sys.exit(2)

playlist = m3u8.load(input_file)
uris = playlist.segments.uri
target_urls = [base_url+uri for uri in uris]
print("This is the url to the first segment: "+target_urls[0])
print("Please confirm that this is a valid url by downloading it manually, before proceeding.")
with open(output_file, 'w') as fp:
    for url in target_urls:
        fp.write("%s\n" % url)
print("A file - "+output_file+" - is generated in "+os.path.dirname(os.path.realpath(__file__))+" which contains urls of all files that need to be downloaded.")
print("Please verify the data before proceeding to download.")
