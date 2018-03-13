import sys


EQUAL = 'equal'
SIMILAR = 'similar'  # https://pypi.python.org/pypi/abydos
TRANSLIT_SIMILAR = 'translit_similar'  # https://pypi.python.org/pypi/PyICU/


COMPARATOR_CHOICES = (
    (EQUAL, 'equal'),
    (SIMILAR, 'similar'),
    (TRANSLIT_SIMILAR, 'translit_similar'),
)


def equal(val1="", val2=""):
    if(val1==val2):
        return True
    else:
        return False


class Comparator(object):
    def equal(val1="", val2=""):
        if(val1==val2):
            return True
        else:
            return False

    def equalIgnoreCase(val1="", val2=""):
        if val1.lower() == val2.lower():
            return True
        else:
            return False

    def similar(val1="", val2=""):
        if  val1 in val2 or val2 in val1 :
            return True
        else:
            return False



def main(argv):
    try:
        #os.system("python " +argv[1]+" "+argv[2]+" "+argv[3])
        #mycode = "print('ss')"
        #res = exec("Comparator.equal(%s, %s)" % (argv[1], argv[2]))
        res = exec("equal(%s, %s)" % (argv[1], argv[2]))
        print(res)


    except Exception as err:
        print(err)


if __name__ == "__main__":
    main(sys.argv)