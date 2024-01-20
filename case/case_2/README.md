## Masalah

1. Sulitnya membaca data HTML dari python saat mulai melakukan scraping
2. Data yang tidak konsisten (e.g. Pada studi kasus 1, tidak seluruh elemen HTML nama SKU (`div` dengan class `prd_link-product-name`) memiliki elemen HTML jumlah penjualan (`span` dengan class `prd_label-integrity`))
3. Tidak dapat melakukan request ke website

## Cara Mengatasi

1. Menggunakan function `prettify()` yang disediakan oleh `BeautifulSoup` untuk memudahkan pembacaan data (e.g. File `example_soup.html` pada directory `case_1` untuk memudahkan pembacaan elemen HTML yang merupakan hasil request ke website Tokopedia)
2. Mengkonsistensi data (e.g. Pada studi kasus 1, diambil data yang selalu konsisten yaitu elemen HTML parent (`div` dengan class `css-1asz3by`), kemudian dicari setiap child berupa nama SKU, harga, dan jumlah penjualan. Apabila tidak ada elemen HTML jumlah penjualan, maka ditambahkan berupa 0 terjual)
3. Dapat dilakukan penambahan headers, token, dan lainnya yang diperlukan untuk dapat melakukan request
