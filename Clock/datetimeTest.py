#Test Client for Trotman_DateTime
import Trotman_DateTime as dt
def main():
    time=dt.Clock()
    count=0
    if time.setClock(23,59,59,2,1,2000)==True:
        print('yes')
    else: print('no')
    print(time)
    time.decreaseSecond()
    print(time)

main()