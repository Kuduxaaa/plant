import requests
import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib.parse import unquote


links = '''https://agrokavkaz.ge/samkurnalo-mcenareebi/viristerpha-samkurnalo-mtsenare-retsepti.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/gvirila-matricaria-chamomilla-samkurnalo-mtsenare.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/maqhvali-samkurnalo-mtsenare-retseptebi.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/qatsvi-samkurnalo-mtsenare-retseptebi.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/svia-samkurnalo-da-sasargeblo-mtsenare-retseptebi.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/baghis-pitnis-samkuranlo-thvisebebi-da-retseptebi.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/dedosphlisthitha-samkurnalo-mtsenare-retsepti.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/pharsmanduki-samkurnalo-mtsenare-retsepti.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/krazana-chais-qhvavili-samkurnalo-mtsenare-krazanas-naqhenis-retsepti.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/mravaldzarghva-udzvelesi-samkurnalo-mtsenare-retseptebi.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/gulqhvithela-kalendula-samkurnalo-thvisebebi-retsepti.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/babuatsvera-samkurnalo-mtsenare-naqhenis-retsepti.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/tskhenistsabla-devai-tsabl-samkurnalo-mtsenare.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/shavbalakha-naqhenis-balakhi-samkurnalo-mtsenare-retseptebi.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/askili-veluri-vardi-samkurnalo-mtsenare.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/thavshava-oregano-samkurnalo-mtsenare.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/kuneli-samkurnalo-mtsenare-ramdenime-retsepti.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/tchintchari-urtica-urens-samkurnalo-mtsenare.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/ombalo-sasargeblo-mtsenare.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/ghighilo-samkurnalo-mtsenare-ghighilos-qhvavilebis-naqheni.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/barambo-samkurnalo-mtsenare.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/thirkmlis-chai-samkurnalo-mtsenare.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/samkurnalo-tukhti-romelsats-udzvelesi-droidan-iqheneben.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/samkurnalo-salbis-shalphei-movla-moqhvana-gamoqheneba.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/qristesiskhla-samkurnalo-mtsenare-retsepti.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/anclis-sasargeblo-thvisebebi.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/jadvari-gugulis-kaba-orchis-maculata-l.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/aghmosavluri-nadzvi-samkurnalo-mtsenare.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/samkurnalo-mtsenareebi-phithri-maradmtsvane-viscum-album-l.html
https://agrokavkaz.ge/fermerta-skola/phermeris-bibliotheka-tsatskhvi-dakhasiatheba-gavrtseleba-nedleuli-gamoqheneba.html
https://agrokavkaz.ge/samkurnalo-mcenareebi/mukha-quercus-samkurnalo-mtsenare-retsepti.html
https://agrokavkaz.ge/dargebi/memcenareoba/kvliavi-movla-moqhvana-sasargeblo-thvisebebi.html
https://agrokavkaz.ge/dargebi/memcenareoba/samkurnalo-katabalakhas-valeriani-movla-moqhvana-gamoqheneba.html'''.split('\n')

image_index = 1

def download_image(image_url, file_name):
    global image_index
    response = requests.get(image_url)
    
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
            image_index += 1
            
    else:
        print(f"Failed to download image: {response.status_code}")


html = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>{}</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <!-- Favicon -->
    <link href="../img/favicon.ico" rel="icon">

    <!-- Google Web Fonts -->
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Roboto:wght@500;700&display=swap" rel="stylesheet">

    <!-- Icon Font Stylesheet -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.0/css/all.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">

    <!-- Libraries Stylesheet -->
    <link href="../lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">

    <!-- Customized Bootstrap Stylesheet -->
    <link href="../css/bootstrap.min.css" rel="stylesheet">

    <!-- Template Stylesheet -->
    <link href="../css/style.css" rel="stylesheet">
</head>

<body>
    <!-- Topbar Start -->
    <div class="container-fluid px-5 d-none d-lg-block">
        <div class="row gx-5 py-3 align-items-center">
            <div class="col-lg-3">
                <div class="d-flex align-items-center justify-content-start">
                    <i class="bi bi-phone-vibrate fs-1 text-primary me-2"></i>
                    <h2 class="mb-0">+995 (557) 345 689</h2>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="d-flex align-items-center justify-content-center">
                    <a href="../index.html" class="navbar-brand ms-lg-5">
                        <h1 class="m-0 display-4 text-primary"><span class="text-secondary">Farm</span>Fresh</h1>
                    </a>
                </div>
            </div>
            <div class="col-lg-3">
                <div class="d-flex align-items-center justify-content-end">
                    <a class="btn btn-primary btn-square rounded-circle me-2" href="#"><i class="fab fa-twitter"></i></a>
                    <a class="btn btn-primary btn-square rounded-circle me-2" href="#"><i class="fab fa-facebook-f"></i></a>
                    <a class="btn btn-primary btn-square rounded-circle me-2" href="#"><i class="fab fa-linkedin-in"></i></a>
                    <a class="btn btn-primary btn-square rounded-circle" href="#"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
    </div>
    <!-- Topbar End -->


    <!-- Navbar Start -->
    <nav class="navbar navbar-expand-lg bg-primary navbar-dark shadow-sm py-3 py-lg-0 px-3 px-lg-5 mb-4">
        <a href="index.html" class="navbar-brand d-flex d-lg-none">
            <h1 class="m-0 display-4 text-secondary"><span class="text-white">Farm</span>Fresh</h1>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <div class="navbar-nav mx-auto py-0">
                <a href="../index.html" class="nav-item nav-link">მთავარი</a>
                <a href="../about.html" class="nav-item nav-link">ჩვენს შესახებ</a>
                <a href="../service.html" class="nav-item nav-link">სერვისები</a>
                <a href="../products.html" class="nav-item nav-link">პროდუქცია</a>
                <!-- <div class="nav-item dropdown">
                    <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">Pages</a>
                    <div class="dropdown-menu m-0">
                        <a href="blog.html" class="dropdown-item">Blog Grid</a>
                        <a href="detail.html" class="dropdown-item">Blog Detail</a>
                        <a href="feature.html" class="dropdown-item">Features</a>
                        <a href="team.html" class="dropdown-item">The Team</a>
                        <a href="testimonial.html" class="dropdown-item">Testimonial</a>
                    </div>
                </div> -->
                <a href="#contact.html" class="nav-item nav-link">კონტაქტი</a>
            </div>
        </div>
    </nav>

    <div class="container py-6 mt-4">
        <div class="row row d-flex justify-content-center">
            <div class="col-lg-10">
                <div class="mb-5">
                    <div class="row g-5 mb-5">
                        <div class="col-md-12">
                            <img class="img-fluid w-100" src="../img/products/{}.jpg" alt="">
                        </div>
                    </div>

                    <h1 class="mb-4">{}</h1>

                    {}
                </div>
            </div>
        </div>
    </div>
    <!-- Blog End -->


    <!-- Footer Start -->
    <div class="container-fluid bg-footer bg-primary text-white mt-5">
        <div class="container">
            <div class="row gx-5">
                <div class="col-lg-8 col-md-6">
                    <div class="row gx-5">
                        <div class="col-lg-4 col-md-12 pt-5 mb-5">
                            <h4 class="text-white mb-4">კონტაქტი</h4>
                            <div class="d-flex mb-2">
                                <i class="bi bi-geo-alt text-white me-2"></i>
                                <p class="text-white mb-0">ხაშური, ქუჩა #34</p>
                            </div>
                            <div class="d-flex mb-2">
                                <i class="bi bi-envelope-open text-white me-2"></i>
                                <p class="text-white mb-0">info@example.com</p>
                            </div>
                            <div class="d-flex mb-2">
                                <i class="bi bi-telephone text-white me-2"></i>
                                <p class="text-white mb-0">+995 (557) 123 456</p>
                            </div>
                            <div class="d-flex mt-4">
                                <a class="btn btn-secondary btn-square rounded-circle me-2" href="#"><i class="fab fa-twitter"></i></a>
                                <a class="btn btn-secondary btn-square rounded-circle me-2" href="#"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-12 pt-0 pt-lg-5 mb-5">
                            <h4 class="text-white mb-4">სწრაფი ლინკები</h4>
                            <div class="d-flex flex-column justify-content-start">
                                <a class="text-white mb-2" href="#"><i class="bi bi-arrow-right text-white me-2"></i>მთავარი</a>
                                <a class="text-white mb-2" href="#"><i class="bi bi-arrow-right text-white me-2"></i>ჩვენს შესახებ</a>
                                <a class="text-white" href="#"><i class="bi bi-arrow-right text-white me-2"></i>კონტაქტი</a>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-12 pt-0 pt-lg-5 mb-5">
                            <h4 class="text-white mb-4">პოპულარული ლინკები</h4>
                            <div class="d-flex flex-column justify-content-start">
                                <a class="text-white mb-2" href="#"><i class="bi bi-arrow-right text-white me-2"></i>მთავარი</a>
                                <a class="text-white mb-2" href="#"><i class="bi bi-arrow-right text-white me-2"></i>ჩვენს შესახებ</a>
                                <a class="text-white" href="#"><i class="bi bi-arrow-right text-white me-2"></i>კონტაქტი</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 mt-lg-n5">
                    <div class="d-flex flex-column align-items-center justify-content-center text-center h-100 bg-secondary p-5">
                        <h4 class="text-white">სიახლე</h4>
                        <h6 class="text-white">გადაიხადე ახლა უკვე კრიპტოთი</h6>
                        <p class="mt-2">ჩვენ უკვე ვთანამშრომლობთ კომპანიასთან რომელიც ჩვენს კლიენტებს მისცემს საშუალებას ისარგებლონ კრიპტო გადახდებით ჩვენს საიტზე</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container-fluid bg-dark text-white py-4">
        <div class="container text-center">
            <p class="mb-0">&copy; <a class="text-secondary fw-bold" href="#">FarmFresh</a> 2023 ყველა უფლება დაცულია</p>
        </div>
    </div>
    <!-- Footer End -->


    <!-- Back to Top -->
    <a href="#" class="btn btn-secondary py-3 fs-4 back-to-top"><i class="bi bi-arrow-up"></i></a>


    <!-- JavaScript Libraries -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="../lib/easing/easing.min.js"></script>
    <script src="../lib/waypoints/waypoints.min.js"></script>
    <script src="../lib/counterup/counterup.min.js"></script>
    <script src="../lib/owlcarousel/owl.carousel.min.js"></script>

    <!-- Template Javascript -->
    <script src="../js/main.js"></script>
</body>

</html>'''

def parse(url):
    global image_index
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    figure = soup.find('figure', {'class': 'entry-thumbnail'})
    image_url = figure.find('img').get('src')
    
    download_image(image_url, f'C:\\Users\\nikak\\Desktop\\plant\\img\\products\\{image_index}.jpg')
    
    
# </div>''')
    
    
for link in links:
    parse(link)
