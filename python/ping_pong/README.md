# ROS2 - Python

Pinpon(masa tenis) oynayan node'lar.

# Paket adı: ping_pong
ping_pong paketimiz bildiğimiz masa tenisi oynayan ros2 node'larına benzer, ping node'u ileti gönderir, pong node'u da bu iletiyi aldığı taktirde yanıt olarak başka bir ileti gönderir, ardından ping node'u pong node'undan gelen iletiyi aldığını belirtir ve bu döngü ping node'u durana kadar devam eder.

- ping.py: pong node'una bir ileti gönderir, sürekli ileti göndermeye çalışır initial node budur.
- pong.py: ping'den veri gelmediği sürece bekler, veri geliyorsa veriyi aldım der ve karşılık döndürür.

# Klavuz.
Burada uzun uzun anlatmayacağım, bir önceki [meraba](../meraba) örneğinden paketin nasıl derleneceğine ve çalıştırılacağına bakabilirsiniz. Belirtmem gereken hususlar ise:
- path: colcon ile build ederken veya paketin env'ini source ederken belirteceğiniz yol(path) önemli bu yüzden sürekli ls ve pwd komutlarıyla nerede olduğunuzu bilmeniz gerekir, keza bundan sonraki örneklerde de aynı şekilde yapmalısınız.
- pkgname: paket adı da bir önceki örnekten farklı olacaktır önceki örnekte "simple_sample" iken burada "ping_pong" tercih ettik yani gerek **colcon** komutun kullanırken gerek **ros2** komutuyla işlem yaparken paket adını doğru girmeniz gerekli aksi taktirde çalışmaz.
- nodename: node adları da değişti, önceki örnekte "talker" ve "listener" vardı lakin artık "ping" ve "pong" var bu da önemli bir detay, node'u çalıştırırken doğru adla/isimle çağırmak gereklidir.
