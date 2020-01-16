@author Emirhan Yılmaz

Konu Başlığı: Erkeklerde kafa boyutu ve beyin ağırlığı karşılaştırması
Özet: Bu çalışmada ilk olarak kimlikleri belirsiz, cinsiyeti erkek olan 57 kişinin kafa boyutu ve beyin ağırlığını içeren bir veri seti elde ettim. En küçük kareler yöntemini kullanarak birbirine bağlı bu iki veri arasındaki bağlantıyı gerçeğe en yakın olacak şekilde doğru denklemini yazdım.
Temel Katkı:
Örneğin, kafa boyutu 4512 cm3 olan ve beyin ağırlığı 1530 gram olan bir insan vardır.
Denklemimiz 1530 = 4512a + b (y = ax + b) olarak ifade edilir. Burada x kafa boyutunu, y ise beyin ağırlığını temsil eder.
Toplam 57 örneklem aldığımızda oluşan 2 bilinmeyenli 57 denklemi çözüp a ve b yi bulmak için en küçük kareler yönteminden faydalandım.
Çözüm:
                  
En küçük kareler metoduyla a ve b’yi bulmak için yaptığım işlemler sırasıyla:
1-İlk olarak x değişkenimizin yani kafa boyutunun toplamını ve karelerinin toplamını buldum:
∑_(n=1)^N▒Xn = 220296
∑_(n=1)^N▒Xn2 = 857742970
2-Daha sonra y değişkenimizin yani beyin ağırlığının toplamını ve her bir x değeriyle her bir y değerinin çarpımını buldum:
∑_(n=1)^N▒Yn  = 77815
∑_(n=1)^N▒XnYn =  302000202

3-Denklemimizde gösterilen N değeri örneklem sayımızdır yani 57.
N = 57
4-Son olarak bulduğumuz bu değerleri matrislerde yerine koydum ve matris hesaplamasını matlab’da yaptığımda a ve b değerlerimizi yani doğru denklemimizi elde ettim.

[█(a@b)]  = [■(857742970&220296@220296&57)](-1)   x [█(302000202@77815)] 

a = 0,1985		Y = 0,1985x + 597,84 
b = 597,84
