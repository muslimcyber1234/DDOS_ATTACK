import os,sys,time,requests
#Clean screen
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
logo = R+"""
echo "\033[32;1m==================================================================================="
toilet -f standard -F gay "DDOS ATTACK  "
toilet -f standard -F gay "By"
toilet -f standard -F gay "muslimmcyber"
toilet -f standard -F gay "1234"
echo "\033[32;1m==================================================================================="
echo ""
echo "Author   : muslimcyber1234"
echo "Gmail    : muslimcyber1234@gmail.com"
echo "github   : https://github.com/muslimcyber1234"
echo "Message  : hubungi saya jika script ini bermasalah dan jangan di salah gunakan secript ini"
sleep 1
echo "Thank you: muslimcyber1234
echo "\033[32;1m==================================================================================="

                                             <NNN>  
                                           <NNY    
                 <ooooo>--.               ((       
               Aoooooooooooo>--.           \\      
              AooodNNNNNNNNNNNNNNNN>--.     ))     
          (  AoodNNNNNNNNNNNNNNNNNNNNNNN>-///'     
          \\AodNNNNNNNNNNNNNNNNNNNNNNNNNNNY/       
           AodNNNNNNNNNNNNNNNNNNNNNNNNNNNNN      
          AdNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNA        
         (/)NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNA       
         //<NNNNNNNNNNNNNNNNNY'   YNNY YNNNN       
 ,====#Y//   `<NNNNNNNNNNNY       ANY     YNA      
               ANY<NNNNYYN       .NY        YN.    
             (NNY       NN      (NND       (NND    
                      (NNU  
                             
 ____  ____   ___  ____       _  _____ _____  _    ____ _  __             
|  _ \|  _ \ / _ \/ ___|     / \|_   _|_   _|/ \  / ___| |/ /  
| | | | | | | | | \___ \    / _ \ | |   | | / _ \| |   | ' / 
| |_| | |_| | |_| |___) |  / ___ \| |   | |/ ___ \ |___| . \  
|____/|____/ \___/|____/  /_/   \_\_|   |_/_/   \_\____|_|\_\ 

                         _            
                        | |_   _   _
                        | '_ \| | | |
                        | |_) | |_| |
                        |_.__/ \__, |
                               |____/
..............                                  
            ..,;:ccc,.                          
          ......''';lxO.                        
.....''''..........,:ld;                        
           .';;;:::;,,.x,                       
      ..'''.            0Xxoc:,.  ...           
  ....                ,ONkc;,;cokOdc',.         
 .                   OMo           ':ddo.       
                    dMc               :OO;      
                    0M.                 .:o.    
                    ;Wd                         
                     ;XO,                       
                       ,d0Odlc;,..              
                           ..',;:cdOOd::,.      
                                    .:d;.':;.   
                                       'd,  .'  
                                         ;l   ..
                                          .o    
                                            c   
                                            .'  
                                             . 
                                              
                     _ _                      _              
 _ __ ___  _   _ ___| (_)_ __ ___   ___ _   _| |__   ___ _ __
| '_ ` _ \| | | / __| | | '_ ` _ \ / __| | | | '_ \ / _ \ '__| 
| | | | | | |_| \__ \ | | | | | | | (__| |_| | |_) |  __/ |  
|_| |_| |_|\__,_|___/_|_|_| |_| |_|\___|\__, |_.__/ \___|_|  
                                        |___/ 
                     _ ____  _____  _  _
                    / |___ \|___ / | || |
                    | | __) | |_ \ | || |_
                    | |/ __/ ___) ||__   _|
                    |_|_____|____/    |_|
                                                                                                                      
    """+G+"""FRANS-O,CONER"""+R+"""   /___/"""
                      
def run(x):
	for n in x+"\n":
		sys.stdout.write(n)
		sys.stdout.flush()
		time.sleep(0.1)
def main():
	os.system('clear')
	print logo
	print
	no = raw_input(Y+"["+W+"?"+Y+"]["+W+"IP ADRESS TARGET"+Y+"]>> "+G)
	run(Y+"[!] Checking IP Target ...")
	time.sleep(4)
	if no < 5:
		print R+"[!] Target Not Found"
		sys.exit()
	elif 'DDOS ATACK, silahkan masukan IP adress target':
		print Y+"["+W+"LOCATION"+Y+"]: "+W+"Indonesian IP adress"
		time.sleep(4)
		serang(no)
	else:
		print R+"[!] Tool Not Support "+no
		print G+"[!] Tool Support Indonesian IP adress "
		sys.exit()

def serang(no):
	os.system('clear')
	print logo
	run(Y+"[!] Attack ...")
	time.sleep(2)
	while True:
		try:
			print G+"Sukses send DDOS ATTACK To: "+Y+no
		except:
			pass

if __name__ == '__main__':
	try:
		main()
	except requests.exceptions.ConnectionError:
		print R+"[x] No Connection"
		sys.exit()