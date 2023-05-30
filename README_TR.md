# Proje Başlığı

Bu proje, sakal veya yüz temasıyla baş ağrısına yol açabilen alışkanlıklardan kurtulmaya yardımcı olmayı amaçlamaktadır. Proje, el hareketlerini yüz yakınında algılamak ve bir hatırlatma olarak bir bildirim sesi çalmak için bilgisayarlı görü tekniklerini kullanmaktadır.

## Özellikler

- Kamera erişimi ve el tespiti için Python 3 ve OpenCV kullanır.
- El landmark tespiti için MediaPipe kütüphanesini kullanır.
- Belirli bir el hareketi algılandığında bildirim sesi çalar.
- Arka planda çalışır, böylece program başka görevleri yerine getirirken kullanılabilir.

## Gereksinimler

- Python 3.x
- OpenCV
- MediaPipe
- playsound

## Kurulum

1. Depoyu klonlayın:

git clone https://github.com/rifatdinc/Take-your-hand-off.git

2. Gerekli paketleri yükleyin:

pip install -r requirements.txt

## Kullanım

1. Programı çalıştırın:

python3 main.py

2. Kamera arka planda başlayacak ve el hareketleri sürekli olarak izlenecektir.
3. Sakal çekme gibi belirli bir el hareketi algılandığında bildirim sesi çalınacaktır.

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Herhangi bir öneriniz veya iyileştirmeniz varsa, lütfen bir konu açın veya bir pull talebi gönderin.

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.


