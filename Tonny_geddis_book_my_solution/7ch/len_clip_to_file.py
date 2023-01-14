
def main():
    fileObj = open('video_clip.txt', 'w')
    print('\ninput len clip, if no more clip, return - 0\n')

    while True:
        len_klip = input('len klip: ')
        if len_klip == '0':
            break
        fileObj.write(len_klip + '\n')
    fileObj.close()

main()