# ros2_playground

Alt klasörlerdeki README'leri okuyarak her bir playground hakkında daha detaylı bilgi edinebilirsiniz.

Kolay başlangıç için **run.sh** scriptini kullanabilirsiniz bu sayede "docker" ortamı üzerinden, sağlanan örnekleri çalıştırmak mümkün olacaktır:
```sh
sh run.sh <dir> <dir>..
```

Parametre olarak dizin(ler) belirtmek yeterlidir.
Örn:
```sh
sh run.sh "python/meraba"
```

Dosya dizin yapısı:
```
├── .gitignore
├── LICENSE
├── python/
│   ├── meraba/ < ros2 101.
│   ├── ping_pong/ < ros2 ile masa tenisi.
│   └── README.md
├── README.md < Şu anda buradasınız.
└── run.sh
```

# License
[GPLv3](./LICENSE)
