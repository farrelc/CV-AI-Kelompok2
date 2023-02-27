<div align="center">
  <img src="https://user-images.githubusercontent.com/76652264/207518434-a899f0cc-db33-4511-aed9-d523e325fdd7.png">
</div>
<br>

<a href="https://www.python.org/downloads/release/python-387/"><img src="https://img.shields.io/badge/Python%20-3.8.7-blue.svg"/></a>
<a href="https://opencv.org/releases/"><img src="https://img.shields.io/badge/OpenCV%20-4.6.0-green.svg"/></a>
<a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/Tkinter%20-0.1.0-red.svg"/></a>
<a href="https://google.github.io/mediapipe/getting_started/python.html "><img src="https://img.shields.io/badge/MediaPipe%20-9.0.0-yellow.svg"/></a>
<a href="https://numpy.org/install/"><img src="https://img.shields.io/badge/Numpy%20-1.19.4-white.svg"/></a>

# Overview

Eye Refresh Alert adalah aplikasi berbasis GUI/desktop yang digunakan untuk melakukan monitoring terhadap mata selama beraktivitas di depan layar laptop/komputer. 
Aplikasi ini akan mengingatkan pengguna untuk mengistirahatkan mata akibat dari interaksi mata yang menatap layar selama batas waktu yang ditentukan.

Eye Refresh Alert merupakan salah satu produk atau hasil dari kegiatan Focus Group Artificial Intelligence Laboratory Telkom University. Aplikasi ini dibuat menggunakan bahasa scripting python dengan library Tkinter sebagai GUI. Proses monitoring atau deteksi mata dari aplikasi ini memanfaatkan model <a href = "https://google.github.io/mediapipe/solutions/face_mesh">Face Mesh</a> dari platform yang dibuat oleh google yaitu <a href = "https://google.github.io/mediapipe/">Mediapipe</a>. 

# Download and Install
Eye Refresh Alert dapat di download melalui tautan <a href = 'https://tiny.one/eye-refresh-alert'>berikut</a>

Instalasi dari aplikasi ini cukup sederhana kerena aplikasi ini berupa installer yang siap digunakan. Berikut adalah langkah-langkah instalasi:

<div>
  <li>Buka installer Eye Refresh Alert</li>
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207900921-269e4e15-6b9d-4252-8d8b-91cb81112ecb.png">
  </div>
  <br>
</div>

<div>
  <li>Pilih direktori atau tempat aplikasi ini akan diinstall</li>
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207901584-1236ef9d-9f5e-4e56-9d0d-e0ad5f198470.png">
  </div>
  <br>
</div>

<div>
  <li>Klik Centang untuk menampilkan shortcut aplikasi pada desktop (rekomendasi) </li>
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207901929-9bdbbcf0-81e9-46e3-8d0e-0dcac6dbe0dd.png">
  </div>
  <br>
</div>

<div>
  <li>Tunggu proses instalasi sampai selesai</li>
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207902667-6c45fffa-dc32-4cd7-a286-fd9fde551e49.png">
  </div>
  <br>
</div>

<div>
  <li>Klik finish jika aplikasi telah berhasil terinstall tanpa ada masalah</li>
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207903128-cd8ab9ed-391e-4bf7-8cb8-f39e3b827a85.png">
  </div>
  <br>
</div>

# User Guide

<div>
  <p>Aplikasi Eye Refresh Alert dibuat dengan UI sesederhana mungkin sehingga dapat memudahkan pengguna dalam menggunakan aplikasi ini. Tampilan awal dari aplikasi ini adalah sebagai berikut.</p>
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207903999-e042bf1f-9b03-410c-b043-ec52bf365632.png" width = "600">
  </div>
  <br>
</div>

<div>
  <p>Jika pengguna ingin mengaktifkan kamera maka dapat mengklik tombol "Toggle Webcam". Saat ini pilihan webcam yang tersedia dari aplikasi ini hanya 1 saja, sehingga pastikan perangkat PC/Laptop anda sudah terpasang secara default sebuah webcam. </p>
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207907063-029e7571-f560-490a-b500-38447ae695fe.png" width = "600"> 
  </div>
  <br>
</div>

<div>
  <p>Pilihan waktu atau timer berada pada bagian "Select Time Threshold". Waktu yang ada pada bagian ini adalah batas waktu yang digunakan untuk interaksi mata dengan layar perangkat. Jika mata telah berinteraksi selama waktu yang dipilih maka nanti akan ada notifikasi untuk mengistirahatkan mata. Pilihan waktu ini ada 3 yaitu 20 menit, 40 menit dan 60 menit. </p>
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207913541-773b26bc-afd9-4a1d-97eb-ce6c304fb694.png" width = "600"> 
  </div>
  <br>
</div>

<div>
  <p>Jika webcam dan pemilihan waktu telah dilakukan maka pengguna dapat mengklik tombol "Start" untuk melakukan monitoring interaksi mata. Berikut adalah tampilan ketika aplikasi ini melakukan monitoring terhadap interaksi mata dengan layar perangkat. Pengguna dapat memberhentikan monitoring dengan mengklik tombol "Stop" dan melakukan "Reset" jika diperlukan. Waktu akan terus berjalan selama wajah terdeteksi dan mata pengguna terbuka. Jika wajah tidak terdeteksi di layar atau mata tertutup maka perhitungan waktu akan dihentikan. </p>  
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207914354-0cecc0c9-f03e-4cf7-a4b2-84d391ab3666.png" width = "600"> 
  </div>
  <br>
</div>

<div>
  <p>Jika batas waktu telah habis notifikasi dari aplikasi ini akan memberikan peringatan sebagai berikut</p>  
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207917623-b46033fa-437b-434f-9528-91e96a4e33f8.png" width = "600"> 
  </div>
  <br>
</div>

<div>
  <p>Aplikasi ini juga akan melakukan pemberhentian monitoring secara otomatis jika wajah tidak terdeteksi di layar atau mata tertutup selama kurun waktu tertentu. Untuk saat ini batas waktu yang digunakan adalah 5 menit. Artinya jika selama 5 menit wajah tidak terdeteksi di layar atau mata tertutup maka aplikasi ini akan melakukan pemberhentian monitoring dan memberika notifikasi sebagai berikut.</p>  
  <br>
  <div align="center">
    <img src="https://user-images.githubusercontent.com/76652264/207918692-fe4f8f49-da88-42c0-aeaf-5bc0cdd9ec2c.png" width = "600"> 
  </div>
  <br>
</div>

# Contribution Guidelines
Jika anda ingin melakukan improvisasi dan perbaikan terhadap aplikasi Eye Refresh Alert, sangat dipersilahkan untuk melakukan clone untuk project ini dan melakukan pull request. Depedencies yang digunakan untuk project/aplikasi ini adalah sebagai berikut:

<div align = "center">
<table>
<thead>
  <tr>
    <th>Depedencies</th>
    <th>Version</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Python</td>
    <td>3.8.7</td>
  </tr>
  <tr>
    <td>OpenCV</td>
    <td>4.6.0</td>
  </tr>
  <tr>
    <td>TkInter</td>
    <td>0.1.0</td>
  </tr>
  <tr>
    <td>MediaPipe</td>
    <td>9.0.0</td>
  </tr>
  <tr>
    <td>NumPy</td>
    <td>1.19.4</td>
  </tr>
</tbody>
</table>
</div>

# References

<li><a href = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6020759/">Digital eye strain: prevalence, measurement and amelioration</a></li>
<li><a href = "https://arxiv.org/abs/2006.11341">Real-time Pupil Tracking from Monocular Video for Digital Puppetry</a></li>
<li><a href = "https://www.irjet.net/archives/V8/i5/IRJET-V8I5427.pdf">Eye Detection using Haar Cascade Classifier</a></li>




