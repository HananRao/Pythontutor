import sys
_filename = sys.argv[0]
_usage = """
Usage: python %s 21.3 C
Takes an argument of a temperature and unit,
either C, F or K and prints it in the other two
""" % _filename


def C2F(C):
    # Convert Celsius to Fahrenheit
    F = 9.0 / 5 * C + 32
    return F


def F2C(F):
    # Convert Fahrenheit to Celsius
    C = 5.0 / 9 * (F - 32)
    return C


def C2K(C):
    # Convert Celsius to Kelvin
    K = C + 273.15
    return K


def K2C(K):
    # Convert Kelvin to Celsius
    C = K - 273.15
    return C


def F2K(F):
    # Convert Fahrenheit to Kelvin
    K = F2C(F) + 273.15
    return K


def K2F(K):
    # Convert Kelvin to Fahrenheit
    F = C2F(K - 273.15)
    return F

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(_usage)
        raise IndexError(
            'Both temperature and unit must be given on the command-line')
    if sys.argv[2] == 'C':
        C = float(sys.argv[1])
        print('%g F %g K' % (C2F(C), C2K(C)))
    elif sys.argv[2] == 'F':
        F = float(sys.argv[1])
        print('%g C %g K' % (F2C(F), F2K(F)))
    elif sys.argv[2] == 'K':
        K = float(sys.argv[1])
        print('%g F %g C' % (K2F(K), K2C(K)))

"""
Sample run:
python convert_temp2.py 21.3 C
70.34 F 294.45 K
python convert_temp2.py 21.3 F
-5.94444 C 267.206 K
python convert_temp2.py 21.3 K
-421.33 F -251.85 C
"""
