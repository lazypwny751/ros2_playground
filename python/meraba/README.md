# ROS2 - Python

ROS2 rclpy'e giriş, Meraba ros2.

## Paket adı: simple_sample
simple_sample: paketimizin genel özetini geçelim, source olarak eklediğimiz dosyalar "simple_sample/simple_sample/listener.py" ile "simple_sample/simple_sample/talker.py" dosyalarıdır.

- talker.py: Bu dosya bizim yayıncı node'umuzun kaynak kodunu içermekte, yaptığı da zamanlayıcı içinde sürekli "Merabaa!" gibisinden bir değer döndürmesi, listener buradaki timer'ı tanıyor ve oradan gelecek verilere ihtiyacı olacak.
- listener.py: Listener dosyası ise yayıncı(talker.py) node'umuzda yayınladığımız "Merabaa!" değerlerini topluyor.

## NOT: 
 - Ping-Pong: Ek olarak istersek listener'dan da talker'a "reply" ile geri dönüş yapabiliriz, o da diğer örnekte olsun.

## Klavuz.
Öncelikle projemizi derlememiz lazım bunun için colcon aracını kullancaz:
```sh
colcon build --packages-select simple_sample
```

Paket başarıyla derlendikten sonra, bazı dosyaları env'e almamız lazım ki paketimizi ros2 tanısın:

```sh
source install/setup.bash
```

artık yayıncı node'u başlatabiliriz:
```sh
ros2 run simple_sample talker
```

Artık talker node'umuz hazır, terminalde şu tarz bir veri görüyorsak sıkıntı yok:

```
root@70b29c265470:/mnt# ros2 run simple_sample talker
[INFO] [1760724857.428124388] [talker]: Send: "Merabaaa sayaci!": 0"
[INFO] [1760724858.405099873] [talker]: Send: "Merabaaa sayaci!": 1"
[INFO] [1760724859.405078475] [talker]: Send: "Merabaaa sayaci!": 2"
[INFO] [1760724860.405094723] [talker]: Send: "Merabaaa sayaci!": 3"
[INFO] [1760724861.405126373] [talker]: Send: "Merabaaa sayaci!": 4"
...
```

geriye listener(receiver) node'umuz kaldı onu da göstereyim, eğer benim gibi docker'da çalışıyorsan, önce docker kısmını anlatayım, listener'da kullandığımız konteyner'ı bulup orada bash oturumu açalım:
```sh
# ana makinada
> docker ps -a | grep "osrf/ros"
< 70b29c265470   osrf/ros:humble-desktop   "/ros_entrypoint.sh …"   8 minutes ago   Up 8 minutes             optimistic_jemison
```
işte konteynerımızı bulduk docker kafasına göre isim atamış hatta o da "optimistic_jemison" son stünda görünüyor istersen id ile istersen adı ile hitap et farketmez, ben konteyner adını kullanacağım.

Hadi listener'ı için konteyner'a girelim.
```
# ana makinada
docker exec -it -w "/mnt" optimistic_jemison /bin/bash
# farklı bi shell oturumu açtığımız için gerekli dosyaları tekrardan source edelim.
source /opt/ros/humble/setup.bash
source install/setup.bash
```

bundan sonraki adım docker'da da aynı docker harici ortamda da aynı:
```sh
ros2 run simple_sample listener
```

şu tarz bi çıktı görüyorsak on numara olmuştur.
```
root@0de19604d147:/mnt# ros2 run simple_sample listener
[INFO] [1760725443.374115609] [listener]: Receive: "Merabaaa sayaci!": 140"
[INFO] [1760725444.344393250] [listener]: Receive: "Merabaaa sayaci!": 141"
[INFO] [1760725445.344468503] [listener]: Receive: "Merabaaa sayaci!": 142"
[INFO] [1760725446.344501411] [listener]: Receive: "Merabaaa sayaci!": 143"
[INFO] [1760725447.344476160] [listener]: Receive: "Merabaaa sayaci!": 144"
[INFO] [1760725448.344501511] [listener]: Receive: "Merabaaa sayaci!": 145"
[INFO] [1760725449.344532118] [listener]: Receive: "Merabaaa sayaci!": 146"
[INFO] [1760725450.344600915] [listener]: Receive: "Merabaaa sayaci!": 147"
[INFO] [1760725451.344553260] [listener]: Receive: "Merabaaa sayaci!": 148"
[INFO] [1760725452.344970676] [listener]: Receive: "Merabaaa sayaci!": 149"
[INFO] [1760725453.344938895] [listener]: Receive: "Merabaaa sayaci!": 150"
...
```
