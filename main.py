import re

def write_res(words, fout):
    year = clean_string(re.search(r"^\d{4}", words[0]))
    if year == '2020;':
        fout.write(year)
        fout.write(clean_string(re.search(r"(\d+\.\d)", words[1])))
        fout.write(clean_string(re.search(r"\d+\.\d{2}", words[2])))
        fout.write(clean_string(re.search(r"\d+", words[3])))
        fout.write(clean_string(re.search(r"([1-9]|[12][0-9]|3[01])", words[4])))
        fout.write(clean_string(re.search(r"([1-9]|[1][12])", words[5])))
        fout.write(clean_string(re.search(r"(\d+\.\d)", words[6])))
        fout.write(clean_string(re.search(r"\d+\.\d{2}", words[7])))
        fout.write(clean_string(re.search(r"[A-Za-z1-9]{4,7}", words[8])))
        fout.write(clean_string(re.search(r"\d+\.\d{2}", words[9])))
        fout.write("\n")

def clean_string(s, whitespace=True):
    result = s.group(0)
    if whitespace:
        result = re.sub("\s", "", result)
    return(result + ";")


def find_in_file():
    # Use a breakpoint in the code line below to debug your script.
    fin = open("in_file.txt", "r")
    fout = open("out_file.txt", "w")
    s = fin.readline()
    while s:
        words = re.split(r'\s*[;:?]\s*', s)
        print(words)
        write_res(words, fout)
        s = fin.readline()


if name == 'main':
    find_in_file()