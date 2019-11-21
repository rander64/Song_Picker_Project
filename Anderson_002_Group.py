"""\nRiley Anderson
Jessica Cobb
DSCI 15310
Section 002
5 November 2019\n"""

print(__doc__,"\n")

#import modules
import random
import urllib
import webbrowser
import pandas as pd

#import song data as dataframe
song_df = pd.read_csv('C:/Users/drand/Documents/Python Scripts/song_database.csv')

#lists of possible program inputs
a_list = ["pop", "alternative/indie", "alternative rock", "rock", "hard rock", "metal", "holiday", "r&b/soul", "hip-hop/rap", "country", "dance"]
b_list = ["fast", "medium", "slow"]
c_list = ["happy", "sad", "angry"]
d_list = ["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]

#subsets data from song_df
def song_picker (a, b, c, d):
    assert a.lower() in a_list
    assert b.lower() in b_list
    assert c.lower() in c_list
    assert d.lower() in d_list
    gen = song_df["genre"] == a.lower()
    tem = song_df["tempo"] == b.lower()
    moo = song_df["mood"] == c.lower()
    era = song_df["era"] == d.lower()
    all_filters = gen & tem & moo & era
    return song_df[all_filters]

#dataframe reduced to song list
song_list = song_df['song'].tolist()

#randomly select song based on user input; outputs the inputs, song, and lyrics; searches for song on Spotify   
def random_sel (a, b, c, d): 
    options = song_picker(a, b, c, d)
    options_list = options['song'].tolist()
    choice = random.choice(options_list)
    song_data = urllib.parse.quote(song_df['song'][song_list.index(choice)])
    search = webbrowser.open("https://open.spotify.com/search/"+song_data)
    print("\n","SELECTION:",a,",",b,",",c,",",d,"\n\n","SONG:",song_df['song'][song_list.index(choice)],"\n\n","LYRICS:\n",song_df['lyrics'][song_list.index(choice)],"\n")
    print("\n","Your song is now open in Spotify on your internet browser.\n")
    return search

#randomly select song based on user input; outputs the inputs and song; searches for song on Spotify  
def random_sel_no_lyrics (a, b, c, d): 
    options = song_picker(a, b, c, d)
    options_list = options['song'].tolist()
    choice = random.choice(options_list)
    song_data = urllib.parse.quote(song_df['song'][song_list.index(choice)])
    search = webbrowser.open("https://open.spotify.com/search/"+song_data)
    print("\n","SELECTION:",a,",",b,",",c,",",d,"\n\n","SONG:",song_df['song'][song_list.index(choice)],"\n")
    print("\n","Your song is now open in Spotify on your internet browser.\n")
    return search

#asks for song genre, tempo, mood, and era; asks if user wants lyrics and runs random_sel or random_sel_no_lyrics; asks to refresh selection
def asker ():
    
    while True:
        a = str(input("What song genre are you looking for? (pop, alternative/indie, alternative rock, rock, hard rock, metal, holiday, r&b/soul, hip-hop/rap, country, dance)\n").lower())
        if a.lower() not in a_list:
            print("\n","What was that?")
            continue
        else:
            break
    while True:
        b = str(input("What song tempo are you looking for? (fast, medium, slow)\n").lower())
        if b.lower() not in b_list:
            print("\n","What was that?")
            continue
        else:
            break
    while True:
        c = str(input("What song mood are you looking for? (happy, sad, angry)\n").lower())
        if c.lower() not in c_list:
            print("\n","What was that?")
            continue
        else:
            break
    while True:
        d = str(input("What song era are you looking for? (1950s, 1960s, 1970s, 1980s, 1990s, 2000s, 2010s)\n").lower())
        if d.lower() not in d_list:
            print("\n","What was that?")
            continue
        else:
            break
    while True:
        lyrics = str(input("Would you like the song lyrics? (y/n)\n").lower())
        if lyrics == "y":
            try: 
                random_sel(a, b, c, d)
            except IndexError:
                print("\n","SELECTION:",a,",",b,",",c,",",d,"\n\n","SONG:","Option not available","\n\n","LYRICS: N/A","\n")
            break
        elif lyrics == "n":
            try: 
                random_sel_no_lyrics(a, b, c, d)
            except IndexError:
                print("\n","SELECTION:",a,",",b,",",c,",",d,"\n\n","SONG:","Option not available")
            break
        else:
            print("\n","What was that?")
            continue
    while True:
        refresh = str(input("Would you like to refresh the song selection? (y/n)\n").lower())
        if refresh == "y":
            if lyrics == "y":
                try: 
                    random_sel(a, b, c, d)
                except IndexError:
                    print("\n","SELECTION:",a,",",b,",",c,",",d,"\n\n","SONG:","Option not available","\n\n","LYRICS: N/A","\n")
            elif lyrics == "n":
                try: 
                    random_sel_no_lyrics(a, b, c, d)
                except IndexError:
                    print("\n","SELECTION:",a,",",b,",",c,",",d,"\n\n","SONG:","Option not available")
            else:
                print("\n","What was that?")
                continue
        elif refresh == "n":
            break
        else:
            print("\n","What was that?")
            continue
    loop()

#asks to restart selection process                  
def loop ():
    ask_again = str(input("Would you like another suggestion? (y/n)\n").lower())
    if ask_again == 'y':
        print("\n")
        asker()
    elif ask_again == 'n':
        print("\n","Okay, enjoy the song!")
    else:
        print("\n","What was that?/n")
        loop()

#program starts
if __name__ == '__main__':
    asker()
    

