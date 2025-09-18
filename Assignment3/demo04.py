#Given stock prices over 7 days:
  # prices = [105, 110, 108, 112, 115, 116, 114].

  # - Compute the 3-day rolling average using slicing.
  # - Explanation:
  #   - (105+110+108)/3 ≈ 107.67
  #   - (110+108+112)/3 = 110.0
   #  - ... and so on

prices=[105, 110, 108, 112, 115, 116, 114]
average=[]

def TRaverage():
    for i in range(len(prices)-2):
        result=prices[i:i+3]
        average=sum(result)/len(result)
        average.append(round(average,2))
    print("Given prices",prices)
    print("3-day rolling average:",average)    
TRaverage()  
        
