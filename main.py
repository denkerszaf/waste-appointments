import sys

from appointments import appointments

if __name__ == "__main__":
    if len(sys.argv) < 2 :
        print("Usage: " + sys.argv[0] + " inputfile outputfile")
        exit(1)
    appointments.main(sys.argv[1], sys.argv[2])
