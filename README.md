# multiThread -> ThreadPool -> POOL
Python'da çoklu iş parçacılığı (thread) kullanarak görevleri paralel olarak yürütmek için tasarlanmış basit bir kütüphane

# Açıklama:

POOL sınıfı, Python'da çoklu iş parçacığı (thread) kullanarak görevleri paralel olarak yürütmek için tasarlanmış basit bir kütüphanedir. Bu sayede I/O yoğun işlemlerde önemli performans artışları elde edilebilir.

# Özellikler:

* Görevleri Paralel Olarak Yürütme: Birden fazla görevi aynı anda çalıştırma imkanı sağlar.
* Esneklik: Görevlerin sonuçlarını kaydetme veya anında yazdırma gibi farklı seçenekler sunar.
* Kullanımı Kolay: Basit bir arayüz ile görevleri eklemek ve sonuçları almak mümkündür.

# Kurulum:

Bu kütüphaneyi kullanmak için herhangi bir ek kurulum gerekmez. Kodunuzu içeren dizinde bu dosyayı (README.md) ve POOL sınıfının tanımlandığı Python dosyasını bulundurun.
```batch
git clone https://github.com/Mefamex/multiThread.git
```

# Kullanım:

```Python
from threadPool import POOL

# Bir pool nesnesi oluştur
pool = POOL(max_threads=4)  # Maksimum 4 iş parçacığı kullanılacak

# Görevleri tanımla
def kare_al(x):
    return x * x

def topla(x, y):
    return x + y

# Görevleri pool'a ekle
results = pool.submit(kare_al, 4)
results += pool.submit(topla, 2, 3)

# Tüm görevlerin tamamlanmasını bekle ve sonuçları al
futures, elapsed_time, total_time = pool.join()

print(futures)  # [16, 5]
print(f"Toplam geçen süre: {elapsed_time:.2f} saniye")
```
Kodu dikkatli kullanın.

# Parametreler:

* **max_threads**: Maksimum iş parçacığı sayısı.
* **logFuture**: Görev sonuçlarını bir listede saklayıp saklamayacağını belirtir.
* **ResultwhenDone**: Görev sonuçlarını tamamlandıktan hemen sonra yazdırıp yazdırmayacağını belirtir.

# Notlar:

* Bu sınıf, I/O yoğun işlemler için daha uygundur. CPU yoğun işlemler için multiprocessing modülünü kullanmak daha etkili olabilir.
* Çok fazla iş parçacığı kullanmak sistem performansını olumsuz etkileyebilir. İş parçacığı sayısını dikkatli seçin.
# Lisans:

Bu kütüphane açık kaynaklıdır ve [lisans türü] lisansı altında dağıtılır.

# Daha Fazla Bilgi:

* [Projenin GitHub adresi](https://github.com/Mefamex/multiThread.git)
* [Yazar -> Mefamex](https://github.com/Mefamex)
* [Web sitesi](https:mefamex.com)

# Ek Özellikler (İsteğe Bağlı):

* **Örnek Kullanım Senaryoları**: Farklı kullanım örnekleri vererek kütüphanenin nasıl kullanılacağını daha iyi anlatabilirsiniz.
* **Performans Testleri**: Kütüphanenin performansını gösteren test sonuçları ekleyebilirsiniz.
* **Sınırlamalar**: Kütüphanenin hangi durumlarda kullanılmaması gerektiğini belirtebilirsiniz.
Bu README.md örneğini, projenizin özel ihtiyaçlarına göre özelleştirebilirsiniz.

Not: [lisans türü], [Projenin GitHub adresi] ve [İletişim için e-posta adresi] gibi yer tutucuları gerçek değerlerinizle değiştirin.

Ek İpuçları:

Açık ve anlaşılır bir dil kullanın: Teknik terimleri mümkün olduğunca az kullanmaya çalışın.
Başlıkları ve alt başlıkları kullanarak içeriği düzenleyin: Okuyucunun kolayca takip edebilmesini sağlayın.
Kod örneklerini uygun şekilde biçimlendirin: Kod parçalarını okunabilir hale getirin.
Görseller kullanın: Karmaşık kavramları görsel olarak açıklamak için diyagramlar veya grafikler kullanabilirsiniz.
Bu README.md dosyası, kullanıcıların kütüphanenizi daha iyi anlamalarına ve kullanmalarına yardımcı olacaktır.
