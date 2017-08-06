import sys,os,time ,hashlib ;
import argparse
from urllib import * ;
import requests;


def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest() ;


def get_subtitle(path , lan=""):
    url = "http://api.thesubdb.com"
    header= {'User-Agent': 'SubDB/1.0 (Subtitles_grabber/0.1; http://github.com/nateshmbhat/Subtitles_grabber)'};
    if isfile:
        file_hash = get_hash(path) ;
        r = requests.get("http://api.thesubdb.com" , headers=header , params = {'action': 'search' , 'hash' : file_hash})
        if(r.status_code == 404):
            print("Subtitle NOT FOUND for  : {}".format(path)) ;
            return ;
        elif r.status_code == 200 :
            print("Avaliable Languages are : \n")
            lan = r.text ;
            for i,lan in enumerate(r.text.split(',')):
                print(str(i+1)+' . '+get_language(lan));

        while(True):
            avail_list =  r.text.split(',')
            num_list = input("Enter the number for the corresponding language to be downloaded : ").split(',')
            lan_list = [] ;
            var_continue = False ;

            for i in num_list:
                try:
                    lan_list.append(avail_list[int(i)-1]);
                except IndexError:
                    print("\n\nINVALID INPUT !!! \n\n")
                    time.sleep(1) ;
                    var_continue = True ;
                    break ;
            if var_continue:
                continue ;
            break ;

        r = requests.get(url , headers = header , params = {'action' : 'download' , 'hash' : file_hash , 'languages' : ",".join(lan_list)})
        if(r.status_code == 404):
            print("SUBTITLE NOT FOUND !!! ") ;
            return ;
        if not os.path.isfile(path[0:path.rfind('.')]+'.srt'):
            subtitle = r.text ;
            with open(path[0:path.rfind('.')]+'.srt' ,'w') as f:
                in_index= 0
                end_index = 1
                while(True):
                    try:
                        f.write(subtitle[in_index : end_index]);
                        in_index+=1 ; end_index+=1
                    except UnicodeEncodeError:
                        f.write(' ');
                        in_index+=1 ; end_index+=1

                    except IndexError:
                        break ;


    else:
        file_hash = get_hash(path);
        r = requests.get(url, headers=header,params={'action': 'download', 'hash': file_hash, 'languages': lan});
        if (r.status_code == 404):
            print("\n\nSUBTITLE NOT FOUND !!! for {} ".format(path));
            return;
        if not os.path.isfile(path[0:path.rfind('.')]+'.srt'):
            subtitle = r.text ;
            with open(path[0:path.rfind('.')]+'.srt' ,'w' , encoding='utf-8') as f:
                in_index= 0
                end_index = 1
                while(True):
                    try:
                        f.write(subtitle[in_index : end_index]);
                        in_index+=1 ; end_index+=1
                        if (subtitle[in_index] == ''):
                            break;

                    except UnicodeEncodeError:
                        f.write(' ');
                        in_index+=1 ; end_index+=1

                    except IndexError:
                        break ;



def get_language(language_code):
    return {'en' : 'English' , 'pt' : 'Portuguese'  , 'es' : "Spanish" , 'fr' : 'French' , 'it' : 'Italian' , 'nl' : 'Dutch' , 'pl' : 'Polish'  , 'ro' : 'Romanian'  , 'sv' : 'Swedish' , 'tr' : 'Turkish'}[language_code]


def get_batch_sub(path , lan):
    file_list = os.listdir(path)
    for i in file_list:
        if i[i.rfind('.')+1 : ] not in 'mkv,flv,avi,mp4,wmv,mpeg,mpg,m4v,svi,3gp,f4v,f4p,f4a,f4b,swf'.split(','):
            continue;

        if(os.path.isdir(path+'\\'+i)):
            get_batch_sub(path+'\\'+i , lan)
        if(os.path.isfile(path+'\\'+i)):
            get_subtitle(path+'\\'+i ,  lan);



def init():
    global isfile
    isfile = True;
    if args.loc:
        path= args.loc

    else:
        path = input("Enter the location of the Video folder or the location of the individual video to get its subtitle : ") ;
        
    if  (os.path.isfile(path)):
        isfile = True ;
        get_subtitle(path) ;

    elif(os.path.isdir(path)):

        isfile = False ;
        print("""
    
        1. English
        2 . Portuguese
        3 . Spanish
        4 . French
        5 . Italian
        6 . Dutch
        7 . Polish
        8 . Romanian
        9 . Swedish
        10 . Turkish
        
        """)

        while(True):
            try:
                if args.lan:
                    lc = args.lan

                else:
                    lc = int(input("Enter the language NUMBER to download subtitle in the corresponding language (If subtitle is not present in the specified language only English is downloaded if found ) : "))
                    
                if lc<1 or lc>10:
                    raise ValueError;
            except ValueError:
                for i in "Invalid Input !!! \n\n":
                    print(i , end="") ;
                    time.sleep(0.05) ;
                time.sleep(0.5) ;
                continue
            break;

        lc = list({'en': 'English', 'pt': 'Portuguese', 'es': "Spanish", 'fr': 'French', 'it': 'Italian', 'nl': 'Dutch','pl': 'Polish', 'ro': 'Romanian', 'sv': 'Swedish', 'tr': 'Turkish'}.items())[lc-1][0] ;
        if lc!='en' :
            lan = 'en'
        else:
            lan  = lc+',en' ;
        get_batch_sub(path , lan);




if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--loc',type=str , default=None , help="Location of the video file or folder")
    parser.add_argument('--lan',type=int , default=None , help='''
    
    Language code to get the subtitles for the specified language :
    Here are the list of languages and thier corresponding codes

        1. English
        2 . Portuguese
        3 . Spanish
        4 . French
        5 . Italian
        6 . Dutch
        7 . Polish
        8 . Romanian
        9 . Swedish
        10 . Turkish
    ''')

    args = parser.parse_args()

    init()
