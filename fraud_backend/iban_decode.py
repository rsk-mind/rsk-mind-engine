#! /usr/bin/env python
# -*- coding: latin-1 -*-

class Country:
    """Class for country specific iban data."""

    def __init__(self, name, code, bank_form, acc_form):
        """Constructor for Country objects.

        Arguments:
            name      - Name of the country
            code      - Country Code from ISO 3166
            bank_form - Format of bank/branch code part (e.g. "0 4a 0 ")
            acc_form  - Format of account number part (e.g. "0  11  2n")
        """
        self.name = name
        self.code = code
        self.bank = self._decode_format(bank_form)
        self.acc  = self._decode_format(acc_form)

    def bank_lng(self):
        return reduce(lambda sum, part: sum + part[0], self.bank, 0)

    def acc_lng(self):
        return reduce(lambda sum, part: sum + part[0], self.acc, 0)

    def total_lng(self):
        return 4 + self.bank_lng() + self.acc_lng()

    def _decode_format(self, form):
        form_list = []
        for part in form.split(" "):
            if part:
                typ = part[-1]
                if typ in ("a", "n"):
                    part = part[:-1]
                else:
                    typ = "c"
                lng = int(part)
                form_list.append((lng, typ))
        return tuple(form_list)

# BBAN data from ISO 13616, Country codes from ISO 3166 (www.iso.org).
iban_data = (Country("Andorra",        "AD", "0  4n 4n", "0  12   0 "),
             Country("Albania",        "AL", "0  8n 0 ", "0  16   0 "),
             Country("Austria",        "AT", "0  5n 0 ", "0  11n  0 "),
             Country("Bosnia and Herzegovina",
                                       "BA", "0  3n 3n", "0   8n  2n"),
             Country("Belgium",        "BE", "0  3n 0 ", "0   7n  2n"),
             Country("Bulgaria",       "BG", "0  4a 4n", "2n  8   0 "),
             Country("Switzerland",    "CH", "0  5n 0 ", "0  12   0 "),
             Country("Cyprus",         "CY", "0  3n 5n", "0  16   0 "),
             Country("Czech Republic", "CZ", "0  4n 0 ", "0  16n  0 "),
             Country("Germany",        "DE", "0  8n 0 ", "0  10n  0 "),
             Country("Denmark",        "DK", "0  4n 0 ", "0   9n  1n"),
             Country("Estonia",        "EE", "0  2n 0 ", "2n 11n  1n"),
             Country("Spain",          "ES", "0  4n 4n", "2n 10n  0 "),
             Country("Finland",        "FI", "0  6n 0 ", "0   7n  1n"),
             Country("Faroe Islands",  "FO", "0  4n 0 ", "0   9n  1n"),
             Country("France",         "FR", "0  5n 5n", "0  11   2n"),
             Country("United Kingdom", "GB", "0  4a 6n", "0   8n  0 "),
             Country("Georgia",        "GE", "0  2a 0 ", "0  16n  0 "),
             Country("Gibraltar",      "GI", "0  4a 0 ", "0  15   0 "),
             Country("Greenland",      "GL", "0  4n 0 ", "0   9n  1n"),
             Country("Greece",         "GR", "0  3n 4n", "0  16   0 "),
             Country("Croatia",        "HR", "0  7n 0 ", "0  10n  0 "),
             Country("Hungary",        "HU", "0  3n 4n", "1n 15n  1n"),
             Country("Ireland",        "IE", "0  4a 6n", "0   8n  0 "),
             Country("Israel",         "IL", "0  3n 3n", "0  13n  0 "),
             Country("Iceland",        "IS", "0  4n 0 ", "2n 16n  0 "),
             Country("Italy",          "IT", "1a 5n 5n", "0  12   0 "),
             Country("Kuwait",         "KW", "0  4a 0 ", "0  22   0 "),
             Country("Kazakhstan",     "KZ", "0  3n 0 ", "0  13   0 "),
             Country("Lebanon",        "LB", "0  4n 0 ", "0  20   0 "),
             Country("Liechtenstein",  "LI", "0  5n 0 ", "0  12   0 "),
             Country("Lithuania",      "LT", "0  5n 0 ", "0  11n  0 "),
             Country("Luxembourg",     "LU", "0  3n 0 ", "0  13   0 "),
             Country("Latvia",         "LV", "0  4a 0 ", "0  13   0 "),
             Country("Monaco",         "MC", "0  5n 5n", "0  11   2n"),
             Country("Montenegro",     "ME", "0  3n 0 ", "0  13n  2n"),
             Country("Macedonia, Former Yugoslav Republic of",
                                       "MK", "0  3n 0 ", "0  10   2n"),
             Country("Mauritania",     "MR", "0  5n 5n", "0  11n  2n"),
             Country("Malta",          "MT", "0  4a 5n", "0  18   0 "),
             Country("Mauritius",      "MU", "0  4a 4n", "0  15n  3a"),
             Country("Netherlands",    "NL", "0  4a 0 ", "0  10n  0 "),
             Country("Norway",         "NO", "0  4n 0 ", "0   6n  1n"),
             Country("Poland",         "PL", "0  8n 0 ", "0  16n  0 "),
             Country("Portugal",       "PT", "0  4n 4n", "0  11n  2n"),
             Country("Romania",        "RO", "0  4a 0 ", "0  16   0 "),
             Country("Serbia",         "RS", "0  3n 0 ", "0  13n  2n"),
             Country("Saudi Arabia",   "SA", "0  2n 0 ", "0  18   0 "),
             Country("Sweden",         "SE", "0  3n 0 ", "0  16n  1n"),
             Country("Slovenia",       "SI", "0  5n 0 ", "0   8n  2n"),
             Country("Slovak Republic",
                                       "SK", "0  4n 0 ", "0  16n  0 "),
             Country("San Marino",     "SM", "1a 5n 5n", "0  12   0 "),
             Country("Tunisia",        "TN", "0  2n 3n", "0  13n  2n"),
             Country("Turkey",         "TR", "0  5n 0 ", "1  16   0 "))

def country_data(code):
    """Search the country code in the iban_data list."""
    for country in iban_data:
        if country.code == code:
            return country
    return None

def mod97(digit_string):
    """Modulo 97 for huge numbers given as digit strings.

    This function is a prototype for a JavaScript implementation.
    In Python this can be done much easier: long(digit_string) % 97.
    """
    m = 0
    for d in digit_string:
        m = (m * 10 + int(d)) % 97
    return m

def fill0(s, l):
    """Fill the string with leading zeros until length is reached."""
    import string
    return string.zfill(s, l)

def strcmp(s1, s2):
    """Compare two strings respecting german umlauts."""
    chars = "AaÄäBbCcDdEeFfGgHhIiJjKkLlMmNnOoÖöPpQqRrSsßTtUuÜüVvWwXxYyZz"
    lng = min(len(s1), len(s2))
    for i in range(lng):
        d = chars.find(s1[i]) - chars.find(s2[i]);
        if d != 0:
            return d
    return len(s1) - len(s2)

def country_index_table():
    """Create an index table of the iban_data list sorted by country names."""
    tab = range(len(iban_data))
    for i in range(len(tab) - 1, 0, -1):
        for j in range(i):
            if strcmp(iban_data[tab[j]].name, iban_data[tab[j+1]].name) > 0:
                t = tab[j]; tab[j] = tab[j+1]; tab[j+1] = t
    return tab

def checksum_iban(iban):
    """Calculate 2-digit checksum of an IBAN."""
    code     = iban[:2]
    checksum = iban[2:4]
    bban     = iban[4:]

    # Assemble digit string
    digits = ""
    for ch in bban.upper():
        if ch.isdigit():
            digits += ch
        else:
            digits += str(ord(ch) - ord("A") + 10)
    for ch in code:
        digits += str(ord(ch) - ord("A") + 10)
    digits += checksum

    # Calculate checksum
    checksum = 98 - mod97(digits)
    return fill0(str(checksum), 2)

def fill_account(country, account):
    """Fill the account number part of IBAN with leading zeros."""
    return fill0(account, country.acc_lng())

def invalid_part(form_list, iban_part):
    """Check if syntax of the part of IBAN is invalid."""
    for lng, typ in form_list:
        if lng > len(iban_part):
            lng = len(iban_part)
        for ch in iban_part[:lng]:
            a = ("A" <= ch <= "Z")
            n = ch.isdigit()
            c = n or a or ("a" <= ch <= "z")
            if (not c and typ == "c") or \
               (not a and typ == "a") or \
               (not n and typ == "n"):
                return 1
        iban_part = iban_part[lng:]
    return 0

def invalid_bank(country, bank):
    """Check if syntax of the bank/branch code part of IBAN is invalid."""
    return len(bank) != country.bank_lng() or \
           invalid_part(country.bank, bank)

def invalid_account(country, account):
    """Check if syntax of the account number part of IBAN is invalid."""
    return len(account) > country.acc_lng() or \
           invalid_part(country.acc, fill_account(country, account))

def calc_iban(country, bank, account, alternative = 0):
    """Calculate the checksum and assemble the IBAN."""
    account = fill_account(country, account)
    checksum = checksum_iban(country.code + "00" + bank + account)
    if alternative:
        checksum = fill0(str(mod97(checksum)), 2)
    return country.code + checksum + bank + account

def iban_okay(iban):
    """Check the checksum of an IBAN."""
    return checksum_iban(iban) == "97"

class IBANError(Exception):
    def __init__(self, errmsg):
        Exception.__init__(self, errmsg)

def create_iban(code, bank, account, alternative = 0):
    """Check the input, calculate the checksum and assemble the IBAN.

    Return the calculated IBAN.
    Return the alternative IBAN if alternative is true.
    Raise an IBANError exception if the input is not correct.
    """
    err = None
    country = country_data(code)
    if not country:
        err = "Unknown Country Code: %s" % code
    elif len(bank) != country.bank_lng():
        err = "Bank/Branch Code length %s is not correct for %s (%s)" % \
              (len(bank), country.name, country.bank_lng())
    elif invalid_bank(country, bank):
        err = "Bank/Branch Code %s is not correct for %s" % \
              (bank, country.name)
    elif len(account) > country.acc_lng():
        err = "Account Number length %s is not correct for %s (%s)" % \
              (len(account), country.name, country.acc_lng())
    elif invalid_account(country, account):
        err = "Account Number %s is not correct for %s" % \
              (account, country.name)
    if err:
        raise IBANError(err)
    return calc_iban(country, bank, account, alternative)

def check_iban(iban):
    """Check the syntax and the checksum of an IBAN.

    Return the parts of the IBAN: Country Code, Checksum, Bank/Branch Code and
    Account number.
    Raise an IBANError exception if the input is not correct.
    """
    err = None
    code     = iban[:2]
    checksum = iban[2:4]
    bban     = iban[4:]
    country = country_data(code)
    if not country:
        err = "Unknown Country Code: %s" % code
    elif len(iban) != country.total_lng():
        err = "IBAN length %s is not correct for %s (%s)" % \
              (len(iban), country.name, country.total_lng())
    else:
        bank_lng = country.bank_lng()
        bank     = bban[:bank_lng]
        account  = bban[bank_lng:]
        if invalid_bank(country, bank):
            err = "Bank/Branch Code %s is not correct for %s" % \
                  (bank, country.name)
        elif invalid_account(country, account):
            err = "Account Number %s is not correct for %s" % \
                  (account, country.name)
        elif not(checksum.isdigit()):
            err = "IBAN Checksum %s is not numeric" % checksum
        elif not iban_okay(iban):
            err = "Incorrect IBAN: %s >> %s %s %s %s" % \
                  (iban, code, checksum, bank, account)
    if err:
        raise IBANError(err)
    return code, checksum, bank, account

def print_new_iban(code, bank, account):
    """Check the input, calculate the checksum, assemble and print the IBAN."""
    try:
        iban = create_iban(code, bank, account)
    except IBANError, err:
        print err
        return ""
    print "  Correct IBAN: %s << %s ?? %s %s" % (iban, code, bank, account)
    return iban

def print_iban_parts(iban):
    """Check the syntax and the checksum of an IBAN and print the parts."""
    try:
        code, checksum, bank, account = check_iban(iban)
    except IBANError, err:
        print err
        return ()
    print "  Correct IBAN: %s >> %s %s %s %s" % (iban, code, checksum,
                                                 bank, account)
    return code, checksum, bank, account

def print_format():
    """Print a table with the country specific iban format."""
    print "IBAN-Format (a = A-Z, n = 0-9, c = A-Z/a-z/0-9):"
    print "                    | Bank/Branch-Code      | Account Number"
    print " Country       Code | check1  bank  branch  |" + \
          " check2 number check3"
    print "--------------------|-----------------------|" + \
          "---------------------"
    for idx in country_index_table():
        country = iban_data[idx]
        if len(country.name) <= 14:
            print country.name.ljust(14), "|", country.code, "|",
        else:
            print country.name
            print "               |", country.code, "|",
        for lng, typ in country.bank:
            if lng:
                print str(lng).rjust(3), typ.ljust(2),
            else:
                print "  -   ",
        print " |",
        for lng, typ in country.acc:
            if lng:
                print str(lng).rjust(3), typ.ljust(2),
            else:
                print "  -   ",
        print

def print_test_data(*data):
    """Print a table with iban test data."""
    for code, bank, account, checksum in data:
        created_iban = print_new_iban(code, bank, account)
        if created_iban:
            iban = code + checksum + bank + \
                   fill_account(country_data(code), account)
            print_iban_parts(iban)
            if iban != created_iban:
                if iban == create_iban(code, bank, account, 1):
                    print "  Alternative IBAN"
                else:
                    print "  Changed IBAN"

def print_examples():
    print "IBAN-Examples:"
    print_test_data(("AD", "00012030",    "200359100100",         "12"),
                    ("AL", "21211009",    "0000000235698741",     "47"),
                    ("AT", "19043",       "00234573201",          "61"),
                    ("BA", "129007",      "9401028494",           "39"),
                    ("BE", "539",         "007547034",            "68"),
                    ("BG", "BNBG9661",    "1020345678",           "80"),
                    ("CH", "00762",       "011623852957",         "93"),
                    ("CY", "00200128",    "0000001200527600",     "17"),
                    ("CZ", "0800",        "0000192000145399",     "65"),
                    ("DE", "37040044",    "0532013000",           "89"),
                    ("DK", "0040",        "0440116243",           "50"),
                    ("EE", "22",          "00221020145685",       "38"),
                    ("ES", "21000418",    "450200051332",         "91"),
                    ("FI", "123456",      "00000785",             "21"),
                    ("FO", "6460",        "0001631634",           "62"),
                    ("FR", "2004101005",  "0500013M02606",        "14"),
                    ("GB", "NWBK601613",  "31926819",             "29"),
                    ("GE", "NB",          "0000000101904917",     "29"),
                    ("GI", "NWBK",        "000000007099453",      "75"),
                    ("GL", "6471",        "0001000206",           "89"),
                    ("GR", "0110125",     "0000000012300695",     "16"),
                    ("HR", "1001005",     "1863000160",           "12"),
                    ("HU", "1177301",     "61111101800000000",    "42"),
                    ("IE", "AIBK931152",  "12345678",             "29"),
                    ("IL", "010800",      "0000099999999",        "62"),
                    ("IS", "0159",        "260076545510730339",   "14"),
                    ("IT", "X0542811101", "000000123456",         "60"),
                    ("KW", "CBKU",        "0000000000001234560101", "81"),
                    ("KZ", "125",         "KZT5004100100",        "86"),
                    ("LB", "0999",        "00000001001901229114", "62"),
                    ("LI", "08810",       "0002324013AA",         "21"),
                    ("LT", "10000",       "11101001000",          "12"),
                    ("LU", "001",         "9400644750000",        "28"),
                    ("LV", "BANK",        "0000435195001",        "80"),
                    ("MC", "1273900070",  "0011111000h79",        "11"),
                    ("ME", "505",         "000012345678951",      "25"),
                    ("MK", "250",         "120000058984",         "07"),
                    ("MR", "0002000101",  "0000123456753",        "13"),
                    ("MT", "MALT01100",   "0012345MTLCAST001S",   "84"),
                    ("MU", "BOMM0101",    "101030300200000MUR",   "17"),
                    ("NL", "ABNA",        "0417164300",           "91"),
                    ("NO", "8601",        "1117947",              "93"),
                    ("PL", "10901014",    "0000071219812874",     "61"),
                    ("PT", "00020123",    "1234567890154",        "50"),
                    ("RO", "AAAA",        "1B31007593840000",     "49"),
                    ("RS", "260",         "005601001611379",      "35"),
                    ("SA", "80",          "000000608010167519",   "03"),
                    ("SE", "500",         "00000058398257466",    "45"),
                    ("SI", "19100",       "0000123438",           "56"),
                    ("SK", "1200",        "0000198742637541",     "31"),
                    ("SM", "U0322509800", "000000270100",         "86"),
                    ("TN", "10006",       "035183598478831",      "59"),
                    ("TR", "00061",       "00519786457841326",    "33"))

def print_test():
    print "IBAN-Test:"
    print_test_data(("XY", "1",           "2",                    "33"),
                    ("AD", "11112222",    "C3C3C3C3C3C3",         "11"),
                    ("AD", "1111222",     "C3C3C3C3C3C3",         "11"),
                    ("AD", "X1112222",    "C3C3C3C3C3C3",         "11"),
                    ("AD", "111@2222",    "C3C3C3C3C3C3",         "11"),
                    ("AD", "1111X222",    "C3C3C3C3C3C3",         "11"),
                    ("AD", "1111222@",    "C3C3C3C3C3C3",         "11"),
                    ("AD", "11112222",    "@3C3C3C3C3C3",         "11"),
                    ("AD", "11112222",    "C3C3C3C3C3C@",         "11"),
                    ("AL", "11111111",    "B2B2B2B2B2B2B2B2",     "54"),
                    ("AL", "1111111",     "B2B2B2B2B2B2B2B2",     "54"),
                    ("AL", "X1111111",    "B2B2B2B2B2B2B2B2",     "54"),
                    ("AL", "1111111@",    "B2B2B2B2B2B2B2B2",     "54"),
                    ("AL", "11111111",    "@2B2B2B2B2B2B2B2",     "54"),
                    ("AL", "11111111",    "B2B2B2B2B2B2B2B@",     "54"),
                    ("AT", "11111",       "22222222222",          "17"),
                    ("AT", "1111",        "22222222222",          "17"),
                    ("AT", "X1111",       "22222222222",          "17"),
                    ("AT", "1111@",       "22222222222",          "17"),
                    ("AT", "11111",       "X2222222222",          "17"),
                    ("AT", "11111",       "2222222222@",          "17"),
                    ("BA", "111222",      "3333333344",           "79"),
                    ("BA", "11122",       "3333333344",           "79"),
                    ("BA", "X11222",      "3333333344",           "79"),
                    ("BA", "11@222",      "3333333344",           "79"),
                    ("BA", "111X22",      "3333333344",           "79"),
                    ("BA", "11122@",      "3333333344",           "79"),
                    ("BA", "111222",      "X333333344",           "79"),
                    ("BA", "111222",      "3333333@44",           "79"),
                    ("BA", "111222",      "33333333X4",           "79"),
                    ("BA", "111222",      "333333334@",           "79"),
                    ("BE", "111",         "222222233",            "93"),
                    ("BE", "11",          "222222233",            "93"),
                    ("BE", "X11",         "222222233",            "93"),
                    ("BE", "11@",         "222222233",            "93"),
                    ("BE", "111",         "X22222233",            "93"),
                    ("BE", "111",         "222222@33",            "93"),
                    ("BE", "111",         "2222222X3",            "93"),
                    ("BE", "111",         "22222223@",            "93"),
                    ("BG", "AAAA2222",    "33D4D4D4D4",           "20"),
                    ("BG", "AAAA222",     "33D4D4D4D4",           "20"),
                    ("BG", "8AAA2222",    "33D4D4D4D4",           "20"),
                    ("BG", "AAA@2222",    "33D4D4D4D4",           "20"),
                    ("BG", "AAAAX222",    "33D4D4D4D4",           "20"),
                    ("BG", "AAAA222@",    "33D4D4D4D4",           "20"),
                    ("BG", "AAAA2222",    "X3D4D4D4D4",           "20"),
                    ("BG", "AAAA2222",    "3@D4D4D4D4",           "20"),
                    ("BG", "AAAA2222",    "33@4D4D4D4",           "20"),
                    ("BG", "AAAA2222",    "33D4D4D4D@",           "20"),
                    ("CH", "11111",       "B2B2B2B2B2B2",         "60"),
                    ("CH", "1111",        "B2B2B2B2B2B2",         "60"),
                    ("CH", "X1111",       "B2B2B2B2B2B2",         "60"),
                    ("CH", "1111@",       "B2B2B2B2B2B2",         "60"),
                    ("CH", "11111",       "@2B2B2B2B2B2",         "60"),
                    ("CH", "11111",       "B2B2B2B2B2B@",         "60"),
                    ("CY", "11122222",    "C3C3C3C3C3C3C3C3",     "29"),
                    ("CY", "1112222",     "C3C3C3C3C3C3C3C3",     "29"),
                    ("CY", "X1122222",    "C3C3C3C3C3C3C3C3",     "29"),
                    ("CY", "11@22222",    "C3C3C3C3C3C3C3C3",     "29"),
                    ("CY", "111X2222",    "C3C3C3C3C3C3C3C3",     "29"),
                    ("CY", "1112222@",    "C3C3C3C3C3C3C3C3",     "29"),
                    ("CY", "11122222",    "@3C3C3C3C3C3C3C3",     "29"),
                    ("CY", "11122222",    "C3C3C3C3C3C3C3C@",     "29"),
                    ("CZ", "1111",        "2222222222222222",     "68"),
                    ("CZ", "111",         "2222222222222222",     "68"),
                    ("CZ", "X111",        "2222222222222222",     "68"),
                    ("CZ", "111@",        "2222222222222222",     "68"),
                    ("CZ", "1111",        "X222222222222222",     "68"),
                    ("CZ", "1111",        "222222222222222@",     "68"),
                    ("DE", "11111111",    "2222222222",           "16"),
                    ("DE", "1111111",     "2222222222",           "16"),
                    ("DE", "X1111111",    "2222222222",           "16"),
                    ("DE", "1111111@",    "2222222222",           "16"),
                    ("DE", "11111111",    "X222222222",           "16"),
                    ("DE", "11111111",    "222222222@",           "16"),
                    ("DK", "1111",        "2222222223",           "79"),
                    ("DK", "111",         "2222222223",           "79"),
                    ("DK", "X111",        "2222222223",           "79"),
                    ("DK", "111@",        "2222222223",           "79"),
                    ("DK", "1111",        "X222222223",           "79"),
                    ("DK", "1111",        "22222222@3",           "79"),
                    ("DK", "1111",        "222222222X",           "79"),
                    ("EE", "11",          "22333333333334",       "96"),
                    ("EE", "1",           "22333333333334",       "96"),
                    ("EE", "X1",          "22333333333334",       "96"),
                    ("EE", "1@",          "22333333333334",       "96"),
                    ("EE", "11",          "X2333333333334",       "96"),
                    ("EE", "11",          "2@333333333334",       "96"),
                    ("EE", "11",          "22X33333333334",       "96"),
                    ("EE", "11",          "223333333333@4",       "96"),
                    ("EE", "11",          "2233333333333X",       "96"),
                    ("ES", "11112222",    "334444444444",         "71"),
                    ("ES", "1111222",     "334444444444",         "71"),
                    ("ES", "X1112222",    "334444444444",         "71"),
                    ("ES", "111@2222",    "334444444444",         "71"),
                    ("ES", "1111X222",    "334444444444",         "71"),
                    ("ES", "1111222@",    "334444444444",         "71"),
                    ("ES", "11112222",    "X34444444444",         "71"),
                    ("ES", "11112222",    "3@4444444444",         "71"),
                    ("ES", "11112222",    "33X444444444",         "71"),
                    ("ES", "11112222",    "33444444444@",         "71"),
                    ("FI", "111111",      "22222223",             "68"),
                    ("FI", "11111",       "22222223",             "68"),
                    ("FI", "X11111",      "22222223",             "68"),
                    ("FI", "11111@",      "22222223",             "68"),
                    ("FI", "111111",      "X2222223",             "68"),
                    ("FI", "111111",      "222222@3",             "68"),
                    ("FI", "111111",      "2222222X",             "68"),
                    ("FO", "1111",        "2222222223",           "49"),
                    ("FO", "111",         "2222222223",           "49"),
                    ("FO", "X111",        "2222222223",           "49"),
                    ("FO", "111@",        "2222222223",           "49"),
                    ("FO", "1111",        "X222222223",           "49"),
                    ("FO", "1111",        "22222222@3",           "49"),
                    ("FO", "1111",        "222222222X",           "49"),
                    ("FR", "1111122222",  "C3C3C3C3C3C44",        "44"),
                    ("FR", "111112222",   "C3C3C3C3C3C44",        "44"),
                    ("FR", "X111122222",  "C3C3C3C3C3C44",        "44"),
                    ("FR", "1111@22222",  "C3C3C3C3C3C44",        "44"),
                    ("FR", "11111X2222",  "C3C3C3C3C3C44",        "44"),
                    ("FR", "111112222@",  "C3C3C3C3C3C44",        "44"),
                    ("FR", "1111122222",  "@3C3C3C3C3C44",        "44"),
                    ("FR", "1111122222",  "C3C3C3C3C3@44",        "44"),
                    ("FR", "1111122222",  "C3C3C3C3C3CX4",        "44"),
                    ("FR", "1111122222",  "C3C3C3C3C3C4@",        "44"),
                    ("GB", "AAAA222222",  "33333333",             "45"),
                    ("GB", "AAAA22222",   "33333333",             "45"),
                    ("GB", "8AAA222222",  "33333333",             "45"),
                    ("GB", "AAA@222222",  "33333333",             "45"),
                    ("GB", "AAAAX22222",  "33333333",             "45"),
                    ("GB", "AAAA22222@",  "33333333",             "45"),
                    ("GB", "AAAA222222",  "X3333333",             "45"),
                    ("GB", "AAAA222222",  "3333333@",             "45"),
                    ("GE", "AA",          "2222222222222222",     "98"),
                    ("GE", "A",           "2222222222222222",     "98"),
                    ("GE", "8A",          "2222222222222222",     "98"),
                    ("GE", "A@",          "2222222222222222",     "98"),
                    ("GE", "AA",          "X222222222222222",     "98"),
                    ("GE", "AA",          "222222222222222@",     "98"))
    print_test_data(("GI", "AAAA",        "B2B2B2B2B2B2B2B",      "72"),
                    ("GI", "AAA",         "B2B2B2B2B2B2B2B",      "72"),
                    ("GI", "8AAA",        "B2B2B2B2B2B2B2B",      "72"),
                    ("GI", "AAA@",        "B2B2B2B2B2B2B2B",      "72"),
                    ("GI", "AAAA",        "@2B2B2B2B2B2B2B",      "72"),
                    ("GI", "AAAA",        "B2B2B2B2B2B2B2@",      "72"),
                    ("GL", "1111",        "2222222223",           "49"),
                    ("GL", "111",         "2222222223",           "49"),
                    ("GL", "X111",        "2222222223",           "49"),
                    ("GL", "111@",        "2222222223",           "49"),
                    ("GL", "1111",        "X222222223",           "49"),
                    ("GL", "1111",        "22222222@3",           "49"),
                    ("GL", "1111",        "222222222X",           "49"),
                    ("GR", "1112222",     "C3C3C3C3C3C3C3C3",     "61"),
                    ("GR", "111222",      "C3C3C3C3C3C3C3C3",     "61"),
                    ("GR", "X112222",     "C3C3C3C3C3C3C3C3",     "61"),
                    ("GR", "11@2222",     "C3C3C3C3C3C3C3C3",     "61"),
                    ("GR", "111X222",     "C3C3C3C3C3C3C3C3",     "61"),
                    ("GR", "111222@",     "C3C3C3C3C3C3C3C3",     "61"),
                    ("GR", "1112222",     "@3C3C3C3C3C3C3C3",     "61"),
                    ("GR", "1112222",     "C3C3C3C3C3C3C3C@",     "61"),
                    ("HR", "1111111",     "2222222222",           "94"),
                    ("HR", "111111",      "2222222222",           "94"),
                    ("HR", "X111111",     "2222222222",           "94"),
                    ("HR", "111111@",     "2222222222",           "94"),
                    ("HR", "1111111",     "X222222222",           "94"),
                    ("HR", "1111111",     "222222222@",           "94"),
                    ("HU", "1112222",     "34444444444444445",    "35"),
                    ("HU", "111222",      "34444444444444445",    "35"),
                    ("HU", "X112222",     "34444444444444445",    "35"),
                    ("HU", "11@2222",     "34444444444444445",    "35"),
                    ("HU", "111X222",     "34444444444444445",    "35"),
                    ("HU", "111222@",     "34444444444444445",    "35"),
                    ("HU", "1112222",     "X4444444444444445",    "35"),
                    ("HU", "1112222",     "3X444444444444445",    "35"),
                    ("HU", "1112222",     "344444444444444@5",    "35"),
                    ("HU", "1112222",     "3444444444444444X",    "35"),
                    ("IE", "AAAA222222",  "33333333",             "18"),
                    ("IE", "AAAA22222",   "33333333",             "18"),
                    ("IE", "8AAA222222",  "33333333",             "18"),
                    ("IE", "AAA@222222",  "33333333",             "18"),
                    ("IE", "AAAAX22222",  "33333333",             "18"),
                    ("IE", "AAAA22222@",  "33333333",             "18"),
                    ("IE", "AAAA222222",  "X3333333",             "18"),
                    ("IE", "AAAA222222",  "3333333@",             "18"),
                    ("IL", "111222",      "3333333344",           "64"),
                    ("IL", "11122",       "3333333344",           "64"),
                    ("IL", "X11222",      "3333333344",           "64"),
                    ("IL", "11@222",      "3333333344",           "64"),
                    ("IL", "111X22",      "3333333344",           "64"),
                    ("IL", "11122@",      "3333333344",           "64"),
                    ("IL", "111222",      "X333333333333",        "64"),
                    ("IL", "111222",      "333333333333@",        "64"),
                    ("IS", "1111",        "223333333333333333",   "12"),
                    ("IS", "111",         "223333333333333333",   "12"),
                    ("IS", "X111",        "223333333333333333",   "12"),
                    ("IS", "111@",        "223333333333333333",   "12"),
                    ("IS", "1111",        "X23333333333333333",   "12"),
                    ("IS", "1111",        "2@3333333333333333",   "12"),
                    ("IS", "1111",        "22X333333333333333",   "12"),
                    ("IS", "1111",        "22333333333333333@",   "12"),
                    ("IT", "A2222233333", "D4D4D4D4D4D4",         "43"),
                    ("IT", "A222223333",  "D4D4D4D4D4D4",         "43"),
                    ("IT", "82222233333", "D4D4D4D4D4D4",         "43"),
                    ("IT", "AX222233333", "D4D4D4D4D4D4",         "43"),
                    ("IT", "A2222@33333", "D4D4D4D4D4D4",         "43"),
                    ("IT", "A22222X3333", "D4D4D4D4D4D4",         "43"),
                    ("IT", "A222223333@", "D4D4D4D4D4D4",         "43"),
                    ("IT", "A2222233333", "@4D4D4D4D4D4",         "43"),
                    ("IT", "A2222233333", "D4D4D4D4D4D@",         "43"),
                    ("KW", "AAAA",        "B2B2B2B2B2B2B2B2B2B2B2", "93"),
                    ("KW", "AAA",         "B2B2B2B2B2B2B2B2B2B2B2", "93"),
                    ("KW", "8AAA",        "B2B2B2B2B2B2B2B2B2B2B2", "93"),
                    ("KW", "AAA@",        "B2B2B2B2B2B2B2B2B2B2B2", "93"),
                    ("KW", "AAAA",        "@2B2B2B2B2B2B2B2B2B2B2", "93"),
                    ("KW", "AAAA",        "B2B2B2B2B2B2B2B2B2B2B@", "93"),
                    ("KZ", "111",         "B2B2B2B2B2B2B",        "21"),
                    ("KZ", "11",          "B2B2B2B2B2B2B",        "21"),
                    ("KZ", "X11",         "B2B2B2B2B2B2B",        "21"),
                    ("KZ", "11@",         "B2B2B2B2B2B2B",        "21"),
                    ("KZ", "111",         "@2B2B2B2B2B2B",        "21"),
                    ("KZ", "111",         "B2B2B2B2B2B2@",        "21"),
                    ("LB", "1111",        "B2B2B2B2B2B2B2B2B2B2", "88"),
                    ("LB", "111",         "B2B2B2B2B2B2B2B2B2B2", "88"),
                    ("LB", "X111",        "B2B2B2B2B2B2B2B2B2B2", "88"),
                    ("LB", "111@",        "B2B2B2B2B2B2B2B2B2B2", "88"),
                    ("LB", "1111",        "@2B2B2B2B2B2B2B2B2B2", "88"),
                    ("LB", "1111",        "B2B2B2B2B2B2B2B2B2B@", "88"),
                    ("LI", "11111",       "B2B2B2B2B2B2",         "73"),
                    ("LI", "1111",        "B2B2B2B2B2B2",         "73"),
                    ("LI", "X1111",       "B2B2B2B2B2B2",         "73"),
                    ("LI", "1111@",       "B2B2B2B2B2B2",         "73"),
                    ("LI", "11111",       "@2B2B2B2B2B2",         "73"),
                    ("LI", "11111",       "B2B2B2B2B2B@",         "73"),
                    ("LT", "11111",       "22222222222",          "15"),
                    ("LT", "1111",        "22222222222",          "15"),
                    ("LT", "X1111",       "22222222222",          "15"),
                    ("LT", "1111@",       "22222222222",          "15"),
                    ("LT", "11111",       "X2222222222",          "15"),
                    ("LT", "11111",       "2222222222@",          "15"),
                    ("LU", "111",         "B2B2B2B2B2B2B",        "27"),
                    ("LU", "11",          "B2B2B2B2B2B2B",        "27"),
                    ("LU", "X11",         "B2B2B2B2B2B2B",        "27"),
                    ("LU", "11@",         "B2B2B2B2B2B2B",        "27"),
                    ("LU", "111",         "@2B2B2B2B2B2B",        "27"),
                    ("LU", "111",         "B2B2B2B2B2B2@",        "27"),
                    ("LV", "AAAA",        "B2B2B2B2B2B2B",        "86"),
                    ("LV", "AAA",         "B2B2B2B2B2B2B",        "86"),
                    ("LV", "8AAA",        "B2B2B2B2B2B2B",        "86"),
                    ("LV", "AAA@",        "B2B2B2B2B2B2B",        "86"),
                    ("LV", "AAAA",        "@2B2B2B2B2B2B",        "86"),
                    ("LV", "AAAA",        "B2B2B2B2B2B2@",        "86"),
                    ("MC", "1111122222",  "C3C3C3C3C3C44",        "26"),
                    ("MC", "111112222",   "C3C3C3C3C3C44",        "26"),
                    ("MC", "X111122222",  "C3C3C3C3C3C44",        "26"),
                    ("MC", "1111@22222",  "C3C3C3C3C3C44",        "26"),
                    ("MC", "11111X2222",  "C3C3C3C3C3C44",        "26"),
                    ("MC", "111112222@",  "C3C3C3C3C3C44",        "26"),
                    ("MC", "1111122222",  "@3C3C3C3C3C44",        "26"),
                    ("MC", "1111122222",  "C3C3C3C3C3@44",        "26"),
                    ("MC", "1111122222",  "C3C3C3C3C3CX4",        "26"),
                    ("MC", "1111122222",  "C3C3C3C3C3C4@",        "26"),
                    ("ME", "111",         "222222222222233",      "38"),
                    ("ME", "11",          "222222222222233",      "38"),
                    ("ME", "X11",         "222222222222233",      "38"),
                    ("ME", "11@",         "222222222222233",      "38"),
                    ("ME", "111",         "X22222222222233",      "38"),
                    ("ME", "111",         "222222222222@33",      "38"),
                    ("ME", "111",         "2222222222222X3",      "38"),
                    ("ME", "111",         "22222222222223@",      "38"),
                    ("MK", "111",         "B2B2B2B2B233",         "41"),
                    ("MK", "11",          "B2B2B2B2B233",         "41"),
                    ("MK", "X11",         "B2B2B2B2B233",         "41"),
                    ("MK", "11@",         "B2B2B2B2B233",         "41"),
                    ("MK", "111",         "@2B2B2B2B233",         "41"),
                    ("MK", "111",         "B2B2B2B2B@33",         "41"),
                    ("MK", "111",         "B2B2B2B2B2X3",         "41"),
                    ("MK", "111",         "B2B2B2B2B23@",         "41"),
                    ("MR", "1111122222",  "3333333333344",        "21"),
                    ("MR", "111112222",   "3333333333344",        "21"),
                    ("MR", "X111122222",  "3333333333344",        "21"),
                    ("MR", "1111@22222",  "3333333333344",        "21"),
                    ("MR", "11111X2222",  "3333333333344",        "21"),
                    ("MR", "111112222@",  "3333333333344",        "21"),
                    ("MR", "1111122222",  "X333333333344",        "21"),
                    ("MR", "1111122222",  "3333333333@44",        "21"),
                    ("MR", "1111122222",  "33333333333X4",        "21"),
                    ("MR", "1111122222",  "333333333334@",        "21"),
                    ("MT", "AAAA22222",   "C3C3C3C3C3C3C3C3C3",   "39"),
                    ("MT", "AAAA2222",    "C3C3C3C3C3C3C3C3C3",   "39"),
                    ("MT", "8AAA22222",   "C3C3C3C3C3C3C3C3C3",   "39"),
                    ("MT", "AAA@22222",   "C3C3C3C3C3C3C3C3C3",   "39"),
                    ("MT", "AAAAX2222",   "C3C3C3C3C3C3C3C3C3",   "39"),
                    ("MT", "AAAA2222@",   "C3C3C3C3C3C3C3C3C3",   "39"),
                    ("MT", "AAAA22222",   "@3C3C3C3C3C3C3C3C3",   "39"),
                    ("MT", "AAAA22222",   "C3C3C3C3C3C3C3C3C@",   "39"))
    print_test_data(("MU", "AAAA2222",    "333333333333333DDD",   "37"),
                    ("MU", "AAAA222",     "333333333333333DDD",   "37"),
                    ("MU", "8AAA2222",    "333333333333333DDD",   "37"),
                    ("MU", "AAA@2222",    "333333333333333DDD",   "37"),
                    ("MU", "AAAAX222",    "333333333333333DDD",   "37"),
                    ("MU", "AAAA222@",    "333333333333333DDD",   "37"),
                    ("MU", "AAAA2222",    "X33333333333333DDD",   "37"),
                    ("MU", "AAAA2222",    "33333333333333@DDD",   "37"),
                    ("MU", "AAAA2222",    "3333333333333338DD",   "37"),
                    ("MU", "AAAA2222",    "333333333333333DD@",   "37"),
                    ("NL", "AAAA",        "2222222222",           "57"),
                    ("NL", "AAA",         "2222222222",           "57"),
                    ("NL", "8AAA",        "2222222222",           "57"),
                    ("NL", "AAA@",        "2222222222",           "57"),
                    ("NL", "AAAA",        "X222222222",           "57"),
                    ("NL", "AAAA",        "222222222@",           "57"),
                    ("NO", "1111",        "2222223",              "40"),
                    ("NO", "111",         "2222223",              "40"),
                    ("NO", "X111",        "2222223",              "40"),
                    ("NO", "111@",        "2222223",              "40"),
                    ("NO", "1111",        "X222223",              "40"),
                    ("NO", "1111",        "22222@3",              "40"),
                    ("NO", "1111",        "222222X",              "40"),
                    ("PL", "11111111",    "2222222222222222",     "84"),
                    ("PL", "1111111",     "2222222222222222",     "84"),
                    ("PL", "X1111111",    "2222222222222222",     "84"),
                    ("PL", "1111111@",    "2222222222222222",     "84"),
                    ("PL", "11111111",    "X222222222222222",     "84"),
                    ("PL", "11111111",    "222222222222222@",     "84"),
                    ("PT", "11112222",    "3333333333344",        "59"),
                    ("PT", "1111222",     "3333333333344",        "59"),
                    ("PT", "X1112222",    "3333333333344",        "59"),
                    ("PT", "111@2222",    "3333333333344",        "59"),
                    ("PT", "1111X222",    "3333333333344",        "59"),
                    ("PT", "1111222@",    "3333333333344",        "59"),
                    ("PT", "11112222",    "X333333333344",        "59"),
                    ("PT", "11112222",    "3333333333@44",        "59"),
                    ("PT", "11112222",    "33333333333X4",        "59"),
                    ("PT", "11112222",    "333333333334@",        "59"),
                    ("RO", "AAAA",        "B2B2B2B2B2B2B2B2",     "91"),
                    ("RO", "AAA",         "B2B2B2B2B2B2B2B2",     "91"),
                    ("RO", "8AAA",        "B2B2B2B2B2B2B2B2",     "91"),
                    ("RO", "AAA@",        "B2B2B2B2B2B2B2B2",     "91"),
                    ("RO", "AAAA",        "@2B2B2B2B2B2B2B2",     "91"),
                    ("RO", "AAAA",        "B2B2B2B2B2B2B2B@",     "91"),
                    ("RS", "111",         "222222222222233",      "48"),
                    ("RS", "11",          "222222222222233",      "48"),
                    ("RS", "X11",         "222222222222233",      "48"),
                    ("RS", "11@",         "222222222222233",      "48"),
                    ("RS", "111",         "X22222222222233",      "48"),
                    ("RS", "111",         "222222222222@33",      "48"),
                    ("RS", "111",         "2222222222222X3",      "48"),
                    ("RS", "111",         "22222222222223@",      "48"),
                    ("SA", "11",          "B2B2B2B2B2B2B2B2B2",   "46"),
                    ("SA", "1",           "B2B2B2B2B2B2B2B2B2",   "46"),
                    ("SA", "X1",          "B2B2B2B2B2B2B2B2B2",   "46"),
                    ("SA", "1@",          "B2B2B2B2B2B2B2B2B2",   "46"),
                    ("SA", "11",          "@2B2B2B2B2B2B2B2B2",   "46"),
                    ("SA", "11",          "B2B2B2B2B2B2B2B2B@",   "46"),
                    ("SE", "111",         "22222222222222223",    "32"),
                    ("SE", "11",          "22222222222222223",    "32"),
                    ("SE", "X11",         "22222222222222223",    "32"),
                    ("SE", "11@",         "22222222222222223",    "32"),
                    ("SE", "111",         "X2222222222222223",    "32"),
                    ("SE", "111",         "222222222222222@3",    "32"),
                    ("SE", "111",         "2222222222222222X",    "32"),
                    ("SI", "11111",       "2222222233",           "92"),
                    ("SI", "1111",        "2222222233",           "92"),
                    ("SI", "X1111",       "2222222233",           "92"),
                    ("SI", "1111@",       "2222222233",           "92"),
                    ("SI", "11111",       "X222222233",           "92"),
                    ("SI", "11111",       "2222222@33",           "92"),
                    ("SI", "11111",       "22222222X3",           "92"),
                    ("SI", "11111",       "222222223@",           "92"),
                    ("SK", "1111",        "2222222222222222",     "66"),
                    ("SK", "111",         "2222222222222222",     "66"),
                    ("SK", "X111",        "2222222222222222",     "66"),
                    ("SK", "111@",        "2222222222222222",     "66"),
                    ("SK", "1111",        "X222222222222222",     "66"),
                    ("SK", "1111",        "222222222222222@",     "66"),
                    ("SM", "A2222233333", "D4D4D4D4D4D4",         "71"),
                    ("SM", "A222223333",  "D4D4D4D4D4D4",         "71"),
                    ("SM", "82222233333", "D4D4D4D4D4D4",         "71"),
                    ("SM", "AX222233333", "D4D4D4D4D4D4",         "71"),
                    ("SM", "A2222@33333", "D4D4D4D4D4D4",         "71"),
                    ("SM", "A22222X3333", "D4D4D4D4D4D4",         "71"),
                    ("SM", "A222223333@", "D4D4D4D4D4D4",         "71"),
                    ("SM", "A2222233333", "@4D4D4D4D4D4",         "71"),
                    ("SM", "A2222233333", "D4D4D4D4D4D@",         "71"),
                    ("TN", "11222",       "333333333333344",      "23"),
                    ("TN", "1122",        "333333333333344",      "23"),
                    ("TN", "X1222",       "333333333333344",      "23"),
                    ("TN", "1@222",       "333333333333344",      "23"),
                    ("TN", "11X22",       "333333333333344",      "23"),
                    ("TN", "1122@",       "333333333333344",      "23"),
                    ("TN", "11222",       "X33333333333344",      "23"),
                    ("TN", "11222",       "333333333333@44",      "23"),
                    ("TN", "11222",       "3333333333333X4",      "23"),
                    ("TN", "11222",       "33333333333334@",      "23"),
                    ("TR", "11111",       "BC3C3C3C3C3C3C3C3",    "95"),
                    ("TR", "1111",        "BC3C3C3C3C3C3C3C3",    "95"),
                    ("TR", "X1111",       "BC3C3C3C3C3C3C3C3",    "95"),
                    ("TR", "1111@",       "BC3C3C3C3C3C3C3C3",    "95"),
                    ("TR", "11111",       "@C3C3C3C3C3C3C3C3",    "95"),
                    ("TR", "11111",       "B@3C3C3C3C3C3C3C3",    "95"),
                    ("TR", "11111",       "BC3C3C3C3C3C3C3C@",    "95"),
                    ("DE", "12345678",    "5",                    "06"),
                    ("DE", "12345678",    "16",                   "97"),
                    ("DE", "12345678",    "16",                   "00"),
                    ("DE", "12345678",    "95",                   "98"),
                    ("DE", "12345678",    "95",                   "01"))

geoname = {'AD': '3041565',
 'AE': '290557',
 'AF': '1149361',
 'AG': '3576396',
 'AI': '3573511',
 'AL': '783754',
 'AM': '174982',
 'AN': '8505032',
 'AO': '3351879',
 'AQ': '6697173',
 'AR': '3865483',
 'AS': '5880801',
 'AT': '2782113',
 'AU': '2077456',
 'AW': '3577279',
 'AX': '661882',
 'AZ': '587116',
 'BA': '3277605',
 'BB': '3374084',
 'BD': '1210997',
 'BE': '2802361',
 'BF': '2361809',
 'BG': '732800',
 'BH': '290291',
 'BI': '433561',
 'BJ': '2395170',
 'BL': '3578476',
 'BM': '3573345',
 'BN': '1820814',
 'BO': '3923057',
 'BQ': '7626844',
 'BR': '3469034',
 'BS': '3572887',
 'BT': '1252634',
 'BV': '3371123',
 'BW': '933860',
 'BY': '630336',
 'BZ': '3582678',
 'CA': '6251999',
 'CC': '1547376',
 'CD': '203312',
 'CF': '239880',
 'CG': '2260494',
 'CH': '2658434',
 'CI': '2287781',
 'CK': '1899402',
 'CL': '3895114',
 'CM': '2233387',
 'CN': '1814991',
 'CO': '3686110',
 'CR': '3624060',
 'CS': '8505033',
 'CU': '3562981',
 'CV': '3374766',
 'CW': '7626836',
 'CX': '2078138',
 'CY': '146669',
 'CZ': '3077311',
 'DE': '2921044',
 'DJ': '223816',
 'DK': '2623032',
 'DM': '3575830',
 'DO': '3508796',
 'DZ': '2589581',
 'EC': '3658394',
 'EE': '453733',
 'EG': '357994',
 'EH': '2461445',
 'ER': '338010',
 'ES': '2510769',
 'ET': '337996',
 'FI': '660013',
 'FJ': '2205218',
 'FK': '3474414',
 'FM': '2081918',
 'FO': '2622320',
 'FR': '3017382',
 'GA': '2400553',
 'GB': '2635167',
 'GD': '3580239',
 'GE': '614540',
 'GF': '3381670',
 'GG': '3042362',
 'GH': '2300660',
 'GI': '2411586',
 'GL': '3425505',
 'GM': '2413451',
 'GN': '2420477',
 'GP': '3579143',
 'GQ': '2309096',
 'GR': '390903',
 'GS': '3474415',
 'GT': '3595528',
 'GU': '4043988',
 'GW': '2372248',
 'GY': '3378535',
 'HK': '1819730',
 'HM': '1547314',
 'HN': '3608932',
 'HR': '3202326',
 'HT': '3723988',
 'HU': '719819',
 'ID': '1643084',
 'IE': '2963597',
 'IL': '294640',
 'IM': '3042225',
 'IN': '1269750',
 'IO': '1282588',
 'IQ': '99237',
 'IR': '130758',
 'IS': '2629691',
 'ISO': 'geonameid',
 'IT': '3175395',
 'JE': '3042142',
 'JM': '3489940',
 'JO': '248816',
 'JP': '1861060',
 'KE': '192950',
 'KG': '1527747',
 'KH': '1831722',
 'KI': '4030945',
 'KM': '921929',
 'KN': '3575174',
 'KP': '1873107',
 'KR': '1835841',
 'KW': '285570',
 'KY': '3580718',
 'KZ': '1522867',
 'LA': '1655842',
 'LB': '272103',
 'LC': '3576468',
 'LI': '3042058',
 'LK': '1227603',
 'LR': '2275384',
 'LS': '932692',
 'LT': '597427',
 'LU': '2960313',
 'LV': '458258',
 'LY': '2215636',
 'MA': '2542007',
 'MC': '2993457',
 'MD': '617790',
 'ME': '3194884',
 'MF': '3578421',
 'MG': '1062947',
 'MH': '2080185',
 'MK': '718075',
 'ML': '2453866',
 'MM': '1327865',
 'MN': '2029969',
 'MO': '1821275',
 'MP': '4041468',
 'MQ': '3570311',
 'MR': '2378080',
 'MS': '3578097',
 'MT': '2562770',
 'MU': '934292',
 'MV': '1282028',
 'MW': '927384',
 'MX': '3996063',
 'MY': '1733045',
 'MZ': '1036973',
 'NA': '3355338',
 'NC': '2139685',
 'NE': '2440476',
 'NF': '2155115',
 'NG': '2328926',
 'NI': '3617476',
 'NL': '2750405',
 'NO': '3144096',
 'NP': '1282988',
 'NR': '2110425',
 'NU': '4036232',
 'NZ': '2186224',
 'OM': '286963',
 'PA': '3703430',
 'PE': '3932488',
 'PF': '4030656',
 'PG': '2088628',
 'PH': '1694008',
 'PK': '1168579',
 'PL': '798544',
 'PM': '3424932',
 'PN': '4030699',
 'PR': '4566966',
 'PS': '6254930',
 'PT': '2264397',
 'PW': '1559582',
 'PY': '3437598',
 'QA': '289688',
 'RE': '935317',
 'RO': '798549',
 'RS': '6290252',
 'RU': '2017370',
 'RW': '49518',
 'SA': '102358',
 'SB': '2103350',
 'SC': '241170',
 'SD': '366755',
 'SE': '2661886',
 'SG': '1880251',
 'SH': '3370751',
 'SI': '3190538',
 'SJ': '607072',
 'SK': '3057568',
 'SL': '2403846',
 'SM': '3168068',
 'SN': '2245662',
 'SO': '51537',
 'SR': '3382998',
 'SS': '7909807',
 'ST': '2410758',
 'SV': '3585968',
 'SX': '7609695',
 'SY': '163843',
 'SZ': '934841',
 'TC': '3576916',
 'TD': '2434508',
 'TF': '1546748',
 'TG': '2363686',
 'TH': '1605651',
 'TJ': '1220409',
 'TK': '4031074',
 'TL': '1966436',
 'TM': '1218197',
 'TN': '2464461',
 'TO': '4032283',
 'TR': '298795',
 'TT': '3573591',
 'TV': '2110297',
 'TW': '1668284',
 'TZ': '149590',
 'UA': '690791',
 'UG': '226074',
 'UM': '5854968',
 'US': '6252001',
 'UY': '3439705',
 'UZ': '1512440',
 'VA': '3164670',
 'VC': '3577815',
 'VE': '3625428',
 'VG': '3577718',
 'VI': '4796775',
 'VN': '1562822',
 'VU': '2134431',
 'WF': '4034749',
 'WS': '4034894',
 'XK': '831053',
 'YE': '69543',
 'YT': '1024031',
 'ZA': '953987',
 'ZM': '895949',
 'ZW': '878675'}

def decode(x):
    code, checksum, bank, account = check_iban(x)

    return (x, geoname[code], checksum, bank, account)
