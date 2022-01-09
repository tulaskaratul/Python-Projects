#print colored text with python using colorama module 
 
import colorama 
 
from colorama import Fore, Back, Style 
 
colorama.init(autoreset=True) 
 
print(Fore.BLUE+Back.YELLOW+"My name is Kiddu " + Fore.YELLOW+Back.BLUE+ "I am your friend") 
 
print(Back.CYAN+"Hi, My Name is Atul ") 
 
print(Fore.RED+Back.GREEN+"Okay, Sayonara") 
