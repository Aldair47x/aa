import zmq
import sys

def loadFiles(path):
    files = {}
    dataDir = os.fsencode(path)
    for file in os.listdir(dataDir):
        fileName = os.fsdecode(file)
        print("Loading {}".format(fileName))
        files[fileName] = file
    return files

def main():

    if len(sys.argv) != 4:
        print("Error")
        exit()

    directory = sys.argv[2]
    port = sys.argv[1]

    context = zmq.Context()
    s = context.socket(zmq.REP)
    s.bind("tcp://*:{}".format(port))
    files = loadFiles(directory)

    while True:
        msg = s.recv_json()
        if msg["op"] == "list":
            s.send_json({"files": list(files.keys())})

if __name__ == '__main__':
    main()
