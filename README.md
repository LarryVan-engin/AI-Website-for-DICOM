Step to create a website

/create site
django-admin startproject site1 ("site1" is the name of website)
(or if it's error can use 'python -m django startproject site1')

/point to folder or site
cd site1 (if get out the folder or site 'cd ..' )

/install database...
python manage.py migrate

/local host server gate 8888
python manage.py runserver 8888

Now the server is running so we cannot access the terminal. So press Crtl + C to return accessing terminal.

/create super user for server
python manage.py createsuperuser
admin (name of user)
123 (password user. recommend hard password)

then text the line code 'python manage.py runserver 8888' to run server again, then add '/admin' continous on the site address to access into login site.


/create a module 
python manage.py startapp home ('home' is the name of module)

/add a module 
setting.py -> Installed apps -> 'home'

/create a template (trang chu cua website)
New folder -> 'Templates' -> create 'home.html'

/access to 'home.html'
html5-boilerplate


/write a title
	<header>
	<header>
    <body>

<h4>Here is title place </h4> //DAY LA NOI DUNG HAM home.html
...
	<body>
/access to site1 -> settings.py
add module 'home' at 'INSTALLED APP'

/view.py (dung de xem noi dung tra ve tren server)

def get_home(request): //'request' is the variance 
	return render(request,'home.html') //ham nay tra ve trang home.html

/urls.py (import duong dan tu server den trang web)

from home import view as home

urlspattern...

path('',home.get_home) //ham nay tro ve ham get_home

/after applying all the settings, now run the server again
python manage.py migrate 
python manage.py runserver 8888

(Remember to save manually on the VSC before migrating server)

//connect database mysql to django
/download XAMPP
/access XAMPP -> start APACHE and MYSQL
/access admin in MYSQL
/Co so du lieu -> creat site1

//back to VSC (ta co co ban 2 module da tao)
/settings.py -> DATABASE -> custom to engine, name, user, password, host.

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "site1",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
    }
}

pip install pymysql

/sau do save 
python manage.py migrate

//neu bao loi mariadb thi phai upgrade mariadb len ban cao hon trong xampp. len youtube coi huong dan

/neu thanh cong thi refresh lai server va se thay thong tin duoc cap nhat len site1

//tao file static/app
/import 3 files source js, css va images

//truy cap bootstrap de tim file css va html template voi javascript
//import link source bootstrap

/design tren home.html
{% load static %}

<head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <!-- css -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
        <link href-"{% static 'home/css/style.css' %}" rel="stylesheet" />
        <link href-"{% static 'home/css/owl.carousel.min.css' %}" rel="stylesheet" />
        <link href-"{% static 'home/css/all.min.css' %}" rel="stylesheet" />
        <!-- js -->
        <script https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js />
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.min.js" integrity="sha384-VQqxDN0EQCkWoxt/0vsQvZswzTHUVOImccYmSyhJTp7kGtPed0Qcx8rK9h9YEgx+" crossorigin="anonymous"></script>
        <script src="{% static 'home/js/s3.js' %}"> </script>
        <script src="{% static 'home/js/myscript.js' %}"> </script>
        <script src="{% static 'home/js/all.min.js' %}"> </script>
            
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
    </head>

//import navbar (thanh dieu huong)

<nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
              <a class="navbar-brand" href="#">Navbar</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                  </li>
                  <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Dropdown
                    </a>
                    <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="#">Action</a></li>
                      <li><a class="dropdown-item" href="#">Another action</a></li>
                      <li><hr class="dropdown-divider"></li>
                      <li><a class="dropdown-item" href="#">Something else here</a></li>
                    </ul>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link disabled" aria-disabled="true">Disabled</a>
                  </li>
                </ul>
                <form class="d-flex" role="search">
                  <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                  <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
              </div>
            </div>
          </nav>

//icon tren menu bar
<body>
        <!-- Header menu -->
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
              <a class="navbar-brand" href="#">
                <img src="{% static 'decor/images/logo1.png' %}" width= "80" height= "80"/>AI FOR DICOM
              </a>

//banner tren website
{% block banner_slide %}
<div id="carouselExampleDark" class="carousel carousel-dark slide">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
      <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="3" aria-label="Slide 4"></button>

    </div>
    
    <div class="carousel-inner">
      <div class="carousel-item active" data-bs-interval="10000">
        <img src="{% static "decor/images/banner/ban1.png" %}" class="d-block w-100" alt="AI production">
        <div class="carousel-caption d-none d-md-block">
          <h5>AI production</h5>
          <p>Artificial Intelligent in analysing DICOM images.</p>
        </div>
      </div>

      <div class="carousel-item" data-bs-interval="2000">
        <img src="{% static "decor/images/banner/ban2.png" %}" class="d-block w-100" alt="Second slide">
        <div class="carousel-caption d-none d-md-block">
          <h5></h5>
          <p>Supply solutions for DICOM analysists.</p>
        </div>
      </div>
      
      <div class="carousel-item">
        <img src="{% static "decor/images/banner/ban3.gif" %}" class="d-block w-100" alt="Third slide">
        <div class="carousel-caption d-none d-md-block">
          <h5>Faster and more accurate</h5>
          <p>Presentative content</p>
        </div>
      </div>

      <div class="carousel-item">
        <img src="{% static "decor/images/banner/ban4.png" %}" class="d-block w-100" alt="Fourth slide" height="680">
        <div class="carousel-caption d-none d-md-block">
          <h5>Big data, big brain</h5>
          <p>Presentative content</p>
        </div>
      </div>

    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
{% endblock  %}


