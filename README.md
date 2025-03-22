# SimpleNotebook

SimpleNotebook, notlarınızı kolayca oluşturmanızı, güncellemenizi, silmenizi ve listeleyebilmenizi sağlayan basit bir not alma uygulamasıdır. PyQt5 ile geliştirilmiş bir grafik arayüzüne sahiptir ve notlarınızı JSON formatında yerel bir dosyada saklar. Pastel renklerle tasarlanmış sevimli bir arayüzü vardır!

## Özellikler
- Yeni not ekleme
- Mevcut notları listeleme
- Notları güncelleme
- Notları silme
- JSON dosyasına otomatik kaydetme
- Sevimli ve pastel temalı arayüz

## Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki yazılımlara ihtiyacınız var:
- Python 3.6 veya üstü
- PyQt5 kütüphanesi

## Kurulum
1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/Busradeveci/SimpleNotebook-project.git

### Proje dizinine gidin:

cd SimpleNotebook

### Gerekli bağımlılıkları yükleyin:
pip install PyQt5

### Projeyi çalıştırın:
python main.py


## Kullanım
Uygulamayı çalıştırdığınızda karşınıza bir pencere çıkacak. Aşağıdaki düğmeleri kullanarak notlarınızı yönetebilirsiniz:
Add Note: Yeni bir not eklemek için başlık, içerik, tarih ve ID girin.
List Notes: Mevcut notları listeleyin.
Update Note: Bir notu güncellemek için ID ile yeni bilgileri girin.
Delete Note: Silmek istediğiniz notun ID’sini girin.
Exit: Uygulamayı kapatın.
Notlarınız notes.json dosyasına otomatik olarak kaydedilir ve uygulama her açıldığında bu dosyadan yüklenir.

Örnek Kullanım
"Add Note" düğmesine tıklayın.
Açılan kutucuklara sırasıyla başlık, içerik, tarih ve benzersiz bir ID girin.
Notunuz listeye eklenecek ve notes.json dosyasına kaydedilecektir.


![Ekran görüntüsü 2025-03-22 230553](https://github.com/user-attachments/assets/c283f946-70b2-4c89-aace-2a5fb6ebe2fa)
![Ekran görüntüsü 2025-03-22 230623](https://github.com/user-attachments/assets/81c0ab5e-011f-458b-931b-7e4128305078)


Katkıda Bulunma
Projeyi geliştirmek isterseniz:
Bu depoyu fork edin.
Yeni bir dal oluşturun: git checkout -b yeni-ozellik
Değişikliklerinizi yapın ve commit edin: git commit -m "Açıklama"
Dalınızı push edin: git push origin yeni-ozellik
Bir Pull Request oluşturun.

