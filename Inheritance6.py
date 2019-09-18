from abc import ABCMeta, abstracmethod
import math

#mendefiniikan kelas abstrak
class Bangun3D(metaclass=ABCMeta):
  #mendefinisikan metode abstrak
  @abstractmethod
  def cetakData(self):
    pass
   @abstractmethod
   def hitungVolume(self):
    pass
   @abstractmethod
   def cetakvolume(self):
      pass
      
 #mendefinisikan kelas konkrit yang merupaka
 #turunan dari kelas abastrak
 
class Kotak(Bangun3D):
    def __init__(self, p, l=None, t=None):
        if l == None and t == None:
        #jika berupa kubus
        self.panjang = self.lebar = \
        self.tinggi = p
     else:
         #jika berupa balok
         self.panjang = p 
         self.lebar = 1
         self.tinggi = t
     #mengimplementasikan metode cetakData()
     def cetakData(self):
          print("panjang\t: ", self.panjang)
          print("lebar\t: ", self.lebar)
          print("tinggi\t: ", self.tinggi)
          
      #mengimplementasikan metode hitungVolume()
      def hitungVolume(self):
          return math.pi * pow(self.jarijari, 2) * \
                  self.tinggi
       
      #mengimplementasikan metode cetakVolume()
      def cetakVolume(self):
          print("Volume Tabung \t= ",
                 self. hitungVolume())
                 
     def main():
        obj1 = Kotak(6, 5, 4) #balok
        print("BALOK")
        obj1.cetakData()
        obj1.cetakVolume()
        
        obj2 = Kotak(5) # kubus
        print("\nKUBUS")
        obj2.cetakData()
        obj2.cetakVolume()
        
        obj3 = Tabung(3, 4) #tabung
        print("\nTABUNG")
        obj3.cetakData()
        obj3.cetakVolume()
        
   if __name__ == "__main__":
      main()
