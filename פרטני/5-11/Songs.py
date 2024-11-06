
def my_mp3_playlist(file):
    dict_songs = {}
    for row in file:
        dict_songs[row.split(";")[0]] = "".join([row.split(";")[2]])

    def second(vallue):
         return vallue[1]
    sorted_dict = sorted(dict_songs.items(), key=second)
    long_song = (sorted_dict[-1][0])
    number_of_songs = len(dict_songs.items())
    singers_dic = {} # singer : counter

    for row in file:
        singers_dic[row.split(";")[1]] =0

    for row in file:
        singers_dic[row.split(";")[1]] +=1
    def counter(value):
       return value[1]

    singer = sorted(singers_dic, key=counter)[0]

    write_file.write(f"{long_song}, {number_of_songs},{singer}")

    return (long_song,number_of_songs,singer)











with open("songs.txt", "r") as file:
    file_cont = file.readlines()

write_file = open("resault.txt", "w")

print(my_mp3_playlist(file_cont))

